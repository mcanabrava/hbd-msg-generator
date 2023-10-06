# streamlit_app.py
import streamlit as st
import requests

def main():
    st.title("Happy Birthday Message Generator")

    # Add subtext below the title
    st.write("""Do you want to send a special birthday message but are feeling low on creativity today? No worries, I've got your back.
    \nFill in the fields below to create an awesome personalized HBD message
    (or just hit submit with the default values to check how it works!)""")

    # Create sorted lists for dropdown options
    relationship_options = sorted([
        'Friend', 'Work colleague', 'Best friend', 'Wife', 'Husband', 'Boyfriend', 
        'Girlfriend', 'Mother', 'Father', 'Grandfather', 'Grandmother', 'Son', 
        'Daughter', 'Grandson', 'Granddaughter', 'Aunt', 'Uncle', 'Teacher', 
        'Enemy', 'Worst enemy', 'Sister', 'Brother'
    ])
    
    language_options = sorted([
        'English', 'Portuguese', 'Spanish', 'Italian', 'Turkish', 'Japanese', 
        'Chinese', 'Korean', 'Russian'
    ])

    # Form Header
    st.markdown("### Parameters")

    # Create a form to input data with default values
    friend_name = st.text_input("Birthday Person", "John")
    
    relationship_type = st.selectbox("Relationship Type", relationship_options, index=relationship_options.index('Friend'))  
    
    words = st.text_input("Key-words (comma-separated)", "parties, sports, crazy")  
    
    max_words = st.number_input("Max Words (50 - 500)", min_value=50, max_value=500, value=150)  
    
    style = st.selectbox("Style", ['Greeting', 'Poem'], index=0) 
    
    language = st.selectbox("Language", language_options, index=language_options.index('English'))  # Default: english


    # Description text for API Key
    st.markdown("### API Key")

    # Create input field for API key
    api_key = st.text_input("Enter your exclusive VIP key to try out the app", "")

    # Create a button to submit the form
    if st.button("Generate Message"):
        # Prepare the data to send to the Flask API
        data = {
            'friend_name': friend_name,
            'relationship_type': relationship_type,
            'words': words.split(','),
            'max_words': max_words,
            'style': style,
            'language': language
        }
        
        # Get the API key from the input field
        api_key_value = api_key.strip() 

        # Set up headers with the API key
        headers = {
            'Authorization': api_key_value
        }

        # Make a POST request to your Flask API with the headers
        api_endpoint = "https://hbd-generator-api-9f00c701fce0.herokuapp.com/birthday-messages" 
        response = requests.post(api_endpoint, json=data, headers=headers)

        if response.status_code == 201:
            st.success("Birthday message generated successfully:")
            st.write(response.json()) 
        else:
            st.error(f"Failed to generate the birthday message. Error: {response.status_code} - {response.text}")


    # Add a footer with a hyperlink
    # Create a CSS style to move the text to the bottom
css = """
<style>
.footer-text {
    position: absolute;
    bottom: 100x; /* Adjust this value as needed to control the vertical position */
    left: 240px; /* Adjust this value as needed to control the horizontal position */
    font-size: 14px; /* Adjust this value to make the text smaller */
}
</style>
"""

# Add the CSS style to the page
st.markdown(css, unsafe_allow_html=True)

# Add a footer with a hyperlink
st.markdown('<div class="footer-text">Created by Marcelo Canabrava, 2023. <a href="https://github.com/mcanabrava">Check out my GitHub for the source code.</a></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
