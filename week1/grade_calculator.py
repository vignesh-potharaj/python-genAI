# Basic Grade Calculator with Dictionary

def calculate_grade(score):
    grade_ranges = {
        (90, 100): 'A',
        (80, 89.99): 'B',
        (70, 79.99): 'C',
        (60, 69.99): 'D',
        (0, 59.99): 'F'
    }
    
    for (low, high), grade in grade_ranges.items():
        if low <= score <= high:
            return grade
    
    return 'Invalid'

def main():
    print("=== Basic Grade Calculator  ===")
    
    try:
        # Get input from user
        score = float(input("Enter your score (0-100): "))
        
        # Validate input
        if score < 0 or score > 100:
            print("Error: Score must be between 0 and 100")
            return
        
        # Calculate grade
        grade = calculate_grade(score)
        
        # Display result
        print(f"\nScore: {score:.1f}")
        print(f"Grade: {grade}")
        
        # Use dictionary for feedback
        feedback_dict = {
            'A': "Excellent! Keep up the great work!",
            'B': "Good job! Solid performance.",
            'C': "You passed! Consider reviewing material.",
            'D': "You passed, but seek extra help.",
            'F': "Please meet with your instructor."
        }
        
        print(f"Feedback: {feedback_dict.get(grade, 'grade')}")
            
    except ValueError:
        print("Error: Please enter a valid number")

if __name__ == "__main__":
    main()