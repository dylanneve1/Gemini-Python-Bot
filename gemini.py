import google.generativeai as genai
from gtts import gTTS
import os

# Authentication (using your provided API key)
genai.configure(api_key='AIzaSyCL26YNMVu0u-z46hU7d1Hkw4FqNJkaCC4')

# Choose a Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat history (optional)
chat_history = []

def main():
  print("Welcome to the Gemini CLI Chat!")

  while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
      break 

    # Send request to Gemini
    response = send_message_to_gemini(user_input, model, chat_history)

    # Handle and display response
    print("Gemini:", response)
    speak(response) # Speak the response

    # Update chat history (optional)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "model", "content": response}) 

def send_message_to_gemini(message, model, history=[]):
  # Format history for the API 
  formatted_history = []
  for item in history:
    formatted_history.append({"role": item['role'], "parts": [item['content']]})

  # Create a chat object if it doesn't exist
  if not formatted_history:
    chat = model.start_chat()
  else:
    chat = model.start_chat(history=formatted_history) 

  # Send the user's message
  response = chat.send_message(message)

  # Return the response text
  return response.text 

def speak(text):
  """Speaks the given text using gTTS."""
  tts = gTTS(text=text, lang='en') # Use English 
  tts.save("response.mp3")        # Save to an MP3 file
  os.system("afplay response.mp3") # Play the MP3 file (macOS)
  # For Windows, use: os.system("start response.mp3")
  # For Linux, you might need to install a player like mpg123: os.system("mpg123 response.mp3")

if __name__ == "__main__":
  main()

