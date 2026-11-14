def normalize_us_phone(phone_input: str) -> str:
    """
    Cleans and formats a 10-digit U.S. phone number.
    Returns the formatted string or an error message if invalid.
    """
    # 1. Remove leading/trailing whitespace
    cleaned = phone_input.strip()

    # 2. Replace formatting characters with spaces
    for ch in ["-", "(", ")", "."]:
        cleaned = cleaned.replace(ch, " ")

    # 3. Join pieces back together to isolate only the digits
    parts = cleaned.split()
    digits_only = "".join(parts)

    # 4. Validate length and format the output
    if len(digits_only) == 10:
        area = digits_only[0:3]
        mid = digits_only[3:6]
        end = digits_only[6:]
        return f"({area}) {mid}-{end}"
    else:
        return "Error: Please enter exactly 10 digits."


# This block lets you run the script interactively
if __name__ == "__main__":
    user_input = input("Enter a U.S. phone number (any format): ")
    result = normalize_us_phone(user_input)
    print(f"formatted number: {result}")
