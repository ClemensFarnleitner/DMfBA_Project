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
| Checkbox               | Column     | Description                                     |
|------------------------|------------|-------------------------------------------------|
| :heavy_check_mark:     | `post_id`  | Unique identifier of the question post.         |
| :heavy_check_mark:     | `votes`    | Number of votes the question has received.      |
| :heavy_check_mark:     | `answers`  | Number of answers the question has received.    |
| :heavy_check_mark:     | `views`    | Number of times the question has been viewed.   |
| :heavy_check_mark:     | `title`    | Title of the question.                          |
| :heavy_check_mark:     | `link`     | URL link to the question page.                  |
| :heavy_check_mark:     | `excerpt`  | Short summary or excerpt of the question content. |
| :heavy_check_mark:     | `tags`     | List of tags associated with the question.      |
| :heavy_check_mark:     | `user_name`| Name of the user who posted the question.       |
| :heavy_check_mark:     | `user_rep` | Reputation score of the user who posted the question. |

### Question Details
| Checkbox               | Column               | Description                                        |
|------------------------|----------------------|----------------------------------------------------|
| :heavy_check_mark:     | `post_id`            | Unique identifier of the question post.            |
| :heavy_check_mark:     | `date_created`       | Date and time when the question was created.       |
| :heavy_check_mark:     | `last_activity_date` | Date and time of the last activity on the question. |
| :heavy_check_mark:     | `view_count`         | Number of times the question has been viewed.      |
| :heavy_check_mark:     | `question_text`      | Full text content of the question.                 |
| :heavy_check_mark:     | `detailed_tags`      | List of tags associated with the question in detail. |
| :heavy_check_mark:     | `user_name`          | Name of the user who posted the question.          |
| :heavy_check_mark:     | `user_profile_link`  | URL link to the profile of the user who posted the question. |
| :heavy_check_mark:     | `reputation_score`   | Reputation score of the user who posted the question. |

### Answer
| Checkbox               | Column             | Description                                     |
|------------------------|--------------------|-------------------------------------------------|
| :heavy_check_mark:     | `answer_id`        | Unique identifier of the answer.                |
| :heavy_check_mark:     | `vote_count`       | Number of votes the answer has received.        |
| :heavy_check_mark:     | `answer_content`   | Full text content of the answer.                |
| :heavy_check_mark:     | `creation_date`    | Date and time when the answer was created.      |
| :heavy_check_mark:     | `user_name`        | Name of the user who posted the answer.         |
| :heavy_check_mark:     | `user_profile_link`| URL link to the profile of the user who posted the answer. |
| :heavy_check_mark:     | `reputation_score` | Reputation score of the user who posted the answer. |
| :heavy_check_mark:     | `post_id`          | Identifier of the question that the answer belongs to. |

### Comment
| Checkbox               | Column             | Description                                     |
|------------------------|--------------------|-------------------------------------------------|
| :heavy_check_mark:     | `comment_id`       | Unique identifier of the comment.               |
| :heavy_check_mark:     | `content`          | Text content of the comment.                    |
| :heavy_check_mark:     | `creation_date`    | Date and time when the comment was created.     |
| :heavy_check_mark:     | `user_name`        | Name of the user who posted the comment.        |
| :heavy_check_mark:     | `user_profile_link`| URL link to the profile of the user who posted the comment. |
| :heavy_check_mark:     | `reputation_score` | Reputation score of the user who posted the comment. |
| :heavy_check_mark:     | `answer_id`        | Identifier of the answer that the comment belongs to. |

### Author
| Checkbox               | Column                  | Description                                         |
|------------------------|------------------------|-----------------------------------------------------|
| :x:                    | `username`             | Name of the author.                                 |
| :x:                    | `member_since`         | Date the author joined.                             |
| :x:                    | `last_seen`            | Last seen activity of the author.                   |
| :x:                    | `reputation`           | Total reputation score of the author.               |
| :x:                    | `people_reached`       | Number of people reached by the author's contributions. |
| :x:                    | `answers_count`        | Total number of answers provided by the author.     |
| :x:                    | `questions_count`      | Total number of questions asked by the author.      |
| :x:                    | `community_name`       | Name of the community the author is a part of.      |
| :x:                    | `community_reputation` | Author's reputation within the community.           |
| :x:                    | `badge_name`           | Name of the badge earned by the author.             |
| :x:                    | `badge_awarded_date`   | Date when the badge was awarded to the author.      |
| :x:                    | `answer_id`            | Identifier of the answer that the author belongs to. |
| :x:                    | `comment_id`           | Identifier of the comment that the author belongs to  |

