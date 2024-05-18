from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_response(user_input):
  """Generates a response from the AI based on the user's input."""
  completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "user", "content": user_input},
      ]
  )

  return completion.choices[0].message

def is_exit_command(user_input):
  """Checks if the user input is an exit command."""
  return user_input.lower() in ["exit", "quit", "bye"]

# Start the conversation
print("AI: Hello!")
while True:
  # Get user input
  user_input = input("User: ")

  # Check if the user wants to exit
  if is_exit_command(user_input):
    break

  # Generate AI response
  ai_response = generate_response(user_input)

  # Print AI response
  print("AI:", ai_response)
