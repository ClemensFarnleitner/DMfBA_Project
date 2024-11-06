from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import time  # for throttling requests

url = "https://stackoverflow.com/questions/tagged/h2o"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
questions_container = soup.find("div", id="questions")

# Dictionaries to store summary and detailed question data
questions_summary = {}
questions_details = {}

x = 1
# Loop through each question summary
for x, question in enumerate(questions_container.find_all("div", class_="s-post-summary"), start=1):
    post_id = question.get("data-post-id")
    votes = question.find("span", class_="s-post-summary--stats-item-number").text
    answers_count = question.find("div", class_="has-answers").find("span",
                                                                    class_="s-post-summary--stats-item-number").text if question.find(
        "div", class_="has-answers") else "0"
    views = question.find("div", title=lambda x: x and "views" in x).find("span",
                                                                          class_="s-post-summary--stats-item-number").text
    title_element = question.find("h3", class_="s-post-summary--content-title").find("a")
    title = title_element.text
    link = "https://stackoverflow.com" + title_element['href']
    excerpt = question.find("div", class_="s-post-summary--content-excerpt").text.strip()
    tags = [tag.text for tag in question.find("div", class_="s-post-summary--meta-tags").find_all("a", class_="s-tag")]
    user_info = question.find("div", class_="s-user-card--info")
    user_name = user_info.find("a").text if user_info else "Unknown"
    user_rep = user_info.find("li", class_="s-user-card--rep").text if user_info else "N/A"
    time_element = question.find("time", class_="s-user-card--time")

    # Store summary in dictionary using post_id as key
    questions_summary[post_id] = {
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

    # Fetch and parse the question details page
    question_response = requests.get(link)
    question_soup = BeautifulSoup(question_response.content, "html.parser")

    metadata_container = question_soup.find("div", class_="d-flex fw-wrap pb8 mb16 bb bc-black-200")
    date_created = metadata_container.find("time", itemprop="dateCreated")[
        'datetime'] if metadata_container and metadata_container.find("time", itemprop="dateCreated") else None
    last_activity_element = metadata_container.find("a", href="?lastactivity")
    last_activity_date = last_activity_element['title'] if last_activity_element else None

    # Extract view count dynamically
    try:
        view_text = question_soup.find("div", class_="flex--item ws-nowrap mb8")['title']
        view_count = int(view_text.split()[1])
    except (AttributeError, IndexError, TypeError, ValueError):
        view_count = 0

    # Extract question text
    question_text_element = question_soup.find("div", class_="s-prose js-post-body", itemprop="text")
    question_text = question_text_element.get_text(separator="\n").strip() if question_text_element else None

    # Extract tags from the question details page
    tags_container = question_soup.find("div", class_="post-taglist")
    detailed_tags = [tag.text for tag in
                     tags_container.find_all("a", class_="s-tag post-tag")] if tags_container else []

    user_info_container = question_soup.find("div", class_="user-info")
    if user_info_container:
        user_name = user_info_container.find("div", class_="user-details").find(
            "a").text.strip() if user_info_container.find("div", class_="user-details").find("a") else None
        user_profile_link = "https://stackoverflow.com" + user_info_container.find("a")['href']
        reputation_score = user_info_container.find("span",
                                                    class_="reputation-score").text.strip() if user_info_container.find(
            "span", class_="reputation-score") else None
        badges = {
            "bronze": user_info_container.find("span", class_="badgecount").text.strip() if user_info_container.find(
                "span", class_="badgecount") else None
        }
    else:
        user_name = "Unknown"
        user_profile_link = None
        reputation_score = "N/A"
        badges = {"bronze": "0"}

    # Add user details to questions_details dictionary
    questions_details[post_id] = {
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

    # Extract answers
    answers = []
    answers_container = question_soup.find("div", id="answers")
    if answers_container:
        for answer in answers_container.find_all("div", class_="answer"):
            answer_id = answer["data-answerid"]
            vote_count = int(answer["data-score"])
            answer_content = answer.find("div", class_="s-prose js-post-body").get_text(separator="\n").strip()
            creation_date = answer.find("time", itemprop="dateCreated")["datetime"]

            user_info = answer.find("div", class_="user-details")
            user_name = user_info.find("a").text.strip() if user_info.find("a") else None
            user_profile_link = "https://stackoverflow.com" + user_info.find("a")["href"] if user_info.find(
                "a") else None
            reputation_score = user_info.find("span", class_="reputation-score").text if user_info.find("span",
                                                                                                        class_="reputation-score") else None

        # Extract comments on the answer
        comments = []
        comments_container = answer.find("ul", class_="comments-list")
        if comments_container:
            for comment in comments_container.find_all("li", class_="comment"):
                comment_text = comment.find("span", class_="comment-copy").get_text(strip=True)
                comment_author = comment.find("a", class_="comment-user").text
                comment_author_link = "https://stackoverflow.com" + comment.find("a", class_="comment-user")["href"]
                comment_date = comment.find("span", class_="relativetime-clean").get_text()
                comments.append({
                    "comment_text": comment_text,
                    "comment_author": comment_author,
                    "comment_author_link": comment_author_link,
                    "comment_date": comment_date
                })

            answers.append({
                "answer_id": answer_id,
                "vote_count": vote_count,
                "answer_content": answer_content,
                "creation_date": creation_date,
                "user_name": user_name,
                "user_profile_link": user_profile_link,
                "reputation_score": reputation_score,
                "comments": comments
            })

    # Add answer details to questions_details dictionary
    questions_details[post_id]["answer_count"] = len(answers)
    questions_details[post_id]["answers"] = answers

    # Throttle requests to avoid overloading the server
    time.sleep(1)

    # Limit scraping to 10 questions for demonstration
    if x == 1:
        break

    x += 1

# Save data to JSON
data_to_save = {
    "questions_summary": questions_summary,
    "questions_details": questions_details,
}

with open("stackoverflow_h2o_data.json", "w") as outfile:
    json.dump(data_to_save, outfile, indent=4)

# Save questions summary to CSV
df_summary = pd.DataFrame.from_dict(questions_summary, orient="index")
df_summary.to_csv("stackoverflow_h2o_summary.csv", index_label="post_id")

# Output each question's summary and details
for item_id, summary in questions_summary.items():
    print(f"\n{'='*40}\nQuestion ID: {item_id}\n{'='*40}")
    print(f"Title: {summary['title']}")
    print(f"Link: {summary['link']}")
    print(f"Votes: {summary['votes']}")
    print(f"Answers: {summary['answers']}")
    print(f"Views (Summary): {summary['views']}")
    print(f"Excerpt: {summary['excerpt']}")
    print(f"Tags: {', '.join(summary['tags'])}")
    print(f"Posted by: {summary['user_name']} (Reputation: {summary['user_rep']})\n")

    # Get details for the current question
    details = questions_details.get(item_id, {})
    print("Question Details:")
    print(f"Date Created: {details.get('date_created', 'N/A')}")
    print(f"Last Activity Date: {details.get('last_activity_date', 'N/A')}")
    print(f"View Count: {details.get('view_count', 'N/A')}")
    print(f"Detailed Tags: {', '.join(details.get('detailed_tags', []))}")
    print(f"Question Text:\n{details.get('question_text', 'N/A')}\n")

    print("User Details:")
    print(f"User Name: {details.get('user_name', 'N/A')}")
    print(f"Profile Link: {details.get('user_profile_link', 'N/A')}")
    print(f"Reputation Score: {details.get('reputation_score', 'N/A')}")
    print(f"Badges: {details.get('badges', 'N/A')}")
    print(f"Answer Count: {details.get('answer_count', 'N/A')}\n")

    print("Answers:")
    for i, answer in enumerate(details.get("answers", []), start=1):
        print(f"\n  Answer {i}:")
        print(f"  Answer ID: {answer['answer_id']}")
        print(f"  Vote Count: {answer['vote_count']}")
        print(f"  Content:\n    {answer['answer_content']}")
        print(f"  Creation Date: {answer['creation_date']}")
        print(f"  Answered by: {answer['user_name']} (Profile: {answer['user_profile_link']})")
        print(f"  Reputation: {answer['reputation_score']}")

        print("  Comments:")
        if answer["comments"]:
            for j, comment in enumerate(answer["comments"], start=1):
                print(f"    Comment {j}:")
                print(f"      Text: {comment['comment_text']}")
                print(f"      Author: {comment['comment_author']}")
                print(f"      Author Profile: {comment['comment_author_link']}")
                print(f"      Date: {comment['comment_date']}")
        else:
            print("    No comments.")

