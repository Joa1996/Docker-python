import pandas as pd
# Read base data from local csv file
INPUT_FILEPATH= './data/courses.csv'
course_feedback = pd.read_csv(INPUT_FILEPATH)
# Create overall grade column
course_feedback['Overall'] = course_feedback.iloc[:, 4:7].mean(axis=1).round(2)
# Write new data frame to CSV locally
OUTPUT_FILEPATH = './data/course_feedback_finished.csv'
course_feedback.to_csv(OUTPUT_FILEPATH, encoding='utf-8', index=False)