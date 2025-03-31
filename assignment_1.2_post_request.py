'''
Assignment 1.2: Modifying a Socket Example to Send a POST Request
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_1.2_post_request.py

Objective: This code demonstrates how to send a POST request using Python's 
socket library. Modify a basic socket example to send a POST request. POST 
requests allow you to send data to a server, such as form submissions. We’ll
keep things simple by using plain text data instead of JSON.

Prerequisites:

a) Understand What POST Requests Do
A POST request sends data from the client (your program) to the server.
For example, you can send information like "name=John&age=30".

b) Choose the Data to Send
Decide on the information you want to send. For this example, we will
send the following: name=John&age=30.

1) Update the HTTP Request Line
Change the first line of your request from GET to POST. It should now
look like:

POST /post HTTP/1.1

4) Add Required HTTP Headers
Include headers that describe the type and size of the data you’re sending:

    * Content-Type: application/x-www-form-urlencoded – Tells the server 
    you're sending form-style data.
    * Content-Length: 17 – The length of the data, which in this case is 17
    characters (name=John&age=30).

5) Prepare the Request Body
The body contains the data you are sending. For example:
    name=John&age=30

6) Combine Everything into a Full Request
The complete request should look like this (in text format):

POST /post HTTP/1.1
Host: postman-echo.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 17

name=John&age=30
      
Notice the blank line between the headers and the body.

7) Send the Request
Use the send() method of your socket object to send this request to the server.

8) Receive and Display the Response
Use the recv() method of your socket object to receive the server’s response.
Print it to the console to verify that the server echoes back the data you
sent.

'''

# Import the socket library
import socket

# set variables
host = "postman-echo.com"   # server name
port = 80             # port number for http
content_type = "application/x-www-form-urlencoded"  # Content-Type header

post_message = "POST /Post HTTP/1.1\r\n"
post_message += f"Host: {host}\r\n"
post_message += f"Content-Type: {content_type}\r\n"
post_message += "Content-Length: 16\r\n\r\n"  # 16 characters
post_message += "name=John&age=30" # Body of the POST request
post_message += "\r\n"  # End of headers

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server - provide server name or address and port
server_address = (host, port)
client_socket.connect(server_address)

# 1 modify initial request to be a POST vs GET
print()
print("Post Request sent to server...")
print()
client_socket.send(post_message.encode())  # Send data to the server

# Step 4: Receive the response
response_from_post = client_socket.recv(4096)  # Receive up to 4096 bytes
print("Response from server:")
print()
print(response_from_post.decode())  # Print the response

# Step 5: Close the connection
client_socket.close()
