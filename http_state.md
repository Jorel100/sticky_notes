# HTTP State Preservation in Web Applications

## Overview

HTTP is inherently stateless, which poses a challenge for web applications that need to maintain state across multiple requests. Various techniques are employed to overcome this limitation, ensuring a seamless user experience.

## Techniques for State Preservation

### 1. Cookies

Cookies are small pieces of data stored by the client’s browser. They are sent with every HTTP request to the server.

- **Example**: 
  ```http
  Set-Cookie: sessionId=abc123; Path=/; HttpOnly

### 2. Sessions

Sessions store data on the server side. The client holds a session ID in a cookie, and the server uses this ID to retrieve session data.

 # Setting a session value
request.session['username'] = 'jorel_jack'

### 3. Url Patterns

State information can be passed through URL parameters.

# Example
https://example.com/profile?user=123

### 4.  Web Storage (Local Storage and Session Storage)

HTML5 provides local storage and session storage for storing data on the client side.

# Example
// Local storage
localStorage.setItem('username', 'john_doe');
// Session storage
sessionStorage.setItem('username', 'john_doe');


### User Authentication
Process:
User submits credentials.
Server validates credentials and responds with a token or sets a cookie.
Client includes token or cookie in subsequent requests.

### Session Management in Django
Django handles sessions using middleware and stores session data in the database by default.

# Accessing session data
username = request.session.get('username', 'Guest')









