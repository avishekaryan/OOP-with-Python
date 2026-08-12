# Socket Programming Questions

## 1. Basic Concepts

1. Define the following terms:
   - Socket
   - Protocol
   - IP address
   - Port
   - Localhost

2. Explain the difference between a **client** and a **server** in the TCP client-server model.

3. What is the role of the following in Python socket programming?
   - `socket.AF_INET`
   - `socket.SOCK_STREAM`

4. Why do we use **ports** in addition to **IP addresses**?

5. What does the `SO_REUSEADDR` socket option do, and why is it important?

---

## 2. TCP vs UDP

1. Compare **TCP** and **UDP** in terms of:
   - Reliability
   - Message ordering
   - Typical use cases

2. Give one example of a real-world application that is best implemented with:
   - TCP
   - UDP

3. Briefly explain the **TCP three-way handshake**.

---

## 3. Python Client Code

1. Write a short Python TCP client that:
   - Connects to `localhost` on port `65432`
   - Sends the text `"Hello Server"`
   - Receives a response
   - Prints the response as a string

2. Why should a client use `sendall()` instead of `send()`?

3. What happens if you call:

   ```python
   sock.sendall("Hello")
   ```

   without encoding the string?

4. What exception is raised when the server is not running and the client attempts to connect?

---

## 4. Python Server Code

1. List the **six main steps** of a TCP server program.

2. In the daytime server example, explain the purpose of each of the following:

   - `bind((HOST, PORT))`
   - `listen(5)`
   - `accept()`

3. How does a server detect that a client has disconnected cleanly using `recv()`?

4. Why is it important to wrap sockets with `with` in Python?

---

## 5. Error Handling and Best Practices

1. Describe how to handle the following exceptions in a client:
   - `socket.timeout`
   - `ConnectionRefusedError`

2. Why should you never send raw exception messages back to a client in production?

3. What is the risk of binding a development server to `0.0.0.0` instead of `localhost`?

4. Why is it important to set a maximum receive size when calling `recv(n)`?

---

## 6. Concurrency and Protocol Design

1. Explain the difference between an **iterative server** and a **threaded server**.

2. How does using:

   ```python
   threading.Thread(..., daemon=True)
   ```

   affect server shutdown behavior?

3. What is a simple **line-based text protocol**, and why is `makefile()` useful for implementing it?

4. Describe a protocol design for a chat server that supports a `QUIT` command.

5. What are the three main responsibilities of a server in a client-server architecture?