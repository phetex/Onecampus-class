def detect_foul_language(text):
    fLang = ['stupid', 'crazy', 'clown', 'idiot', 'mad', 'bastard', 'bitch', 'fool', 'niggar']
    
    # Convert the text to lowercase for case-insensitive matching
    text = text.lower()
    
    # Check if any foul language word exists in the text
    for word in fLang:
        if word in text:
            return True
    
    return False

# Test the function
is_foul_language = detect_foul_language(text)
print("Contains foul language:", is_foul_language)
