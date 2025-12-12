import re
import json
import sys

def parse_qa_file(file_path):
    """
    Parse markdown file with @@qa...@@endqa blocks containing Q&A JSON objects.
    Returns list of parsed Q&A dicts.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all @@qa...@@endqa blocks
    pattern = r'@@qa\s*(.*?)\s*@@endqa'
    blocks = re.findall(pattern, content, re.DOTALL)
    
    qa_list = []
    
    for block in blocks:
        # Split block into individual JSON objects
        lines = block.strip().split('\n')
        current_json = []
        
        for line in lines:
            line = line.strip()
            if line:
                current_json.append(line)
                # Check if we have a complete JSON object (ends with })
                if line.endswith('}'):
                    try:
                        json_str = '\n'.join(current_json)
                        qa_obj = json.loads(json_str)
                        
                        # Validate required fields
                        required_fields = ['question', 'answer', 'topic', 'difficulty']
                        if all(field in qa_obj for field in required_fields):
                            qa_list.append(qa_obj)
                        else:
                            print(f"Warning: Missing required fields, skipping...")
                        
                        current_json = []  # Reset for next object
                        
                    except json.JSONDecodeError as e:
                        print(f"Warning: Invalid JSON format: {e}")
                        current_json = []
    
    return qa_list


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser.py <filepath>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    qa_sets = parse_qa_file(file_path)
    
    print(f"\n{len(qa_sets)} question/answer sets found")
    
    # Show first few as preview
    if qa_sets:
        print("\nPreview of parsed dicts:")
        for i, qa in enumerate(qa_sets[:3], 1):
            print(f"\n{i}. {qa}")
