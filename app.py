import streamlit as st

class User:
    """ A class to represent a user's profile. """
    def __init__(self, name: str, email: str = '', date_of_birth: str = '', zip_code: str = ''):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.zip_code = zip_code
        self.preferences = {}

    def update_profile(self, **kwargs):
        """ Update user profile attributes. """
        for key, value in kwargs.items():
            setattr(self, key, value)

def main():
    """ Main function to drive the Streamlit app. """
    st.title("Legislative Impact Advisor")

    # User name input and basic greeting
    user_name = st.sidebar.text_input("Enter your name to get started:")
    user = User(user_name)

    if user_name:
        st.sidebar.success(f"Welcome, {user_name}! Let's get started.")
        if st.sidebar.button("Start Chat"):
            start_chat(user)

def start_chat(user):
    """ Handles the chat interface and supporting columns. """
    # Layout: three columns (News, Chat, Preferences)
    news_col, chat_col, prefs_col = st.columns([1, 2, 1])

    with news_col:
        st.subheader("Latest News")
        display_news()

    with chat_col:
        st.subheader("Chat Interface")
        handle_chat()

    with prefs_col:
        st.subheader(f"{user.name}'s Preferences")
        display_preferences(user)

def display_news():
    """ Display dummy news content. """
    st.write("Here are the latest updates on relevant bills and legal actions:")
    st.write("1. Bill 1234: New traffic laws coming to the Bay Area.")
    st.write("2. Bill 5678: Changes in tax regulations that might impact your monthly budget.")
    st.write("3. Bill 91011: Healthcare reforms and what they mean for your family.")

def handle_chat():
    """ Simulate a chat interface where users can type messages. """
    user_input = st.text_input("Type your question here...")
    if user_input:
        st.write("Bot Response: We are processing your question...")

def display_preferences(user):
    """ Display user preferences if available. """
    if user.preferences:
        st.write("Your Preferences:")
        for key, value in user.preferences.items():
            st.write(f"{key}: {value}")
    else:
        st.write("No specific preferences set. Let's learn more about your interests!")
        if st.button("Set Preferences"):
            user.preferences = {"Interest": "Healthcare", "Concern": "Taxation"}
            st.write("Preferences updated!")

if __name__ == "__main__":
    main()
