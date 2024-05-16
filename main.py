dic = {('1', 'happy'): 'be happy with what you got', ('2', 'sad'): 'watch Hitori Bocchi', ('3', 'angry'): 'play doom', ('4', 'shy'): 'Be Brave'}

# Get user input with a prompt
sht = input('how do you feel today? \n 1 happy, 2 sad, 3 angry, 4 shy ').strip().lower()

# Check if the input is a valid number or emotion
result = next((value for key, value in dic.items() if sht in key), 'Invalid input. Please enter a valid number or emotion.')

print(result)
