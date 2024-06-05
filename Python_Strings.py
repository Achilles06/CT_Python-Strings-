#1. Product Review Analysis
#Task 1: Keyword Highlighter

def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]

    for review in reviews:
        highlighted_review = review
        for keyword in keywords:
            highlighted_review = highlighted_review.replace(keyword, keyword.upper())
        print(highlighted_review)

reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ] 

highlight_keywords(reviews)

#Task 2: Sentiment Tally
#I cant seem to get this to count correctly. 

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
positive_count = 0
negative_count = 0

def key_word_counter(reviews, positive_words, negative_words):
    for review in reviews:
        #positive_count = sum(1 for word in positive_words if word in review.lower())
        #negative_count = sum(1 for word in negative_words if word in review.lower())
        for word in positive_words:
            if word in review.lower():
                positive_count =+ 1 
        for word in negative_words:
            if word in review.lower():
                negative_count =+ 1

        
    print(f"Positive word count: {positive_count}")
    print(f"Negative word count: {negative_count}")

key_word_counter(reviews, positive_words, negative_words)

def create_summary(review, max_length=30):
    if len(review) <= max_length:
        return review
    else:
        # Find the last space before the max length
        last_space = review.rfind(" ", 0, max_length)
        if last_space == -1:
            # If no space found, just truncate
            return review[:max_length] + "..."
        else:
            return review[:last_space] + "..."
        
for review in reviews:
    summary = create_summary(review)
    print(summary)

#User Input Data Processor
#Task 1: Input Length Validator
def validate_name(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Both first name and last name must be at least 2 characters long.")
    else:
        print("Validation successful!")

user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")

validate_name(user_first_name, user_last_name)

#Task 2: Password Complexity Checker
def password_checker(password):
    if len(password) < 8:
        return "Password must be 8 characters long."
    elif not any(c.isupper() for c in password):
        return "Password must contain at least one uppercase letter."
    elif not any(c.islower() for c in password):
        return "Password must contain at least one lower case."
    elif not any(c.isdigit() for c in password):
        return "Password must contain at least one number."
    else:
        return "Password meets complexity requirements."
    
user_password = input("Enter your password: ")
result = password_checker(user_password)
print(result)

#Task 3: Email Formatter

#3. Interactive Help Desk Bot 
#Task 1: Command Parser
def process_user_input(user_input):
    predefined_commands = ["help", "issue", "contact support"]

    for command in predefined_commands:
        if command in user_input.lower():
            if command == "help":
                print("Sure! How can I assist you?")
            elif command == "issue":
                print("I apologize for any inconvenience. Please provide more details about the issue.")
            elif command == "contact support":
                print("You can contact our support team at support@example.com.")
            return

    print("No predefined command found. Feel free to continue with your input.")

user_text = input("Enter your text: ")
process_user_input(user_text)

#Task 2: Issue Categorizer
def categorize_issue(user_input):
    keywords = {
        "login": "Login-related issue",
        "performance": "Performance-related issue",
        "error": "Error or bug"
    }

    for keyword, category in keywords.items():
        if keyword in user_input.lower():
            return f"Issue category: {category}"

    return "Issue category not identified."


user_issue = input("Describe the issue: ")
print(categorize_issue(user_issue))