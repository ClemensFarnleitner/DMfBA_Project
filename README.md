# DMfBA_Project

This project is a Python-based web scraper designed to collect and organize data from StackOverflow questions tagged with `h2o`. It extracts comprehensive information about questions, answers, and comments related to the H2O open-source machine learning platform. The collected data is structured and saved into CSV files for easy analysis and research purposes.

## Table of Contents
- [Features](#features)
  - [Question](#question)
  - [Question Details](#question-details)
  - [Answer](#answer)
  - [Comment](#comment)
  - [Author](#author)

## Features

### Question
| Checkbox | Column     | Description                                     |
|----------|------------|-------------------------------------------------|
| [x]      | `post_id`  | Unique identifier of the question post.         |
| [x]      | `votes`    | Number of votes the question has received.      |
| [x]      | `answers`  | Number of answers the question has received.    |
| [x]      | `views`    | Number of times the question has been viewed.   |
| [x]      | `title`    | Title of the question.                          |
| [x]      | `link`     | URL link to the question page.                  |
| [x]      | `excerpt`  | Short summary or excerpt of the question content. |
| [x]      | `tags`     | List of tags associated with the question.      |
| [x]      | `user_name`| Name of the user who posted the question.       |
| [x]      | `user_rep` | Reputation score of the user who posted the question. |

### Question Details
| Checkbox | Column               | Description                                        |
|----------|----------------------|----------------------------------------------------|
| [ ]      | `post_id`            | Unique identifier of the question post.            |
| [x]      | `date_created`       | Date and time when the question was created.       |
| [x]      | `last_activity_date` | Date and time of the last activity on the question. |
| [x]      | `view_count`         | Number of times the question has been viewed.      |
| [x]      | `question_text`      | Full text content of the question.                 |
| [x]      | `detailed_tags`      | List of tags associated with the question in detail. |
| [x]      | `user_name`          | Name of the user who posted the question.          |
| [x]      | `user_profile_link`  | URL link to the profile of the user who posted the question. |
| [x]      | `reputation_score`   | Reputation score of the user who posted the question. |
| [ ]      | `badges`             | Badges earned by the user (e.g., bronze, silver, gold). |

### Answer
| Checkbox | Column             | Description                                     |
|----------|--------------------|-------------------------------------------------|
| [x]      | `answer_id`        | Unique identifier of the answer.                |
| [x]      | `vote_count`       | Number of votes the answer has received.        |
| [x]      | `answer_content`   | Full text content of the answer.                |
| [x]      | `creation_date`    | Date and time when the answer was created.      |
| [x]      | `user_name`        | Name of the user who posted the answer.         |
| [x]      | `user_profile_link`| URL link to the profile of the user who posted the answer. |
| [x]      | `reputation_score` | Reputation score of the user who posted the answer. |
| [x]      | `post_id`          | Identifier of the question that the answer belongs to. |

### Comment
| Checkbox | Column             | Description                                     |
|----------|--------------------|-------------------------------------------------|
| [x]      | `comment_id`       | Unique identifier of the comment.               |
| [x]      | `content`          | Text content of the comment.                    |
| [x]      | `creation_date`    | Date and time when the comment was created.     |
| [x]      | `user_name`        | Name of the user who posted the comment.        |
| [x]      | `user_profile_link`| URL link to the profile of the user who posted the comment. |
| [x]      | `reputation_score` | Reputation score of the user who posted the comment. |
| [x]      | `answer_id`        | Identifier of the answer that the comment belongs to. |

### Author
| Checkbox | Field                  | Description                                         |
|----------|------------------------|-----------------------------------------------------|
| [ ]      | `username`             | Name of the author.                                 |
| [ ]      | `member_since`         | Date the author joined.                             |
| [ ]      | `last_seen`            | Last seen activity of the author.                   |
| [ ]      | `reputation`           | Total reputation score of the author.               |
| [ ]      | `people_reached`       | Number of people reached by the author's contributions. |
| [ ]      | `answers_count`        | Total number of answers provided by the author.     |
| [ ]      | `questions_count`      | Total number of questions asked by the author.      |
| [ ]      | `community_name`       | Name of the community the author is a part of.      |
| [ ]      | `community_reputation` | Author's reputation within the community.           |
| [ ]      | `badge_name`           | Name of the badge earned by the author.             |
| [ ]      | `badge_awarded_date`   | Date when the badge was awarded to the author.      |
