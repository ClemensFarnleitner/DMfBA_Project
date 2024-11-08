import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

class CSVWriter:
    def __init__(self):
        pass

    def write_question_csv(self, data):
        df = pd.DataFrame(data).T
        file_name = "h2o_stackoverflow_questions_summary.csv"
        file_exists = os.path.isfile(file_name)
        df.to_csv(file_name, mode="a", header=not file_exists, index="post_id")

    def write_answer_csv(self, data):
        df = pd.DataFrame(data).T
        file_name = "h2o_stackoverflow_answers_summary.csv"
        file_exists = os.path.isfile(file_name)
        df.to_csv(file_name, mode="a", header=not file_exists, index="answer_id")
    
    def write_question_details_csv(self, data):
        df = pd.DataFrame(data).T
        file_name = "h2o_stackoverflow_questions_details.csv"
        file_exists = os.path.isfile(file_name)
        df.to_csv(file_name, mode="a", header=not file_exists, index="post_id")

    def write_comment_csv(self, data):
        df = pd.DataFrame(data).T
        file_name = "h2o_stackoverflow_comments_summary.csv"
        file_exists = os.path.isfile(file_name)
        df.to_csv(file_name, mode="a", header=not file_exists, index="comment_id")

class StackOverFlowFetcher:
    def __init__(self):
        self.base_url = "https://stackoverflow.com/questions/tagged/h2o?tab=newest&pagesize=50"
        self.csv_writer = CSVWriter()

    def fetch_page(self, page=1):
        response = requests.get(f"{self.base_url}&page={page}")
        return response
    
    def get_max_pages(self):
        response = self.fetch_page(1)
        soup = BeautifulSoup(response.content, "html.parser")
        pagination = soup.find("div", class_="s-pagination")
        if pagination:
            page_numbers = [
                int(a.text) for a in pagination.find_all("a", class_="s-pagination--item js-pagination-item")
                if a.text.isdigit()
            ]
            max_page = max(page_numbers) if page_numbers else 1
            return max_page
        return 1

    def question_extraction(self, response):
        soup = BeautifulSoup(response.content, "html.parser")
        questions_container = soup.find("div", id="questions")
        return questions_container
    
    def question_summary(self, questions_container):
        questions_summary = {}
        for question in questions_container.find_all("div", class_="s-post-summary"):
            post_id = question.get("data-post-id")
            votes = question.find("span", class_="s-post-summary--stats-item-number").text
            answers_count = question.find("div", class_="has-answers").find("span", class_="s-post-summary--stats-item-number").text if question.find("div", "has-answers") else "0"
            views = question.find("div", title=lambda x: x and "views" in x).find("span", "s-post-summary--stats-item-number").text
            title_element = question.find("h3", "s-post-summary--content-title").find("a")
            title = title_element.text
            link = "https://stackoverflow.com" + title_element['href']
            excerpt = question.find("div", "s-post-summary--content-excerpt").text.strip()
            tags = [tag.text for tag in question.find("div", "s-post-summary--meta-tags").find_all("a", "s-tag")]
            user_info = question.find("div", "s-user-card--info")
            user_name = user_info.find("a").text if user_info else "Unknown"
            user_rep = user_info.find("li", "s-user-card--rep").text if user_info else "N/A"

            # Fetch answers to the question
            self.answer_summary(link, post_id)

            # Fetch question details
            self.question_details(link, post_id)

            # Store summary in dictionary using post_id as key
            questions_summary[post_id]= {
                "post_id": post_id,
                "votes": votes,
                "answers": answers_count,
                "views": views,
                "title": title,
                "link": link,
                "excerpt": excerpt,
                "tags": tags,
                "user_name": user_name,
                "user_rep": user_rep
            }
            
            time.sleep(1)

        # Write questions into CSV
        self.csv_writer.write_question_csv(questions_summary)
    
    def question_details(self, link, post_id):
        questions_details = {}
        question_response = requests.get(link)
        question_soup = BeautifulSoup(question_response.content, "html.parser")

        metadata_container = question_soup.find("div", class_="d-flex fw-wrap pb8 mb16 bb bc-black-200")
        date_created = metadata_container.find("time", itemprop="dateCreated")[
            'datetime'] if metadata_container and metadata_container.find("time", itemprop="dateCreated") else None
        last_activity_element = metadata_container.find("a", href="?lastactivity") if metadata_container else None
        last_activity_date = last_activity_element['title'] if last_activity_element else None
        try:
            view_text = question_soup.find("div", class_="flex--item ws-nowrap mb8")['title']
            view_count = int(view_text.split()[1])
        except (AttributeError, IndexError, TypeError, ValueError):
            view_count = 0

        question_text_element = question_soup.find("div", class_="s-prose js-post-body", itemprop="text")
        question_text = question_text_element.get_text(separator="\n").strip() if question_text_element else None
        tags_container = question_soup.find("div", class_="post-taglist")
        detailed_tags = [tag.text for tag in tags_container.find_all("a", class_="s-tag post-tag")] if tags_container else []

        user_info_container = question_soup.find("div", class_="user-info")
        if user_info_container:
            user_name = user_info_container.find("div", class_="user-details").find(
                "a").text.strip() if user_info_container.find("div", "user-details").find("a") else None
            user_profile_link = "https://stackoverflow.com" + user_info_container.find("a")['href']
            reputation_score = user_info_container.find("span",
                                                        class_="reputation-score").text.strip() if user_info_container.find(
                "span", "reputation-score") else None
            badges = {
                "bronze": user_info_container.find("span", class_="badgecount").text.strip() if user_info_container.find(
                    "span", "badgecount") else None
            }
        else:
            user_name = "Unknown"
            user_profile_link = None
            reputation_score = "N/A"
            badges = {"bronze": "0"}

        # Add user details to questions_details dictionary
        questions_details[post_id] = {
            "post_id": post_id,
            "date_created": date_created,
            "last_activity_date": last_activity_date,
            "view_count": view_count,
            "question_text": question_text,
            "detailed_tags": detailed_tags,
            "user_name": user_name,
            "user_profile_link": user_profile_link,
            "reputation_score": reputation_score,
            "badges": badges
        }

        time.sleep(1)

        # Write question details into CSV
        self.csv_writer.write_question_details_csv(questions_details)
    
    def answer_summary(self, link, post_id):
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")

        answers_container = soup.find("div", id="answers")
        if answers_container:
            for answer in answers_container.find_all("div", class_="answer"):
                answers_summary = {}
                answer_id = answer["data-answerid"]
                vote_count = int(answer["data-score"])
                answer_content = answer.find("div", "s-prose js-post-body").get_text(separator="\n").strip()
                creation_date = answer.find("time", itemprop="dateCreated")["datetime"]
                user_info = answer.find("div", "user-details")
                user_name = user_info.find("a").text.strip() if user_info.find("a") else None
                user_profile_link = "https://stackoverflow.com" + user_info.find("a")["href"] if user_info.find("a") else None
                reputation_score = user_info.find("span", "reputation-score").text if user_info.find("span", "reputation-score") else None

                # Fetch comments to the answer
                self.comment_summary(answer, answer_id)

                answers_summary [answer_id]= {
                    "answer_id": answer_id,
                    "vote_count": vote_count,
                    "answer_content": answer_content,
                    "creation_date": creation_date,
                    "user_name": user_name,
                    "user_profile_link": user_profile_link,
                    "reputation_score": reputation_score,
                    "post_id": post_id
                }

                # Write answer into CSV
                self.csv_writer.write_answer_csv(answers_summary)
    
    def comment_summary(self, answer, answer_id):
        comments_container = answer.find("div", class_="js-comments-container")
        comments_summary = {}
        if comments_container:
            for comment in comments_container.find_all("li", class_="comment js-comment"):
                comment_id = comment["data-comment-id"]
                comment_content = comment.find("span", class_="comment-copy").get_text(separator="\n").strip()
                comment_date = comment.find("span", class_="relativetime-clean").get_text()
                user_info = comment.find("div", class_="comment-user")
                user_name = user_info.find("a").text.strip() if user_info else None
                user_profile_link = "https://stackoverflow.com" + user_info.find("a")["href"] if user_info else None
                reputation_score = user_info.find("span", "reputation-score").text if user_info else None

                comments_summary [comment_id]= {
                    "comment_id": comment_id,
                    "content": comment_content,
                    "creation_date": comment_date,
                    "user_name": user_name,
                    "user_profile_link": user_profile_link,
                    "reputation_score": reputation_score,
                    "answer_id": answer_id
                }

            # Write comments into CSV
            self.csv_writer.write_comment_csv(comments_summary)

if __name__ == "__main__":
    timestamp_start = time.time()
    fetcher = StackOverFlowFetcher()
    max_pages = fetcher.get_max_pages()
    print(f"Max number of pages: {max_pages}")

    # Comment this number in order to fetch all pages
    max_pages = 1

    for page in range(1, max_pages + 1):
        response = fetcher.fetch_page(page)
        questions_container = fetcher.question_extraction(response)
        fetcher.question_summary(questions_container)
        time.sleep(2)  # Longer pause between page fetches
        print("=" * 50)
        print(f"Data fetched for page {page}")
        print("Switching to next page...")
        print("=" * 50)
    print("Data fetched for all pages.")
    print("=" * 50)

    df_questions = pd.read_csv("h2o_stackoverflow_questions_summary.csv")
    df_questions_details = pd.read_csv("h2o_stackoverflow_questions_details.csv")
    df_answers = pd.read_csv("h2o_stackoverflow_answers_summary.csv")
    df_comments = pd.read_csv("h2o_stackoverflow_comments_summary.csv")

    print(f"Total number of questions: {len(df_questions)}")
    print(f"Total number of question details: {len(df_questions_details)}")
    print(f"Total number of answers: {len(df_answers)}")
    print(f"Total number of comments: {len(df_comments)}")

    print(f"Time taken: {round((time.time() - timestamp_start),1)} seconds")
