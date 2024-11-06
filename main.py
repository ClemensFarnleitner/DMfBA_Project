from bs4 import BeautifulSoup
import requests

url = "https://stackoverflow.com/questions/tagged/h2o"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
questions_container = soup.find("div", id="questions")

# Dictionaries to store summary and detailed question data
questions_summary = {}
questions_details = {}

# Loop through each question summary
for question in questions_container.find_all("div", class_="s-post-summary"):
    post_id = question.get("data-post-id")
    votes = question.find("span", class_="s-post-summary--stats-item-number").text
    answers = question.find("div", class_="has-answers").find("span", class_="s-post-summary--stats-item-number").text if question.find("div", class_="has-answers") else "0"
    views = question.find("div", title=lambda x: x and "views" in x).find("span", class_="s-post-summary--stats-item-number").text
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
        "answers": answers,
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
    date_created = metadata_container.find("time", itemprop="dateCreated")['datetime'] if metadata_container.find("time", itemprop="dateCreated") else None
    last_activity_element = metadata_container.find("a", href="?lastactivity")
    last_activity_date = last_activity_element['title'] if last_activity_element else None
    view_count = int(question_soup.find("div", class_ ="flex--item ws-nowrap mb8")['title'].split()[1]) if question_soup.find("div", class_ ="flex--item ws-nowrap mb8") else int(question_soup.find("div", class_ ="flex--item ws-nowrap mb8 mr16")['title'].split()[1])


    questions_details[post_id] = {
        "date_created": date_created,
        "last_activity_date": last_activity_date,
        "view_count": view_count,
    }

    break

for item in questions_summary:
    print("**********", item, "**********")
    print("votes: ", questions_summary[item]["votes"])  
    print("answers: ", questions_summary[item]["answers"])
    print("views: ", questions_summary[item]["views"])
    print("title: ", questions_summary[item]["title"])
    print("link: ", questions_summary[item]["link"])
    print("excerpt: ", questions_summary[item]["excerpt"])
    print("tags: ", questions_summary[item]["tags"])
    print("user_name: ", questions_summary[item]["user_name"])
    print("user_rep: ", questions_summary[item]["user_rep"])
    
    print("question details:")
    print("date_created: ", questions_details[item]["date_created"])
    print("last_activity_date: ", questions_details[item]["last_activity_date"])
    print("view_count: ", questions_details[item]["view_count"])
    print("\n")