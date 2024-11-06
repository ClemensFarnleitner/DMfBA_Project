from bs4 import BeautifulSoup
import requests

url = "https://stackoverflow.com/questions/tagged/h2o"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Finding the main questions container
questions_container = soup.find("div", id="questions")

# List to store all question dictionaries
questions_data = []

# Loop through each question summary
for question in questions_container.find_all("div", class_="s-post-summary"):
    # Extract the necessary information and store it in a dictionary
    question_data = {
        "post_id": question.get("data-post-id"),
        "votes": question.find("span", class_="s-post-summary--stats-item-number").text,
        "answers": question.find("div", class_="has-answers").find("span", class_="s-post-summary--stats-item-number").text if question.find("div", class_="has-answers") else "0",
        "views": question.find("div", title=lambda x: x and "views" in x).find("span", class_="s-post-summary--stats-item-number").text,
        "title": question.find("h3", class_="s-post-summary--content-title").find("a").text,
        "link": "https://stackoverflow.com" + question.find("h3", class_="s-post-summary--content-title").find("a")['href'],
        "excerpt": question.find("div", class_="s-post-summary--content-excerpt").text.strip(),
        "tags": [tag.text for tag in question.find("div", class_="s-post-summary--meta-tags").find_all("a", class_="s-tag")],
        "user_name": question.find("div", class_="s-user-card--info").find("a").text if question.find("div", class_="s-user-card--info") else "Unknown",
        "user_rep": question.find("div", class_="s-user-card--info").find("li", class_="s-user-card--rep").text if question.find("div", class_="s-user-card--info") else "N/A",
    }
    
    # Append the dictionary to the list
    questions_data.append(question_data)

# show how many questions have been found 
print(len(questions_data))
for question in questions_data:
    print(question, "\n")
