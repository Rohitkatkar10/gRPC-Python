Both-streaming folder

In this folder, we are using stream-stream RPC(Remote procedure call) method.
Here we are getting multiple requests from client and in response server will respond
to every request.

we can have multiple clients & connect them to single server. For that we need to define number of thread (max_thread=N)
in server. This means how many client that we want to connect with server. I have set "N" value as 100.
Meaning we have up to 100 clients to this server. you can have any number there.

To run multiple clients in one go use "multiple_client.py" file. we can mention number clients that we want
to run in one go. server will respond each client and will not mismatch response or will not give one clients response
to another client.

--XXX--