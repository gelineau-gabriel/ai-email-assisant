from email_assistant.analyzer import analyze_email

def main():
    print("=== AI email assistant === \n")
    email=input("Enter your email:")
    result=analyze_email(email)
    print(f"priority : {result.priority} \n summary : {result.summary} \n suggested reply : {result.suggested_reply} \n key points :")
    for element in result.key_points:
        print("-"+element) 

if __name__ == "__main__":
    main()