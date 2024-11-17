# Data Managament for Business Analytics Group Work

Below are the details of each CSV file generated by the script, including their purpose, column names, and descriptions.

## Data Summary (Fetched on `2024-11-17`):
- Total number of questions: **1887**
- Total number of question details: **1887**
- Total number of answers: **2092**
- Total number of comments: **1963**
- Total number of authors: **1882**

---

### 1. `h2o_stackoverflow_questions_summary.csv`

#### **Description:**
This CSV contains a summary of questions tagged with `h2o` on Stack Overflow. It provides an overview of the questions, including their titles, votes, views, tags, and links.

| Column Name   | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `post_id`     | Unique identifier for each question.                                        |
| `votes`       | Number of votes the question has received.                                 |
| `answers`     | Number of answers submitted to the question.                               |
| `views`       | Number of views the question has received.                                 |
| `title`       | Title of the question.                                                     |
| `link`        | URL link to the question on Stack Overflow.                                |
| `excerpt`     | Short excerpt or summary of the question's content.                        |
| `tags`        | List of tags associated with the question (e.g., `h2o`, `python`).         |

---

### 2. `h2o_stackoverflow_questions_details.csv`

#### **Description:**
This CSV contains detailed metadata about each question, including creation and activity dates, detailed tags, and author information.

| Column Name         | Description                                                                  |
|---------------------|------------------------------------------------------------------------------|
| `post_id`           | Unique identifier for each question.                                         |
| `date_created`      | Date and time when the question was created.                                 |
| `last_activity_date`| Date and time of the last activity (e.g., answer or comment).                |
| `view_count`        | Total number of views for the question.                                      |
| `question_text`     | Full text of the question's content.                                         |
| `detailed_tags`     | Detailed list of tags associated with the question.                          |
| `user_name`         | Username of the question's author.                                           |
| `user_profile_link` | URL link to the author's profile on Stack Overflow.                          |
| `reputation_score`  | Reputation score of the question's author at the time of question creation.  |

---

### 3. `h2o_stackoverflow_answers_summary.csv`

#### **Description:**
This CSV contains information about answers to questions tagged with `h2o`. It includes details about the answers' content, vote count, creation date, and authorship.

| Column Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `answer_id`       | Unique identifier for each answer.                                          |
| `vote_count`      | Number of votes the answer has received.                                    |
| `answer_content`  | Full text of the answer.                                                   |
| `creation_date`   | Date and time when the answer was created.                                  |
| `user_name`       | Username of the author who provided the answer.                            |
| `user_profile_link` | URL link to the author's profile on Stack Overflow.                       |
| `reputation_score`| Reputation score of the answer's author at the time of answer creation.     |
| `post_id`         | Unique identifier of the question this answer is associated with.           |

---

### 4. `h2o_stackoverflow_comments_summary.csv`

#### **Description:**
This CSV contains details about comments on answers to questions tagged with `h2o`. It includes comment text, creation date, and author details.

| Column Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `comment_id`      | Unique identifier for each comment.                                         |
| `content`         | Full text of the comment.                                                  |
| `creation_date`   | Date and time when the comment was posted.                                  |
| `user_name`       | Username of the comment's author.                                           |
| `user_profile_link` | URL link to the author's profile on Stack Overflow.                       |
| `reputation_score`| Reputation score of the comment's author at the time of comment creation.   |
| `answer_id`       | Unique identifier of the answer this comment is associated with.            |

---

### 5. `h2o_stackoverflow_authors_summary.csv`

#### **Description:**
This CSV contains comprehensive information about the authors of questions, answers, and comments. It includes their reputation, badges, activity, and profile details.

| Column Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `user_id`         | Unique identifier for the author.                                           |
| `user_name`       | Display name of the author.                                                 |
| `user_profile_link` | URL link to the author's profile on Stack Overflow.                       |
| `badges`          | Dictionary of badge counts (`gold`, `silver`, `bronze`).                   |
| `reputation`      | Total reputation score of the author.                                       |
| `reached`         | Total number of people reached by the author's posts.                      |
| `answer_count`    | Total number of answers provided by the author.                            |
| `questions_count` | Total number of questions asked by the author.                             |
| `member_since`    | Date when the author joined Stack Overflow.                                |
| `post_id`     | Unique identifier for each question.                                        |