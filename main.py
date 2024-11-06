from bs4 import BeautifulSoup
import requests

url = "https://stackoverflow.com/questions/tagged/h2o"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Finding the main questions container
questions_container = soup.find("div", id="questions")

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

    # Print the extracted information in a clean format
    print(f"Post ID: {post_id}")
    print(f"Votes: {votes}")
    print(f"Answers: {answers}")
    print(f"Views: {views}")
    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Excerpt: {excerpt}")
    print(f"Tags: {', '.join(tags)}")
    print(f"User: {user_name}")
    print(f"Reputation: {user_rep}")
    print("-" * 40)  # Separator line between questions
    break