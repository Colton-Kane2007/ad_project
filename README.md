# Anomally Detection Project:
## Anomalies in the Codeup Curriculum Data

# Project description with goals:
* This is a notebook where I analyze anomalies within the dataset from Codeup. Using the data science pipeline, I grab the data, prepare it, explore it, and visualize it in order to answer questions about the data.
# Initial questions I have of the data:
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Which lessons are least accessed?
5. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?

# Data Dictionary:
|Feature|Dtype, Description|
|:--------|:-----------|
|datetime|	datetime, index/date and time|
|lesson|	object, name of lesson accessed|
|user_id|	int64, id for user accessing lesson|
|cohort_id|	float64, id for user cohort|
|ip|	object, ip address|
|year|	int32, year from datetime|
|month|	object, month from datetime|
|weekday|	object, weekday from datetime|
|hour|	int32, hour from datetime|
# Project planning:
* Aquire data from Google Drive
 
* Prepare data
   * Create engineered columns from existing data
       * datetime
       * year
       * month
       * weekday
       * hour
   * Separate columns
   * Rename columns descriptively
   * Drop old date and time columns
   * Change datetime column to datetime type
   * Set datetime to index
   * Setting nulls to 0 for users with no cohort id, to show they have no cohort
 
* Explore data in search of answers to initial questions

# Project goal
  * Answer questions about anomalies in the data, and send a professional email with a link to my work, questions answered, and a slide to be used in an existing slideshow

# Steps to reproduce
  * Download txt file from link. Clone wrangle file and change username for file path. Read in data.
