
# College Assistant Agent

college_info = {
    "timing": "College timing is 9:00 AM to 4:00 PM.",
    "library": "The library is open from 9:00 AM to 5:00 PM.",
    "attendance": "Maintain at least the attendance required by your college.",
    "exam": "Check the official college notice for exam dates.",
    "subjects": "You can ask your faculty for the current subject list."
}

print("🎓 Welcome to College Assistant!")
print("Ask about timing, library, attendance, exam, or subjects.")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ").lower().strip()

    if question == "exit":
        print("Assistant: Goodbye!")
        break

    found = False

    for keyword, answer in college_info.items():
        if keyword in question:
            print("Assistant:", answer)
            found = True
            break

    if not found:
        print("Assistant: Please contact your college office for this information.")
