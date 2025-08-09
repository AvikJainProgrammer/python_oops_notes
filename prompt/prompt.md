please create notes out of this making it short but leaving nothing of substance. 

___

questions:
  - question_id: 1
    question_type: qna
    question_text: "`What is the name of the project?`"
    answer: "Simple Learner"
    case_sensitive: false

  - question_id: 2
    question_type: fib
    question_text: "`In Power BI`, the feature used to create relationships between different tables is called the <<Model>> view."
    case_sensitive: true

  - question_id: 3
    question_type: mcq
    question_text: "`Which of the following is a feature of Power BI?`"
    options:
      - "Data Visualization"
      - "Machine Learning"
      - "Web Development"
      - "Game Development"
    correct_answer: "Data Visualization"

  - question_id: 4
    question_type: list_completion
    question_text: "`List the features of Power BI.`"
    answer: 
      - "Data Import"
      - "Data Transformation"
      - "Data Visualization"
      - "Collaboration"
      - "Integration with other services"
    case_sensitive: true
    order_sensitive: false
  - question_id: 5A
    question_type: descriptive_text
    question_text: "`Describe the process of creating a Power BI report.`"
    answer: "To create a Power BI report, you first import your data, then transform it as needed, create visualizations using the data, and finally publish the report to the Power BI service for sharing and collaboration."
    case_sensitive: false
    guided: true
  - question_id: 7
    question_type: code_fib
    language: go
    question_text: "`Fill in the missing parts of the Go program:`"
    question_code: |
      package main

      import (
          "<<fmt>>"
          "<<math>>"
      )

      func calculateArea(radius float64) float64 {
          return <<math>>.<<Pi>> * radius * radius
      }

      func main() {
          var r float64 = 5.5
          area := calculateArea(r)
          <<fmt>>.<<Printf>>("Area: %.2f\n", area)
      }
    case_sensitive: true
  - question_id: 8
    question_type: write_code
    language: python
    question_text: "`Write a hello world program in Python.`"
    question_code: |
      def hello_world():
          print("Hello, World!")
      hello_world()
    case_sensitive: true
    guided: false
  - question_id: 9
    question_type: list_completion
    question_text: |
      List the key steps shown in the following Python code for reading a CSV file:

      ```python
      import pandas as pd

      df = pd.read_csv('data.csv')
      print(df.head())
      ```
    answer:
      - "Import pandas"
      - "Read CSV file"
      - "Display first few rows"
    case_sensitive: false
    order_sensitive: true


The above are examples of question types and content formatted in yaml format. The only question_text can be formatted in markdown if needed. For fib type question, the question_text cannot be formatted in markdown. Simple text will work for it. Keep guided true for question types that have a guided setting. 
Based on the following text I need you to make some questions

___
In the question_text Mention the attributes and methods , what each function should do and the print statements to be added afterwords. Don't include the comments. Also mention the various attribute values to use. 