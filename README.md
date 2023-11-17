
# Decimal to Hexadecimal Conversion using Python - TCP and UDP
This GitHub project demonstrates a simple client-server application for converting decimal numbers to their hexadecimal equivalents using Python. The project specifically focuses on the practical application of TCP and UDP communication protocols.

## Technologies Utilized:
***Python***: Primary programming language for implementing the client-server architecture and decimal to hexadecimal conversion logic.
***Socket Programming***: Utilized for establishing communication between client and server over a network.
TCP (Transmission Control Protocol) and UDP (User Datagram Protocol): Transport layer protocols used for communication between the client and server.

## Description:
This repository contains Python scripts for both the server and client sides. The server script listens for incoming connections and performs decimal to hexadecimal conversion upon receiving an integer input from the client. The client script initiates the connection and sends the decimal input to the server, receiving the hexadecimal output in return.

## Server Process:
The TCP server script creates a socket, binds it to a specified IP address and port, listens for incoming connections, and upon connection, performs the decimal to hexadecimal conversion.

## Client Process:
The TCP client script creates a socket, connects to the server's IP address and port, sends an integer input to the server, and receives the hexadecimal output.

## Usage:
Clone the repository.
Run the server script on the host machine.
Run the client script on another machine or in a separate terminal window, providing an integer input for conversion.
View the hexadecimal output received from the server on the client-side.

## Conclusion:
This project serves as a practical illustration of client-server communication using TCP and UDP protocols and showcases the conversion of decimal numbers to hexadecimal equivalents. The provided references offer additional insights into socket programming and client-server architectures.