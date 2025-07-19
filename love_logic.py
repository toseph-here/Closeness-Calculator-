def calculate_love_percentage(text):
    text = text.lower().replace("/", "").replace("love", "").strip()

    if " and " in text:
        names = text.split(" and ")
        if len(names) == 2:
            combined = names[0].strip() + names[1].strip()
            score = sum(ord(c) for c in combined if c.isalpha())
            percentage = (score % 101) + 7
            return f"❤️ Mutual closeness score between {names[0]} and {names[1]} is: {percentage}%"
        else:
            return "❌ Invalid input format. Use: /love Name1 and Name2"
    
    elif " for " in text:
        names = text.split(" for ")
        if len(names) == 2:
            combined = names[0].strip()
            score = sum(ord(c) for c in combined if c.isalpha())
            percentage = (score % 101) + 7
            return f"💌 Feelings of {names[0]} for {names[1]}: {percentage}%"
        else:
            return "❌ Invalid input format. Use: /love Name1 for Name2"
    
    else:
        return "❓ Use format: /love Name1 and Name2 or /love Name1 for Name2"
