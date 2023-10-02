# hbd_generator
Happy birthday generator using ChatGPT OpenAI API.

The goal of this project is to develop an API that can run on localhost, so I can simulate receiving input and returning answers to a hypothetical front-end, that can be developed later as a follow-up project.

This API will run on top of the OpenAI API, basically organizing distinct input in order to provide a structured command for ChatGPT. It demonstrates how easy it is to use AI via already existing APIs.

To start, you'll need a way to run a local server that listens for incoming HTTP requests. You can use a web framework like Flask or FastAPI for this purpose. We'll use Flask in this example.

After configuring Flask, you'll need to create an endpoint that accepts POST requests and sends them to the OpenAPI model to get a response.

## Running the app step by step

First, you need to set up a Flask application. You can do this by installing Flask if you haven't already:

```pip install Flask```

Now, check the app.py file for the basic server configuration, make the necessary adjustments if any and kick-off the server with ```python app.py``` command. Your Flask app will start on localhost at the default port 5000.

Accessing localhost in port 5000 directly will return an error, given that there is no defined route for this URL. However, it should be possible to access the defined route for both GET and POST requests: http://localhost:5000/birthday-messages

Finally, to test it with Postman, send a POST request to http://localhost:5000/generate with JSON data containing the parameters you want to use for generating the message. It is possible to configure the following variables:

- friend_name
- relationship_type
- words to be included on the message
- maximum number of words
- style
- language for the message

Please see the examples below for illustrative purposes:

**Example 1 - Alice**
```
{
  "friend_name": "Alice",
  "relationship_type": "friend",
  "words": [
    "flowers", 
    "red", 
    "love"],
  "max_words": 50,
  "style": "greeting"
}
```

![alice](images/AliceRequest.png)

**Example 2 - Bob**
```
{
    "friend_name": "Bob",
    "relationship_type": "best friend",
    "words": [
        "skate",
        "adventures",
        "crazy"
    ],
    "max_words": 100,
    "style": "rhyme",
    "language": "english"
}
```
![bob](images/BobRequest.png)


If any of this values is not specified, defaults will be used to fill out the missing details, as in this empty JSON string example that defaults to a poem for a work colleague named John.

![john](images/JohnRequest.png)

Finally, it is possible to use the GET method to retrieve previous generated HBD messages. This might be useful in case the user generated multiple messages in a row and wants to go back to a previous generated version, for example.

![GetPreview](images/GetPreview.png)

## Next steps

The goal of this project was simply to try out ChatGPT API, but I decided to list a suggestion of next steps for those who want to build on the code I have already created or to my future self:

1. Improve validation and error handling 
2. Data persistence
3. User authentication and authorization
4. Rate limit and throttling
5. API documentation