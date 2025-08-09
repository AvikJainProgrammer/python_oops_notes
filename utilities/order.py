import yaml

def reorder_question_ids(input_yaml_file, output_yaml_file):
    # Read the YAML file
    with open(input_yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    
    # Check if questions exist in the data
    if not data or 'questions' not in data:
        print("No questions found in the YAML file.")
        return
    
    # Reassign question IDs sequentially
    for index, question in enumerate(data['questions'], start=1):
        question['question_id'] = index
    
    # Write the updated data back to a new YAML file
    with open(output_yaml_file, 'w') as file:
        yaml.safe_dump(data, file, sort_keys=False)
    
    print(f"Question IDs reordered and saved to {output_yaml_file}")

# Example usage
if __name__ == "__main__":
    input_file = "/Users/avikjain/Documents/projects/python_oops_notes/1.Oop_fundamentals/practice/questions.yaml"
    output_file = "/Users/avikjain/Documents/projects/python_oops_notes/1.Oop_fundamentals/practice/questions_ordered.yaml"
    reorder_question_ids(input_file, output_file)

