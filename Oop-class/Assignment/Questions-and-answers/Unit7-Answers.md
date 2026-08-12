# Unit 7 — Socket Programming

## Definition Type Questions (2 Marks)

### Q1. Define the following terms: Socket, Protocol, IP address, Port, Localhost.

- These five terms together describe how two programs find and talk to each other over a network, so it helps to define them as a connected set rather than in isolation.
- A socket is the actual endpoint through which a program sends and receives data — think of it as the "plug" a program uses to join the network, identified by an IP address plus a port number.
- A protocol is simply the agreed set of rules two sides follow so the data makes sense to both of them — for example TCP, UDP, or HTTP.
- An IP address is what identifies which device on the network the data should reach.
- A port then narrows this down further — it tells the device which particular application on it should receive the data, since one device can run many programs at once.
- Localhost (`127.0.0.1`) is a special address that simply means "this same computer," which is why it is used to test a client and server running side by side on one machine.

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # the socket
sock.connect(("localhost", 65432))   # localhost + port
```

---

### Q2. What is the role of `socket.AF_INET` and `socket.SOCK_STREAM`?

- When a socket is created in Python, these two arguments are what actually decide what kind of socket it will be.
- `socket.AF_INET` sets the address family — in plain terms, it tells the socket to expect IPv4-style addresses.
- `socket.SOCK_STREAM` sets the socket type — it tells the socket to behave like TCP, i.e. reliable and in order, rather than the fire-and-forget style of UDP.

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # IPv4 + TCP
```

---

### Q3. What exception is raised when the server is not running and the client attempts to connect?

- If a client tries to reach a server that simply is not there, Python does not fail silently — it raises `ConnectionRefusedError`.
- This happens right at the `connect()` call, because the operating system itself reports back that nothing is listening on that port.

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(("localhost", 65432))   # no server running here
except ConnectionRefusedError:
    print("Server is not available")
```

---

### Q4. What happens if you call `sock.sendall("Hello")` without encoding the string?

- Since sockets only understand raw bytes and not Python strings, this line does not run quietly — it raises a `TypeError`.
- The fix is to convert the string into bytes first, using `.encode()`, before it is handed to the socket.

```python
# sock.sendall("Hello")            # TypeError: str does not support buffer
sock.sendall("Hello".encode())     # correct
```

---

## 6 Mark Questions

### Q1. Explain the difference between a client and a server in the TCP client-server model.

- To answer this, it helps to think in terms of who acts first and who waits.
- The server is the one that waits — it starts up, binds itself to a fixed IP address and port, and then simply listens for anyone who wants to connect.
- The client, on the other hand, is the one that acts — it already knows the server's address and actively initiates the connection using `connect()`.
- Once connected, both sides can send and receive data, but only the client can start a new connection; the server can only respond to one that already exists.
- In practice, this is why the server tends to stay running continuously, while a client connects, does its work, and disconnects — a web browser connecting to a website is a familiar everyday example of this pattern.

```python
# server (waits)
server_sock.bind(("localhost", 65432))
server_sock.listen()
conn, addr = server_sock.accept()   # blocks until a client connects

# client (acts)
client_sock.connect(("localhost", 65432))
```

---

### Q2. Why do we use ports in addition to IP addresses?

- An IP address alone only tells the network which device to deliver data to — it says nothing about which program on that device should actually receive it.
- Since a single device can be running a web server, a mail server, and a chat server all at once, some way of separating their traffic is needed — that is exactly what a port number does.
- So it is really the pair — IP address plus port, e.g. `192.168.1.5:80` — that uniquely points to one specific application on one specific device.
- Without this pairing, the operating system would have no way of knowing which running program an incoming packet was actually meant for.

---

### Q3. What does the `SO_REUSEADDR` socket option do, and why is it important?

- Normally, after a server closes, the operating system holds the port in a `TIME_WAIT` state for a short while, in case any delayed packets are still arriving.
- This is usually harmless, except that it also stops the same script from being restarted immediately, since the port still looks "busy."
- `SO_REUSEADDR`, set using `sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)` before `bind()`, tells the OS to allow reuse of that port anyway.
- This matters most during development, where a server script is stopped and restarted frequently — without it, each restart could fail with an "address already in use" error.

---

### Q4. Give one example of a real-world application best implemented with TCP, and one with UDP.

- Which protocol fits best really comes down to what matters more for that application: getting every byte correctly, or getting data quickly.
- For something like file transfer or web browsing (HTTP/HTTPS), correctness matters far more than a few milliseconds of delay, so TCP is the natural fit here.
- For something like a live video call or online gaming, on the other hand, a slightly dropped packet is usually less noticeable than a delay caused by waiting for it to be resent — so UDP is preferred instead.
- This trade-off between reliability and speed is really the deciding factor whenever choosing between the two.

---

### Q5. Briefly explain the TCP three-way handshake.

- Before any actual data can be exchanged, TCP first needs both sides to agree that a connection exists — this agreement is what the three-way handshake achieves.
- It begins with the client sending a `SYN` packet, essentially asking the server, "can we start a connection?"
- The server then answers with a `SYN-ACK`, which both agrees to the request and makes its own request back.
- Finally, the client responds with an `ACK`, confirming the agreement — only after this final step is the connection considered fully established.

```
[Client: SYN ->] [Server: SYN-ACK <-] [Client: ACK ->] [Connection Established]
```

---

### Q6. Why should a client use `sendall()` instead of `send()`?

- The catch with plain `send()` is that it does not promise to send everything you give it in one go — it may only manage part of the data, and it is up to the programmer to notice this and send the rest.
- That means using `send()` correctly would require manually looping and tracking how many bytes are still left to send, which is easy to get wrong.
- `sendall()` removes this burden entirely — internally, it keeps sending until either the full message has gone through or an error occurs.
- Because of this, `sendall()` is the safer and more common choice for straightforward client/server messaging in Python.

---

### Q7. List the six main steps of a TCP server program.

- Every TCP server, no matter how complex, is really built around the same six-step skeleton.
- 1. Create a socket with `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`.
- 2. Bind it to an address and port using `bind((HOST, PORT))`, so clients know where to find it.
- 3. Put it into listening mode with `listen(n)`, so it is ready to accept connections.
- 4. Accept an incoming connection with `accept()`, which hands back a fresh socket for talking to that particular client.
- 5. Exchange data over that connection using `recv()` and `sendall()`.
- 6. Close the connection once the exchange is done, freeing it up for the next client.

```python
[socket()] -> [bind()] -> [listen()] -> [accept()] -> [recv()/send()] -> [close()]
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 1. create
s.bind(("localhost", 65432))                            # 2. bind
s.listen(5)                                              # 3. listen
conn, addr = s.accept()                                  # 4. accept
data = conn.recv(1024)                                   # 5. recv/send
conn.sendall(data)
conn.close()                                             # 6. close
```

---

### Q8. Explain the purpose of `bind((HOST, PORT))`, `listen(5)`, and `accept()`.

- These three calls together take a bare socket and turn it into a working server, each one adding one piece of that behaviour.
- `bind((HOST, PORT))` is what reserves a specific address and port for the server, so clients have somewhere fixed to connect to.
- `listen(5)` then switches the socket into listening mode, and the `5` sets how many pending connections can queue up before new ones are refused.
- Finally, `accept()` is where the server actually pauses and waits for a client — once one arrives, it hands back a brand-new socket dedicated to that client, while the original socket goes back to listening for the next one.

```python
s.bind(("localhost", 65432))
s.listen(5)               # up to 5 pending connections can queue
conn, addr = s.accept()   # blocks, then returns a new socket for this client
print("Connected by", addr)
```

---

### Q9. How does a server detect that a client has disconnected cleanly using `recv()`?

- Interestingly, `recv()` does not raise an error when a client disconnects politely — instead, it simply returns an empty bytes object, `b''`.
- This is a useful distinction: any real message will always come back as non-empty bytes, so an empty result is the clear signal that nothing more is coming.
- This is why server loops typically include a check like `if not data: break` right after `recv()`, to stop reading from a client that has left.
- If the client instead disappears abruptly rather than closing cleanly, the server is more likely to see an exception such as `ConnectionResetError` instead.

```python
while True:
    data = conn.recv(1024)
    if not data:            # empty bytes = client disconnected cleanly
        break
    print("Received:", data.decode())
conn.close()
```

---

### Q10. Why is it important to wrap sockets with `with` in Python?

- Writing `with socket.socket(...) as sock:` matters because it guarantees `sock.close()` gets called automatically once the block ends — whether that block finished normally or was interrupted by an error.
- Without it, closing the socket becomes the programmer's own responsibility on every single exit path, and it is easy to forget one, especially the error path.
- Left unclosed, sockets quietly use up file descriptors and ports, which becomes a real problem in a server that keeps running or looping over many clients.
- So really, this is the same safety pattern already familiar from file handling in Python, just applied to network connections instead.

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("localhost", 65432))
    sock.sendall(b"Hello")
# socket is automatically closed here, even if an error occurred
```

---

### Q11. Describe how to handle `socket.timeout` and `ConnectionRefusedError` in a client.

- Both of these are things that can genuinely go wrong when a client tries to reach a server, so handling them well makes the difference between a clean message and a crash.
- `socket.timeout` shows up when an operation such as `connect()` or `recv()` takes longer than the limit set with `sock.settimeout(seconds)`.
- `ConnectionRefusedError` shows up when the server side simply is not there to accept the connection at all.
- The straightforward way to handle both is to wrap the socket calls in `try/except`, so the client can explain what went wrong instead of just crashing.

```python
try:
    sock.settimeout(5)
    sock.connect((HOST, PORT))
except socket.timeout:
    print("Connection timed out")
except ConnectionRefusedError:
    print("Server is not available")
```

---

### Q12. Why should you never send raw exception messages back to a client in production?

- It might seem helpful to just forward the error straight to the client, but this ends up sharing more than it should.
- A raw exception often contains internal details — file paths, database structure, stack traces — which is exactly the kind of information an attacker could use against the system.
- The safer approach is to log the full exception on the server for developers to see, while the client only receives something generic, such as "An error occurred."
- This follows a broader security habit worth remembering: never expose implementation details to users who do not need them.

---

### Q13. What is the risk of binding a development server to `0.0.0.0` instead of `localhost`?

- Binding to `localhost` (`127.0.0.1`) keeps things safely contained, since only the same machine can connect to the server.
- Binding to `0.0.0.0` instead opens the server up on every network interface, meaning other devices on the network — or beyond, if exposed — can reach it too.
- For a development server, which is often unfinished, unauthenticated, or full of debug information, that extra reach is exactly the problem, since it can be discovered and attacked far more easily.
- So `0.0.0.0` should really only be used once the server is deliberately meant to be reachable and has been properly secured for it.

---

### Q14. Why is it important to set a maximum receive size when calling `recv(n)`?

- The value `n` in `recv(n)` is not just a technical detail — it is what limits how much data the server is willing to accept in a single call.
- Without a sensible bound (like 1024 or 4096), a faulty or malicious client could send an enormous or endless stream of data, and the server would keep consuming memory trying to receive it.
- Keeping `n` fixed and reasonable keeps memory use predictable no matter what a client sends.
- For anything larger than one call can hold, the safer approach is to read it in a loop across several bounded `recv()` calls, rather than trying to receive it all at once.

```python
chunks = []
while True:
    chunk = conn.recv(4096)   # bounded, e.g. 4KB at a time
    if not chunk:
        break
    chunks.append(chunk)
```

---

### Q15. How does `threading.Thread(..., daemon=True)` affect server shutdown behavior?

- This setting decides whether Python waits for that thread before letting the whole program close.
- A daemon thread is allowed to be abandoned — if the main program ends, daemon threads are simply stopped along with it, with no waiting.
- So if every client-handling thread is created with `daemon=True`, the server process can exit immediately when the main thread stops, even mid-conversation with a client.
- Without `daemon=True`, the opposite happens — the program would sit and wait for every one of those threads to finish naturally before it can close.
- This is why `daemon=True` is common in simple servers, since it lets something like Ctrl+C shut everything down cleanly rather than leaving it hanging.

```python
import threading
conn, addr = s.accept()
t = threading.Thread(target=handle_client, args=(conn,), daemon=True)
t.start()   # this thread won't block the program from exiting
```

---

### Q16. What is a simple line-based text protocol, and why is `makefile()` useful for implementing it?

- A line-based text protocol keeps things simple by treating every message as plain text ending in a newline character (`\n`) — nothing more complicated than that.
- The difficulty is that raw `recv()` calls do not naturally respect these line breaks, so reconstructing one clean line at a time normally needs manual buffering.
- `sock.makefile('r')` avoids that hassle by wrapping the socket so it behaves like a normal file, meaning `.readline()` can be used directly instead.
- That single change makes reading "one full message at a time" almost effortless, which is exactly why simple protocols like a chat server or command-based server tend to rely on it.

```python
conn_file = conn.makefile("r")
for line in conn_file:
    line = line.strip()
    print("Received line:", line)
```

---

### Q17. What are the three main responsibilities of a server in a client-server architecture?

- Underneath all the specific features a server might have, its job really comes down to three consistent responsibilities.
- 1. Listening — binding to an address/port and staying ready for clients to connect.
- 2. Handling requests — once a client is connected, reading what it sends and working out what should be done with it.
- 3. Responding — sending the result back to the client, and deciding whether to keep the connection open for more messages or close it.

---

## 12 Mark Questions

### Q1. Compare TCP and UDP in terms of reliability, message ordering, and typical use cases.

**Introduction**

TCP and UDP are both ways of sending data across a network, but the question really being asked here is: what do you give up, and what do you gain, by choosing one over the other?

**Body**

- On reliability, TCP is connection-oriented and actively guarantees delivery — every packet is acknowledged, and anything lost is automatically resent. UDP makes no such promise; a packet can simply vanish, and neither side is notified.
- On ordering, TCP takes responsibility for reassembling data in exactly the order it was sent, even if individual packets arrive out of sequence. UDP does not bother with this at all — datagrams may arrive in any order, and it is left entirely to the application to sort that out if it matters.
- There is also a setup difference worth noting: TCP cannot send anything until the three-way handshake has established a connection, whereas UDP can simply fire off a datagram immediately, with no handshake at all.
- This connects directly to speed: all of TCP's reliability machinery — acknowledgements, retransmission, ordering — adds overhead, while UDP's simplicity is precisely what makes it faster and better suited to real-time data.
- So when it comes to typical use cases, TCP suits things like web browsing, file transfer, and email, where getting complete and correct data matters more than shaving off milliseconds.
- UDP, by contrast, suits things like live video calls, online gaming, and DNS lookups, where a slightly dropped packet is far less disruptive than waiting for it to be resent.

**Conclusion**

Ultimately, the comparison comes down to one trade-off repeated in different forms — reliability versus speed — and the right protocol is simply whichever side of that trade-off the application actually needs.

---

### Q2. Write a short Python TCP client that connects to localhost on port 65432, sends "Hello Server", receives a response, and prints it as a string.

**Introduction**

Writing a TCP client is really just a matter of following the same short sequence every time: open a socket, connect it, send something, wait for a reply, and read that reply back.

**Body**

- Since sockets only work with raw bytes, the string being sent has to be encoded first, and whatever comes back has to be decoded before it is readable again.

```python
import socket

HOST = "localhost"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall("Hello Server".encode())
    data = sock.recv(1024)
    print("Received:", data.decode())
```

- Here, `with socket.socket(...) as sock:` takes care of closing the socket automatically, so nothing is left open by accident.
- `sock.connect((HOST, PORT))` is what actually reaches out and opens the connection to the server.
- `sock.sendall("Hello Server".encode())` converts the text into bytes and makes sure the complete message gets sent, not just part of it.
- `sock.recv(1024)` then waits for the server's reply, and `.decode()` turns that reply back into a normal, readable string.

**Conclusion**

Once this create-connect-send-receive-close pattern is understood, it can be reused almost unchanged for any simple TCP client, which is exactly why it is worth remembering as a template rather than just one example.

---

### Q3. Explain the difference between an iterative server and a threaded server.

**Introduction**

Both of these are valid ways to build a TCP server, and the real question they raise is: what happens when more than one client wants to talk to the server at the same time?

**Body**

- An iterative server answers this by not really solving it — each client is accepted, fully handled from start to finish, and only then does the server move on to `accept()` the next one, meaning clients are served strictly one after another.
- A threaded server takes a different approach: as soon as a client connects, it is handed off to its own thread (for example, `threading.Thread(target=handle_client, args=(conn,))`), and the server immediately goes back to `accept()` the next client, so multiple clients end up being served at the same time.
- This has a direct consequence in practice: in an iterative server, one slow or long-lived client blocks every other client behind it, since nothing else can be served until that one finishes.
- A threaded server avoids that particular problem, but it introduces its own — now the programmer has to think about thread safety (protecting any shared data with locks) and about resource limits, since too many threads can overwhelm the system.

```
[Iterative] [accept] -> [handle client fully] -> [accept next client] -> ...
[Threaded] [accept] -> [spawn thread to handle client] -> [accept next client immediately] -> (threads run in parallel)
```

- This is also why the right choice depends on the situation: an iterative server is perfectly fine for something quick like a daytime or echo server, whereas a chat server — where clients stay connected for a long time and need serving simultaneously — really calls for a threaded design.

**Conclusion**

In short, the choice between iterative and threaded servers is a trade-off between simplicity and responsiveness, and most real applications involving multiple long-lived clients end up needing the threaded (or asynchronous) approach.

---

### Q4. Describe a protocol design for a chat server that supports a QUIT command.

**Introduction**

Designing this protocol really means answering two questions at once: how are ordinary chat messages represented, and how does the server tell an ordinary message apart from a request to leave?

**Body**

- The simplest solution is a line-based text protocol — every message a client sends is plain text ending in a newline (`\n`), which the server can read cleanly using `makefile()` and `.readline()`.
- In normal use, once a client connects and is accepted, whatever line it sends is simply broadcast out to all the other connected clients, so everyone sees the conversation.
- The `QUIT` command is handled by treating it as a special case: if an incoming line is exactly `QUIT`, the server does not broadcast it as a chat message — instead, it understands this as the client's intent to disconnect.

```python
for line in conn_file:
    line = line.strip()
    if line == "QUIT":
        broadcast(f"{username} has left the chat")
        break
    else:
        broadcast(f"{username}: {line}")
conn.close()
```

- Once `QUIT` is received, the server has a clear sequence to follow: stop reading further from that client, let everyone else know they have left, remove them from the active client list, and close their socket.

```
[Client sends line] -> QUIT? -> yes -> [notify others, remove client, close socket] | no -> [broadcast message to all clients]
```

- This design works best alongside a threaded server, since each client is handled in its own thread — meaning one client typing `QUIT` has no effect on anyone else's ongoing conversation.

**Conclusion**

What makes this design effective is not complexity but clarity — a simple text protocol with one clearly defined command is enough to let the chat server support graceful, predictable disconnection without extra machinery.

---
