# 08_Networking_Security - Computer Networking & Security Protocols Study Guide

- **Total Cards**: 1384

---

## 📂 Category: 5G Core Networks (1 cards)

### 🔴 Senior Level

#### 1. What responsibilities does the SMF (Session Management Function) manage in the 5G Core network?
**Answer:**
It handles session management, IP address allocation and management, and acts as a DHCP-like service for user equipment.


## 📂 Category: Access Networks (1 cards)

### 🟡 Mid Level

#### 1. How does DOCSIS handle upstream and downstream channels?
**Answer:**
It uses frequency division multiplexing (FDM) to divide channels, allowing for multiple frequency channels with specified throughput.


## 📂 Category: Addressing & IPv4 (1 cards)

### 🟢 Junior Level

#### 1. What type of address space is reserved for private networks, such as a home network, according to RFC 1918?
**Answer:**
RFC 1918 reserves private IPv4 address spaces, including 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.


## 📂 Category: Application Layer (124 cards)

### 🟢 Junior Level

#### 1. Compare client-server and peer-to-peer (P2P) network architectures.
**Answer:**
In a client-server architecture, there is an always-on server that services requests from multiple clients, where clients do not communicate directly. In P2P architecture, hosts (peers) communicate directly with each other without dedicated servers, utilizing resources of user-controlled devices.

#### 2. Describe the relationship between DNS and applications like HTTP.
**Answer:**
DNS is used by applications like HTTP to resolve hostnames to IP addresses, allowing them to establish connections to web servers.

#### 3. Describe the typical process of transferring a web page using non-persistent connections.
**Answer:**
The client initiates a TCP connection, sends a request, receives a response, and then closes the connection, repeating this for each object in the page.

#### 4. Give an example of a canonical hostname and its alias.
**Answer:**
Canonical hostname: relay1.west-coast.enterprise.com; Alias: www.enterprise.com.

#### 5. How can cookies be used in web-based applications like email services?
**Answer:**
They help identify users during their session by storing a unique session identifier on the client side, allowing them to stay logged in and access their accounts seamlessly across HTTP requests.

#### 6. How do application-layer protocols typically operate?
**Answer:**
Application-layer protocols, like HTTP and SMTP, are usually implemented in software and facilitate communication between applications on different end systems.

#### 7. How do content distribution networks (CDNs) relate to web caches?
**Answer:**
CDNs install geographically distributed caches to localize traffic and improve access speeds.

#### 8. How do cookies enable a website to identify users?
**Answer:**
By sending a unique identification number in a cookie header within the HTTP response, which the browser stores and sends back in future requests.

#### 9. How does DNS help reduce network traffic, average delay, and assist users?
**Answer:**
DNS provides a mnemonic hostname for users to easily remember web addresses instead of numeric IP addresses, and reduces network traffic and average delay by caching desired IP addresses in nearby DNS servers.

#### 10. How does P2P file distribution alleviate the burden on the server?
**Answer:**
Each peer can redistribute portions of the file it has received to other peers.

#### 11. How does a cache check if a cached object is still valid?
**Answer:**
By issuing a conditional GET request with the "If-Modified-Since:" header set to the object's last modified date.

#### 12. How does a message travel from one process to another over a network?
**Answer:**
The sending application process passes the message through its socket API, which transport and network layers then route across the network to the receiving process's corresponding socket.

#### 13. How does the SMTP client send messages to the server?
**Answer:**
It uses the established TCP connection to transmit the message after handshaking.

#### 14. How does the application layer contribute to network communication?
**Answer:**
The application layer hosts network applications and their protocols (such as HTTP, SMTP, and DNS), enabling user-facing processes to interact with network services.

#### 15. How does the server manage persistent connections in HTTP/1.1?
**Answer:**
The server leaves the TCP connection open for subsequent requests from the same client and typically closes it after a configurable timeout period of inactivity.

#### 16. How is a peer-to-peer (P2P) file-sharing system structured in terms of client and server processes?
**Answer:**
In P2P file sharing, architecture is decentralized; any peer can act as a client (downloading) and a server (uploading) simultaneously depending on the transaction.

#### 17. How is a web cache typically implemented in an organization?
**Answer:**
It is purchased, deployed, and configured by an Internet Service Provider (ISP) or an enterprise/university organization to reduce bandwidth consumption and response times.

#### 18. How many TCP connections are created for each object in an HTTP web page using non-persistent connections?
**Answer:**
Each non-persistent connection transports exactly one request and one response message, resulting in multiple TCP connections for multiple objects.

#### 19. In standard web applications, which processes act as the client and the server?
**Answer:**
The browser process running on the user's machine acts as the client, while the remote web server process processes HTTP requests and serves content.

#### 20. In the HTTP cookie exchange process, what does the user's browser do with the Set-Cookie header?
**Answer:**
It appends the identification number and hostname to its local cookie file for subsequent requests.

#### 21. Name a popular file-sharing application that utilizes peer-to-peer (P2P) architecture.
**Answer:**
BitTorrent is a well-known file-sharing application that uses P2P architecture.

#### 22. On which protocol and port does DNS typically run?
**Answer:**
DNS runs over both UDP and TCP, predominantly using port 53.

#### 23. What additional delay does DNS introduce to Internet applications?
**Answer:**
DNS can add a latency penalty when resolving hostnames to IP addresses prior to socket connection establishment.

#### 24. What additional information can DHCP provide to a host besides an IP address?
**Answer:**
It can provide the subnet mask, default gateway router address, and local DNS server address.

#### 25. What address does the DHCP client use to send its initial discover message?
**Answer:**
The client sends the message to the layer 3 broadcast address of 255.255.255.255 and layer 2 broadcast MAC address of FF:FF:FF:FF:FF:FF.

#### 26. What analogy is used to explain the Internet's socket interface?
**Answer:**
The socket interface is like the postal service’s rules for mailing a letter (including addressing and postage), where a process is analogous to a house, and its socket is like the door through which messages are sent and received.

#### 27. What approach do typical users take regarding mail servers?
**Answer:**
They run a user agent on their local host and access a mailbox on a shared, always-on mail server.

#### 28. What are Content Distribution Networks (CDNs) used for?
**Answer:**
CDNs are used to distribute on-demand video streams efficiently to users worldwide.

#### 29. What are TLD servers?
**Answer:**
Top-Level Domain (TLD) servers manage domains such as .com, .org, and country-specific domains, providing IP addresses for authoritative DNS servers.

#### 30. What are header lines in an HTTP request message?
**Answer:**
They provide additional information about the request, following the request line.

#### 31. What are some drawbacks of using non-persistent connections in HTTP?
**Answer:**
Each object requires a new connection, leading to increased overhead on the server and longer delays for each object delivery.

#### 32. What are the benefits of using a web cache?
**Answer:**
Reduced response time for client requests and decreased traffic on an institution's access link to the Internet.

#### 33. What are the four components of cookie technology?
**Answer:**
1) Cookie header in the HTTP response, 2) Cookie header in the HTTP request, 3) Cookie file on the user's system, 4) Back-end database at the website.

#### 34. What are the main components of a DNS message?
**Answer:**
A DNS message consists of a header, a question section, an answer section, an authority section, and an additional section.

#### 35. What are the three major components of the Internet mail system?
**Answer:**
User agents, mail servers, and the Simple Mail Transfer Protocol (SMTP).

#### 36. What are the two predominant architectural paradigms used in modern network applications?
**Answer:**
Client-server architecture and peer-to-peer (P2P) architecture.

#### 37. What are the two types of HTTP messages defined in the HTTP specifications?
**Answer:**
Request messages and response messages.

#### 38. What distinguishes HTTP/1.1 from HTTP/1.0?
**Answer:**
HTTP/1.1, introduced later, includes performance improvements such as persistent connections and pipelining over HTTP/1.0.

#### 39. What distinguishes persistent from non-persistent HTTP connections?
**Answer:**
Persistent HTTP uses the same server socket for multiple requests, while non-persistent HTTP creates and closes a new TCP connection for each request/response.

#### 40. What do HTTP status codes 200 OK, 301 Moved Permanently, 404 Not Found, and 505 HTTP Version Not Supported signify?
**Answer:**
200 indicates request success; 301 indicates a permanent redirection with the new URL in the Location header; 404 means the document does not exist on the server; 505 indicates the requested HTTP version is unsupported.

#### 41. What does DASH stand for, and how does it improve video streaming?
**Answer:**
DASH stands for Dynamic Adaptive Streaming over HTTP; it allows clients to dynamically request different video bit-rate segments based on current bandwidth availability.

#### 42. What does a Type A DNS record represent?
**Answer:**
A Type A record provides the direct mapping from a hostname (e.g., example.com) to its corresponding IPv4 address.

#### 43. What does a mail server do for each recipient's mailbox?
**Answer:**
It manages and maintains the incoming and outgoing messages stored in that mailbox, facilitating protocols like SMTP, IMAP, and POP3.

#### 44. What does a peer do when it first joins a BitTorrent P2P torrent?
**Answer:**
A peer starts with zero file chunks and incrementally accumulates them over time by simultaneously downloading missing pieces from peers while uploading chunks it possesses.

#### 45. What does the DELETE method do in an HTTP request?
**Answer:**
It allows a user or application to delete an object on a Web server.

#### 46. What does the HTTP 304 Not Modified response indicate to a web cache?
**Answer:**
It indicates that the cached resource has not been altered since the specified timestamp, allowing the cache to safely forward its stored copy to the client.

#### 47. What does the Last-Modified header indicate in an HTTP response?
**Answer:**
It shows the time and date when the requested object was created or last modified.

#### 48. What does the header of a DNS message contain?
**Answer:**
The header contains a unique query identifier, flags indicating the message type (query or reply), and counts of various data sections.

#### 49. What function do user agents serve in the email system?
**Answer:**
They allow users to read, reply to, forward, save, and compose messages.

#### 50. What happens to an email message after a user agent sends it?
**Answer:**
The message is sent to the user's mail server and placed in the outgoing message queue.

#### 51. What happens to the TCP connection after the server sends an object in a non-persistent connection?
**Answer:**
The TCP connection is closed after the object is sent.

#### 52. What happens to the server's resources with persistent connections?
**Answer:**
Persistent connections reduce the overhead of establishing new connections for each request, allowing more efficient use of server resources.

#### 53. What happens when a CDN cluster's storage becomes full?
**Answer:**
The CDN removes less frequently requested videos to make space for new content.

#### 54. What happens when a user first visits a website that uses cookies?
**Answer:**
The server creates a unique identification number, stores it in its database, and sends it to the user's browser in a Set-cookie header.

#### 55. What happens when a web browser requests a URL?
**Answer:**
The browser extracts the hostname, sends a DNS query to a server, receives the corresponding IP address, and then connects to the web server using that IP address. Your computer also sends a connection request message to the web server, waits for a reply, and then sends a GET message to request the web page.

#### 56. What is BitTorrent?
**Answer:**
BitTorrent is a popular peer-to-peer (P2P) protocol for file distribution.

#### 57. What is a "torrent" in BitTorrent terminology?
**Answer:**
A torrent is the collection of all peers participating in the distribution of a particular file.

#### 58. What is a CNAME record used for in DNS, and what is a hostname?
**Answer:**
A CNAME record provides a canonical hostname for an alias hostname, allowing different names to point to the same resource. A hostname is a mnemonic identifier for a host, such as www.facebook.com or www.google.com.

#### 59. What is a classic example of a client-server application, and what is a data center in this context?
**Answer:**
A classic example is the Web, where a web server services requests from browsers running on client hosts. A data center is a facility housing multiple servers that collectively handle requests for popular Internet services, allowing for scalability and reliability.

#### 60. What is a key benefit of P2P architectures?
**Answer:**
P2P architectures are inherently self-scalable, as each peer adds both service capacity and download bandwidth while generating workload by requesting files.

#### 61. What is a key benefit of using DHCP for network management?
**Answer:**
DHCP (Dynamic Host Configuration Protocol) automates IP address allocation and configuration parameters, making it easier for network administrators to manage node onboarding and prevent address conflicts.

#### 62. What is a process in the context of network applications?
**Answer:**
A process is a program running within an end system, responsible for communication with other processes.

#### 63. What is a prominent example of a peer-to-peer (P2P) file distribution protocol?
**Answer:**
BitTorrent.

#### 64. What is another common name for a web cache?
**Answer:**
A proxy server.

#### 65. What is the basic process of HTTP streaming?
**Answer:**
The client establishes a TCP connection with the server, issues an HTTP GET request, and the server sends the video file in an HTTP response.

#### 66. What is the basic structure of a network application?
**Answer:**
A network application consists of pairs of processes that send messages to each other over a network.

#### 67. What is the central issue when developing a distributed Internet application?
**Answer:**
The central issue is how one program on one end system instructs the Internet to deliver data to another program on a different end system.

#### 68. What is the default mode of HTTP regarding connection type?
**Answer:**
The default mode of HTTP uses persistent connections.

#### 69. What is the difference between network applications and application-layer protocols?
**Answer:**
An application-layer protocol is a critical component of a network application (defining how application processes pass messages), but a network application encompasses many components beyond just the protocol, such as UI, local data storage, and auxiliary logic.

#### 70. What is the difference between the GET and HEAD methods in HTTP?
**Answer:**
The GET method requests a representation of the specified resource and includes the resource data in the response body. The HEAD method requests the exact same headers as GET but omits the actual requested object body in the response, often used for link validation or checking resource metadata.

#### 71. What is the function of DHCP?
**Answer:**
DHCP automatically allocates IP addresses and network configuration information to hosts.

#### 72. What is the function of the Application Programming Interface (API) in the context of network sockets?
**Answer:**
The API provides the programming interface through which network applications are built, allowing communication between the application layer and transport layer via sockets.

#### 73. What is the key difference between HTTP/1.0 and HTTP/1.1 regarding connections?
**Answer:**
HTTP/1.0 uses non-persistent connections, while HTTP/1.1 supports persistent connections by default.

#### 74. What is the most important performance measure for streaming video?
**Answer:**
Average end-to-end throughput, along with low packet loss and jitter to prevent rebuffering.

#### 75. What is the primary function of a web cache (proxy server)?
**Answer:**
To satisfy HTTP requests on behalf of an origin web server by storing and serving copies of recently requested objects, thereby reducing latency and bandwidth consumption.

#### 76. What is the primary purpose of cookies in HTTP?
**Answer:**
To allow websites to track users and maintain user sessions despite HTTP's stateless nature.

#### 77. What is the principal application-layer protocol for Internet email?
**Answer:**
Simple Mail Transfer Protocol (SMTP).

#### 78. What is the process for a computer fetching a webpage from a server?
**Answer:**
The computer sends a connection request (e.g., TCP 3-way handshake), receives a reply, sends an HTTP GET message with the webpage name, and receives the requested webpage data.

#### 79. What is the purpose of a socket in network applications?
**Answer:**
A socket is a software abstraction and programming interface that allows an application process to send and receive messages over the network via transport layer protocols.

#### 80. What is the purpose of the PUT method in HTTP?
**Answer:**
It allows a user to upload an object to a specific URI path on a Web server, replacing or creating the resource.

#### 81. What is the purpose of the mail access protocols (e.g., IMAP, POP3)?
**Answer:**
To retrieve messages stored on a mail server to a local mail client.

#### 82. What is the role of a web cache in terms of server-client relationships?
**Answer:**
The cache acts as both a server to the client and a client to the origin server.

#### 83. What is the role of an application-layer protocol?
**Answer:**
An application-layer protocol defines how processes running on different end systems communicate by structuring messages exchanged between them.

#### 84. What is the significance of Internet delay in web caching?
**Answer:**
It is the time taken for an HTTP request to travel to the origin server and receive a response, which can be significant compared to local cache responses.

#### 85. What is the significance of a server having a fixed IP address in client-server architecture?
**Answer:**
The fixed IP address allows clients to always contact the server directly, ensuring reliable communication.

#### 86. What is the significance of the Cookie header in an HTTP request?
**Answer:**
It allows the server to identify which user is making the request based on the identification number stored in the cookie.

#### 87. What is the state management characteristic of HTTP?
**Answer:**
HTTP is a stateless protocol, meaning servers do not retain information about clients between requests.

#### 88. What is the status code 400 Bad Request used for?
**Answer:**
It is a generic error code indicating that the request could not be understood by the server.

#### 89. What is the trade-off involved in video compression?
**Answer:**
Video can be compressed to achieve various bit rates, trading off video quality (fidelity) for reduced bandwidth and bit rate consumption.

#### 90. What is the well-known port number for a Web server (HTTP)?
**Answer:**
The well-known port number for an unencrypted Web server (HTTP) is 80.

#### 91. What mechanism does HTTP provide to verify if a cached object is up to date?
**Answer:**
The Conditional GET mechanism.

#### 92. What problem does caching introduce in web responses, and how is it managed?
**Answer:**
Cached objects may be stale if the original resource has been modified since caching. This is typically managed using conditional GET requests and HTTP headers like If-Modified-Since.

#### 93. What strategy does BitTorrent use to determine which chunks to request?
**Answer:**
The strategy is called "rarest first," where peers request the rarest chunks first.

#### 94. What type of database architecture does the Domain Name System (DNS) use?
**Answer:**
A distributed database implemented across a global, hierarchical tree of DNS servers (Root, TLD, Authoritative).

#### 95. What types of content distribution networks (CDNs) exist?
**Answer:**
Shared CDNs (like Akamai) and dedicated CDNs (like Google and Netflix).

#### 96. Why is P2P architecture considered self-scaling?
**Answer:**
Because peers can act as redistributors as well as consumers, reducing the overall burden on any single server.

#### 97. Why is a centralized DNS server not practical?
**Answer:**
A centralized DNS server creates a single point of failure, presents a massive performance bottleneck under high traffic volume, and fails to provide low-latency proximity for geographically diverse clients.

#### 98. Why is it impractical for a mail server to reside on a user's local host?
**Answer:**
The user's host would need to remain always on and connected to the Internet to receive new mail.

#### 99. Why is throughput important for certain applications like Internet telephony?
**Answer:**
Certain applications require a minimum instantaneous throughput to function properly, such as maintaining a stable, low-latency audio stream in Internet telephony.


### 🟡 Mid Level

#### 1. Describe the initial steps when a user tries to access a video through a CDN.
**Answer:**
The user's host sends a DNS query for the video URL, and the CDN intercepts this request to determine the suitable server cluster.

#### 2. How do browsers typically work around HOL blocking in HTTP/1.1?
**Answer:**
By opening multiple parallel TCP connections.

#### 3. How does DASH (Dynamic Adaptive Streaming over HTTP) benefit mobile users?
**Answer:**
It allows video streaming clients to dynamically adapt video chunk bitrates in real-time based on fluctuating available network bandwidth during a streaming session.

#### 4. How does DASH enable better streaming for users with varying Internet access rates?
**Answer:**
Dynamic Adaptive Streaming over HTTP (DASH) provides multiple video versions encoded at different bit rates and segments them into chunks. The client dynamically requests chunks at different bit rates based on real-time available bandwidth and buffer levels.

#### 5. How does file distribution differ between client-server and P2P architectures regarding server burden and upload capacity?
**Answer:**
In client-server, the server must send a copy of the file to each peer individually, burdening the server and consuming significant bandwidth. In P2P, the upload capacity depends on the upload rate of the server plus the aggregate upload rates of all participating peers.

#### 6. How does the distribution time in Peer-to-Peer (P2P) architecture compare to client-server architecture as the number of peers increases?
**Answer:**
Unlike client-server architectures where distribution time scales linearly with the number of clients due to server upload limits, P2P distribution time scales sub-linearly because each peer contributes upload bandwidth as it downloads.

#### 7. How does video compression allow for multiple versions of the same video?
**Answer:**
Compression creates different quality versions of a video, each at different bit rates (Adaptive Bitrate Streaming), allowing users to select or dynamically switch based on their available bandwidth.

#### 8. What are recursive and iterative DNS queries?
**Answer:**
A recursive query asks a DNS server to resolve a hostname on behalf of the client, while an iterative query requires the client to contact multiple servers directly for resolution.

#### 9. What are root DNS servers?
**Answer:**
Root DNS servers provide the IP addresses of TLD servers and are distributed globally, with over 1000 instances based on 13 root server designs.

#### 10. What are some challenges faced by P2P applications?
**Answer:**
P2P applications face challenges related to security, performance, and reliability due to their decentralized structure.

#### 11. What are the primary goals of HTTP/2?
**Answer:**
To reduce perceived latency, enable multiplexing, prioritize requests, and efficiently compress HTTP header fields.

#### 12. What are the two conditions that define a conditional GET request?
**Answer:**
It must use the GET method and include an "If-Modified-Since:" header line.

#### 13. What could happen if BitTorrent did not implement a tit-for-tat mechanism?
**Answer:**
Without it, many users would become free riders, leading to the potential failure of the system.

#### 14. What does the DASH (Dynamic Adaptive Streaming over HTTP) protocol define in network video streaming?
**Answer:**
It defines the manifest file format (Media Presentation Description) and sequence of HTTP GET chunk requests exchanged between a media server and client to adaptively adjust video bitrate.

#### 15. What does the framing sub-layer in HTTP/2 do?
**Answer:**
It breaks messages into frames, interleaves them, and allows for reassembly on the other end.

#### 16. What happens when a client queries DNS for a name mapped to multiple IP addresses?
**Answer:**
The server responds with the entire set of IP addresses, rotating the order of the addresses within each reply.

#### 17. What happens when a web cache receives a request for an object it does not have?
**Answer:**
It opens a TCP connection to the origin server to retrieve the object, stores a copy locally, and then sends it to the client.

#### 18. What is an MX record in DNS?
**Answer:**
A record that allows a company's mail server and Web server to have identical (aliased) hostnames.

#### 19. What is one of the main enhancements of HTTP/2 to address Head-of-Line (HOL) blocking?
**Answer:**
The use of framing to break messages into small interleaved frames over a single TCP connection.

#### 20. What is pipelining in the context of HTTP persistent connections?
**Answer:**
Pipelining allows a client to send multiple requests over a single persistent connection without waiting for each corresponding response, significantly improving the efficiency of data retrieval and reducing latency.

#### 21. What is the central issue when developing a distributed Internet application?
**Answer:**
The central issue is how one program on one end system instructs the Internet to deliver data to another program on a different end system.

#### 22. What is the difference between a recursive query and an iterative query in DNS?
**Answer:**
In a recursive query, the DNS server is asked to resolve the hostname on behalf of the client, while in an iterative query, the server returns the best answer it has without further resolution.

#### 23. What is the purpose of the "tit-for-tat" incentive mechanism in BitTorrent?
**Answer:**
The tit-for-tat mechanism discourages free-riding by encouraging peers to share file chunks reciprocally based on current upload rates, optimizing the overall swarm distribution speed.

#### 24. What is the relationship between connection sockets and processes in a web server?
**Answer:**
A web server may spawn a new process for each connection, or it may use one process to handle multiple connections by creating new threads with new connection sockets.

#### 25. What is the significance of HTTP/2 in web communication?
**Answer:**
HTTP/2 introduces new features and optimizations for faster and more efficient web communication compared to its predecessors.


## 📂 Category: Application Layer & CDN (1 cards)

### 🟡 Mid Level

#### 1. What are three major problems with streaming video directly from a single data center?
**Answer:**
1) Distance from clients leads to reduced throughput, 2) repeated transmission of popular videos wastes bandwidth, and 3) a single point of failure exists if the data center goes down.


## 📂 Category: Application Layer & Cloud Architecture (1 cards)

### 🟢 Junior Level

#### 1. What is the function of a load balancer in a cloud data center?
**Answer:**
To distribute incoming network requests across multiple backend hosts based on server health, algorithms, and current load, optimizing resource utilization.


## 📂 Category: Application Layer & Content Delivery (1 cards)

### 🟢 Junior Level

#### 1. What is the main purpose of a Content Distribution Network (CDN)?
**Answer:**
To manage servers in multiple locations to distribute video and web content efficiently to users globally.


## 📂 Category: Application Layer & DNS (3 cards)

### 🟢 Junior Level

#### 1. What happens to cached DNS records when they exceed their TTL?
**Answer:**
Cached DNS records are discarded after their TTL expires to ensure that the information is up-to-date.

#### 2. What is the Domain Name System (DNS)?
**Answer:**
The Domain Name System (DNS) is a directory service that translates hostnames to IP addresses, allowing users to access websites using easy-to-remember names instead of numeric addresses. It also supports host aliasing for hosts with complicated hostnames.


### 🟡 Mid Level

#### 1. What is the advantage of having multiple DNS root servers sharing the same IP address via IP-Anycast?
**Answer:**
It distributes the load and ensures that DNS queries are directed to the nearest available server, improving query response times.


## 📂 Category: Application Layer & P2P (2 cards)

### 🟢 Junior Level

#### 1. What happens to a peer once it acquires the entire file?
**Answer:**
It may either leave the torrent selfishly or continue to upload chunks altruistically.


### 🟡 Mid Level

#### 1. What is meant by "neighboring peers" in BitTorrent?
**Answer:**
Neighboring peers are other nodes in the swarm with whom a peer has successfully established active TCP connections for data exchange.


## 📂 Category: Application Layer / DNS (2 cards)

### 🟢 Junior Level

#### 1. How long is the typical time-to-live (TTL) for cached DNS records?
**Answer:**
The TTL for cached DNS records is often set to two days.


### 🟡 Mid Level

#### 1. How many IP addresses are currently assigned to root DNS servers, and how is IP-Anycast involved?
**Answer:**
There are 13 IP addresses for root DNS servers, but IP-Anycast directs queries to the nearest server assigned to these addresses.


## 📂 Category: Application Layer / HTTP (2 cards)

### 🟢 Junior Level

#### 1. How do web caches interact with browsers and impact network traffic?
**Answer:**
A browser directs HTTP requests to a web cache first. If the cache holds a valid fresh copy, it returns it immediately (satisfying the request locally); otherwise, it fetches from the origin server. This reduces access link traffic intensity and lowers response latency.

#### 2. How does an HTTP client transmit a stored cookie back to an origin server?
**Answer:**
By automatically including a 'Cookie:' HTTP request header containing the stored state identification key-value pairs in subsequent HTTP requests sent to that server domain.


## 📂 Category: Application Layer Protocols (15 cards)

### 🟢 Junior Level

#### 1. How do SMTP clients and servers interact before transferring message payloads?
**Answer:**
They perform an application-layer text-based handshake involving HELO/EHLO commands, authentication, and declaring the sender (MAIL FROM) and recipient (RCPT TO) addresses.

#### 2. How do client and server processes define their roles during the initiation of a communication session?
**Answer:**
The client process is the active entity that initiates the connection request, whereas the server process is the passive entity that listens and waits for incoming connection requests.

#### 3. How do persistent connections improve efficiency in HTTP?
**Answer:**
Persistent connections keep the underlying TCP connection open for multiple request-response cycles, avoiding the overhead of repeated TCP handshakes for multiple embedded objects.

#### 4. How do processes on different end systems communicate?
**Answer:**
Processes on different end systems communicate by exchanging messages over a computer network across transport layer sockets.

#### 5. How do web browsers and servers communicate using the HTTP protocol?
**Answer:**
Browsers (clients) transmit HTTP request messages detailing requested methods and URIs, and servers process them to return HTTP response messages containing status codes and requested objects.

#### 6. How is the DNS system structured?
**Answer:**
DNS is structured in a distributed, hierarchical database with multiple classes of servers: root DNS servers, TLD DNS servers, and authoritative DNS servers.

#### 7. What HTTP response status code is sent if a web object has not been modified since the last cached version?
**Answer:**
HTTP/1.1 304 Not Modified, which instructs the client to use its cached copy without retransmitting the body.

#### 8. What is a major drawback of traditional HTTP streaming?
**Answer:**
All clients receive the same encoding of the video, regardless of their available bandwidth.

#### 9. What is the effect of replacing GET with HEAD in an HTTP request?
**Answer:**
You will see the HTTP message lines without receiving the object itself.

#### 10. What is the main purpose of the Domain Name System (DNS)?
**Answer:**
To translate human-readable hostnames to IP addresses.

#### 11. What protocol does SMTP use for establishing a connection to send messages?
**Answer:**
TCP, typically on port 25 (or port 587 for message submission with STARTTLS).

#### 12. What role do authoritative DNS servers play?
**Answer:**
They permanently store and maintain DNS resource records (such as A, AAAA, CNAME) mapping hostnames to IP addresses for specific organizations, providing definitive answers to DNS queries.

#### 13. What underlying transport protocols are used by HTTP, HTTP/3, SMTP, and SNMP?
**Answer:**
HTTP and SMTP use TCP. HTTP/3 uses QUIC (over UDP). SNMP typically uses UDP datagrams for payload delivery despite its unreliability.

#### 14. When is the POST method used in an HTTP request?
**Answer:**
When the user submits data through a form, and the contents of the form fields are included in the entity body.


### 🟡 Mid Level

#### 1. What protocol does QUIC aim to improve upon for secure HTTP?
**Answer:**
HTTP/2, with HTTP/3 incorporating QUIC for transport layer security and performance improvements.


## 📂 Category: Architecture & Principles (1 cards)

### 🟡 Mid Level

#### 1. How does the 'end-to-end principle' relate to UDP?
**Answer:**
It dictates that lower-layer protocols like UDP should provide minimal functionality (just checksums and multiplexing), leaving complex features like reliability, flow control, and error recovery to be implemented at the application layer if needed.


## 📂 Category: Cellular Networks (1 cards)

### 🟡 Mid Level

#### 1. What is the International Mobile Subscriber Identity (IMSI)?
**Answer:**
A globally unique 64-bit identifier stored on the SIM card, used to identify a subscriber in the cellular network.


## 📂 Category: Cellular and Mobile Networks (3 cards)

### 🟢 Junior Level

#### 1. How do the Internet and cellular networks differ regarding the concepts of home and visited networks?
**Answer:**
The traditional Internet lacks a strict architectural notion of home and visited networks, whereas cellular networks are explicitly designed around defined home and visited network roles.


### 🟡 Mid Level

#### 1. How does LTE architecture compare functionally with WiFi WLANs?
**Answer:**
While certain baseline functions overlap (such as base stations matching access points), LTE elements incorporate complex core network control planes and unique management roles not found in traditional WLANs.


### 🔴 Senior Level

#### 1. How does an LTE network manage device mobility?
**Answer:**
It dynamically utilizes data tunnels that adapt to changes in a device's point of attachment without requiring the entire end-to-end communication path to be re-established.


## 📂 Category: Cloud & Data Centers (1 cards)

### 🟢 Junior Level

#### 1. What are the three primary purposes of data centers?
**Answer:**
1. Serve content to users (like web pages and streaming video).
2. Provide massively-parallel computing for data processing tasks.
3. Offer cloud computing services to other companies.


## 📂 Category: Cloud Computing (1 cards)

### 🟢 Junior Level

#### 1. What is a major trend in computing regarding IT needs?
**Answer:**
Companies increasingly use cloud providers like Amazon Web Services and Microsoft Azure to handle their IT needs.


## 📂 Category: Cloud Infrastructure (2 cards)

### 🟢 Junior Level

#### 1. How does virtualization contribute to cloud computing growth?
**Answer:**
Virtualization decouples software applications from physical hardware, allowing for flexible resource management, multi-tenancy, and rapid scaling.


### 🟡 Mid Level

#### 1. What is the purpose of availability zones as pioneered by cloud providers like Amazon?
**Answer:**
To improve reliability and fault tolerance by replicating data centers across isolated, nearby physical locations with independent power, cooling, and networking.


## 📂 Category: Congestion Control (14 cards)

### 🟢 Junior Level

#### 1. How does network congestion affect performance received by upper-layer applications?
**Answer:**
Congestion leads to degraded performance, manifested as increased packet delays, jitter, and reduced overall throughput.

#### 2. What are the costs associated with network congestion?
**Answer:**
Large queuing delays, packet retransmissions, wasted bandwidth, and reduced throughput.


### 🟡 Mid Level

#### 1. How does TCP respond to a packet loss event detected by timeouts?
**Answer:**
It sets the congestion window (cwnd) back to 1 MSS and restarts the slow start process, while also initiating congestion avoidance mechanisms.

#### 2. What does network-assisted congestion control entail?
**Answer:**
Routers provide explicit feedback (e.g., ICMP Source Quench, Explicit Congestion Notification - ECN) regarding the network's current congestion state directly to the sender or receiver to throttle transmission rates.

#### 3. What form can feedback in network-assisted congestion control take?
**Answer:**
A simple indication of congestion, like a choke packet, or more sophisticated feedback like maximum sending rate notifications.

#### 4. What is TCP's approach to congestion control classified as?
**Answer:**
End-to-end congestion control, where the network layer provides no explicit feedback to the hosts, and end systems must infer congestion via loss events or round-trip delay variations.

#### 5. What is the primary function of active queue management (AQM)?
**Answer:**
AQM algorithms help manage packet dropping and marking to alleviate congestion before router buffers are completely full.

#### 6. Why is it necessary to have mechanisms for dropping or marking packets (like ECN)?
**Answer:**
These mechanisms signal congestion to the sender, helping to manage traffic and reduce the likelihood of overwhelming network resources.


### 🔴 Senior Level

#### 1. How do Round-Trip Times (RTTs) affect TCP fairness when connections share a bottleneck?
**Answer:**
TCP connections with smaller RTTs ramp up their congestion window more quickly than those with larger RTTs, resulting in an unequal, non-fair bandwidth distribution across competing streams.

#### 2. How does TCP's Additive Increase/Multiplicative Decrease (AIMD) algorithm optimize throughput and ensure fairness?
**Answer:**
AIMD linearly increases the congestion window during congestion-free periods (additive increase) and cuts it drastically upon detecting packet loss (multiplicative decrease), allowing multiple TCP connections to converge toward an equal share of bandwidth.

#### 3. How does direct feedback differ from indirect feedback in network-assisted congestion control?
**Answer:**
Direct feedback comes explicitly from routers to senders (e.g., ICMP source quench or explicit congestion notification ACK), while indirect feedback involves the receiver implicitly notifying the sender of congestion based on marked or dropped packets.

#### 4. What is TCP Vegas and how does it detect congestion?
**Answer:**
TCP Vegas is a delay-based congestion control algorithm that continuously measures the round-trip time (RTT) for acknowledged packets and compares actual throughput against expected uncongested throughput, adjusting its congestion window proactively before packet loss occurs.

#### 5. What is the goal of active queue management (AQM) algorithms?
**Answer:**
AQM algorithms aim to manage packet queuing effectively to prevent congestion and maintain a balance between throughput and delay.

#### 6. Why is it important for congestion control protocols in data centers to be fast-reacting?
**Answer:**
To maintain high efficiency in an environment with very low delays and high bandwidth.


## 📂 Category: Content Delivery Networks (2 cards)

### 🔴 Senior Level

#### 1. How does a CDN use IP-Anycast to distribute content?
**Answer:**
The CDN assigns the same IP address to multiple geographically dispersed servers and uses BGP to advertise routes to these servers, allowing router policies to naturally direct users to the topologically nearest one.

#### 2. What is the main job of a CDN after the initial BGP address advertisement in an IP-Anycast setup?
**Answer:**
Distributing content from the closest replica server to the user, determined dynamically by the underlying BGP routing decisions.


## 📂 Category: Content Delivery Networks (CDNs) (1 cards)

### 🔴 Senior Level

#### 1. Why do CDNs typically avoid using IP-Anycast for long-lived TCP-based connections?
**Answer:**
BGP routing table changes can occur mid-session, directing subsequent packets of the same TCP connection to different physical CDN servers, thereby breaking state and disrupting the connection.


## 📂 Category: Content Distribution (1 cards)

### 🟢 Junior Level

#### 1. What is the difference between a private CDN and a third-party CDN?
**Answer:**
A private CDN is owned by the content provider (e.g., Google’s CDN for YouTube), while a third-party CDN distributes content for multiple providers (e.g., Akamai).


## 📂 Category: Core Internet Architecture (1 cards)

### 🟢 Junior Level

#### 1. What role do packet switches play in the Internet?
**Answer:**
Packet switches facilitate data exchange between end systems but are not concerned with the actual applications.


## 📂 Category: DNS (2 cards)

### 🟢 Junior Level

#### 1. What does a Type NS DNS record indicate?
**Answer:**
A Type NS record specifies the hostname of an authoritative DNS server for a given domain.


### 🟡 Mid Level

#### 1. What is a resource record (RR) in the context of DNS?
**Answer:**
A four-tuple consisting of (Name, Value, Type, TTL) that contains information about a domain.


## 📂 Category: DNS & Addressing (2 cards)

### 🟢 Junior Level

#### 1. What is a local DNS server?
**Answer:**
A local DNS server, also known as a default name server, is provided by an ISP and handles DNS queries from clients, acting as a proxy to the DNS hierarchy.


### 🟡 Mid Level

#### 1. What is a key benefit of using IP-Anycast in DNS resolution?
**Answer:**
It helps direct DNS queries to the nearest root DNS server, improving response time and efficiency.


## 📂 Category: Data Center Architecture (4 cards)

### 🟢 Junior Level

#### 1. What is a Modular Data Center (MDC)?
**Answer:**
A factory-built “mini data center” housed in a shipping container, designed for quick deployment.

#### 2. Why are data center designs considered company secrets?
**Answer:**
They provide critical competitive advantages to leading cloud computing companies.


### 🔴 Senior Level

#### 1. What is a key feature of Facebook's data center architecture regarding ToR switches?
**Answer:**
Each ToR switch connects up to four different tier-2 switches in distinct spline planes.

#### 2. Why are some of the largest data center operators building their switches in-house?
**Answer:**
To utilize commodity, off-the-shelf, merchant silicon instead of purchasing from switch vendors.


## 📂 Category: Data Center Infrastructure (1 cards)

### 🟢 Junior Level

#### 1. What is the role of cooling systems in data center costs?
**Answer:**
They account for a portion of the infrastructure costs necessary for maintaining optimal operating conditions.


## 📂 Category: Data Center Networking (18 cards)

### 🟢 Junior Level

#### 1. How are hosts in data centers typically connected to ToR (Top-of-Rack) switches?
**Answer:**
Each host has a network interface that connects to its ToR switch, usually with high-speed 40 Gbps or 100 Gbps Ethernet connections.

#### 2. What are the typical link capacities in modern data center networks?
**Answer:**
Data centers commonly utilize links of 40 Gbps and 100 Gbps.

#### 3. What types of networks exist in a Modular Data Center?
**Answer:**
Internal networks within containers and a core network connecting the containers.

#### 4. Why is networking innovation crucial in modern data centers?
**Answer:**
It is key to reducing overall operational costs and maximizing performance across massive server clusters.


### 🟡 Mid Level

#### 1. How can data center design address the issue of limited host-to-host capacity?
**Answer:**
Solutions include deploying higher-rate switches, co-locating related services, using multi-rooted tree topologies (e.g., Clos networks), and increasing path diversity/connectivity between switches.

#### 2. How do cloud providers customize their data center infrastructure?
**Answer:**
They build or modify components like network adapters, switches, and routers to meet specific needs.

#### 3. How many hosts can a shipping container-based Modular Data Center (MDC) accommodate?
**Answer:**
Up to a few thousand hosts.

#### 4. What are Virtual Machines (VMs) used for in data centers?
**Answer:**
VMs allow for seamless migration between physical servers, enhancing flexibility and resource utilization.

#### 5. What are the main drivers and host components behind the evolution of data center networking?
**Answer:**
Drivers include cost reduction, virtualization, physical constraints, modularity, and customization. Primary host components include CPU, memory, and disk storage.

#### 6. What is the hierarchical, tiered network in data centers designed to emulate?
**Answer:**
A large crossbar switch that allows any host to communicate with any other host.

#### 7. What percentage of data center costs are typically attributed to hosts?
**Answer:**
About 45%.

#### 8. Why is co-locating services and data important in data center networking?
**Answer:**
It minimizes inter-rack communication latencies, optimizes bisection bandwidth usage, and helps reduce network bottlenecks.


### 🔴 Senior Level

#### 1. How do large data center operators manage their architecture?
**Answer:**
By implementing logically centralized control that separates the data plane from the control plane.

#### 2. How many links does Google's Jupiter data center fabric have between the ToR switch and its servers?
**Answer:**
48 links.

#### 3. How many tier-1 switches can a tier-2 switch connect to in Facebook’s architecture?
**Answer:**
Up to 4 tier-1 switches in its spline plane.

#### 4. What is a proposed solution for VM migration in data center networks?
**Answer:**
Treating the entire data center as a single, flat layer-2 network to simplify VM movement.

#### 5. What is the consequence of limited host-to-host capacity in a hierarchical architecture?
**Answer:**
High demand can result in reduced bandwidth for flows between hosts in different racks.

#### 6. Why is automated configuration important in large-scale data centers?
**Answer:**
Due to the immense scale and frequency of node changes, automated provisioning and configuration are crucial for operational state management, rapid deployment, and configuration drift prevention.


## 📂 Category: Data Center Networks (5 cards)

### 🟢 Junior Level

#### 1. What is a Top of Rack (TOR) switch?
**Answer:**
A physical network switch mounted at the top of a server rack that interconnects the servers within that rack and uplinks to the core/spine data center switches.

#### 2. What role do border routers play in data center networks?
**Answer:**
They connect the data center network to the public Internet and handle traffic between external clients and internal hosts.


### 🟡 Mid Level

#### 1. What architectural trend is observed in modern data center networks regarding switch hardware?
**Answer:**
A shift towards using commodity white-box switches built from merchant silicon rather than expensive proprietary hardware.

#### 2. What are the primary design goals for cloud providers when architecting modern data center networks?
**Answer:**
To reduce capital and operational costs while improving latency, throughput performance, reliability, and ease of horizontal expansion.

#### 3. What role does the control plane play in data center networks?
**Answer:**
It manages the network through software, influencing how data is routed and handled.


## 📂 Category: Data Link & Error Control (1 cards)

### 🟡 Mid Level

#### 1. What is forward error correction (FEC)?
**Answer:**
FEC allows the receiver to detect and correct errors without needing retransmissions, improving the efficiency of data transmission, especially in real-time applications.


## 📂 Category: Data Link Layer (118 cards)

### 🟢 Junior Level

#### 1. Describe a point-to-point link.
**Answer:**
A link that consists of a single sender at one end and a single receiver at the other end.

#### 2. Describe how CRC codes work for error detection and contrast with parity checks.
**Answer:**
CRC codes append additional bits to data so the total is divisible by a predetermined generator pattern using modulo-2 arithmetic. In contrast, a basic parity check adds a single bit to ensure the total number of 1s in the data is even (even parity) or odd (odd parity).

#### 3. Describe the basic operation steps of CSMA/CD from the adapter's perspective.
**Answer:**
Obtain a datagram, sense the channel, transmit if idle, monitor for collisions, abort if necessary, and wait before retrying.

#### 4. Describe the basic operational principle of the original ALOHA protocol.
**Answer:**
In pure ALOHA, a node transmits a frame immediately upon arrival without waiting for a time slot.

#### 5. Describe the purpose of error-detection bits in link-layer frames.
**Answer:**
Error-detection bits help the receiving node identify whether the received data has been corrupted during transmission.

#### 6. Give examples of technologies that use broadcast links.
**Answer:**
Ethernet and wireless LANs.

#### 7. How does Slotted ALOHA differ from the pure ALOHA protocol regarding time synchronization?
**Answer:**
Slotted ALOHA requires time synchronization among nodes, while pure ALOHA does not.

#### 8. How does a link-layer controller manage frame transmission?
**Answer:**
On the sending side, it encapsulates the network-layer datagram into a link-layer frame and transmits it over the physical medium, while on the receiving side, it extracts the datagram from the received frame.

#### 9. How does a node respond after detecting a collision in CSMA/CD?
**Answer:**
The node immediately aborts the transmission, sends a jam signal to ensure all other nodes detect the collision, and enters a backoff period, waiting a random amount of time (determined via binary exponential backoff) before trying to retransmit.

#### 10. How does the cocktail party analogy relate to broadcast channels in computer networks?
**Answer:**
It illustrates how multiple nodes can transmit and listen simultaneously on a shared medium, highlighting the need for Medium Access Control (MAC) protocols to coordinate who speaks and when to avoid collisions.

#### 11. How does the type field in an Ethernet frame assist in multiplexing?
**Answer:**
The type field indicates which network-layer protocol the data field contains, allowing the receiving adapter to process it accordingly.

#### 12. How has Ethernet evolved in terms of topology?
**Answer:**
Ethernet has transitioned from a shared medium bus topology using coaxial cables to a switch-based star topology using twisted-pair or fiber-optic cables.

#### 13. How long is a standard MAC address and how is it typically represented?
**Answer:**
A standard MAC address is 6 bytes long and is usually expressed in hexadecimal notation.

#### 14. Name two common random access protocols.
**Answer:**
ALOHA protocols and Carrier Sense Multiple Access (CSMA) protocols.

#### 15. Name two link-layer protocols designed for point-to-point links.
**Answer:**
Point-to-Point Protocol (PPP) and High-Level Data Link Control (HDLC).

#### 16. What administrative flexibility does VLAN configuration provide when an employee changes departments?
**Answer:**
The network operator can simply reconfigure the VLAN software logically on the switch without requiring any physical cable or port changes.

#### 17. What advantage do network switches offer regarding heterogeneous links?
**Answer:**
Different links in a LAN connected via switches can operate at completely different speeds, duplex modes, and physical media types.

#### 18. What are link-layer addresses commonly referred to as?
**Answer:**
MAC addresses (Media Access Control addresses).

#### 19. What are the two important rules for polite human conversation that parallel CSMA protocols?
**Answer:**
1) Listen before speaking (carrier sensing). 2) Stop talking if someone else begins (collision detection).

#### 20. What are the two main components of a link layer implementation?
**Answer:**
The link layer is implemented using both hardware (typically in a network adapter) and software that runs on the host's CPU.

#### 21. What are the two types of network links?
**Answer:**
Point-to-point links and broadcast links.

#### 22. What are the two types of physical media that Ethernet can utilize?
**Answer:**
Copper wires (e.g., twisted pair) and fiber optic cables.

#### 23. What common network error necessitates the implementation of error detection mechanisms?
**Answer:**
Bit errors caused by thermal noise, signal attenuation, or interference, which can corrupt packet payloads or headers during transmission.

#### 24. What distinguishes point-to-point links from shared broadcast channels in Gigabit Ethernet?
**Answer:**
Point-to-point links use switches, while shared broadcast channels use hubs.

#### 25. What do CSMA and CSMA/CA stand for in networking and 802.11 protocols?
**Answer:**
CSMA stands for Carrier Sense Multiple Access. CSMA/CA stands for Carrier Sense Multiple Access with Collision Avoidance.

#### 26. What does a link-layer frame consist of?
**Answer:**
A link-layer frame consists of a data field containing the encapsulated network-layer datagram and several control/header fields, with the specific structure defined by the underlying link-layer protocol.

#### 27. What does the destination address field in an Ethernet frame contain?
**Answer:**
It contains the MAC address of the destination adapter.

#### 28. What does the hub do in a hub-based star topology Ethernet network?
**Answer:**
The hub boosts the signal of incoming bits and sends them out to all other interfaces, creating a broadcast LAN.

#### 29. What does the term 'carrier sensing' mean in the context of CSMA protocols?
**Answer:**
It refers to a network node listening to the shared transmission medium to check for traffic before attempting to transmit.

#### 30. What happens if an Ethernet frame fails the CRC check?
**Answer:**
The receiving adapter simply discards the frame without sending any acknowledgment.

#### 31. What happens if an acknowledgment is not received after a transmission?
**Answer:**
The transmitting station assumes an error occurred and retransmits the frame.

#### 32. What happens to a MAC address in a switch's table if no frames are received from that address after a certain period?
**Answer:**
It gets deleted due to aging.

#### 33. What happens when an adapter receives a frame with a destination MAC address that matches its own?
**Answer:**
The adapter extracts the enclosed datagram and passes it up the protocol stack for further processing.

#### 34. What information does a switch store in its forwarding table when it receives a frame?
**Answer:**
The source MAC address, the interface from which the frame arrived, and the current time

#### 35. What is "collision detection" in CSMA/CD?
**Answer:**
It is the process where a transmitting node listens for interference and stops transmitting if a collision is detected.

#### 36. What is a broadcast link?
**Answer:**
A link where multiple sending and receiving nodes are connected to the same shared broadcast channel.

#### 37. What is a simple form of error detection used in link layers?
**Answer:**
A single parity bit, where its value is set to ensure the total number of 1s in the data frame is even (even parity) or odd (odd parity).

#### 38. What is framing in the context of link-layer protocols?
**Answer:**
Framing encapsulates each network-layer datagram within a link-layer frame before transmission, consisting of a data field and header fields.

#### 39. What is the MAC broadcast address for Ethernet and 802.11 LANs?
**Answer:**
The broadcast address is represented as FF-FF-FF-FF-FF-FF in hexadecimal notation.

#### 40. What is the function of the preamble in an Ethernet frame?
**Answer:**
It wakes up receiving adapters and synchronizes their internal clocks to the sender's clock.

#### 41. What is the maximum transmission unit (MTU) and data field size for standard Ethernet frames?
**Answer:**
The MTU (maximum size of the data field) for standard Ethernet is 1,500 bytes.

#### 42. What is the most prevalent LAN technology used in corporate, university, and home networks?
**Answer:**
Ethernet

#### 43. What is the primary behavior of nodes in ALOHA protocols?
**Answer:**
Nodes transmit frames immediately whenever they have data, completely independently of the activity of other nodes, risking collisions.

#### 44. What is the primary function of a link-layer switch?
**Answer:**
To receive incoming link-layer frames, inspect them, and transparently forward them onto outgoing links based on layer-2 addresses.

#### 45. What is the primary service provided by the link layer?
**Answer:**
To move a datagram from one node to an adjacent node over a single communication link.

#### 46. What is the purpose of CSMA/CD in early Ethernet networks?
**Answer:**
To manage and resolve collisions that occur when multiple nodes transmit data simultaneously over a shared medium by listening to the channel and backing off after detecting a collision.

#### 47. What is the purpose of error detection and correction techniques in the link layer (such as CRC)?
**Answer:**
CRC and other error detection codes are used in wired and wireless protocols to identify bit errors introduced during transmission across links, allowing for the retransmission or correction of corrupted data.

#### 48. What is the purpose of the source address field in an Ethernet frame?
**Answer:**
It contains the MAC address of the adapter that transmits the frame onto the LAN.

#### 49. What is the role of a switch table?
**Answer:**
To determine the forwarding and filtering of frames based on MAC addresses.

#### 50. What is the role of the cyclic redundancy check (CRC) in an Ethernet frame?
**Answer:**
The CRC field allows the receiving adapter to detect bit errors in the frame.

#### 51. What is the significance of the sequence number field in an 802.11 frame?
**Answer:**
It allows the receiver to differentiate between new frames and retransmissions of previous frames.

#### 52. What is the significance of the switch table in Ethernet switching?
**Answer:**
The switch table maps MAC addresses to the corresponding switch interfaces, allowing the switch to filter and forward frames correctly.

#### 53. What is the significance of the term "collision" in the context of multiple access protocols?
**Answer:**
A collision occurs when multiple nodes transmit frames simultaneously, resulting in data loss.

#### 54. What kind of service does Ethernet provide to the network layer?
**Answer:**
Ethernet provides a connectionless and unreliable service.

#### 55. What major change did Ethernet installations undergo in the early 2000s?
**Answer:**
Hubs were replaced by switches, making Ethernet installations more efficient and capable of handling traffic without collisions.

#### 56. What mechanisms do link-layer protocols use for error detection?
**Answer:**
Link-layer protocols use error-detection bits included in frames and perform error checks at the receiving node to detect bit errors caused by issues like signal attenuation and electromagnetic noise.

#### 57. What must a node do if it senses that the channel is busy in CSMA?
**Answer:**
The node must wait until the channel is idle before transmitting.

#### 58. What occurs when a switch receives a frame for which it has no entry in its switch table?
**Answer:**
The switch floods/broadcasts the frame to all interfaces except the one it was received on.

#### 59. What occurs when network adapter B receives a frame with a destination MAC address not matching its own?
**Answer:**
Adapter B discards the frame.

#### 60. What response does a host receive when it sends an ARP query?
**Answer:**
An ARP reply from the device matching the queried IP address, containing its corresponding MAC (hardware) address.

#### 61. What role does the network adapter play in the link layer?
**Answer:**
The network adapter implements many link layer services including framing, link access, and error detection, encapsulating datagrams in link-layer frames for transmission.

#### 62. Why is ARP considered 'plug-and-play'?
**Answer:**
Because hosts and routers automatically build and maintain their ARP tables dynamically through broadcast requests and replies without requiring manual administrative configuration.

#### 63. Why is Ethernet considered to provide an unreliable service to the network layer?
**Answer:**
It does not acknowledge frames that pass or fail the CRC check; frames that fail are simply discarded without notification.

#### 64. Why is Slotted ALOHA considered a decentralized protocol?
**Answer:**
Because each node independently detects collisions and decides when to retransmit.

#### 65. Why is a preamble important in an Ethernet frame?
**Answer:**
The 7-byte preamble (followed by the 1-byte SFD) is used to synchronize the receiving network adapter's internal clock with the sender's transmission clock.

#### 66. Why is error detection at the link layer crucial for data integrity?
**Answer:**
It prevents the forwarding of corrupted datagrams, ensuring that only error-free data is passed to the network layer, which is vital for maintaining overall network reliability.

#### 67. Why is it important for the transmitting station to wait for an acknowledgment?
**Answer:**
It confirms that the data frame was received intact by the destination station.

#### 68. Why is there often no need for a traditional MAC collision-avoidance protocol in modern switch-based Ethernet networks?
**Answer:**
Because full-duplex switches coordinate transmissions and prevent collisions using dedicated buffers, making legacy multi-access protocols unnecessary.


### 🟡 Mid Level

#### 1. Can VLANs extend across IP routers?
**Answer:**
Yes, allowing islands of LANs to connect and form a single VLAN over larger geographic areas.

#### 2. Can the 802.11 MAC protocol be used for point-to-point links?
**Answer:**
Yes, particularly when using directional antennas and increased transmission power over long distances.

#### 3. Define forward error correction (FEC).
**Answer:**
Techniques that allow a receiver to detect and correct errors without needing retransmission from the sender.

#### 4. How do ALOHA protocols differ from CSMA in terms of transmission behavior?
**Answer:**
ALOHA protocols do not listen to the channel before transmitting (pure/slotted transmission without carrier sensing), whereas CSMA (Carrier Sense Multiple Access) protocols listen to the channel first to check if it is idle.

#### 5. How do stations prevent and handle collisions in multi-access channels (such as CSMA/CD)?
**Answer:**
Stations sense the channel, enter a random backoff phase, and transmit when idle. In CSMA/CD specifically, if a collision is detected during transmission, the node immediately stops transmitting and waits for a randomized backoff time before retrying.

#### 6. How does a node decide to transmit in ALOHA protocols?
**Answer:**
Independently of the activity of other nodes; it transmits immediately when data is ready, neither checking if another node is transmitting nor stopping mid-transmission if a collision occurs.

#### 7. How does traffic segmentation behave in port-based VLANs versus MAC-based VLANs?
**Answer:**
In a port-based VLAN, broadcast traffic from one port can only reach other ports within the same VLAN group. In a MAC-based VLAN, the switch dynamically determines VLAN membership by evaluating the source MAC address of the connected device rather than the physical port.

#### 8. How does two-dimensional parity enhance error detection and correction?
**Answer:**
Two-dimensional parity checks both rows and columns of data, allowing the receiver to detect and correct single-bit errors by identifying the specific intersection of the corrupted row and column.

#### 9. How does user mobility impact traditional switched LANs versus VLANs?
**Answer:**
In traditional switched LANs, employees moving between groups necessitate physical cabling changes. VLANs limit broadcast traffic and isolate groups logically, allowing mobility without physical recabling.

#### 10. In the context of CSMA/CD, what happens after a node experiences its first collision?
**Answer:**
It randomly chooses a K value from {0, 1} and may wait before attempting to transmit again using binary exponential backoff.

#### 11. What MAC address should a host on Subnet 1 use to send a datagram to a host on Subnet 2?
**Answer:**
The MAC address of the router interface that serves as the first hop (e.g., E6-E9-00-17-BB-4B for the interface 111.111.111.110).

#### 12. What algorithm do cable modems use to manage retransmissions after a collision?
**Answer:**
They use a binary exponential backoff algorithm.

#### 13. What are the ideal characteristics of a multiple access protocol for a broadcast channel?
**Answer:**
High throughput when one node is active, fair sharing of throughput among active nodes, decentralized control, and simplicity.

#### 14. What does a Medium Access Control (MAC) protocol specify?
**Answer:**
The distributed rules and algorithms for how nodes coordinate access and transmit frames onto a shared communication link to avoid or manage collisions.

#### 15. What does the Tag Protocol Identifier (TPID) signify in an 802.1Q Ethernet frame?
**Answer:**
It has a fixed hexadecimal value of 0x8100, which indicates the presence of an 802.1Q VLAN tagging header.

#### 16. What does the efficiency of CSMA/CD represent?
**Answer:**
The long-run fraction of time frames are being transmitted on the channel without collisions.

#### 17. What happens if an Ethernet frame (or IP datagram) is less than the minimum required size?
**Answer:**
The data field must be “stuffed” to fill it out to a minimum size (e.g., 46 bytes for Ethernet data) to ensure valid collision detection.

#### 18. What happens if two or more frames collide in Slotted ALOHA?
**Answer:**
All nodes detect the collision event before the slot ends.

#### 19. What happens to undeclared ports in a VLAN configuration?
**Answer:**
They belong to a default VLAN until assigned to a specific VLAN by the network manager.

#### 20. What happens when a collision occurs in a random access protocol?
**Answer:**
Each node involved waits a random delay before retransmitting its frame.

#### 21. What happens when a node detects that the channel is busy in CSMA/CD?
**Answer:**
The node waits for the channel to become idle before attempting to transmit.

#### 22. What happens when a station begins to transmit a frame in IEEE 802.11?
**Answer:**
The station transmits the entire frame without the ability to abort, even if a collision occurs.

#### 23. What happens when a station does not receive an acknowledgment (ACK) in IEEE 802.11?
**Answer:**
It assumes an error occurred and retransmits the frame after using the CSMA/CA protocol to access the channel again.

#### 24. What is one major drawback of the polling protocol?
**Answer:**
It introduces polling delays, especially if many nodes are inactive, reducing effective throughput.

#### 25. What is one solution for handling corrupted ACK or NAK packets in reliable data transfer protocols?
**Answer:**
To add a new type of packet or use retransmission mechanisms where the sender asks the receiver to repeat the acknowledgment.

#### 26. What is the maximum value for n in the binary exponential backoff algorithm for Ethernet?
**Answer:**
The maximum value of n in the binary exponential backoff algorithm for Ethernet is capped at 10.

#### 27. What is the polling protocol in the context of multiple access protocols?
**Answer:**
A protocol where a designated master node polls each node in a round-robin manner to explicitly grant them permission to transmit.

#### 28. What is the primary advantage of random access protocols?
**Answer:**
They allow nodes to transmit at the full channel rate without being limited by rigid time slots or frequency assignments.

#### 29. What is the primary purpose of the 802.11 MAC protocol?
**Answer:**
To coordinate the transmissions of multiple wireless devices or access points (APs) sharing the same channel using mechanisms like CSMA/CA.

#### 30. What is the problem with having a large number of switches for small workgroups?
**Answer:**
It leads to inefficient use of switches, requiring multiple switches for small groups without providing traffic isolation.

#### 31. What is the purpose of the 802.11 MAC protocol?
**Answer:**
To coordinate transmissions between multiple wireless devices (stations) to prevent data frame collisions.

#### 32. What is the purpose of the duration field in an 802.11 frame?
**Answer:**
To indicate the time required for the transmission of the data frame and its acknowledgment, facilitating NAV (Network Allocation Vector) updates.

#### 33. What is the purpose of using a random backoff time in CSMA/CD?
**Answer:**
To avoid repeated collisions if two nodes try to transmit again after a collision.

#### 34. What is the purpose of using redundant bit transmission in the MAC layer?
**Answer:**
To perform forward error correction.

#### 35. What is the role of link-layer software in a host's CPU?
**Answer:**
It handles higher-level link-layer functionality, such as addressing and responding to controller interrupts.

#### 36. What is the role of the adapter in a CSMA/CD protocol?
**Answer:**
The adapter prepares frames, senses the channel, and monitors for collisions while transmitting.

#### 37. What is the significance of the last byte of the Ethernet preamble?
**Answer:**
The last byte (Start Frame Delimiter) signals that the important payload data is about to follow.

#### 38. What is the spanning tree limitation in a switched network?
**Answer:**
It restricts the active topology of a switched network to prevent cycling of broadcast frames.

#### 39. What is the token-passing protocol?
**Answer:**
A decentralized protocol where a special frame called a token is passed among nodes, allowing the node holding the token to transmit frames.

#### 40. What is two-dimensional parity, and how does it improve error detection?
**Answer:**
It uses both row and column parity bits computed across a data block, enabling the detection of all two-bit errors and the correction of certain single-bit errors.

#### 41. What occurs after a collision in the original ALOHA protocol?
**Answer:**
The node retransmits the frame with probability p after the collision.

#### 42. What protocol standard defines the extended Ethernet frame format for VLAN trunking?
**Answer:**
The IEEE 802.1Q standard, which inserts a 4-byte VLAN tag into the Ethernet frame header.

#### 43. Why might a link-layer reliable delivery service be considered unnecessary?
**Answer:**
It can be redundant for low bit-error links, such as fiber, coax, and many twisted-pair copper links, as these links are inherently less prone to transmission errors.


### 🔴 Senior Level

#### 1. How does the choice of the generator polynomial (G) impact CRC functionality?
**Answer:**
The generator polynomial must have a most significant bit of 1 and dictates the specific mathematical error-detection capabilities, determining which burst error lengths and single/double bit errors can be detected.

#### 2. How is an ARP query constructed, sent, and modified for advanced use cases?
**Answer:**
An ARP query packet is constructed containing the sender's IP/MAC and target's IP, sent as a broadcast frame (FF:FF:FF:FF:FF:FF) on the subnet. In advanced flat networks or VM migration scenarios, ARP may be optimized using mechanisms like gratuitous ARP, DNS-style query systems, or controller-based mapping instead of pure broadcasts.

#### 3. What are the first seven bytes of the Ethernet preamble set to?
**Answer:**
Each of the first seven bytes of the Ethernet preamble has a value of 10101010.

#### 4. What does a long propagation delay in a broadcast channel imply for CSMA performance?
**Answer:**
It increases the vulnerability window, raising the chance that a carrier-sensing node will fail to detect an ongoing transmission, leading to collisions.

#### 5. What happens when there is little traffic on the upstream channel in a cable modem network?
**Answer:**
Cable modems may transmit data frames during slots normally assigned for mini-slot-request frames to reduce waiting time.

#### 6. What is the efficiency and effective transmission rate of Slotted ALOHA?
**Answer:**
The maximum efficiency of Slotted ALOHA is 1/e (approximately 0.37 or 37%), which represents the long-run fraction of successful slots when many active nodes are continuously attempting transmission. The effective transmission rate is 0.37R bps (where R is the channel rate).

#### 7. What is the probability that a node has a successful transmission in pure ALOHA?
**Answer:**
The probability of a successful transmission in pure ALOHA is given by P = G * e^(-2G), where G is the normalized channel load (throughput efficiency maxes out at 18.4% for G = 0.5).


## 📂 Category: Data Link Layer & Error Control (1 cards)

### 🟢 Junior Level

#### 1. What happens to frames that fail the CRC check in Ethernet?
**Answer:**
They are discarded without any acknowledgment sent back to the sender.


## 📂 Category: Data Link Layer & LANs (4 cards)

### 🟢 Junior Level

#### 1. What is the function of a Medium Access Control (MAC) protocol?
**Answer:**
A MAC protocol specifies the rules for transmitting frames onto a shared communication link, coordinating transmission access among multiple nodes to avoid collisions.


### 🟡 Mid Level

#### 1. What happens to ARP entries if a device disconnects from the subnet?
**Answer:**
The ARP entries for the disconnected device are eventually deleted from the ARP tables of other devices in the subnet.

#### 2. What is the first step for a host on a subnet to send a datagram to a host on another subnet?
**Answer:**
The sending host must pass the datagram to its network adapter (NIC) and indicate an appropriate destination MAC address (typically the default gateway's MAC address resolved via ARP).


### 🔴 Senior Level

#### 1. What is the formula for calculating the efficiency of CSMA/CD?
**Answer:**
Efficiency = 1 / (1 + 5 * (dprop / dtrans)), where dprop is the propagation delay and dtrans is the transmission delay.


## 📂 Category: Data Link Layer & Medium Access Control (1 cards)

### 🔴 Senior Level

#### 1. What happens to CSMA/CD efficiency as propagation delay (dprop) approaches zero?
**Answer:**
The efficiency approaches 1, indicating no wasted time due to collisions.


## 📂 Category: Data Link Layer & Reliable Data Transfer (1 cards)

### 🟡 Mid Level

#### 1. What structural change was introduced in rdt2.2 compared to rdt2.1 for ACK messages?
**Answer:**
The receiver must explicitly include the sequence number of the packet being acknowledged in the ACK message.


## 📂 Category: Data Link Layer & Switching (4 cards)

### 🟡 Mid Level

#### 1. How are ARP broadcasts managed in data centers?
**Answer:**
Each subnet is partitioned into smaller VLAN subnets to localize ARP broadcast traffic and prevent broadcast storms.

#### 2. What is VLAN trunking?
**Answer:**
A method for interconnecting VLAN switches where a special port is configured to belong to all VLANs, allowing frames from any VLAN to be forwarded over the trunk link. Inter-VLAN communication can be achieved by connecting a VLAN switch port to an external router configured to belong to both VLANs, or via layer 3 switches.

#### 3. What is included in an 802.1Q VLAN-tagged frame?
**Answer:**
A standard Ethernet frame with an added four-byte VLAN tag in the header containing the VLAN ID (VID) and priority information.

#### 4. What solution is used to update the switch's forwarding table when H1 moves to AP2?
**Answer:**
AP2 sends a broadcast Ethernet frame with H1’s source address to the switch to update its forwarding table.


## 📂 Category: Data Link Layer / Addressing (1 cards)

### 🟡 Mid Level

#### 1. Why can't the sending host use the destination host's MAC address directly across different subnets?
**Answer:**
The MAC address used must belong to a device on the same local subnet (or default gateway); otherwise, Layer 2 frames will not match any network adapter on that local segment.


## 📂 Category: Data Link Layer / Hardware (1 cards)

### 🟢 Junior Level

#### 1. How does a Layer 2 switch differ fundamentally from a network hub?
**Answer:**
A switch operates at Layer 2 (Data Link), maintaining a MAC address table to intelligently forward frames and segment collision domains. A hub operates at Layer 1 (Physical), blindly repeating incoming electrical bits out to all other connected ports, sharing a single collision domain.


## 📂 Category: Data Link Layer / Switching (1 cards)

### 🟢 Junior Level

#### 1. How does a Layer 2 switch determine whether to forward or filter a frame, and how does it handle unknown destination MAC addresses?
**Answer:**
The switch checks its internal switch table (CAM table) for the destination MAC address. If found, it forwards the frame only to the corresponding interface. If not found, it floods (broadcasts) the frame to all interfaces except the one it was received on.


## 📂 Category: Datacenter Networks (1 cards)

### 🔴 Senior Level

#### 1. What networking challenge arises when using multiple Modular Datacenters (MDCs)?
**Answer:**
Designing the core network to provide high host-to-host bandwidth while interconnecting numerous containers.


## 📂 Category: Domain Name System (2 cards)

### 🟢 Junior Level

#### 1. What is the purpose of an MX record in DNS?
**Answer:**
An MX record specifies the canonical name of a mail server for a given hostname, directing email to the appropriate mail transfer agent.

#### 2. What is the purpose of load distribution in DNS?
**Answer:**
Load distribution in DNS helps balance incoming traffic among replicated servers by dynamically rotating the order of IP addresses returned in response to DNS queries (Round-Robin DNS).


## 📂 Category: Domain Name System (DNS) (1 cards)

### 🟢 Junior Level

#### 1. What is the impact of DNS caching?
**Answer:**
DNS caching reduces query traffic and delays by storing previously resolved IP addresses, allowing quicker access for repeated requests.


## 📂 Category: Error Detection (1 cards)

### 🟢 Junior Level

#### 1. What is the primary difference between checksumming methods and cyclic redundancy check (CRC)?
**Answer:**
Checksumming is simpler and typically implemented in software, while CRC is more computationally complex and implemented in hardware for efficiency.


## 📂 Category: Error Detection & Correction (1 cards)

### 🟡 Mid Level

#### 1. What is a major limitation of using single parity bits for error detection?
**Answer:**
It can undetectably fail if an even number of bit errors occur.


## 📂 Category: Hardware & Switching (1 cards)

### 🟢 Junior Level

#### 1. What is the range of access speeds for Ethernet switches in typical setups?
**Answer:**
Users typically have 100 Mbps to tens of Gbps access.


## 📂 Category: IP Addressing (2 cards)

### 🟢 Junior Level

#### 1. What does the subnet mask in CIDR notation (e.g., /24) specify?
**Answer:**
It indicates the exact number of bits allocated to the network portion of the IP address, defining the boundary and size of the subnet.

#### 2. Who does an organization contact to obtain a block of IP addresses?
**Answer:**
The organization typically contacts its Internet Service Provider (ISP).


## 📂 Category: Internet Control Message Protocol (ICMP) (1 cards)

### 🟡 Mid Level

#### 1. What was the original purpose of the ICMP Source Quench message?
**Answer:**
The Source Quench message was used for congestion control, allowing a congested router to request that a host reduce its transmission rate.


## 📂 Category: LAN Architecture (4 cards)

### 🟢 Junior Level

#### 1. What role do link-layer switches play in data transmission within a switched LAN?
**Answer:**
They forward incoming frames to the appropriate output interface based on the destination MAC address.


### 🟡 Mid Level

#### 1. What is a port-based VLAN?
**Answer:**
A VLAN where switch ports are divided into groups by the network manager, with each group forming a separate broadcast domain.

#### 2. What is a significant change in Ethernet technology over the years?
**Answer:**
The transition from coaxial cable in bus-topologies to switch-based star topologies.

#### 3. What technology can simplify inter-VLAN communication without an external router?
**Answer:**
A Layer 3 switch (multilayer switch) that combines both a VLAN switch and routing capabilities in one unit.


## 📂 Category: LAN Architectures (1 cards)

### 🟡 Mid Level

#### 1. What is the consequence of not having VLANs in a hierarchical LAN configuration?
**Answer:**
Broadcast traffic would traverse the entire network, leading to performance issues and potential security risks.


## 📂 Category: LAN Technologies (1 cards)

### 🟢 Junior Level

#### 1. Why did network administrators historically prefer Ethernet over competing LAN technologies?
**Answer:**
Ethernet was simpler to deploy, cheaper, and provided higher data rates than competing technologies like Token Ring.


## 📂 Category: Link Layer (29 cards)

### 🟢 Junior Level

#### 1. How do link-layer protocols typically detect bit errors?
**Answer:**
By including error-detection bits in the frame and having the receiving node perform an error check.

#### 2. How do link-layer switches differ from routers in terms of addressing?
**Answer:**
Link-layer switches operate without recognizing network-layer addresses and do not use routing algorithms; they forward frames based solely on MAC addresses.

#### 3. How does ARP facilitate communication between devices on the same subnet?
**Answer:**
By resolving IP addresses to MAC addresses, allowing devices to encapsulate IP datagrams in link-layer frames for transmission.

#### 4. How does CSMA/CD improve performance over ALOHA protocols?
**Answer:**
By detecting collisions and aborting transmissions early, reducing wasted time and bandwidth on the shared medium.

#### 5. How does Ethernet provide a connectionless service to the network layer?
**Answer:**
Ethernet sends frames into the LAN without establishing a handshake with the receiving adapter first.

#### 6. How does reliable delivery in link-layer protocols work?
**Answer:**
It guarantees to move each network-layer datagram across the link without error, often using acknowledgments and retransmissions.

#### 7. How does the link layer interact with the network layer during data transmission?
**Answer:**
The network layer passes datagrams down to the link layer for encapsulation and transmission, and the link layer subsequently delivers these frames across the physical medium to the next adjacent node.

#### 8. What are some examples of link-layer protocols?
**Answer:**
Examples include Ethernet, WiFi, and the DOCSIS protocol used in cable networks.

#### 9. What are the key components and physical media of an Ethernet frame?
**Answer:**
An Ethernet frame consists of a preamble, destination address, source address, type field, data field, and cyclic redundancy check (CRC). Physical media include coaxial cable, twisted-pair copper wires, and fiber-optic cables.

#### 10. What are the limitations of using a single parity bit for error detection?
**Answer:**
A single parity bit can fail to detect errors if an even number of bit errors occur, and in burst error conditions, the probability of undetected errors can be significant.

#### 11. What are the three categories of multiple access protocols?
**Answer:**
Channel partitioning protocols, random access protocols, and taking-turns protocols.

#### 12. What is ARP and what is its role in network communications?
**Answer:**
ARP (Address Resolution Protocol) is used to map IP addresses to MAC addresses, allowing devices to communicate over a network.

#### 13. What is a frame in the context of the link layer?
**Answer:**
A frame is the link-layer packet that encapsulates a network-layer datagram with header and trailer fields for transmission across a specific physical link.

#### 14. What is the basic service of any link layer?
**Answer:**
To move a datagram from one node to an adjacent node over a single communication link.

#### 15. What is the function of the Address Resolution Protocol (ARP)?
**Answer:**
ARP translates network-layer addresses (IP addresses) to link-layer addresses (MAC addresses) for devices within the same subnet.

#### 16. What is the function of the link layer?
**Answer:**
The link layer delivers datagrams between nodes along a route and provides services like reliable delivery for specific link-layer protocols.

#### 17. Why might a station discard a frame after several retransmission attempts?
**Answer:**
If acknowledgments are not received after a fixed maximum number of retransmissions, it indicates persistent link issues or node failure, prompting the station to give up and report an error.


### 🟡 Mid Level

#### 1. How does CSMA/CA differ from CSMA/CD?
**Answer:**
CSMA/CA (used in wireless) avoids collisions by utilizing backoff intervals and RTS/CTS exchanges since hidden nodes prevent reliable collision detection. CSMA/CD (used in wired Ethernet) detects collisions during transmission and aborts immediately.

#### 2. How does Gigabit Ethernet maintain compatibility with older Ethernet standards?
**Answer:**
It uses the standard Ethernet frame format, allowing integration with 10BASE-T and 100BASE-T technologies.

#### 3. How does checksumming work as an error-detection technique?
**Answer:**
It sums k-bit integers from the data and uses the 1's complement of the sum as the error-detection bits.

#### 4. How does link-layer reliable delivery differ from transport-layer reliable delivery?
**Answer:**
Link-layer reliable delivery guarantees error-free transmission across the link, often using acknowledgments and retransmissions, while transport-layer reliability typically handles error correction at a broader scope.

#### 5. What are the operations used in CRC calculations?
**Answer:**
All operations are performed using modulo-2 arithmetic, where addition and subtraction are equivalent to the bitwise XOR.

#### 6. What distinguishes an ARP query from an ARP response in terms of how they are sent?
**Answer:**
ARP queries are sent in broadcast frames, while ARP responses are sent in standard unicast frames.

#### 7. What is CSMA/CD and how is it related to Ethernet?
**Answer:**
Carrier Sense Multiple Access with Collision Detection (CSMA/CD) is a protocol used to manage access to the network and handle collisions in a shared broadcast channel.

#### 8. What is the central problem addressed by multiple access protocols?
**Answer:**
Coordinating the access of multiple sending and receiving nodes to a shared broadcast channel.

#### 9. Why might reliable delivery not be provided in some wired link-layer protocols?
**Answer:**
For low bit-error links, like fiber or coaxial cables, reliable delivery at the link layer is often omitted because it is viewed as unnecessary overhead since error rates are extremely low.


### 🔴 Senior Level

#### 1. How do cable modems infer that a mini-slot-request frame has collided?
**Answer:**
They infer a collision if they do not receive a response to their request in the next downstream control message.

#### 2. How does frame transmission time (dtrans) impact CSMA/CD network efficiency?
**Answer:**
As dtrans increases (meaning frames take longer to transmit relative to propagation delay), efficiency approaches 1, indicating highly productive channel utilization because the channel is actively occupied by data for longer periods.

#### 3. What is a jabbering adapter and how do switches handle it?
**Answer:**
A jabbering adapter is a malfunctioning network interface card that continuously sends Ethernet frames without stopping; modern switches can detect this abnormal behavior and automatically disconnect the malfunctioning adapter port.


## 📂 Category: Link Layer & Access Networks (2 cards)

### 🟢 Junior Level

#### 1. What type of topology did the original Ethernet LAN use?
**Answer:**
The original Ethernet LAN used a coaxial bus topology.


### 🔴 Senior Level

#### 1. What type of protocol does the CMTS in a cable access network use to grant transmission permissions?
**Answer:**
It sends a MAP message on a downstream channel to specify which cable modem can transmit during designated mini-slots.


## 📂 Category: Link Layer & Addressing (3 cards)

### 🟢 Junior Level

#### 1. How do a router and a sending host acquire destination and gateway MAC addresses respectively?
**Answer:**
A router uses ARP to resolve the MAC address for a destination IP on a subnet. A sending host similarly acquires the MAC address of the first-hop router using the Address Resolution Protocol (ARP).

#### 2. How does the structure of a MAC address differ from that of an IP address?
**Answer:**
MAC addresses have a flat structure and do not change regardless of network location, while IP addresses have a hierarchical structure and may change when devices move between networks.

#### 3. When a host wants to send a datagram to another host on the same subnet, what must it first determine?
**Answer:**
The MAC address corresponding to the destination IP address using ARP.


## 📂 Category: Link Layer & Error Detection (1 cards)

### 🔴 Senior Level

#### 1. What is the capability of CRC codes in terms of burst error detection?
**Answer:**
They can detect bursts of errors up to a certain length and odd numbers of bit errors.


## 📂 Category: Link Layer & Hardware (2 cards)

### 🟢 Junior Level

#### 1. Who manages the allocation of MAC addresses to ensure uniqueness across devices?
**Answer:**
The IEEE (Institute of Electrical and Electronics Engineers) manages the MAC address space.


### 🟡 Mid Level

#### 1. What are two primary functions of a network adapter in a host?
**Answer:**
Implementing link-layer services like framing and error detection, and facilitating communication with higher protocol layers.


## 📂 Category: Local Area Networks (5 cards)

### 🟢 Junior Level

#### 1. What is one major drawback of a hierarchical LAN configuration regarding traffic?
**Answer:**
Lack of traffic isolation, leading to broadcast traffic traversing the entire network.

#### 2. What role does the network manager play in configuring VLANs?
**Answer:**
The network manager defines port-to-VLAN mappings and manages VLAN membership via software.


### 🟡 Mid Level

#### 1. What are some other methods for defining VLANs besides port-based VLANs?
**Answer:**
MAC-based VLANs, protocol-based VLANs, and other criteria-based VLAN definitions.

#### 2. What can be a downside of completely isolating VLANs?
**Answer:**
It can complicate communication between different VLANs, necessitating additional configurations or routing devices.

#### 3. What is one of the major challenges that VLANs address in hierarchical LANs?
**Answer:**
The need for traffic isolation and efficient network management by creating logical broadcast domains.


## 📂 Category: Medium Access Control (6 cards)

### 🟢 Junior Level

#### 1. What happens if a node transmits a frame without detecting signal energy from other nodes?
**Answer:**
The node completes its frame transmission successfully.


### 🟡 Mid Level

#### 1. How is time divided in Slotted ALOHA?
**Answer:**
Time is divided into slots of size L/R seconds.

#### 2. In Slotted ALOHA, how does a node decide to retransmit a frame after a collision?
**Answer:**
The node retransmits its frame in each subsequent slot with a probability p until successful transmission.

#### 3. What are the core operational assumptions and definition of an "active node" in Slotted ALOHA?
**Answer:**
An active node is one that currently has frames to send. Slotted ALOHA assumes time is divided into discrete slots equal to the transmission time of a fixed frame size of exactly L bits.

#### 4. What fraction of slots in Slotted ALOHA go empty, and how many experience collisions?
**Answer:**
Approximately 37% of the slots are successful, 37% go empty, and 26% experience collisions (derived from Poisson distribution where maximum efficiency is 1/e).

#### 5. What is a potential issue with token-passing protocols?
**Answer:**
If a node fails or fails to release the token, it can disrupt the entire network.


## 📂 Category: Medium Access Control (MAC) (6 cards)

### 🟢 Junior Level

#### 1. Why are multiple access protocols necessary in computer networks?
**Answer:**
To regulate how nodes transmit into a shared broadcast channel to avoid collisions.


### 🟡 Mid Level

#### 1. How do random access protocols differ from channel partitioning protocols?
**Answer:**
In random access protocols, nodes transmit at the full channel rate and independently handle retransmissions after collisions using randomized backoff delays.

#### 2. What is the binary exponential backoff algorithm?
**Answer:**
It is a method where the wait time increases exponentially with the number of collisions experienced.

#### 3. What is the maximum efficiency of Slotted ALOHA and pure ALOHA protocols?
**Answer:**
The maximum efficiency of Slotted ALOHA is 1/e (approximately 0.37) when many nodes are active. Pure ALOHA has a lower maximum efficiency of 1/(2e) (approximately 0.185).

#### 4. When do nodes start to transmit frames in Slotted ALOHA?
**Answer:**
Nodes start to transmit frames only at the beginnings of slots.

#### 5. Why do collisions still occur in CSMA protocols despite carrier sensing?
**Answer:**
Because of non-zero propagation delays; a node may sense the channel as idle and begin transmitting even while another distant node's transmission is already in flight.


## 📂 Category: Mobile & Cellular Networks (6 cards)

### 🟢 Junior Level

#### 1. What scenario describes a mobile user who powers down their device while moving?
**Answer:**
Scenario (a), where the user disconnects from one wireless network and connects to another after powering on their device.


### 🟡 Mid Level

#### 1. What physical factors influence the coverage area of a cellular network cell?
**Answer:**
The transmitting power of the base station and mobile devices, physical obstructions like buildings and terrain, and the type, orientation, and height of base station antennas.

#### 2. Why does the 5G Core network require substantial investments?
**Answer:**
Due to the need for new physical infrastructure that is not backward-compatible with 4G core architectures.


### 🔴 Senior Level

#### 1. What is the role of the User-Plane Function (UPF) in the 5G Core architecture?
**Answer:**
It handles user plane packet routing and forwarding, allowing packet inspection and processing to be distributed and pushed closer to the network edge.

#### 2. What role does the Mobility Management Entity (MME) play during network attachment and control-plane configuration for a mobile device?
**Answer:**
It retrieves authentication, encryption, and network service information for the subscriber, informs the HSS of the device's location, and facilitates mutual authentication and data path configuration.

#### 3. Why has Mobile IP not been widely deployed despite existing technical solutions?
**Answer:**
The lack of motivating business cases, administrative overhead, and the timely development of alternative mobility solutions built directly into cellular networks have hindered Mobile IP deployment.


## 📂 Category: Mobile & Wireless Networks (12 cards)

### 🟢 Junior Level

#### 1. What does the term 'cellular' refer to in cellular network architecture?
**Answer:**
The geographic coverage area is divided into smaller zones called cells, each serviced by a base station that manages wireless mobile devices within its range.

#### 2. What radio band do Bluetooth networks operate in?
**Answer:**
The unlicensed 2.4 GHz Industrial, Scientific, and Medical (ISM) radio band, utilizing frequency hopping spread spectrum (FHSS).


### 🟡 Mid Level

#### 1. What are the two main parts of a 4G LTE network architecture?
**Answer:**
The radio network at the edge and the core network.

#### 2. What are the two main reasons why 802.11 does not implement collision detection?
**Answer:**
The hardware cost to detect collisions is high, and the hidden terminal problem makes it impossible to detect all collisions.

#### 3. What happens to a mobile device in the Idle state?
**Answer:**
It wakes up even less frequently and may not inform the base station of cell changes.


### 🔴 Senior Level

#### 1. How does the base station communicate with the Serving Gateway in LTE networks?
**Answer:**
Through encapsulated UDP segments containing user datagrams tunneled across the core network (Evolved Packet Core).

#### 2. What are the two main sleep states in LTE for power management?
**Answer:**
Discontinuous Reception (DRX) and Idle state.

#### 3. What are the two options for how a mobile device sends datagrams back to the correspondent?
**Answer:**
(4a) The datagram can be tunneled back to the home gateway, or (4b) sent directly to the correspondent from the visited network (local breakout).

#### 4. What are the two tunnels established during the data-plane configuration of a mobile device in LTE?
**Answer:**
One tunnel between the base station and the Serving Gateway, and another between the Serving Gateway and the PDN Gateway in the home network.

#### 5. What happens to cell location tracking when a device is in sleep mode?
**Answer:**
The base stations can no longer track the device, so the MME must locate the device through a process called paging.

#### 6. What is the role of the Mobility Management Entity (MME) in mobile networks?
**Answer:**
The MME tracks the current visited network of the mobile device, updates its location as needed, manages device authentication, and sets up data tunnels for active mobile devices.

#### 7. What protocol is used for tunneling datagrams in 4G/5G and LTE networks?
**Answer:**
The GPRS Tunneling Protocol (GTP), specifically GTP-U for user-plane datagram encapsulation.


## 📂 Category: Mobile & Wireless Security (1 cards)

### 🟡 Mid Level

#### 1. What does the Mutual Authentication phase ensure in cellular networks like LTE?
**Answer:**
It ensures that both the mobile device and the network authenticate each other, verifying the identity of the mobile device against the visited network and vice versa.


## 📂 Category: Mobile Networking (5 cards)

### 🟢 Junior Level

#### 1. What mobility state does scenario (b) represent in terms of device mobility and access networks?
**Answer:**
The device is physically mobile but remains attached to the same access network without changing its link-layer association.


### 🟡 Mid Level

#### 1. What is the limitation of using the existing IP address infrastructure for mobile devices?
**Answer:**
Scalability issues arise because routers would need to maintain entries for billions of mobile devices.


### 🔴 Senior Level

#### 1. What is the difference between direct and indirect routing for datagrams to a mobile device?
**Answer:**
Indirect routing involves a home network coordinating the delivery of messages, while direct routing sends messages directly to the device’s current IP address.

#### 2. What is the main disadvantage of indirect routing?
**Answer:**
It suffers from the triangle routing problem, where datagrams are unnecessarily routed through the home network agent before reaching the visited network.

#### 3. What two types of networks does Mobile IP distinguish between, and how are addresses handled?
**Answer:**
Mobile IP distinguishes between a home network (where a mobile device has a permanent IP address) and foreign networks (where the device is assigned a care-of-address).


## 📂 Category: Mobile Networks (23 cards)

### 🟢 Junior Level

#### 1. What is a mobile device in the context of a 4G LTE network?
**Answer:**
A smartphone, tablet, laptop, or IoT device that connects to the cellular carrier’s network and runs various applications.


### 🟡 Mid Level

#### 1. How does direct routing differ from indirect routing in terms of efficiency?
**Answer:**
Direct routing allows datagrams to be sent directly from the correspondent to the mobile device's visited network, avoiding the inefficiency of routing through the home network.

#### 2. What are the implications of a mobile device having a permanent IP address in its home network?
**Answer:**
It allows for easy identification and routing, but the device must also acquire a temporary IP address in the visited network.

#### 3. What are the three co-existing standards of 5G?
**Answer:**
eMBB (Enhanced Mobile Broadband), URLLC (Ultra Reliable Low-Latency Communications), and mMTC (Massive Machine Type Communications).

#### 4. What does the Home Subscriber Server (HSS) do in a 4G LTE network?
**Answer:**
It stores information about mobile devices and assists in device authentication.

#### 5. What does the home network represent in mobility management?
**Answer:**
It serves as a central point of information and control for mobile devices subscribed to it.

#### 6. What is the primary underlying protocol used for communication among core LTE network elements?
**Answer:**
The Internet Protocol (IP), encapsulating signaling and user-plane traffic over an all-IP flat architecture.

#### 7. What role does the Home Agent play in Mobile IP?
**Answer:**
The Home Agent tracks the location of a mobile device and manages updates from foreign agents in visited networks.


### 🔴 Senior Level

#### 1. How does LTE handle the encapsulation of user data?
**Answer:**
By creating tunnels with unique tunnel endpoint identifiers (TEIDs) for data transmission.

#### 2. How does Mobile IP differ from traditional wired networks, and how does it handle indirect routing?
**Answer:**
Mobile IP accommodates mobile users changing points of attachment (whereas traditional wired networks typically do not) and uses indirect routing with tunneling to connect gateway routers in both home and visited networks.

#### 3. What are the key fundamental challenges in developing a network architecture to support device mobility?
**Answer:**
The notions of home and visited networks, the role of the home network as a control point, control-plane functions for tracking mobile devices, and data-plane routing approaches.

#### 4. What are the roles of the Serving Gateway (S-GW) and Packet Data Network Gateway (P-GW)?
**Answer:**
They route data between the mobile device and the Internet and provide NAT IP addresses to mobile devices.

#### 5. What are the three basic approaches to routing datagrams to a mobile device?
**Answer:**
1) Using existing IP address infrastructure, 2) Mobile device tracking by the home network, 3) Utilizing NAT.

#### 6. What are the three main components of the Mobile IP standard?
**Answer:**
The three main components are agent discovery, registration with the home agent, and indirect routing of datagrams.

#### 7. What are the three phases of mobile device attachment to the LTE network?
**Answer:**
Attachment to a Base Station, Mutual Authentication, and Mobile-device-to-PDN-gateway Data Path Configuration.

#### 8. What are the three sublayers of the LTE mobile device’s link layer?
**Answer:**
Packet Data Convergence (PDCP), Radio Link Control (RLC), and Medium Access Control (MAC).

#### 9. What are the two elements that the 4G Mobility Management Entity (MME) is decomposed into in 5G?
**Answer:**
Access and Mobility Management Function (AMF) and Session Management Function (SMF).

#### 10. What does the Medium Access Control (MAC) layer manage in LTE?
**Answer:**
Transmission scheduling and additional error detection/correction.

#### 11. What does the mobile device search for during the initial attachment phase?
**Answer:**
A primary synchronization signal broadcast by a base station.

#### 12. What is a key requirement for the mobile device when it roams between networks in indirect routing?
**Answer:**
The mobile device must update its location information in the home network's HSS and manage its association/disassociation with visited networks.

#### 13. What is the primary function of the correspondent in indirect routing to a mobile device?
**Answer:**
The correspondent addresses the datagram to the mobile device's permanent address and sends it into the network, remaining entirely unaware of the mobile device's current point of attachment or roaming location.

#### 14. What is the purpose of the Control-plane configuration for the mobile device in a visited network?
**Answer:**
To establish control-plane state indicating the mobile device's residency in the visited network.

#### 15. What role does the home network's gateway router play in indirect routing?
**Answer:**
It intercepts incoming datagrams, consults with the HSS to find the mobile device's current visited network, and forwards the datagram to the visited network gateway.


## 📂 Category: Mobile/Wireless Networks (1 cards)

### 🔴 Senior Level

#### 1. What is the main function of the Packet Data Convergence Protocol (PDCP)?
**Answer:**
IP header compression and decompression, ciphering/deciphering of user and control plane data, and integrity protection in cellular networks (e.g., LTE/5G).


## 📂 Category: Multiplexing (2 cards)

### 🟢 Junior Level

#### 1. What is a limitation of FDM?
**Answer:**
Each node is restricted to a bandwidth of R/N even if it is the only one sending data.

#### 2. What is a major drawback of TDM?
**Answer:**
A node is limited to an average transmission rate of R/N even when it is the only node with packets to send.


## 📂 Category: Multiplexing & Switching (2 cards)

### 🟢 Junior Level

#### 1. In what scenario does packet switching provide similar performance to circuit switching?
**Answer:**
When there are fewer users transmitting data than the maximum aggregate capacity of the link, resulting in little to no queuing delay.


### 🟡 Mid Level

#### 1. In the context of circuit switching, what does each time slot in TDM represent, and how is the transmission rate determined?
**Answer:**
Each time slot represents a dedicated portion of the link's transmission capacity allocated to a specific connection. A circuit's transmission rate is determined by multiplying the frame rate by the number of bits per slot.


## 📂 Category: Multiprotocol Label Switching (1 cards)

### 🟡 Mid Level

#### 1. What is a label-switched router (LSR)?
**Answer:**
An MPLS-capable router that forwards packets based on MPLS labels rather than destination IP addresses.


## 📂 Category: Network Address Translation (NAT) (1 cards)

### 🟡 Mid Level

#### 1. When a device in a home network requests a webpage, what does the NAT router do with the source port number?
**Answer:**
The NAT router generates a new source port number and replaces the original port number in the datagram.


## 📂 Category: Network Architecture (58 cards)

### 🟢 Junior Level

#### 1. At which layer of the protocol stack do processes communicate with each other?
**Answer:**
Processes communicate with each other at the application layer of the five-layer protocol stack.

#### 2. How are access ISPs interconnected in Network Structure 1?
**Answer:**
They are interconnected by a single global transit ISP that provides global reachability.

#### 3. How do access ISPs differ from regional ISPs?
**Answer:**
Access ISPs provide direct physical and logical Internet connectivity to end users (homes/businesses), while regional ISPs serve as intermediaries, connecting access ISPs to higher-tier backbone ISPs.

#### 4. How does packet switching handle link congestion compared to circuit switching?
**Answer:**
Packet switching allows packets to queue and wait for transmission if the link is busy, while circuit switching guarantees a fixed transmission rate.

#### 5. How does the transport layer differ from the network layer?
**Answer:**
The transport layer provides logical communication between processes on different hosts, while the network layer provides logical communication between hosts themselves.

#### 6. How is forwarding typically implemented in routers?
**Answer:**
It is implemented in hardware and takes place at very short timescales (typically a few nanoseconds).

#### 7. In the context of encapsulation, what does a transport-layer segment consist of?
**Answer:**
A transport-layer segment consists of an application-layer message and transport-layer header information that is added by the transport layer.

#### 8. What analogy is used to explain the relationship between the transport layer and the network layer?
**Answer:**
The postal service serves as an analogy for the network layer, moving mail (datagrams) between houses (hosts), while the communicating parties serve as the transport layer, managing communication among the processes.

#### 9. What are the two main types of packet switches in the Internet?
**Answer:**
Routers (network-layer switches) and link-layer switches.

#### 10. What are the two methods used to implement a circuit on a link in circuit-switched networks?
**Answer:**
Frequency-Division Multiplexing (FDM) and Time-Division Multiplexing (TDM).

#### 11. What can cause packet loss in a network?
**Answer:**
Packet loss occurs when the output buffer is full, causing arriving packets or already queued packets to be dropped.

#### 12. What can cause transmission delays to become significant in some cases?
**Answer:**
Transmission delays can be significant for low-speed links, such as dial-up modem links, especially for large packets.

#### 13. What criticism do proponents of packet switching have against circuit switching?
**Answer:**
Circuit switching is wasteful because resources remain idle during silent or inactive periods.

#### 14. What defines a Tier-1 ISP?
**Answer:**
A Tier-1 ISP is a major global Internet service provider that has complete global reach and peers with all other Tier-1 ISPs without paying for transit.

#### 15. What distinguishes a switch from a router in terms of the OSI model?
**Answer:**
A switch operates at layer 2 (data link layer) using MAC addresses, while a router operates at layer 3 (network layer) using IP addresses.

#### 16. What does store-and-forward transmission mean in packet-switched networks?
**Answer:**
The packet switch must receive the entire packet before it can begin transmitting it onto the outbound link.

#### 17. What factors influence the length of queuing delay for a packet at a router output buffer?
**Answer:**
The arrival rate of packets, the transmission rate of the link, and the number of packets already queued and waiting in the buffer to be transmitted.

#### 18. What happens to a large message during encapsulation?
**Answer:**
A large message may be divided into multiple transport-layer segments, which can further be divided into multiple network-layer datagrams for transmission.

#### 19. What is TCP/IP?
**Answer:**
TCP/IP is the foundational suite of communication protocols used to interconnect network devices on the Internet, comprising core protocols such as the Transmission Control Protocol (TCP) and the Internet Protocol (IP).

#### 20. What is an access network?
**Answer:**
An access network is the network that physically connects an end system (host) to the first router (edge router) on a path to any other destination on the Internet.

#### 21. What is encapsulation in networking?
**Answer:**
Encapsulation is the process of adding header information to packets at each layer of the protocol stack, enabling them to be delivered correctly between sender and receiver.

#### 22. What is protocol layering?
**Answer:**
Protocol layering is the structural organization of network protocols into hierarchical layers (e.g., OSI or TCP/IP models). Each layer provides specific services to the layer above and relies on the services provided by the layer below, encapsulating data with layer-specific headers.

#### 23. What is the "network edge" in the context of the Internet?
**Answer:**
The network edge refers to the devices (e.g., computers, smartphones) connected to the Internet, which are known as end systems.

#### 24. What is the main role of access ISPs in the Internet structure?
**Answer:**
Access ISPs connect end systems like PCs, smartphones, and servers to the Internet.

#### 25. What is the primary difference between circuit switching and packet switching regarding resource allocation?
**Answer:**
Circuit switching reserves dedicated resources for the entire session duration, guaranteeing bandwidth, while packet switching uses network resources on-demand without explicit reservations, relying on statistical multiplexing.

#### 26. What is the primary function of the network layer in the OSI model?
**Answer:**
It moves network-layer packets, known as datagrams, from one host to another and determines the optimal routing paths for these datagrams.

#### 27. What is the purpose of header information in encapsulation?
**Answer:**
Header information is used by network devices to route and deliver packets correctly across layers, providing essential control details such as source and destination addresses, protocol types, and sequence numbers.

#### 28. What is the purpose of upper-tier ISPs?
**Answer:**
To interconnect lower-tier ISPs, creating a global Internet infrastructure.

#### 29. What is the relationship between access ISPs, regional ISPs, and tier-1 ISPs in a multi-tier Internet hierarchy?
**Answer:**
Access ISPs connect to regional ISPs, which in turn connect to tier-1 ISPs, forming a customer-provider relationship at each level.

#### 30. What is the role of a packet switch?
**Answer:**
A packet switch forwards packets from one incoming communication link to an outgoing link towards their destination.

#### 31. What is the role of standards in the Internet?
**Answer:**
Standards ensure that systems and products created by different people or companies interoperate.

#### 32. What is the role of standards in the Internet?
**Answer:**
Standards ensure that systems and products created by different people or companies interoperate.

#### 33. What is the role of the physical layer in network communications?
**Answer:**
It is responsible for moving individual bits within a frame from one node to the next over a specific physical transmission medium.

#### 34. What is the significance of redundant network equipment in data centers?
**Answer:**
It ensures high availability of cloud applications by providing backup connections and equipment.

#### 35. What is the structural benefit of the Internet's ISP hierarchy?
**Answer:**
Lower-tier ISPs connect to higher-tier ISPs to obtain global Internet reachability, while higher-tier ISPs interconnect with each other to provide broad backbone coverage.

#### 36. What organization is responsible for managing IP address space globally?
**Answer:**
The Internet Corporation for Assigned Names and Numbers (ICANN).

#### 37. What structural change occurs in Network Structure 2 compared to Structure 1 regarding transit ISPs?
**Answer:**
Multiple competing global transit ISPs are introduced, giving access ISPs a choice of providers.

#### 38. Why do packet-switched networks offer better link efficiency than circuit-switched networks?
**Answer:**
Packet-switched networks allocate bandwidth dynamically on demand (statistical multiplexing), whereas circuit-switched networks reserve dedicated circuits regardless of active usage.

#### 39. Why is it impractical for each access ISP to directly connect to all other access ISPs?
**Answer:**
It would be too costly, requiring each access ISP to have individual communication links to hundreds of thousands of other ISPs worldwide.


### 🟡 Mid Level

#### 1. Describe the hierarchical architecture of a data center network.
**Answer:**
It includes a border router, access routers, and multiple tiers of switches connecting to racks, allowing for scalability to hundreds of thousands of hosts.

#### 2. What advantages does a tiered interconnection network have over a conceptual crossbar switch?
**Answer:**
It provides multiple paths from source to destination, increased capacity through multipath routing, and improved reliability with multiple switch- and link-disjoint paths.

#### 3. What are the three broad types of services performed by middleboxes?
**Answer:**
NAT Translation, Security Services, and Performance Enhancement.

#### 4. What does the "IP hourglass" refer to in Internet architecture?
**Answer:**
The narrow waist of the layered Internet protocol stack where IP (Internet Protocol) is the single network-layer protocol required across all heterogeneous underlying link layers and upper-layer transports.

#### 5. What happens when multiple flows traverse a link in a data center?
**Answer:**
They share the link's capacity, which can significantly reduce the bandwidth available to each flow.

#### 6. What is a potential drawback of protocol layering?
**Answer:**
A potential drawback is that functionality may be duplicated across layers, such as error recovery being implemented both at the link and transport layers.

#### 7. What is the processing difference between switches and routers?
**Answer:**
Switches process frames only up to layer 2 (Data Link), while routers process up to layer 3 (Network), making routers typically slower per packet due to routing table lookups and TTL decrements.

#### 8. What is the purpose of a service model in protocol layering?
**Answer:**
The service model defines the specific services provided by a layer to the layer immediately above it, outlining how adjacent protocols interact within the layered network architecture.

#### 9. What is the role of routers and link-layer switches in a network?
**Answer:**
Routers and link-layer switches organize their hardware and software into layers, enabling them to switch packets through the network, but they typically implement only the bottom layers of the protocol stack.

#### 10. Why is the Software-Defined Networking (SDN) approach becoming more popular?
**Answer:**
It allows for open-source implementations, enabling ISPs and researchers to innovate, program, and propose rapid changes to network-layer functionality.


### 🔴 Senior Level

#### 1. Define middleboxes as per RFC 3234.
**Answer:**
Any intermediary box performing functions apart from normal, standard functions of an IP router on the data path between a source and destination host.

#### 2. What architectural principle emphasizes that the intelligence in the network should be end-to-end?
**Answer:**
The end-to-end argument.

#### 3. What are Clos networks, and who is it named after?
**Answer:**
A type of multi-switch layered interconnection network, named after Charles Clos, who studied such networks in telephony.

#### 4. What argument do critics of packet switching make regarding real-time services?
**Answer:**
They argue that packet switching is unsuitable for real-time services due to variable and unpredictable end-to-end delays.

#### 5. What is the critique regarding middleboxes in relation to the original Internet architecture?
**Answer:**
They blur the separation between the network layer and transport/application layers by implementing functions traditionally done at the edges.

#### 6. What is the relationship between MPLS and SDN (Software-Defined Networking)?
**Answer:**
While MPLS has its own traffic management capabilities, some of those can also be achieved through SDN technology.

#### 7. What is the relationship between the data plane and control plane in modern data centers?
**Answer:**
They are clearly separated, allowing for more efficient management and operation.

#### 8. What is the significance of RFC 1958 in Internet architecture?
**Answer:**
It outlines minimal architectural principles for the Internet, emphasizing connectivity and the role of the Internet Protocol.

#### 9. What key argument does Saltzer's 'end-to-end argument' make regarding system design?
**Answer:**
Certain complex network functions (like reliable delivery, security, and integrity checks) can only be completely and correctly implemented with the knowledge and active participation of applications at the endpoints.


## 📂 Category: Network Architecture & Switching (2 cards)

### 🟢 Junior Level

#### 1. How do layer-2 switches improve network performance compared to legacy hubs?
**Answer:**
By operating on individual collision domains, filtering frames based on MAC addresses, and buffering frames to transmit only onto the targeted segment.

#### 2. How do packet arrival rates impact queuing and packet loss?
**Answer:**
High packet arrival rates, especially when they exceed the switching or processing capacity, lead to longer queues in buffers and an increased probability of packet loss.


## 📂 Category: Network Architecture / Routers (1 cards)

### 🟡 Mid Level

#### 1. What is the role of the routing processor in a router?
**Answer:**
It maintains routing tables, executes routing protocols, and computes the forwarding table for the router.


## 📂 Category: Network Architecture / Switches (1 cards)

### 🔴 Senior Level

#### 1. What is the role of the switch fabric controller in a crossbar switch?
**Answer:**
The switch fabric controller manages which crosspoints are open or closed to direct packets from input to output ports.


## 📂 Category: Network Architectures (2 cards)

### 🟢 Junior Level

#### 1. What is the key difference between client-server and peer-to-peer architectures?
**Answer:**
P2P architectures minimize reliance on always-on infrastructure servers, allowing direct communication between intermittently connected peers.

#### 2. Why might a single server in a client-server architecture become overwhelmed?
**Answer:**
A single server may become overwhelmed by too many concurrent requests, especially for popular services like social networks, creating a central bottleneck.


## 📂 Category: Network Automation (1 cards)

### 🔴 Senior Level

#### 1. How does YANG help ensure the correctness of NETCONF configurations?
**Answer:**
It provides a data modeling language that allows modelers to express precise constraints, types, and structures that must be satisfied by a valid configuration before it is applied.


## 📂 Category: Network Diagnostics (2 cards)

### 🟢 Junior Level

#### 1. What diagnostic output does the Traceroute program generate for each hop?
**Answer:**
It provides the IP address (and resolved hostname) of each intermediate router along the path, along with the round-trip delay measurements for a series of probe packets.


### 🟡 Mid Level

#### 1. How does Traceroute help in understanding end-to-end delay?
**Answer:**
Traceroute sends packets to the destination and records the round-trip delays for each router along the path using ICMP Time Exceeded messages or UDP/TCP probes with incremental TTL values.


## 📂 Category: Network Fundamentals (25 cards)

### 🟢 Junior Level

#### 1. How is the cost of a path defined in a graph representing a network?
**Answer:**
The cost of a path is the sum of the costs of all edges along that path.

#### 2. How is the transmission rate of a communication link measured?
**Answer:**
In bits per second (bps)

#### 3. What are examples of network access types provided by ISPs?
**Answer:**
Cable modem, DSL, high-speed local area networks, and mobile wireless access.

#### 4. What are packets in the context of packet switching?
**Answer:**
Small chunks of data into which long messages are broken for transmission over the network.

#### 5. What are the four types of delays a packet experiences at each node in a packet-switched network?
**Answer:**
Nodal processing delay, queuing delay, transmission delay, and propagation delay.

#### 6. What defines a protocol in computer networking?
**Answer:**
A protocol defines the format, the order of messages exchanged, and the actions taken upon message transmission or receipt.

#### 7. What determines the end-to-end throughput of a network path with multiple sequential links?
**Answer:**
The throughput is determined by the transmission rate of the bottleneck link, which is the link with the lowest capacity along the path.

#### 8. What fundamental physical components connect end systems in a computer network?
**Answer:**
End systems are connected by communication links (wired/wireless media) and packet switches (routers and switches).

#### 9. What is a "circuit" in a circuit-switched network?
**Answer:**
A circuit is a dedicated connection path between the sender and receiver, where resources like transmission rate are reserved for the entire communication session.

#### 10. What is a "network of networks" in the context of the Internet?
**Answer:**
The Internet is composed of multiple networks, including access ISPs, regional ISPs, and tier-1 ISPs, all interconnected to form a global network.

#### 11. What is a network protocol?
**Answer:**
A network protocol is a set of rules that govern the exchange of messages and actions taken by hardware or software components in a device.

#### 12. What is a packet in the context of computer networks?
**Answer:**
A packet is a segment of data with added header bytes that is sent through a network.

#### 13. What is a route or path in a network?
**Answer:**
The sequence of communication links and packet switches a packet travels through from sender to receiver.

#### 14. What is nodal processing delay?
**Answer:**
The time required for a router to examine a packet's header and determine its outbound link, and to check for bit-level errors.

#### 15. What is packet switching?
**Answer:**
A method of transmitting data where long messages are broken into smaller packets that are transmitted independently over communication links.

#### 16. What is propagation delay in a packet-switched network?
**Answer:**
Propagation delay is the time it takes for a bit to propagate from the start of a physical link to the next router, calculated as distance divided by the propagation speed of the medium ($d/s$).

#### 17. What is the main difference between application architecture and network architecture?
**Answer:**
Application architecture is designed by the application developer and dictates how the application is structured over end systems, while network architecture provides a fixed set of core communication services to applications.

#### 18. What is the most complex component of nodal delay?
**Answer:**
Queuing delay, which varies dynamically based on network traffic load and buffer occupancy.

#### 19. What is the primary inefficiency of circuit switching during idle transmission periods?
**Answer:**
Network resources (such as bandwidth and time slots) remain fully reserved and unused during idle periods, preventing other users from utilizing them.

#### 20. What is the throughput of a network in a simple two-link connection?
**Answer:**
Throughput is the minimum of the transmission rates of the two links, min(Rs, Rc), where Rs is the server's link rate and Rc is the client's link rate.

#### 21. When is propagation delay most significant?
**Answer:**
Propagation delay is most significant in wide-area networks, such as when routers are interconnected by a geostationary satellite link.

#### 22. Why are end systems called "hosts" in the Internet?
**Answer:**
End systems are called hosts because they run application programs, such as web browsers and email programs.

#### 23. Why can't networks achieve instantaneous data transfer between end systems?
**Answer:**
Physical laws and hardware constraints dictate limits in propagation delay, transmission throughput, and queueing delays, rendering instantaneous data transfer impossible.


### 🟡 Mid Level

#### 1. What is the difference between store-and-forward transmission and forwarding bits immediately as they arrive?
**Answer:**
Store-and-forward routers wait for the entire packet to arrive, check for bit errors, and then begin transmitting it to the next link. Immediate forwarding (cut-through switching) begins forwarding bits as soon as the header is processed, reducing latency but risking propagation of corrupted frames.

#### 2. What is the effect of transmission speed on queuing delays?
**Answer:**
If the switching fabric and output link operate significantly faster than line arrival speeds, queuing is minimized. Otherwise, if traffic arrival rate temporarily exceeds link capacity, queues grow and lead to packet loss.


## 📂 Category: Network Hardware (1 cards)

### 🟡 Mid Level

#### 1. What is a layer-4 switch?
**Answer:**
A type of load balancer that makes decisions based on the destination port number and destination IP address.


## 📂 Category: Network Infrastructure (5 cards)

### 🟢 Junior Level

#### 1. What function does a digital subscriber line access multiplexer (DSLAM) serve?
**Answer:**
A DSLAM separates data and telephone signals at the telephone company’s central office and sends the data into the Internet.

#### 2. What is an Internet Service Provider (ISP)?
**Answer:**
An ISP provides access to the Internet through networks of packet switches and communication links.

#### 3. What is asymmetric Internet access?
**Answer:**
Asymmetric access refers to a situation where the downstream (download) transmission rate is higher than the upstream (upload) rate, common in DSL and cable networks.


### 🟡 Mid Level

#### 1. What is an Internet Exchange Point (IXP)?
**Answer:**
An IXP is a physical location where multiple ISPs can connect and exchange traffic directly with each other, reducing costs and improving efficiency.

#### 2. Why is memory bandwidth a critical consideration in routers using memory switching?
**Answer:**
Limited memory bandwidth can restrict the rate at which packets are forwarded, affecting overall throughput.


## 📂 Category: Network Layer (99 cards)

### 🟢 Junior Level

#### 1. How do dynamic routing algorithms respond to changes in the network?
**Answer:**
They update routing paths either periodically or in response to changes in network topology or link costs.

#### 2. How does DHCP help in scenarios where devices frequently change subnets, like students moving with laptops?
**Answer:**
DHCP allows automatic reassignment and leasing of IP addresses and gateway configurations, reducing the need for manual network reconfiguration.

#### 3. How does IP fragmentation work in IPv4?
**Answer:**
Large datagrams can be divided into smaller ones to be sent independently, then reassembled at the destination.

#### 4. How does the waste of capacity occur when packets are dropped in the network?
**Answer:**
Transmission capacity used to forward packets to a router is wasted if those packets are dropped before reaching their destination.

#### 5. How is an IPv4 address structured?
**Answer:**
An IPv4 address consists of 32 bits, typically represented as four 8-bit octets expressed as decimal numbers separated by periods (e.g., 192.168.1.1), divided into network and host portions.

#### 6. What advantage does packet switching have in terms of cost and complexity compared to circuit switching?
**Answer:**
Packet switching is simpler and less costly to implement since it doesn't require end-to-end resource reservations or complex signaling protocols prior to transmission.

#### 7. What are routing protocols in the context of the network layer?
**Answer:**
Routing protocols determine the routes datagrams take between sources and destinations in a network, functioning within the IP layer.

#### 8. What are the two important functions of the network layer?
**Answer:**
Forwarding and Routing.

#### 9. What are the two versions of the Internet Protocol in use today?
**Answer:**
IPv4 and IPv6

#### 10. What are two common identifiers for Internet hosts?
**Answer:**
Hostnames and IP addresses.

#### 11. What defines a subnet in IP addressing?
**Answer:**
A subnet is a network segment where devices share the same network address and can communicate directly.

#### 12. What does a DHCP server provide in response to a DHCP discover message?
**Answer:**
The server sends a DHCP offer message containing a proposed IP address, subnet mask, gateway, and other network configuration parameters.

#### 13. What does best-effort service mean in the context of networking?
**Answer:**
It means packets are not guaranteed to be received in order or at all, nor is there any guarantee on delay or available bandwidth.

#### 14. What does the Address Resolution Protocol (ARP) table in a host or router contain?
**Answer:**
Mappings of IPv4 addresses to MAC (layer 2) hardware addresses, along with a time-to-live (TTL) expiration value for each entry.

#### 15. What does the IP protocol specify?
**Answer:**
The format of packets sent and received among routers and end systems.

#### 16. What does the hop limit field in an IPv6 header do?
**Answer:**
It counts down by one for each router that forwards the datagram, and the datagram is discarded when the count reaches zero.

#### 17. What happens when a packet arrives at a router and the outbound link is busy?
**Answer:**
The packet waits in the output buffer, incurring queuing delay.

#### 18. What happens when the Time-to-Live (TTL) field reaches 0 in an IPv4 datagram?
**Answer:**
The router must drop the datagram to prevent it from circulating indefinitely.

#### 19. What hierarchical structure is used in the Internet for addressing end systems?
**Answer:**
IP addresses

#### 20. What is a forwarding table in a router?
**Answer:**
A data structure maintained by a router that maps destination IP address ranges (or header field values) to outgoing link interfaces for packet forwarding.

#### 21. What is an IP address, and what role does it play in network communication?
**Answer:**
An IP address is a 32-bit identifier that uniquely identifies a host on the Internet.

#### 22. What is an IPv4 datagram?
**Answer:**
It is the packet format used in IPv4, consisting of various fields for control and data.

#### 23. What is the difference between static and dynamic routing algorithms?
**Answer:**
Static routing algorithms change routes slowly and typically require manual administrator updates. Dynamic routing algorithms (e.g., OSPF, BGP) adjust routes automatically based on changing network topology and traffic conditions.

#### 24. What is the distinction between routing and forwarding in the network layer?
**Answer:**
Routing refers to the network-wide process (using algorithms like Dijkstra's or Bellman-Ford) of determining the optimal end-to-end path packets take from a sender to a receiver, whereas forwarding is the local action of moving a packet from an input link to the appropriate output link.

#### 25. What is the dotted-decimal notation used for in IPv4 addressing?
**Answer:**
It represents 32-bit IPv4 addresses in a human-readable format, where each of the four bytes (octets) is converted to its decimal value (0-255) separated by dots (e.g., 192.168.1.1).

#### 26. What is the function of the ICMP echo request and echo reply messages?
**Answer:**
The echo request (type 8) is sent by the ping program, and the destination replies with an echo reply (type 0), verifying the host's connectivity.

#### 27. What is the nature of the Internet's network-layer service (IP)?
**Answer:**
IP service is best-effort and unreliable; it does not guarantee delivery, in-order delivery, or data integrity.

#### 28. What is the primary function of routing protocols in routers?
**Answer:**
Protocols in routers determine a packet’s optimal path from source to destination across the network.

#### 29. What is the primary function of the network layer in terms of packet delivery?
**Answer:**
The network layer defines the characteristics of end-to-end delivery of packets between sending and receiving hosts across heterogeneous internetworks.

#### 30. What is the primary protocol used in the Internet’s network layer?
**Answer:**
The Internet Protocol (IP), which defines packet/datagram fields (IPv4/IPv6) and governs how end systems and routers route and process them.

#### 31. What is the primary purpose of the data (payload) field in an IPv4 datagram?
**Answer:**
To carry the transport-layer segment (e.g., TCP or UDP) or other types of encapsulated data to be delivered across the network.

#### 32. What is the primary role of the network layer?
**Answer:**
To move packets from a sending host to a receiving host across different networks via routing and forwarding.

#### 33. What is the primary use of the Internet Control Message Protocol (ICMP)?
**Answer:**
ICMP is primarily used for error reporting and diagnostic operations (such as ping and traceroute) between hosts and routers in a network.

#### 34. What is the purpose of Network Address Translation (NAT)?
**Answer:**
NAT simplifies IPv4 address allocation by allowing multiple devices on a local private network to share a single public IP address when communicating over the public Internet.

#### 35. What is the purpose of the "type of service" (TOS) field in an IPv4 datagram?
**Answer:**
To distinguish different types of IP datagrams for prioritized handling, such as real-time vs. non-real-time traffic.

#### 36. What is the purpose of the IP broadcast address 255.255.255.255?
**Answer:**
It delivers messages to all hosts on the same local subnet.

#### 37. What is the role of a forwarding table in a router?
**Answer:**
It maps destination addresses to the router’s outbound links to determine where to forward incoming packets.

#### 38. What is the significance of the "version number" in an IPv4 datagram?
**Answer:**
It specifies the IP protocol version of the datagram, helping routers interpret its contents correctly.

#### 39. What is the size of an IPv6 address compared to an IPv4 address?
**Answer:**
IPv6 addresses are 128 bits long, compared to the 32 bits of IPv4 addresses.

#### 40. What role does the "protocol" field in an IPv4 datagram play?
**Answer:**
It indicates the transport-layer protocol (e.g., TCP or UDP) to which the data should be passed.

#### 41. What structural anomalies or problems can occur with IP datagrams during network transmission?
**Answer:**
Datagram overflow/fragmentation issues, out-of-order arrival, and bit corruption.

#### 42. When does a host invoke the ARP protocol in a local area network?
**Answer:**
A host invokes ARP when it needs to encapsulate an IP packet into an Ethernet frame destined for an IP address on the local subnet, but does not have the corresponding MAC address in its local ARP cache/table.

#### 43. Why is a brute-force implementation of the IP forwarding table impractical?
**Answer:**
Because it would require over 4 billion entries to cover all possible 32-bit IPv4 addresses exhaustively.


### 🟡 Mid Level

#### 1. After the router receives the frame, what must it do next?
**Answer:**
The router must consult its forwarding table to determine the correct interface for forwarding the datagram.

#### 2. Describe the function of a crossbar switch in switching networks.
**Answer:**
A crossbar switch consists of buses connecting input and output ports, allowing multiple packets to be forwarded simultaneously through separate buses.

#### 3. How do NAT boxes function in a network?
**Answer:**
They implement private network addressing by rewriting datagram header IP addresses and port numbers.

#### 4. How do load-sensitive algorithms help manage network congestion?
**Answer:**
They assign higher costs to congested links, encouraging the routing algorithm to avoid them.

#### 5. How do nodes exchange information in a decentralized routing algorithm?
**Answer:**
Nodes iteratively exchange information with their directly connected neighbors to update and refine their cost estimates.

#### 6. How do output ports function in a router?
**Answer:**
They store packets from the switching fabric and transmit them on the outgoing link, performing necessary layer functions.

#### 7. How does ICMPv6 differ from ICMP for IPv4?
**Answer:**
ICMPv6 reorganizes the type and code definitions and adds new types, like "Packet Too Big" and "unrecognized IPv6 options" error codes.

#### 8. How does Network Address Translation (NAT) assist mobile devices in visited networks?
**Answer:**
NAT assigns a temporary local address to the mobile device within the visited network and correctly translates addresses for incoming and outgoing datagrams.

#### 9. How does a 'centralized routing algorithm' operate compared to a 'decentralized routing algorithm'?
**Answer:**
A centralized routing algorithm computes the least-cost path using complete, global knowledge of the network's topology and link costs (e.g., link-state). In a decentralized algorithm, each node has limited information, knowing only the costs of its directly attached links, and the least-cost path is calculated iteratively through information exchange with neighbors (e.g., distance-vector).

#### 10. How does a NAT-enabled router track and handle internal and external traffic?
**Answer:**
A NAT router appears to the outside world as a single device with a single public IP address, hiding internal network details. It keeps track of internal hosts using a NAT translation table containing private IP/port mappings to public IP/port combinations.

#### 11. How does a home gateway router ensure a correspondent remains unaware of datagram forwarding processes?
**Answer:**
The home gateway encapsulates the original datagram within a new, larger outer datagram before forwarding it across the network.

#### 12. How is an ICMP message encapsulated in an IP datagram?
**Answer:**
ICMP messages are encapsulated directly as the payload of an IP datagram, indicated by the IP protocol number 1 for ICMP.

#### 13. What approach has been widely adopted to transition from IPv4 to IPv6?
**Answer:**
Tunneling, which involves encapsulating IPv6 packets within IPv4 packets for routing through IPv4 networks.

#### 14. What are load-sensitive routing algorithms?
**Answer:**
These algorithms adjust link costs dynamically based on current congestion levels in the network.

#### 15. What does Mobile IP propose regarding home and visited networks?
**Answer:**
Mobile IP incorporates the concept of home networks (permanent IP address anchor) and visited networks (foreign agent routing via care-of addresses), facilitating transparent node mobility across subnets.

#### 16. What does a newly arriving DHCP client do after receiving multiple DHCP offers?
**Answer:**
The client selects one specific lease offer and responds by broadcasting a DHCP request message, locking in the chosen configuration while implicitly declining others.

#### 17. What does the flow label in an IPv6 header do?
**Answer:**
It identifies packets belonging to particular flows that may require special handling or quality of service.

#### 18. What happens if an IPv6 datagram is too large for a router to forward?
**Answer:**
The router drops the datagram and sends a “Packet Too Big” ICMP error message back to the sender.

#### 19. What happens if multiple entries in a forwarding table match a packet's destination address?
**Answer:**
The router uses the longest prefix matching rule to determine which entry to use for forwarding.

#### 20. What happens to the source IP address of a datagram when it passes through a NAT router?
**Answer:**
The source IP address is replaced with the WAN-side IP address of the NAT router.

#### 21. What is CIDR (Classless Interdomain Routing)?
**Answer:**
A method for allocating IP addresses and routing that allows for variable-length subnet masking.

#### 22. What is a distinguishing feature of a centralized routing algorithm?
**Answer:**
It has complete, global information about network connectivity and link costs, calculating end-to-end paths from a single point of view (e.g., link-state algorithms).

#### 23. What is the challenge faced by a correspondent wanting to communicate with a mobile device?
**Answer:**
The correspondent must route datagrams to the mobile device, which may be in its home network or a visited network.

#### 24. What is the difference between a datagram's "identifier" and "fragmentation offset" in IPv4?
**Answer:**
The identifier is used to identify fragments of the same datagram, while the fragmentation offset indicates the position of a fragment in the original datagram.

#### 25. What is the practical application of the Bellman-Ford equation in the Distance Vector (DV) routing algorithm?
**Answer:**
It helps compute the least-cost path and populates the forwarding table with the correct next-hop router for each destination.

#### 26. What is the purpose of the MPLS header in a frame?
**Answer:**
To include the label and other control information necessary for Multi-Protocol Label Switching (MPLS) fast packet forwarding.

#### 27. What is the purpose of the forwarding table in the DV (Distance Vector) algorithm?
**Answer:**
It determines the next-hop router for forwarding packets along the least-cost path to a destination based on distance vector exchanges.

#### 28. What is the purpose of the network service model?
**Answer:**
It defines the characteristics of end-to-end delivery of packets between sending and receiving hosts, such as guaranteed bandwidth, latency bounds, or best-effort delivery.

#### 29. What is the role of the Next Header field in an IPv6 datagram?
**Answer:**
It identifies the protocol to which the contents of the datagram will be delivered, such as TCP or UDP.

#### 30. What is the significance of the NAT translation table?
**Answer:**
It allows the NAT router to map outgoing and incoming traffic by associating external IP and port numbers with internal IP addresses.

#### 31. What is the significance of the set N' in Dijkstra's algorithm?
**Answer:**
N' is the subset of nodes for which the least-cost path from the source is definitively known.

#### 32. What is the traditional approach to implementing routing functionality in routers?
**Answer:**
Each router has its own routing component that communicates with other routers' routing components.

#### 33. What is tunneling in the context of network routing and mobility?
**Answer:**
Tunneling refers to encapsulating a datagram within another datagram (e.g., IP-in-IP) for forwarding, allowing the original datagram to pass through intermediate networks without architectural alteration.

#### 34. What major routing problems does the Distance Vector (DV) algorithm face that the Link State (LS) algorithm avoids?
**Answer:**
The count-to-infinity problem, slow convergence, and routing loops during the update process.

#### 35. What potential issues can arise from dynamic routing algorithms regarding oscillations and loops?
**Answer:**
Dynamic routing algorithms can encounter routing loops and route oscillations (such as when link costs are based on traffic load, causing nodes to repeatedly switch paths).

#### 36. What practical issues besides finding the least cost path influence routing algorithms in the real world?
**Answer:**
Policy issues, such as administrative rules that dictate which routers can or cannot forward packets based on organizational policies and security constraints.

#### 37. What technique can help reduce the number of entries needed in a forwarding table?
**Answer:**
Using prefix matching, where a router matches the prefix of the destination address to table entries.

#### 38. Why is ARP considered to straddle the boundary between the link layer and network layer?
**Answer:**
ARP packets are encapsulated within link-layer frames, but the ARP payload contains both link-layer (MAC) and network-layer (IP) addresses, placing it conceptually between the two layers.


### 🔴 Senior Level

#### 1. Describe head-of-the-line (HOL) blocking in input queuing.
**Answer:**
HOL blocking occurs when a packet at the front of an input queue must wait for another packet, even if its desired output port is free, leading to inefficient queuing.

#### 2. In Dijkstra’s link-state routing algorithm, what do D(v), p(v), and tie-breaking represent?
**Answer:**
D(v) represents the cost of the least-cost path from the source node to destination node v. p(v) indicates the previous node (predecessor) along the current least-cost path from the source to v. If two nodes have the same least-cost path value in an iteration, the tie is broken arbitrarily before updating the set N'.

#### 3. In mobile network indirect routing, where is a datagram initially routed before reaching the mobile node?
**Answer:**
The datagram is initially routed to the mobile device's home network, which then forwards it to the foreign network via tunneling.

#### 4. What additional challenge arises with direct routing compared to indirect routing in mobile networking?
**Answer:**
A mobile-user location protocol is required for the correspondent to query the HSS (Home Subscriber Server) to find the mobile device's current visited network.

#### 5. What additional feature does MOSPF add to OSPF?
**Answer:**
MOSPF extends OSPF to support multicast routing by adding a new type of link-state advertisement (LSA).

#### 6. What are some applications of MPLS in networking?
**Answer:**
Fast restoration of paths, traffic engineering, and the implementation of virtual private networks (VPNs).

#### 7. What does "guaranteed delivery with bounded delay" ensure in networking QoS?
**Answer:**
It guarantees the reliable delivery of packets within a strictly specified maximum delay bound, critical for real-time applications.

#### 8. What happens when router Z routes to X via Y and uses poisoned reverse?
**Answer:**
Z tells Y that the distance to X is infinity (even though it knows the actual distance), ensuring Y won’t route to X via Z, which helps prevent routing loops.

#### 9. What is "Hot Potato Routing" in BGP?
**Answer:**
It refers to the method where a router forwards a packet to the nearest exit point from its AS to minimize the cost within its own AS.

#### 10. What is a flow table in the context of OpenFlow and Software-Defined Networking (SDN)?
**Answer:**
A flow table is an entry in the match-plus-action forwarding table that contains a set of header field values, counters for matched packets, and actions (such as forwarding, dropping, or modifying) to take when a packet matches a particular entry.

#### 11. What is the message complexity of the Distance Vector (DV) routing algorithm?
**Answer:**
The DV algorithm exchanges messages between directly connected neighbors iteratively, and complexity depends on factors like link cost changes and convergence time rather than a static global bound.

#### 12. What is the message complexity of the Link State (LS) routing algorithm?
**Answer:**
O(|N| * |E|), where N is the number of nodes and E is the number of edges, as each node broadcasts its link states to all other nodes in the network.

#### 13. What is the overall impact of high offered load on throughput in multi-hop scenarios?
**Answer:**
Throughput can approach zero as congestion increases due to packet drops and wasted resource utilization across multiple hops.

#### 14. What is the traditional rule of thumb for buffer sizing in routers?
**Answer:**
Buffer size should be equal to the average round-trip time (RTT) multiplied by the link capacity (C).

#### 15. What problem might arise from using IP-Anycast in conjunction with a Content Delivery Network (CDN)?
**Answer:**
BGP routing path changes mid-session can cause different packets in the same persistent TCP connection to be routed to different server replicas, breaking connection state consistency.

#### 16. Why is the Link-State (LS) algorithm considered more robust than Distance-Vector (DV) in case of a router failure?
**Answer:**
LS routers calculate their own routes independently using global topology knowledge, so a failure or incorrect information primarily affects calculations without triggering widespread count-to-infinity problems.

#### 17. Why is traffic engineering important in MPLS networks?
**Answer:**
It allows network operators to manage traffic flows and optimize resource utilization by explicitly directing packets along predetermined paths rather than standard shortest-path routes.

#### 18. Why was fragmentation and reassembly removed from core routers in the IPv6 protocol?
**Answer:**
To speed up IP forwarding within the network core by delegating fragmentation and reassembly tasks solely to the source and destination hosts.


## 📂 Category: Network Layer & Addressing (2 cards)

### 🟢 Junior Level

#### 1. How do NAT routers typically obtain their public IP address?
**Answer:**
NAT routers typically obtain their public IP address dynamically from the ISP via DHCP.

#### 2. What is the first step a newly arriving host must take to connect to a network using DHCP?
**Answer:**
The host must discover a DHCP server by sending a DHCP discover message.


## 📂 Category: Network Layer & Diagnostics (1 cards)

### 🟡 Mid Level

#### 1. How does the Traceroute program use ICMP to determine a path between hosts?
**Answer:**
Traceroute sends IP datagrams with incrementally increasing TTL values; when each TTL expires, routers send ICMP time-exceeded messages back to the source.


## 📂 Category: Network Layer & Mobility (1 cards)

### 🟡 Mid Level

#### 1. What happens to H1's connections if it moves to a different subnet?
**Answer:**
H1 would need to obtain a new IP address, disrupting any ongoing TCP connections.


## 📂 Category: Network Layer & Router Architecture (1 cards)

### 🔴 Senior Level

#### 1. What happens to packets that are sent over a shared bus in a router?
**Answer:**
All output ports receive the packet, but only the port matching the label retains it, while others discard it.


## 📂 Category: Network Layer & Routing (14 cards)

### 🟢 Junior Level

#### 1. How are edge costs typically determined in network graphs?
**Answer:**
Edge costs can reflect factors like physical link length, link speed, propagation delay, or monetary costs associated with using the link.

#### 2. How are individual IP addresses assigned within an organization?
**Answer:**
They can be assigned manually by a system administrator (static assignment) or automatically using the Dynamic Host Configuration Protocol (DHCP).

#### 3. How do routers use IP addresses to forward packets?
**Answer:**
They inspect the destination IP address of an incoming packet, perform a longest-prefix match against their forwarding table to find the appropriate next-hop and outbound link, and rewrite layer-2 headers.

#### 4. What is the longest prefix matching rule?
**Answer:**
It is the rule that states the router forwards a packet to the link interface associated with the longest matching prefix in the forwarding table.

#### 5. What type of mathematical model is used to represent routing problems in networks?
**Answer:**
A graph is used, where nodes represent routers and edges represent physical links between routers.

#### 6. What type of routing protocol is used for routing within an Autonomous System (AS)?
**Answer:**
Intra-AS routing protocol, such as OSPF.

#### 7. What type of service does the Internet's network layer provide?
**Answer:**
Best-effort service.


### 🟡 Mid Level

#### 1. How are forwarding tables configured in routers?
**Answer:**
Through routing algorithms (such as OSPF or BGP) that run in each router, communicating with each other to compute the forwarding table values.

#### 2. How do routers typically handle messages sent to the limited broadcast address 255.255.255.255?
**Answer:**
Routers typically drop limited broadcast packets at the interface boundary and do not forward them to neighboring subnets to mitigate broadcast storms.

#### 3. What is the significance of a router's buffer capacity and drop policies in managing congestion?
**Answer:**
Finite buffer capacity leads to packet drops when buffers are full, affecting overall network performance and requiring retransmissions. Drop policies determine how packets are managed when the queue is full, deciding whether to drop new packets or remove existing ones.

#### 4. What limitations does NAT impose on devices behind it when establishing direct connections?
**Answer:**
NAT can complicate direct peer-to-peer connections and server accessibility due to port number manipulations.

#### 5. What type of ICMP message does a destination host send in response to a UDP datagram with an unlikely port number in Traceroute?
**Answer:**
The destination host sends an ICMP port unreachable message (type 3 code 3).

#### 6. What type of routing algorithm is a 'distance-vector' algorithm?
**Answer:**
It is a decentralized algorithm where each node maintains a vector of estimated costs (distances) to all other nodes and updates these estimates through iterative exchanges with neighboring nodes.


### 🔴 Senior Level

#### 1. What message does BGP use to advertise a subnet's existence to the rest of the Internet?
**Answer:**
BGP messages broadcast prefix reachability information to neighboring ASs.


## 📂 Category: Network Layer / IP (2 cards)

### 🟢 Junior Level

#### 1. Why do routers prefer IP addresses over hostnames for packet forwarding?
**Answer:**
IP addresses have a fixed length and a hierarchical, prefix-aggregatable structure, making them drastically faster and more scalable for routing table lookups.


### 🟡 Mid Level

#### 1. How can NAT support a large number of simultaneous connections with a single public IP address?
**Answer:**
NAT can manage over 60,000 simultaneous connections by utilizing different source port numbers in the translation table for each connection.


## 📂 Category: Network Layer / Routers (2 cards)

### 🟢 Junior Level

#### 1. How does a router determine which outbound link or interface to forward a packet to?
**Answer:**
By examining the packet's destination IP address and using it to index into its forwarding (routing) table, typically employing longest-prefix matching.


### 🟡 Mid Level

#### 1. How do packets traverse a router's internal architecture to reach an output port?
**Answer:**
A packet enters the router through an input port, undergoes header processing and lookup (using the forwarding table to determine the output port), is routed through the switching fabric (via memory, bus, or crossbar), and is queued and transmitted by the designated output port.


## 📂 Category: Network Layer / Routing (5 cards)

### 🟢 Junior Level

#### 1. How do routing algorithms handle multiple paths between two nodes in a network?
**Answer:**
Routing algorithms evaluate all possible paths between the source and destination and select the path with the least total cumulative cost (calculated via metrics like hop count, bandwidth, delay, or cost functions).


### 🟡 Mid Level

#### 1. How does a node update its distance vector in the Distance Vector (DV) routing algorithm?
**Answer:**
A node updates its distance vector using the Bellman-Ford equation: $Dx(y) = \min_v \{{c(x,v) + Dv(y)}\} $, where $c(x,v)$ is the cost to neighbor $v$, and $Dv(y)$ is the cost from $v$ to destination $y$.

#### 2. What is the role of the forwarding table in a node using Dijkstra’s algorithm?
**Answer:**
The forwarding table stores the next-hop node for each destination on the least-cost path from the source.

#### 3. What is the role of the neighbor's distance vector in the DV algorithm?
**Answer:**
A node uses its neighbor’s distance vector to update its own distance estimates to different destinations.


### 🔴 Senior Level

#### 1. How does the speed of convergence differ between LS and DV algorithms?
**Answer:**
LS converges faster with a time complexity of O(|N|²), while DV can converge slowly and may suffer from routing loops during convergence.


## 📂 Category: Network Management (34 cards)

### 🟢 Junior Level

#### 1. Describe the CLI approach to network management.
**Answer:**
The Command Line Interface (CLI) approach allows network operators to issue commands directly to devices, but it can be error-prone and difficult to scale in larger networks.

#### 2. How does VLAN software facilitate user mobility within an organization?
**Answer:**
It allows users to switch departments without needing to physically move cables, merely by reconfiguring VLAN membership on the switch ports.

#### 3. What are some tasks involved in network management?
**Answer:**
Network management includes monitoring, testing, polling, configuring, analyzing, and controlling network resources to meet performance and cost requirements.

#### 4. What defines a managed device in a network management system?
**Answer:**
A managed device is any network equipment, such as routers, switches, or hosts, that resides on a managed network and can be monitored or controlled by a managing server.

#### 5. What does ICANN manage besides IP addresses?
**Answer:**
ICANN also manages DNS root servers and domain name assignments.

#### 6. What does MIB stand for in network management, and what is its role?
**Answer:**
Management Information Base. It is a database containing hierarchical management information used by protocols like SNMP to monitor and configure network devices.

#### 7. What role does SNMP play in network management?
**Answer:**
Simple Network Management Protocol (SNMP) is a widely used protocol for collecting and organizing information about managed devices on IP networks.

#### 8. What type of information can be found in MIB modules and managed devices?
**Answer:**
Operational data, configuration data, device statistics, and protocol-specific information, which can be queried and modified by network managers.


### 🟡 Mid Level

#### 1. Give an example of a type of MIB object.
**Answer:**
A counter, such as the number of IP datagrams discarded due to header errors.

#### 2. How do network switches gather statistics for network management?
**Answer:**
By tracking hardware counters for bandwidth utilization, collision rates, error frames, and traffic classification types via protocols like SNMP or streaming telemetry.

#### 3. How does NETCONF ensure secure communication with managed devices?
**Answer:**
It uses secure, connection-oriented sessions such as TLS over TCP.

#### 4. What are the key advantages and transport considerations of using SNMP for network management?
**Answer:**
SNMP allows for querying and setting values of MIB objects in managed devices, facilitating operational monitoring and device statistics collection. Because it often runs over UDP, it is unreliable and requires the managing server to implement retransmission strategies.

#### 5. What does the GetRequest PDU do in SNMP?
**Answer:**
The GetRequest PDU is sent from a managing server to retrieve the value of one or more MIB object instances from a managed device.

#### 6. What happens when a NETCONF command is issued?
**Answer:**
It changes all or part of a specified configuration at the managed device.

#### 7. What is a Management Information Base (MIB)?
**Answer:**
MIB is a collection of MIB objects that are used by SNMP to manage network devices, defining parameters and state information that can be monitored or configured.

#### 8. What is the function of a network management agent?
**Answer:**
The network management agent is a software process on a managed device that communicates with the managing server and executes local actions under its command.

#### 9. What is the primary purpose of a MIB (Management Information Base)?
**Answer:**
To gather operational state data and configuration data from managed devices into structured objects for network management protocols like SNMP.

#### 10. What is the purpose of a trap message in SNMP?
**Answer:**
Trap messages are unsolicited notifications sent by an agent to the managing server to inform it of exceptional events or changes in state.

#### 11. What is the purpose of notification messages in NETCONF?
**Answer:**
To send asynchronous event notifications from a managed network device to the managing server or client, alerting systems of configuration or state changes.

#### 12. What is the purpose of the network management protocol (e.g., SNMP)?
**Answer:**
The network management protocol facilitates communication between the managing server and managed devices, allowing the server to query device status, configure parameters, and receive asynchronous event notifications (traps).

#### 13. What is the significance of the message ID in NETCONF RPC messages?
**Answer:**
It is used to match requests with their corresponding responses.

#### 14. What role does the managing server play in a NETCONF session?
**Answer:**
It initiates the connection to the managed device and issues commands.

#### 15. What type of messages does NETCONF use to communicate between the managing server and managed devices?
**Answer:**
XML-encoded remote procedure call (RPC) messages.


### 🔴 Senior Level

#### 1. Describe what YANG is used for in network management.
**Answer:**
YANG is a data modeling language that specifies the structure, syntax, and semantics of network management data used by NETCONF.

#### 2. How does the NETCONF/YANG management framework differ from SNMP?
**Answer:**
NETCONF/YANG offers a comprehensive configuration management approach supporting atomic operations, transactional rollbacks, and data modeling across multiple network devices, whereas SNMP primarily focuses on individual device monitoring and OID-based variable retrieval.

#### 3. How many MIB modules are defined in various IETF RFCs?
**Answer:**
Over 400 MIB modules.

#### 4. In the context of NETCONF, what is the function of the RPC reply message?
**Answer:**
It provides the result of an RPC request issued by the managing server.

#### 5. What data type is used for the ipSystemStatsInDelivers object?
**Answer:**
Counter32.

#### 6. What does the <get> or retrieve operation do in NETCONF?
**Answer:**
It retrieves all or part of a given configuration and state data from a managed device.

#### 7. What does the <lock> operation do in NETCONF?
**Answer:**
It locks the entire configuration datastore of a managed device to prevent interference during configuration changes.

#### 8. What is NETCONF primarily used for?
**Answer:**
NETCONF (Network Configuration Protocol) is used to retrieve, set, and modify configuration data at managed devices using an XML-based RPC mechanism over SSH.

#### 9. What is one way that YANG is similar to SMI in SNMP?
**Answer:**
Both specify the structure and semantics of management data.

#### 10. What is the role of the managing server in a network management framework?
**Answer:**
The managing server controls the collection, processing, analysis, and dispatching of network management information and commands, initiating actions to configure, monitor, and control managed devices.

#### 11. Why might a managed device send a discontinuity notification in SNMP?
**Answer:**
Discontinuities in a counter can occur during management system re-initialization, counter rollover, or other specified administrative events.


## 📂 Category: Network Management & SNMP (2 cards)

### 🔴 Senior Level

#### 1. What is the ipSystemStatsInDelivers object used for?
**Answer:**
It defines a 32-bit read-only counter tracking the number of IP datagrams successfully delivered to an upper-layer protocol.

#### 2. What is the maximum access level of the ipSystemStatsInDelivers object?
**Answer:**
Read-only.


## 📂 Category: Network Management & Security (2 cards)

### 🟡 Mid Level

#### 1. What are the types of PDUs defined in SNMPv3?
**Answer:**
The seven types of PDUs include GetRequest, GetNextRequest, GetBulkRequest, SetRequest, Response, InformRequest, and SNMPv2-Trap.


### 🔴 Senior Level

#### 1. How does SNMPv3 improve upon its predecessors regarding security?
**Answer:**
SNMPv3 introduces additional security and administrative capabilities, addressing previous vulnerabilities that limited SNMP's use for control operations.


## 📂 Category: Network Mobility (1 cards)

### 🟡 Mid Level

#### 1. What mobility scenario is addressed when a mobile node maintains active IP sessions while changing points of attachment?
**Answer:**
Scenario (c): A mobile node changes its access network (IP address/subnet) dynamically while actively sending and receiving IP datagrams.


## 📂 Category: Network Performance (15 cards)

### 🟢 Junior Level

#### 1. How do you calculate average throughput?
**Answer:**
Average throughput is calculated by dividing the total file size F by the total time T it takes to transfer the file, expressed as F/T.

#### 2. How does a bottleneck link affect network throughput?
**Answer:**
The bottleneck link is the link with the lowest transmission rate along a path, which determines the maximum possible throughput for data transfer.

#### 3. How does multi-hop routing contribute to packet delay in the network?
**Answer:**
Each hop between routers adds nodal delay, which is the sum of processing, queuing, transmission, and propagation delays at each node.

#### 4. How does packet loss change as traffic intensity increases?
**Answer:**
The fraction of lost packets increases as traffic intensity increases.

#### 5. How does the bottleneck link impact the time to transfer a file?
**Answer:**
The file transfer time is approximated by F / min(R_s, R_c), where F is the file size and min(R_s, R_c) is the transmission rate of the bottleneck link (the lowest-capacity link along the end-to-end path).

#### 6. How is throughput affected if the server and client access links have different rates?
**Answer:**
The throughput is limited by the slower of the two rates, either the server's R_s or the client's R_c, whichever is smaller.

#### 7. How is throughput defined in a communication session?
**Answer:**
Throughput is the rate at which the sending process can deliver bits to the receiving process.

#### 8. How is transmission delay calculated?
**Answer:**
Transmission delay is calculated as the packet length (L) divided by the transmission rate of the link (R), i.e., L/R

#### 9. In packet-switched networks, what factors determine queuing delay?
**Answer:**
The amount of traffic at the router and the number of packets ahead in the queue.

#### 10. In store-and-forward transmission, what is the total delay to transmit one packet of length L over a path with two links operating at rate R?
**Answer:**
2L/R seconds, accounting for transmission delay across both sequential links.

#### 11. What is the main difference between transmission delay and propagation delay?
**Answer:**
Transmission delay depends on the packet's length and link transmission rate (L/R), while propagation delay depends on the physical distance between routers and the propagation speed of the medium (d/s).


### 🟡 Mid Level

#### 1. How does queuing delay behave under bursty traffic and differ from other delay types?
**Answer:**
Queuing delay can be significant when packets arrive in bursts, with the nth packet experiencing a delay of (n - 1) * L/R seconds. Unlike processing, transmission, and propagation delays, queuing delay varies dynamically from packet to packet.

#### 2. How does the delay for sending multiple packets in store-and-forward transmission compare to sending a single packet?
**Answer:**
For P packets transmitted over a series of N store-and-forward links, the total end-to-end delay increases linearly with both the number of packets and the number of links.

#### 3. How is traffic intensity (La/R) calculated?
**Answer:**
Traffic intensity is the ratio of the average rate at which bits arrive at the queue (La) to the transmission rate (R).

#### 4. What might be the consequence of a traffic intensity approaching 1 on a link?
**Answer:**
The delay becomes very large and grows without bound, resulting in unacceptable response times.


## 📂 Category: Network Performance & Architecture (4 cards)

### 🟢 Junior Level

#### 1. What is the formula for end-to-end delay for one packet sent over N links each of rate R?
**Answer:**
Delay = N * (L / R), where N is the number of links, L is the packet length in bits, and R is the transmission rate in bits/sec.

#### 2. What is the formula for the time it takes to transmit a packet over a communication link?
**Answer:**
L / R seconds, where L is the number of bits in the packet and R is the transmission rate of the link in bits/sec.


### 🟡 Mid Level

#### 1. What is the formula for calculating total nodal delay?
**Answer:**
dnode = dproc + dqueue + dtrans + dprop, where dproc is processing delay, dqueue is queuing delay, dtrans is transmission delay, and dprop is propagation delay.

#### 2. What is the general formula for end-to-end delay across N-1 routers (N links)?
**Answer:**
dend-end = N * (dproc + dtrans + dprop), assuming uniform link and router characteristics, where dproc is processing delay, dtrans is transmission delay, and dprop is propagation delay.


## 📂 Category: Network Performance & Delays (1 cards)

### 🟢 Junior Level

#### 1. What happens to a packet during transmission delay?
**Answer:**
The packet's bits are pushed onto the link at the rate determined by the transmission speed of the link.


## 📂 Category: Network Performance & Queuing Theory (1 cards)

### 🔴 Senior Level

#### 1. How does queuing delay behave under various traffic intensity conditions (La/R)?
**Answer:**
1. When traffic intensity is close to zero, average queuing delay is close to zero. 2. When packets arrive periodically at a rate of one packet every L/R seconds, there is no queuing delay. 3. As traffic intensity approaches 1, queuing delay increases rapidly. 4. When intensity exceeds 1, the queue grows infinitely and queuing delay approaches infinity.


## 📂 Category: Network Protocols (1 cards)

### 🟢 Junior Level

#### 1. What does IPX stand for, and what is its purpose?
**Answer:**
Internet Protocol Packet eXchange; it is a networking protocol suite from Novell used for routing packets across local and wide area networks (Note: historical context often links it to NetWare environments, distinct from cellular carrier backbones).


## 📂 Category: Network Routing (1 cards)

### 🟡 Mid Level

#### 1. How do modern Internet routing algorithms (RIP, OSPF, BGP) handle network load?
**Answer:**
They are load-insensitive; link costs are statically configured or based on metrics like hop count/policy rather than reflecting current or recent congestion levels.


## 📂 Category: Network Routing Protocols (2 cards)

### 🟡 Mid Level

#### 1. How often does OSPF send periodic link-state updates, even if no changes have occurred?
**Answer:**
At least once every 30 minutes.


### 🔴 Senior Level

#### 1. If two or more routes remain after applying the BGP elimination rules, how does BGP make the final selection?
**Answer:**
BGP uses router identifiers to make the final selection.


## 📂 Category: Network Security (21 cards)

### 🟢 Junior Level

#### 1. How are firewalls configured to prevent attacks from specific sources?
**Answer:**
By blocking packets based on source and destination IP addresses, transport protocol types, and port numbers using stateless or stateful packet filtering rules.

#### 2. How can distributed denial-of-service (DDoS) attacks increase the impact of DoS attacks?
**Answer:**
DDoS attacks use multiple compromised sources (botnets) to send massive volumes of traffic to a target, making them far harder to filter, trace, and defend against than attacks originating from a single source.

#### 3. How can malware compromise network security?
**Answer:**
Malware can infect devices, allowing attackers to steal information, delete files, or create botnets for further attacks.

#### 4. How can network administrators prevent IP datagram attacks?
**Answer:**
By installing firewalls and intrusion detection systems (IDSs) to monitor and filter malicious packets.

#### 5. How does a bandwidth flooding attack work?
**Answer:**
In a bandwidth flooding attack, an attacker sends an overwhelming amount of packets to a target host, clogging its access link and blocking legitimate traffic.

#### 6. What are the three main categories of DoS attacks?
**Answer:**
Vulnerability attacks, bandwidth flooding, and connection flooding.

#### 7. What does a man-in-the-middle (MitM) attack refer to?
**Answer:**
An attack where an adversary intercepts and potentially alters communication between two trusting parties without their knowledge or consent.

#### 8. What is a botnet?
**Answer:**
A botnet is a network of compromised devices controlled by attackers, often used for tasks like distributing spam or launching denial-of-service attacks.

#### 9. What is a potential security benefit of VLANs in a corporate environment?
**Answer:**
By isolating sensitive departments, VLANs can protect confidential information from unauthorized access by other groups.

#### 10. What is malware and how can it impact systems?
**Answer:**
Malware is malicious software that can infect devices, delete files, steal sensitive information, or enlist devices into botnets for distributed malicious activities such as DDoS attacks.

#### 11. What is the primary method of defense against passive packet sniffing?
**Answer:**
Cryptography and end-to-end encryption (e.g., TLS, IPsec) to render intercepted data unreadable to unauthorized observers.

#### 12. What is the purpose of a firewall in network security?
**Answer:**
To inspect datagrams and packets against security rules and deny suspicious or unauthorized data packets entry into the internal network.


### 🟡 Mid Level

#### 1. Can packet sniffers also be used in wired environments?
**Answer:**
Yes, packet sniffers can capture broadcast packets in wired environments, such as Ethernet LANs, and can be planted on routers to capture all traffic to/from an organization.

#### 2. How can a transport protocol provide security services?
**Answer:**
By encrypting data before transmission and decrypting it upon receipt (e.g., via TLS running on top of TCP), ensuring confidentiality, integrity, and endpoint authentication.

#### 3. How does security function at the network layer?
**Answer:**
By encrypting all datagrams at the source and decrypting them at the destination, providing confidentiality.

#### 4. What characterizes a vulnerability attack?
**Answer:**
A vulnerability attack sends specially crafted payloads or messages to exploit implementation weaknesses in a targeted application or OS, potentially causing crashes or remote execution.

#### 5. What does IP spoofing allow an attacker to do?
**Answer:**
IP spoofing allows an attacker to create and send packets with a false source IP address, potentially masquerading as a trusted user or device.

#### 6. What is a connection flooding attack and a general denial-of-service (DoS) attack?
**Answer:**
A DoS attack renders a network, host, or infrastructure unusable by overwhelming it, preventing legitimate users from accessing services. A connection flooding attack is a specific type of DoS that establishes numerous half-open or fully open TCP connections to a target host, overwhelming it and preventing legitimate connections.

#### 7. What is a packet sniffer?
**Answer:**
A packet sniffer is a passive receiver that captures and records every packet transmitted over a network, which can include sensitive information.

#### 8. What is the importance of mutual authentication in cellular networks?
**Answer:**
It ensures that the network and mobile device verify each other's legitimacy, enhancing security.

#### 9. What role do application-level filters play as network middleboxes?
**Answer:**
They inspect traffic at the application layer to filter out malicious content such as spam, phishing emails, or security threats.


## 📂 Category: Network Security & Monitoring (1 cards)

### 🟡 Mid Level

#### 1. Why are passive packet sniffers difficult to detect?
**Answer:**
Passive packet sniffers do not inject packets into the channel, making their activity less noticeable and harder to identify on the network.


## 📂 Category: Network Security & SDN (1 cards)

### 🟡 Mid Level

#### 1. What is the main purpose of a firewall in the context of OpenFlow?
**Answer:**
To block or filter traffic based on header-field values or to redirect packets for additional processing within Software-Defined Networking (SDN).


## 📂 Category: Network Security & VLANs (1 cards)

### 🟡 Mid Level

#### 1. How do VLANs enhance security, privacy, and traffic isolation in an enterprise network?
**Answer:**
By logically segmenting broadcast domains at layer 2, VLANs ensure that broadcast traffic and unauthorized lateral movement from one group (e.g., guests) do not reach another isolated group (e.g., core systems).


## 📂 Category: Network Services (1 cards)

### 🟡 Mid Level

#### 1. What are examples of performance enhancements provided by network middleboxes?
**Answer:**
Content caching, TLS termination, payload compression, deep packet inspection (DPI), and load balancing of service requests.


## 📂 Category: Network Services & IP (1 cards)

### 🟢 Junior Level

#### 1. What is included in a DHCP ACK message sent by the server?
**Answer:**
The DHCP ACK confirms the requested IP address lease and delivers additional network configuration parameters to the client.


## 📂 Category: Network Services & Protocols (1 cards)

### 🟢 Junior Level

#### 1. Why is DHCP referred to as a plug-and-play or zero-configuration protocol?
**Answer:**
It allows devices to connect to a network and obtain configuration automatically without manual setup.


## 📂 Category: Network Standards (1 cards)

### 🟢 Junior Level

#### 1. What are RFCs?
**Answer:**
Requests for Comments; technical and detailed documents defining Internet protocols and standards published by the IETF.


## 📂 Category: Network Switching (2 cards)

### 🟡 Mid Level

#### 1. What is the benefit of VLANs for managing users who move between groups?
**Answer:**
VLANs allow for easy reconfiguration of the switch without changing physical cabling.

#### 2. What is the broadcast domain for a port in a VLAN?
**Answer:**
A broadcast domain is a set of ports in a VLAN where broadcast traffic is confined.


## 📂 Category: Networking Fundamentals (2 cards)

### 🟢 Junior Level

#### 1. What is the Internet primarily used for?
**Answer:**
The Internet interconnects billions of computing devices worldwide, allowing communication and data exchange.

#### 2. What term is used in Internet jargon to refer to all connected devices?
**Answer:**
Hosts or end systems.


## 📂 Category: Performance & Traffic Engineering (1 cards)

### 🟡 Mid Level

#### 1. What is the relationship between queuing delay and traffic intensity?
**Answer:**
As traffic intensity increases, more packets arrive, leading to longer queuing delays.


## 📂 Category: Performance Metrics (2 cards)

### 🟢 Junior Level

#### 1. What is instantaneous throughput?
**Answer:**
The rate (measured in bits/sec) at which a host is receiving data at any given precise moment during a file transfer or data stream.

#### 2. What is the difference between instantaneous throughput and average throughput?
**Answer:**
Instantaneous throughput is the rate at any specific moment, while average throughput is the total file size divided by the total transfer time.


## 📂 Category: Physical & Wireless Networks (3 cards)

### 🟢 Junior Level

#### 1. How are hosts associated with a base station?
**Answer:**
A host is associated with a base station if it is within communication range and uses that base station to relay data to the larger cellular or Wi-Fi network.


### 🔴 Senior Level

#### 1. How are data bits processed in CDMA?
**Answer:**
Each data bit is divided into mini-slots, with the output of the CDMA encoder calculated as the data bit multiplied by the corresponding CDMA code value for each mini-slot.

#### 2. How are data paths set up from mobile devices to the carrier's gateway router?
**Answer:**
Through wireless first hops between the mobile device and base station, and concatenated IP tunnels managed by the MME (Mobility Management Entity).


## 📂 Category: Physical / Data Link Layer (1 cards)

### 🔴 Senior Level

#### 1. How does a receiver extract data from a specific sender in Code Division Multiple Access (CDMA)?
**Answer:**
The receiver multiplies the combined received signal by the specific sender's unique orthogonal spreading code and integrates/computes the inner product over the chip period, effectively filtering out signals from other senders as noise and recovering the target data.


## 📂 Category: Physical Layer (26 cards)

### 🟢 Junior Level

#### 1. Describe Frequency-Division Multiplexing (FDM).
**Answer:**
FDM divides the channel's bandwidth into different frequencies, assigning each frequency to a node.

#### 2. How do guided media differ from unguided media in network transmissions?
**Answer:**
Guided media use a solid medium (like copper wire or fiber-optic cable), while unguided media propagate in the atmosphere or space (like radio waves).

#### 3. How does Frequency-Division Multiplexing (FDM) work in circuit-switched networks?
**Answer:**
The frequency spectrum is divided into different frequency bands, with each band dedicated to a connection for the duration of the session.

#### 4. How does Time-Division Multiplexing (TDM) ensure dedicated bandwidth for each connection?
**Answer:**
By allocating the same time slot in every frame for each connection.

#### 5. How does signal strength change in wireless links compared to wired links?
**Answer:**
Wireless links experience decreasing signal strength due to attenuation as electromagnetic radiation passes through matter and disperses in free space.

#### 6. How does the 10BASE-T standard differ from the 100BASE-T standard?
**Answer:**
10BASE-T operates at a transmission speed of 10 Mbps over twisted-pair cabling, while 100BASE-T operates at 100 Mbps (Fast Ethernet).

#### 7. What are digital subscriber line (DSL) modems used for?
**Answer:**
DSL modems are used to transmit digital data over existing telephone lines, allowing for both Internet access and phone service.

#### 8. What are some examples of physical media used in the Internet?
**Answer:**
Twisted-pair copper wire, coaxial cable, multimode fiber-optic cable, terrestrial radio spectrum, and satellite radio spectrum.

#### 9. What are some types of physical media used in communication links?
**Answer:**
Coaxial cable, copper wire, optical fiber, and radio spectrum.

#### 10. What are the two categories of physical media?
**Answer:**
Guided media (e.g., fiber, twisted-pair copper) and unguided media (e.g., wireless radio frequencies).

#### 11. What does signal-to-noise ratio (SNR) measure in communications?
**Answer:**
SNR measures the relative strength of a received signal compared to background noise power, typically expressed in decibels (dB), directly impacting channel capacity and data transmission clarity/error rates.

#### 12. What does the "BASE" acronym signify in Ethernet standards (e.g., 1000BASE-T)?
**Answer:**
It signifies baseband Ethernet, meaning the physical media carries only digital Ethernet traffic (rather than broadband multiplexed signals).

#### 13. What does the 'T' and specific prefixes refer to in Ethernet standards like 10BASE-T and 100BASE-FX?
**Answer:**
'T' refers to twisted-pair copper wires. 'FX' refers to Fast Ethernet over fiber optic cables (100 Mbps).

#### 14. What is Time-Division Multiplexing (TDM)?
**Answer:**
A physical or link layer multiplexing technique that divides transmission time into periodic frames and assigns dedicated time slots to each node for communication.

#### 15. What is frequency-division multiplexing in DSL?
**Answer:**
Frequency-division multiplexing allows data and telephone signals to share the same physical line by utilizing different frequency bands for transmission.

#### 16. What is the difference between downstream and upstream transmission rates in DSL?
**Answer:**
Downstream transmission rates are typically higher than upstream rates, making DSL access asymmetric.

#### 17. What is the function of a repeater in early Ethernet standards?
**Answer:**
It receives a signal on one side and regenerates it on the output side to extend the length of the cable.

#### 18. What is the maximum distance limit for 100BASE-T over twisted pair cabling?
**Answer:**
100 meters.

#### 19. What technology allows Gigabit Ethernet to run over category 5 UTP cabling?
**Answer:**
1000BASE-T.


### 🟡 Mid Level

#### 1. How does a higher SNR affect the bit error rate (BER)?
**Answer:**
A higher Signal-to-Noise Ratio (SNR) typically results in a lower Bit Error Rate (BER), making it easier to correctly extract the transmitted signal from background noise.

#### 2. How is SNR typically expressed?
**Answer:**
SNR is usually expressed in decibels (dB), calculated as 20 times the base-10 logarithm of the ratio of the signal amplitude to the noise amplitude.

#### 3. What is the maximum length for the coaxial cables used in 10BASE-2 and 10BASE-5 Ethernet standards?
**Answer:**
Each segment is limited to 500 meters (specifically, 10BASE-5 max segment length is 500m, while 10BASE-2 is 185m, traditionally referenced around these physical limits).

#### 4. What is the relationship between transmission power and BER?
**Answer:**
Increasing transmission power can enhance SNR and decrease BER, but excessive power can lead to unnecessary energy expenditure and interference with other transmissions.


### 🔴 Senior Level

#### 1. How does modulation technique affect BER?
**Answer:**
For a given SNR, a modulation technique with a higher bit transmission rate generally has a higher BER, impacting reliability.

#### 2. What does the value of -1 represent in CDMA encoding?
**Answer:**
In Code Division Multiple Access (CDMA) encoding, a logical data bit of 0 is represented by -1 for mathematical orthogonality and signal processing convenience.

#### 3. What happens if the transmission delay is greater than the propagation delay?
**Answer:**
The first bits of a packet may arrive at the next router while other bits are still being transmitted by the previous router.


## 📂 Category: Physical Layer & History (1 cards)

### 🔴 Senior Level

#### 1. What is the maximum speed of the original Ethernet invented by Metcalfe and Boggs?
**Answer:**
2.94 Mbps.


## 📂 Category: Physical Layer & Wireless (1 cards)

### 🟢 Junior Level

#### 1. Why are bit errors more common in wireless links compared to wired links?
**Answer:**
Due to the effects of signal degradation, interference, and multipath propagation, wireless links are more susceptible to bit errors.


## 📂 Category: Physical Layer / Multiplexing (1 cards)

### 🟢 Junior Level

#### 1. What is the main characteristic of Time-Division Multiplexing (TDM)?
**Answer:**
Time is divided into frames, and each connection is allocated a specific, dedicated time slot within each frame.


## 📂 Category: Physical Layer / Wireless (1 cards)

### 🔴 Senior Level

#### 1. What is the role of the chipping rate in CDMA?
**Answer:**
The chipping rate determines how fast the CDMA code changes, which is essential for encoding and decoding the data bits accurately.


## 📂 Category: Physical/Data Link Layer (1 cards)

### 🟡 Mid Level

#### 1. What does DOCSIS stand for?
**Answer:**
Data-Over-Cable Service Interface Specification.


## 📂 Category: Quality of Service (5 cards)

### 🟡 Mid Level

#### 1. How are packets chosen from the same priority class versus different priority classes in priority queuing?
**Answer:**
Packets from different priority classes are served based on priority (higher priority first). Packets within the same priority class are chosen using the FIFO discipline in order of arrival.

#### 2. What is a round-robin queuing discipline?
**Answer:**
Round-robin scheduling alternates service among different classes of packets, ensuring that each class is served in a circular order without strict priority.

#### 3. What is the function of guaranteed minimal bandwidth in network services?
**Answer:**
It ensures that a specified bit rate (e.g., 1 Mbps) is maintained for the delivery of packets.


### 🔴 Senior Level

#### 1. What is Weighted Fair Queuing (WFQ)?
**Answer:**
WFQ is a generalized packet scheduling algorithm that assigns distinct weights to different traffic classes, ensuring each queue receives a proportionate share of output link bandwidth.

#### 2. What is the purpose of guaranteed minimal bandwidth in a network layer?
**Answer:**
It emulates the behavior of a dedicated transmission link of a specified bit rate, ensuring packets are delivered reliably as long as the transmission rate stays below the specified bandwidth threshold.


## 📂 Category: Quality of Service & Traffic Management (1 cards)

### 🟢 Junior Level

#### 1. What is the first-come-first-served (FCFS) queuing discipline in packet scheduling?
**Answer:**
FCFS, also known as FIFO, processes packets in the order they arrive at the output link queue, serving them sequentially without prioritizing any packet.


## 📂 Category: Quality of Service (QoS) (6 cards)

### 🟡 Mid Level

#### 1. How does priority queuing differ from FCFS?
**Answer:**
Priority queuing classifies packets into different priority classes and always transmits packets from the highest priority class that has packets waiting, typically following FIFO within each class.

#### 2. How does the round robin discipline handle idle links?
**Answer:**
In a round robin discipline, if a scheduled class has no packets to transmit, the scheduler immediately checks the next class to ensure the link remains active.

#### 3. What does guaranteed delivery with bounded delay ensure?
**Answer:**
It guarantees that a packet will be delivered within a specified time frame.

#### 4. What is the main challenge associated with FCFS queuing?
**Answer:**
It can lead to longer wait times and head-of-line blocking for packets in lower-priority classes if high-priority packets keep arriving.

#### 5. Why is it important to consider both throughput and delay in packet scheduling?
**Answer:**
Achieving high throughput without managing delay can lead to issues like bufferbloat, where excessive queuing causes unacceptable latency in packet transmission.


### 🔴 Senior Level

#### 1. What is the Intserv architecture?
**Answer:**
A proposed service model for the Internet aiming to provide end-to-end delay guarantees and congestion-free communication.


## 📂 Category: Quality of Service (QoS) / Queuing (1 cards)

### 🟡 Mid Level

#### 1. What is a work-conserving queuing discipline in network routers?
**Answer:**
A work-conserving queuing discipline guarantees that the output link is never left idle (zero utilization) as long as there is at least one packet queued in the router's buffers waiting for transmission.


## 📂 Category: Queue Management & Congestion (1 cards)

### 🟢 Junior Level

#### 1. What typically happens to a packet when it arrives at a full router queue?
**Answer:**
The packet is dropped, resulting in packet loss.


## 📂 Category: Reliable Data Transfer (6 cards)

### 🟢 Junior Level

#### 1. What feedback mechanism does rdt2.0 use to inform the sender of the reception status of packets?
**Answer:**
ACK and NAK packets.

#### 2. What is the main limitation of the rdt1.0 protocol?
**Answer:**
It assumes a perfectly reliable channel and does not handle any bit errors or packet loss.


### 🟡 Mid Level

#### 1. What happens if a packet experiences a large delay in rdt3.0?
**Answer:**
The sender may prematurely retransmit the packet, even if the original packet or its ACK has not been lost, leading to duplicate packets.

#### 2. What is the main limitation of the rdt3.0 protocol?
**Answer:**
It operates as a stop-and-wait protocol, where the sender must wait for an acknowledgment before sending the next packet, significantly reducing link utilization and performance.

#### 3. What should the sender do if it receives a corrupted ACK in rdt3.0?
**Answer:**
The sender will retransmit the last packet since it cannot be sure of the acknowledgment's validity.

#### 4. What technique from rdt2.2 is used in rdt3.0 to handle retransmissions?
**Answer:**
The use of checksumming, sequence numbers, ACK packets, and retransmissions.


## 📂 Category: Reliable Data Transport (2 cards)

### 🟢 Junior Level

#### 1. What concept does the term "stop-and-wait" refer to in rdt protocols?
**Answer:**
The sender must wait for an acknowledgment before sending the next packet.


### 🟡 Mid Level

#### 1. What determines whether the sender will retransmit a packet in rdt3.0?
**Answer:**
The expiration of the countdown timer.


## 📂 Category: Router Architecture (8 cards)

### 🟢 Junior Level

#### 1. What happens during the lookup process in an input port?
**Answer:**
The router uses the forwarding table to determine the output port for an incoming packet based on its destination address.

#### 2. What type of packets do routers with bus switching typically handle?
**Answer:**
Bus switching is often sufficient for routers operating in small local area and enterprise networks.


### 🟡 Mid Level

#### 1. What are the responsibilities of the routing processor in a router?
**Answer:**
Executing routing protocols, maintaining routing tables, computing forwarding tables, and performing network management functions.

#### 2. What happens if a packet cannot enter the switching fabric immediately?
**Answer:**
The packet may be temporarily blocked and queued at the input port until it can cross the fabric.

#### 3. What is the primary function of the switching fabric in a router?
**Answer:**
The switching fabric is the internal core responsible for transferring packets from an input port memory/interface to the correct output port.

#### 4. What type of queuing occurs at the output port when multiple packets arrive?
**Answer:**
Output queuing occurs, requiring a packet scheduler to select which packet to transmit from the queue.


### 🔴 Senior Level

#### 1. What is the main drawback of switching via a bus in routers?
**Answer:**
The switching speed is limited by the bandwidth of the shared bus, and only one packet can cross the bus at any given time.

#### 2. What technique is used to scale a router’s switching capacity?
**Answer:**
Multiple switching fabrics can be run in parallel, allowing packets to be divided and sent through different paths to the output port.


## 📂 Category: Router Architecture & Congestion Control (1 cards)

### 🔴 Senior Level

#### 1. Why is determining the right amount of buffering in routers complex?
**Answer:**
The interaction between congestion-aware senders and the network core creates a complex relationship that affects optimal buffer size.


## 📂 Category: Router Architecture & Performance (1 cards)

### 🟡 Mid Level

#### 1. How does processing delay affect a router's performance?
**Answer:**
Although processing delay is often negligible, it strongly influences the maximum throughput of a router, or the maximum rate at which it can forward packets.


## 📂 Category: Router Architecture & Switching (1 cards)

### 🟡 Mid Level

#### 1. What can happen to packets during periods of network congestion or when the switching fabric is too slow?
**Answer:**
Packets experience queuing delays or can be dropped due to limited buffer space at input/output ports.


## 📂 Category: Routing & Addressing (2 cards)

### 🟡 Mid Level

#### 1. What are the two main goals of IP-Anycast?
**Answer:**
(1) Replicating content on multiple geographically distributed servers, and (2) routing users to the nearest server.

#### 2. What are the two main reasons for organizing routers into autonomous systems (ASs) in large networks like the Internet?
**Answer:**
To reduce the complexity of route computation and allow administrative autonomy for ISPs.


## 📂 Category: Routing & CDN (1 cards)

### 🔴 Senior Level

#### 1. Why is IP-Anycast well-suited for DNS but less common for CDNs?
**Answer:**
DNS queries are stateless, so routing changes don’t disrupt ongoing connections like they would in stateful, TCP-based applications such as CDNs.


## 📂 Category: Routing & DNS (1 cards)

### 🟡 Mid Level

#### 1. Why is IP-Anycast commonly used in DNS systems and root servers?
**Answer:**
It provides a scalable, efficient method to route queries to the nearest root DNS server using the same IP address, improving global distribution.


## 📂 Category: Routing & Forwarding (4 cards)

### 🟢 Junior Level

#### 1. What is the difference between routing and forwarding in a router?
**Answer:**
Forwarding is the data-plane process of moving a packet from an input link to the appropriate output link at a router. Output port processing specifically includes selecting and de-queuing packets for transmission and performing link-layer and physical-layer transmission functions.

#### 2. Why do network routers not examine transport-layer segments?
**Answer:**
Routers operate strictly up to Layer 3 (Network Layer) to process datagram headers efficiently, ignoring higher-layer payload details.


### 🟡 Mid Level

#### 1. What does a router do once it determines the correct output interface for a datagram?
**Answer:**
It passes the datagram to the adapter of the identified interface, which then encapsulates it in a new frame for the next subnet.

#### 2. What is Equal Cost Multi Path (ECMP) routing?
**Answer:**
A simple multipath routing scheme that performs randomized next-hop selection among equal-cost paths between source and destination to distribute traffic efficiently.


## 📂 Category: Routing & IP (1 cards)

### 🔴 Senior Level

#### 1. What is IP-Anycast?
**Answer:**
A network addressing and routing methodology where the exact same IP address is assigned to multiple servers in different geographic locations, routing clients to the topologically closest instance.


## 📂 Category: Routing & Switching (11 cards)

### 🟢 Junior Level

#### 1. What is a significant drawback of switches compared to routers?
**Answer:**
Layer 2 switches forward traffic based on MAC addresses and can be susceptible to broadcast storms (loops), whereas Layer 3 routers segment broadcast domains and mitigate this risk.

#### 2. What role do output buffers play in packet switches?
**Answer:**
They store packets that are waiting to be transmitted onto a link, particularly when the link is busy.


### 🟡 Mid Level

#### 1. How does MPLS enhance packet forwarding speed and handle network failures?
**Answer:**
MPLS uses fixed-length labels for forwarding packets instead of relying solely on destination IP addresses. Additionally, it handles network failures by rerouting traffic over precomputed failover paths in response to link failures.

#### 2. What is a Virtual Local Area Network (VLAN) and how does a trunk port facilitate it?
**Answer:**
A VLAN allows multiple virtual local area networks to be logically defined over a single physical local area network infrastructure. A VLAN trunk port is a specialized switch port configured to carry traffic for multiple VLANs using encapsulation (e.g., IEEE 802.1Q) between switches.

#### 3. What is a significant distinction between MPLS and traditional link-layer technologies?
**Answer:**
MPLS operates at a higher level (often described as layer 2.5), enabling traffic engineering and management capabilities beyond simple data forwarding.

#### 4. What is queuing delay, and what factors and conditions determine its value?
**Answer:**
Queuing delay is the time a packet spends waiting in a router’s output buffer before transmission. It depends heavily on network congestion levels and arrival rates. It can be zero if the output queue is completely empty and no other packets are currently being transmitted.

#### 5. What protocol is used to route packets across multiple Autonomous Systems?
**Answer:**
Border Gateway Protocol (BGP), the standard exterior gateway protocol of the Internet.

#### 6. What role do input ports play in a router?
**Answer:**
They terminate incoming physical links, perform link-layer functions, and consult the forwarding table for packet forwarding.


### 🔴 Senior Level

#### 1. What is the function of input ports and the switching fabric in a router?
**Answer:**
Input ports perform line termination, link-layer processing, and lookup to determine the appropriate output port. The switching fabric then physically connects the router's input ports to its output ports.

#### 2. What is the function of sophisticated interconnection networks in routers?
**Answer:**
They allow multiple packets from different input ports to be processed simultaneously towards the same output port.

#### 3. What purpose does the NEXT-HOP attribute serve in BGP regarding intra-AS routing?
**Answer:**
It provides the IP address of the router interface that is the next hop to reach a specific destination, linking inter-AS BGP routing with the intra-AS routing protocol to find the least-cost path within the Autonomous System.


## 📂 Category: Routing Algorithms (5 cards)

### 🟢 Junior Level

#### 1. What happens if all edges in a network graph have the same cost?
**Answer:**
The least-cost path is also the shortest path in terms of the number of links between the source and destination.


### 🟡 Mid Level

#### 1. Can routing algorithms work with both undirected and directed graphs?
**Answer:**
Yes, although the discussion focuses on undirected graphs, the algorithms can be extended to work with directed graphs as well.

#### 2. Why might a routing algorithm choose a path that is not the shortest in terms of hops?
**Answer:**
If the shortest path has higher costs (such as bandwidth constraints or congestion), the algorithm may choose a longer path that has a lower overall cost.


### 🔴 Senior Level

#### 1. What happens in the DV algorithm when no more update messages are sent?
**Answer:**
The algorithm enters a quiescent state where no further routing table changes occur unless a link cost changes.

#### 2. Why were early ARPAnet routing algorithms load-sensitive, and what challenges did they face?
**Answer:**
They were designed to dynamically reflect link congestion, but they encountered severe problems such as routing oscillation, instability, and difficulties in accurately representing dynamic link costs.


## 📂 Category: Routing Architecture (1 cards)

### 🔴 Senior Level

#### 1. Why must IP address lookup in high-speed routers be performed using specialized hardware and algorithms?
**Answer:**
Lookups must occur in nanoseconds to keep up with high-speed transmission rates, necessitating specialized hardware like TCAMs and efficient lookup algorithms.


## 📂 Category: Routing Protocols (71 cards)

### 🟢 Junior Level

#### 1. How can routing algorithms be classified based on how they handle changes?
**Answer:**
Routing algorithms can be static or dynamic. Static algorithms rarely change, while dynamic algorithms update routes in response to traffic or topology changes.

#### 2. In network-layer routing, what do the nodes and edges of a graph represent?
**Answer:**
Nodes represent routers, and edges represent the physical links between routers.

#### 3. What is a 'least-cost path' in a network graph?
**Answer:**
It is the path between two nodes that has the lowest sum of edge costs compared to all other possible paths.

#### 4. What is a routing algorithm?
**Answer:**
An algorithm that calculates the paths packets will take through the network.

#### 5. What is meant by the term 'neighbor' in the context of network graphs?
**Answer:**
A node y is a neighbor of node x if there is an edge between them in the graph.

#### 6. What is the cost notation for an edge that does not exist between two nodes in a graph?
**Answer:**
If no edge exists between two nodes, the cost is denoted as infinity (∞).

#### 7. What is the purpose of routing protocols in the Internet?
**Answer:**
To automatically discover network topologies and configure forwarding tables in routers, dynamically determining optimal paths to destination networks.

#### 8. What is the role of human intervention in static routing algorithms?
**Answer:**
Human intervention is often required to manually update or edit link costs and routing paths in static routing algorithms.


### 🟡 Mid Level

#### 1. How do nodes share routing information using the Distance Vector (DV) algorithm, and in which protocols is it used?
**Answer:**
Each node sends a copy of its distance vector directly to its attached neighbors. The DV algorithm is used in routing protocols like RIP, BGP, ISO IDRP, and Novell IPX.

#### 2. How does BGP use the AS-PATH attribute to prevent routing loops?
**Answer:**
If a router detects its own AS in the AS-PATH, it rejects the advertisement to avoid loops.

#### 3. How does OSPF determine the shortest path within an autonomous system?
**Answer:**
Each router constructs a complete topological map of the network and uses Dijkstra’s shortest-path algorithm to calculate routes.

#### 4. How does the Distance Vector (DV) routing algorithm achieve convergence?
**Answer:**
By iteratively exchanging distance vector tables with immediate neighbors and updating local cost estimates using the Bellman-Ford equation, allowing nodes to eventually compute stable, least-cost paths to all destinations.

#### 5. How does the Distance Vector (DV) routing algorithm differ structurally from Link-State (LS)?
**Answer:**
DV is fully decentralized and asynchronous, with nodes only communicating with their immediate neighbors, whereas LS is centralized or distributed globally, requiring complete network topology visibility.

#### 6. How does the Distance-Vector (DV) routing algorithm handle link-cost changes and resolve routing loops?
**Answer:**
A node updates its distance vector and informs its neighbors when it detects a link-cost change. To resolve routing loops caused by increased link costs, the algorithm relies on iterative convergence over several steps until nodes correctly update their routing tables.

#### 7. How does the Link-State (LS) algorithm ensure all nodes share an identical network view?
**Answer:**
Every node floods its local link-state information to all other nodes across the network, guaranteeing a synchronized and consistent view of the global topology.

#### 8. How does the Link-State (LS) routing algorithm differ from Distance-Vector (DV) in information exchange?
**Answer:**
LS requires global topology knowledge and broadcasts link costs to all nodes in the network. In contrast, DV relies solely on localized information exchange exclusively with directly connected neighbors.

#### 9. How is network topology information distributed in a Link-State routing algorithm?
**Answer:**
Each node broadcasts link-state packets containing the identities and costs of its attached links to all other nodes in the network.

#### 10. What are the characteristics of the Distance-Vector (DV) algorithm?
**Answer:**
The DV algorithm is iterative, asynchronous, and distributed.

#### 11. What are the primary inputs for centralized routing algorithms like Link-State (LS)?
**Answer:**
The complete network topology (node connectivity) and the weights/costs of all links across the entire network.

#### 12. What does 'global knowledge' mean in the context of centralized routing algorithms?
**Answer:**
It refers to having complete, centralized information regarding the physical topology, connectivity, and link costs of all nodes and links across the entire network.

#### 13. What does the LS algorithm compute when it finishes running?
**Answer:**
It computes the least-cost path from the source to all other nodes in the network.

#### 14. What does the term "prefix" refer to in the context of BGP?
**Answer:**
A prefix represents a range of IP addresses, typically denoted using CIDR (Classless Inter-Domain Routing) notation, to which BGP routes packets across autonomous systems.

#### 15. What feature does OSPF provide through multiple same-cost paths?
**Answer:**
Equal-Cost Multi-Path (ECMP) routing allows OSPF to install multiple active paths to a single destination if their calculated path costs are identical, enabling effective traffic load balancing across links.

#### 16. What happens during each iteration of Dijkstra’s algorithm?
**Answer:**
The node not in N' with the minimum cost D(v) is added to N', and the costs to its neighboring nodes are updated.

#### 17. What is a 'link-state' algorithm in routing?
**Answer:**
It is a routing algorithm where each node is aware of the costs of all links in the network, using global state information.

#### 18. What is a key difference between OSPF and distance-vector protocols like RIP?
**Answer:**
OSPF uses global link-state information and calculates routes based on the entire network topology, while distance-vector protocols rely on local information from neighbors.

#### 19. What is an eBGP (External BGP) connection?
**Answer:**
An eBGP connection is a Border Gateway Protocol session established between two BGP routers located in different Autonomous Systems (AS).

#### 20. What is stored in a node's distance vector in the Distance Vector (DV) routing algorithm?
**Answer:**
A node's distance vector contains its current estimated least-cost paths from itself to all known destination nodes in the network, updated dynamically based on neighbor advertisements.

#### 21. What is the computational complexity of Dijkstra's algorithm in its basic form?
**Answer:**
The worst-case computational complexity of Dijkstra's algorithm is O(n²), where n is the number of nodes.

#### 22. What is the difference between eBGP and iBGP connections?
**Answer:**
eBGP connects routers between different ASs, while iBGP connects routers within the same AS.

#### 23. What is the key idea behind poisoned reverse in distance-vector algorithms?
**Answer:**
The key idea is that if a router routes through a neighbor to reach a destination, it advertises an infinite distance to that destination back to the neighbor to prevent routing loops.

#### 24. What is the key property of Dijkstra’s algorithm after the kth iteration?
**Answer:**
The least-cost paths are known to k destination nodes, and these k paths have the k smallest costs among all destination nodes.

#### 25. What is the main function of OSPF in the context of intra-AS routing?
**Answer:**
OSPF is a link-state protocol that calculates the shortest paths within an autonomous system by flooding link-state advertisements (Dijkstra's algorithm) to all routers.

#### 26. What is the purpose of hierarchy in OSPF?
**Answer:**
OSPF utilizes areas within an autonomous system to reduce routing table size and control traffic complexity by containing link-state updates within local areas and relying on area border routers (ABRs) for inter-area traffic.

#### 27. What is the role of link weights in OSPF?
**Answer:**
Link weights are set by administrators and influence the routing paths chosen by OSPF, typically based on criteria like link capacity or cost.

#### 28. What is the role of the backbone area (Area 0) in OSPF routing?
**Answer:**
The backbone area is responsible for distributing routing information and forwarding traffic between different non-backbone OSPF areas within an Autonomous System (AS).

#### 29. What triggers a node to send an updated distance vector to its neighbors?
**Answer:**
A node sends its updated distance vector if it detects a change in its distance vector after recalculating it.

#### 30. What type of algorithm is Dijkstra's algorithm and where is it applied in Internet routing?
**Answer:**
Dijkstra's algorithm is a Link-State (LS) routing algorithm that computes the least-cost path from a source node to all other nodes. It is used in the Internet's OSPF (Open Shortest Path First) routing protocol.

#### 31. What types of networks can MPLS interconnect?
**Answer:**
MPLS can interconnect IP devices using its own packet formats and forwarding behaviors.


### 🔴 Senior Level

#### 1. After selecting routes based on local preference, what does BGP consider next?
**Answer:**
It selects the route with the shortest AS-PATH.

#### 2. Can poisoned reverse solve the general count-to-infinity problem?
**Answer:**
No, poisoned reverse can prevent loops involving two nodes, but it cannot detect or prevent loops involving three or more nodes.

#### 3. How can the efficiency of Dijkstra's algorithm be improved in link-state routing?
**Answer:**
By using a heap data structure, the efficiency of finding the minimum distance node can be reduced to logarithmic time, improving overall computational complexity.

#### 4. How can the problem of oscillations in Link-State routing be mitigated?
**Answer:**
One solution is to randomize the time each router sends out link advertisements to avoid synchronization and routing loops.

#### 5. How does BGP advertise the same IP address from multiple servers in an IP-Anycast setup?
**Answer:**
Each server advertises the same IP address from different locations, and routers choose the best path based on the routing algorithm.

#### 6. How does BGP route packets differently compared to intra-AS routing?
**Answer:**
BGP routes packets to CIDRized prefixes, representing a range of IP addresses, rather than specific destination IP addresses.

#### 7. How does IP-Anycast determine the closest server and enhance DNS resilience?
**Answer:**
IP-Anycast uses BGP's route-selection algorithm to select the path with the fewest AS hops, determining the closest server. By distributing DNS root servers globally using this mechanism, it ensures redundancy and reduces query latency.

#### 8. How does a routing loop occur in the Distance Vector (DV) routing algorithm?
**Answer:**
A routing loop occurs when adjacent nodes form circular forwarding dependencies based on outdated distance metrics—for example, if node Y routes through node Z to reach destination X, while node Z simultaneously routes through node Y to reach X.

#### 9. How does poisoned reverse help prevent loops in routing?
**Answer:**
By advertising an infinite distance to a destination to the neighboring router it routes through, the neighbor will not route back through it, preventing two-node loops.

#### 10. How does the Distance Vector (DV) algorithm differ fundamentally from Dijkstra's link-state algorithm?
**Answer:**
The DV algorithm is decentralized and asynchronous, relying entirely on periodic local neighbor exchanges, whereas Dijkstra's algorithm requires a complete map of the network topology globally flooded to all routers.

#### 11. In the context of BGP, what does hot potato routing prioritize?
**Answer:**
It prioritizes reducing the cost of delivering the packet within the local AS, regardless of the cost beyond the AS.

#### 12. What happens during a link-cost increase in the Distance Vector (DV) algorithm?
**Answer:**
The algorithm may temporarily form routing loops, where packets bounce between nodes, leading to the count-to-infinity problem.

#### 13. What happens if a router in BGP receives multiple paths to the same prefix?
**Answer:**
BGP uses a route-selection algorithm to choose the best path based on attributes like local preference, AS-PATH length, and NEXT-HOP.

#### 14. What happens if multiple BGP routes have the same AS-PATH length?
**Answer:**
Hot potato routing is applied, selecting the route with the closest NEXT-HOP.

#### 15. What is a major robustness vulnerability of the Distance Vector (DV) routing algorithm compared to Link State (LS)?
**Answer:**
A faulty or compromised node in the DV algorithm can propagate incorrect routing information and path costs to its neighbors, potentially causing count-to-infinity loops or affecting the entire network.

#### 16. What is a potential issue with using BGP to select routes in an IP-Anycast environment?
**Answer:**
BGP routing is dynamic, so paths may change during a session, leading to inconsistent server selection.

#### 17. What is an iBGP connection?
**Answer:**
It is a BGP connection between routers within the same Autonomous System.

#### 18. What is one unrealistic solution to prevent oscillations in Link-State (LS) algorithms based on traffic load?
**Answer:**
Mandating that link costs do not depend on the amount of traffic carried, which defeats the purpose of routing around congested links.

#### 19. What is self-synchronization in the context of routers running the Link State (LS) routing algorithm?
**Answer:**
Self-synchronization occurs when routers that initially execute the LS algorithm at offset or uncoordinated times naturally begin to run it simultaneously and in phase over time due to network dynamics.

#### 20. What is the AS-PATH attribute in BGP?
**Answer:**
It contains the list of Autonomous Systems through which the BGP advertisement has passed.

#### 21. What is the Bellman-Ford equation used for in the Distance Vector (DV) algorithm?
**Answer:**
It computes the least-cost path by considering the cost to a neighbor and the neighbor's distance to the destination.

#### 22. What is the function of the NEXT-HOP attribute in BGP?
**Answer:**
It identifies the IP address of the router that begins the AS-PATH to a given destination.

#### 23. What is the main drawback of hot potato routing?
**Answer:**
It ignores the costs of the remaining path outside the local AS, potentially increasing overall end-to-end delay and sub-optimal routing efficiency.

#### 24. What is the primary responsibility of BGP (Border Gateway Protocol)?
**Answer:**
To obtain prefix reachability information from neighboring Autonomous Systems (ASs) and determine the best routes based on administrative policies and reachability.

#### 25. What is the role of iBGP in propagating reachability information within an AS?
**Answer:**
iBGP distributes the reachability information learned via eBGP to all internal routers in the AS.

#### 26. What is the significance of BGP advertising both the prefix and its path?
**Answer:**
It allows routers to learn the network structure and determine the most efficient route to the destination.

#### 27. What issue arises from the count-to-infinity problem in Distance Vector (DV) routing?
**Answer:**
Nodes may exchange erroneous route updates for many iterations before converging, significantly delaying the propagation of 'bad news' regarding increased link costs or failures.

#### 28. What role does BGP play in IP-Anycast?
**Answer:**
BGP is used to advertise the same IP address from multiple servers, allowing routers to pick the best route based on the proximity of servers.

#### 29. When does router y poison its reverse path to x in distance-vector routing?
**Answer:**
Router y poisons the reverse path to x when it updates its distance table with the new least-cost path via z.

#### 30. Why do modern Internet routing algorithms avoid congestion-based link costs?
**Answer:**
Because utilizing dynamic congestion metrics as link costs creates a feedback loop that leads to network instability, route oscillations, and flapping.

#### 31. Why does poisoned reverse fail to completely solve the count-to-infinity problem in routing loops involving three or more nodes?
**Answer:**
Poisoned reverse only resolves routing loops between directly adjacent nodes (hop count of 2); loops involving three or more nodes can still develop complex multi-hop count-to-infinity anomalies.

#### 32. Why is BGP considered crucial for the Internet and IP-Anycast?
**Answer:**
BGP is the exterior gateway protocol that interconnects autonomous systems globally. It naturally selects the shortest AS path, which allows it to route IP-Anycast traffic efficiently to the geographically closest available server.


## 📂 Category: Routing Protocols & Security (1 cards)

### 🟡 Mid Level

#### 1. What security features does OSPF support to ensure trusted communication between routers?
**Answer:**
OSPF supports authentication, including MD5 authentication, to ensure that only trusted routers can participate in the protocol.


## 📂 Category: Routing Protocols (BGP) (1 cards)

### 🟡 Mid Level

#### 1. Why does BGP rely on TCP for its session connections?
**Answer:**
TCP guarantees reliable, ordered, and flow-controlled communication for exchanging critical routing tables and updates between BGP peers.


## 📂 Category: Routing and BGP (2 cards)

### 🔴 Senior Level

#### 1. What is the effect of a BGP route change on an IP-Anycast-based connection?
**Answer:**
It may reroute packets mid-connection to a physically different server instance advertising the same Anycast IP, potentially resetting TCP state and causing connection disruption in stateful applications.

#### 2. What is the first rule BGP follows in its route-selection algorithm?
**Answer:**
BGP first selects routes with the highest local preference values among all candidate routes.


## 📂 Category: Routing and Switching (2 cards)

### 🟢 Junior Level

#### 1. What are the four key components of a generic router architecture?
**Answer:**
Input ports, switching fabric, output ports, and routing processor.


### 🔴 Senior Level

#### 1. What are Ternary Content Addressable Memories (TCAMs) used for in routers?
**Answer:**
TCAMs are used for fast lookup of forwarding table entries, allowing for quick packet forwarding decisions.


## 📂 Category: Software Defined Networking (1 cards)

### 🔴 Senior Level

#### 1. What is the role of Software Defined Networking (SDN) in the context of 5G mobility management?
**Answer:**
SDN aims to enable a higher-capacity, lower-latency control plane for 5G cellular networks.


## 📂 Category: Software-Defined Networking (39 cards)

### 🟢 Junior Level

#### 1. How is the data plane in SDN different from the control plane?
**Answer:**
The data plane consists of the switches that execute forwarding rules, while the control plane consists of software and servers that determine and manage those rules.

#### 2. What does SDN stand for, and what is its core architectural principle?
**Answer:**
Software-Defined Networking. Its core principle is decoupling the control plane (deciding how packets are handled) from the data plane (forwarding packets), centralizing control in a software controller.


### 🟡 Mid Level

#### 1. Describe the Packet-in message in OpenFlow.
**Answer:**
The Packet-in message is used to send packets that do not match any flow table entry to the controller for additional processing.

#### 2. What are some examples of network-control applications in SDN?
**Answer:**
Routing applications, access control, and load balancing.

#### 3. What are some of the possible actions that can be defined in a flow table entry?
**Answer:**
Possible actions include forwarding to a specific port, dropping the packet, broadcasting, multicasting, or modifying field values in the packet's header.

#### 4. What are the primary responsibilities of the control plane and the controller in Software-Defined Networking (SDN)?
**Answer:**
The control plane manages flow table entries across the network's switches. The SDN controller maintains network state information, provides it to control applications, and manages switch flow tables.

#### 5. What core characteristic of Software-Defined Networking (SDN) enables generalized packet processing?
**Answer:**
Flow-based forwarding, which makes routing and switching decisions based on multiple header fields across various protocol layers.

#### 6. What does the "unbundling" of network functionality in Software-Defined Networking (SDN) mean?
**Answer:**
It refers to separating the data plane switches, centralized SDN controllers, and network-control applications, allowing them to be independently supplied by different vendors.

#### 7. What happens if a packet does not match any entry in the flow table?
**Answer:**
If a packet does not match any entry in the flow table, it can either be dropped or sent to the remote controller for further processing.

#### 8. What is OpenFlow in the context of SDN?
**Answer:**
A protocol that enables communication between the SDN controller and the forwarding tables of network devices.

#### 9. What is a RESTful API in the context of SDN controllers?
**Answer:**
An architectural API style that allows network-control applications to interact with the SDN controller using standard HTTP REST (Representational State Transfer) requests.

#### 10. What is a key characteristic of the data plane in SDN architectures used by large data centers?
**Answer:**
It consists of relatively simple, commodity switches.

#### 11. What is the difference between destination-based forwarding and generalized forwarding?
**Answer:**
Destination-based forwarding relies solely on the packet's final destination, while generalized forwarding considers multiple factors like origin or type of packet.

#### 12. What is the main advantage of using software-defined networking (SDN)?
**Answer:**
The separation of control plane functionality from the physical routers allows for more flexibility, centralized management, and innovation.

#### 13. What is the main difference between traditional routers and SDN switches in terms of packet forwarding?
**Answer:**
Traditional routers forward packets based primarily on the destination IP address, while SDN switches can forward based on generalized match-plus-action rules across many header field values.

#### 14. What is the primary difference between destination-based forwarding and generalized forwarding?
**Answer:**
Destination-based forwarding matches strictly on the destination IP address to route a packet to a single output port. Generalized forwarding (e.g., OpenFlow) allows matching across multiple header fields across layers and executing varied programmatic actions beyond simple forwarding.

#### 15. What is the primary function of match-plus-action in OpenFlow?
**Answer:**
It specifies how a forwarding device (router/switch) should process and manipulate datagrams based on exact or wildcard matching conditions in packet header values.

#### 16. What role does the remote controller play in an SDN architecture?
**Answer:**
It computes and distributes the forwarding tables used by each router, while the routers perform only the forwarding function.

#### 17. What transport protocol does OpenFlow operate over and what is its assigned default port number?
**Answer:**
OpenFlow operates over TCP with a default port number of 6653 (historically 6633).

#### 18. What type of routing approach does SDN enable compared to traditional per-router control?
**Answer:**
SDN enables more flexible, tailor-made routing approaches by allowing centralized control over flow tables, unlike the rigid per-router control.

#### 19. What types of header fields can be matched in an OpenFlow 1.0 match-plus-action rule?
**Answer:**
Header fields include source and destination MAC addresses, Ethernet type, VLAN fields, IP addresses, transport-layer port numbers, and ingress port IDs.

#### 20. Where is Dijkstra's algorithm executed in SDN, and how does it contrast with traditional router control?
**Answer:**
In SDN, Dijkstra's algorithm is executed as a separate application outside of the packet switches. In traditional router control, it is implemented directly inside every individual router.


### 🔴 Senior Level

#### 1. How are match-plus-action tables installed and updated in packet switches?
**Answer:**
Match-plus-action tables (commonly used in Software-Defined Networking like OpenFlow) are computed, installed, and updated by a remote controller, which can also interact with individual packet switches if needed.

#### 2. How do OpenFlow header field modifications function, and what is the role of Modify-State messages?
**Answer:**
OpenFlow header modifications allow a switch to rewrite values across 10 designated packet-header fields (excluding the IP Protocol field) prior to forwarding. Modify-State messages are used by the SDN controller to add, delete, or update flow table entries and configure switch port properties.

#### 3. How is high availability and scalability achieved in modern SDN controllers?
**Answer:**
By implementing the controller as a distributed system across multiple servers.

#### 4. What are OpenDaylight and ONOS?
**Answer:**
They are examples of popular, scalable, and high-availability Software-Defined Networking (SDN) controllers.

#### 5. What does it mean for an SDN controller to be "logically centralized"?
**Answer:**
The controller presents itself as a single, centralized control entity to network devices, abstracting the underlying physical topology, even though it may be implemented as a distributed system for high availability and scalability.

#### 6. What does the Flow-Removed message in OpenFlow indicate?
**Answer:**
The Flow-Removed message informs the controller that a flow table entry has been removed, either by timeout or due to a Modify-State message.

#### 7. What does the action "Forwarding" entail in an SDN OpenFlow flow table entry?
**Answer:**
Forwarding can involve sending a packet to a specific output port, broadcasting to all ports except the incoming port, or encapsulating and forwarding it to a remote controller.

#### 8. What happens when a link between switches goes down in an SDN-controlled network using OpenFlow?
**Answer:**
The affected switch notifies the SDN controller using a port-status message, prompting updates in flow tables of affected switches.

#### 9. What is Network Functions Virtualization (NFV) in relation to SDN?
**Answer:**
NFV aims to replace dedicated middleboxes with simple commodity servers and switches, similar to how SDN replaces monolithic routers with commodity hardware.

#### 10. What is the "match-plus-action" paradigm in generalized forwarding and SDN?
**Answer:**
A forwarding model where network devices make routing and switching decisions based on matching multiple header fields and executing a variety of programmable actions, such as forwarding, load balancing, or dropping packets.

#### 11. What is the function of the Send-Packet message in OpenFlow?
**Answer:**
The Send-Packet message is used by the controller to send a specific packet out of a specified port at the controlled switch.

#### 12. What is the function of the communication layer in an SDN controller?
**Answer:**
It handles communication between the SDN controller and controlled network devices via a southbound API.

#### 13. What is the purpose of the Configuration message in the OpenFlow protocol?
**Answer:**
The Configuration message allows the controller to query and set a switch’s configuration parameters.

#### 14. What is the purpose of the Port-Status message in OpenFlow?
**Answer:**
The Port-Status message is used by a switch to inform the controller of a change in port status (e.g., link down or up).

#### 15. What is the purpose of the Read-State message in OpenFlow?
**Answer:**
It is used by the SDN controller to collect statistics and counter values directly from the switch’s flow tables and ports.

#### 16. What is the purpose of the northbound interface in SDN controllers?
**Answer:**
It allows network-control applications to interact with the controller, read/write network state, and modify flow tables.

#### 17. What is the significance of the counters in an SDN flow table entry?
**Answer:**
Counters track metrics like the number of packets matched by the entry and the time since the last update, providing insight into traffic and flow performance.


## 📂 Category: Software-Defined Networking (SDN) (11 cards)

### 🟡 Mid Level

#### 1. What are the two primary components of the SDN control plane?
**Answer:**
The SDN controller and the SDN network-control applications.

#### 2. What is the SDN approach to routing functionality?
**Answer:**
A physically separate, remote controller computes and distributes forwarding tables to all routers.

#### 3. What is the analogy used to explain the unbundling of SDN components?
**Answer:**
It is likened to the evolution from mainframe computers (monolithic) to personal computers with separate hardware, OS, and applications.

#### 4. What is the role of wildcards in flow table entries?
**Answer:**
Wildcards allow for more flexible matching, enabling a flow table entry to match a range of values, such as an IP address of 128.119.* to match any address beginning with 128.119.

#### 5. What role do network-control applications play in SDN?
**Answer:**
They monitor, program, and control network devices through APIs provided by the SDN controller.

#### 6. Why are devices referred to as "packet switches" rather than routers or switches in SDN literature?
**Answer:**
They are called "packet switches" because they can make forwarding decisions based on both network-layer and link-layer addresses, transcending the traditional distinctions between routers and switches.


### 🔴 Senior Level

#### 1. How do routers communicate with the remote controller in the Software-Defined Networking (SDN) approach?
**Answer:**
By exchanging control plane messages containing flow tables, forwarding states, and network telemetry via southbound APIs (e.g., OpenFlow).

#### 2. What is meant by "network programmability" in Software-Defined Networking (SDN)?
**Answer:**
The ability to dynamically program and manage the network's behavior and forwarding rules via control applications running in the centralized control plane.

#### 3. What is the historical significance of the Ethane project in SDN development?
**Answer:**
The Ethane project pioneered the use of flow-based Ethernet switches and a centralized controller, eventually evolving into OpenFlow.

#### 4. What is the role of the network-wide state-management layer in SDN controllers?
**Answer:**
It maintains up-to-date information about network state, such as link status, flow tables, and device statistics.

#### 5. Why are not all fields in an IP header available for matching in OpenFlow?
**Answer:**
Some fields are excluded to strike a balance between functionality and complexity, ensuring the abstraction remains useful without becoming overly complicated.


## 📂 Category: Standards & Governance (1 cards)

### 🟢 Junior Level

#### 1. Who develops Internet standards?
**Answer:**
The Internet Engineering Task Force (IETF).


## 📂 Category: Switching & Routing (4 cards)

### 🟢 Junior Level

#### 1. What does it mean that switches are "self-learning"?
**Answer:**
Switches automatically build and update their forwarding tables (MAC address tables) by inspecting the source MAC addresses of incoming frames without requiring manual administrator intervention.

#### 2. When should a network administrator opt for switches over routers?
**Answer:**
In small networks with a few hundred hosts to localize traffic without IP configuration overhead.


### 🟡 Mid Level

#### 1. What does it mean for a crossbar switch to be non-blocking?
**Answer:**
It means that a packet being forwarded to an output port will not be blocked as long as no other packet is simultaneously sent to that same output port.


### 🔴 Senior Level

#### 1. What capability does MPLS provide that standard IP routing does not?
**Answer:**
MPLS (Multi-Protocol Label Switching) allows explicit path routing (traffic engineering), fast reroute, and forwarding packets along pre-determined label-switched paths (LSPs) based on short path labels rather than long IP header lookups.


## 📂 Category: Switching Architecture (1 cards)

### 🟡 Mid Level

#### 1. How does switching via a bus mechanism transfer a packet from an input port to an output port?
**Answer:**
The input port prepends a label to the packet indicating the destination output port and broadcasts/sends it over a shared bus, where only the matching output port grabs it.


## 📂 Category: Switching Architectures (1 cards)

### 🟡 Mid Level

#### 1. What blocking issue arises in crossbar switches?
**Answer:**
If two or more packets from different input ports are simultaneously destined for the same output port, one packet must be buffered at the input port since only one packet can traverse a specific bus/cross point at a time.


## 📂 Category: Switching and LANs (2 cards)

### 🟢 Junior Level

#### 1. What is the main benefit of using VLANs in a switched LAN?
**Answer:**
VLANs improve traffic isolation by confining broadcast traffic to designated groups, enhancing security and performance.

#### 2. What is the main function of switched local area networks (LANs)?
**Answer:**
To connect multiple devices (hosts, routers, servers) using switches that operate at the link layer, forwarding link-layer frames based on destination MAC addresses.


## 📂 Category: System Architecture (1 cards)

### 🟡 Mid Level

#### 1. What is the performance strategy for modular or multi-component systems (MDCs) when components fail?
**Answer:**
They are designed for graceful performance degradation, continuing to operate with reduced performance until a critical failure occurs.


## 📂 Category: Telecommunications (1 cards)

### 🟡 Mid Level

#### 1. Which cellular network generation established the foundational roaming configurations utilized by modern architectures?
**Answer:**
4G LTE networks established core roaming and signaling configurations that continue to be leveraged in 5G and future mobile architectures.


## 📂 Category: Traffic Engineering (1 cards)

### 🟡 Mid Level

#### 1. What is the "golden rule" in traffic engineering regarding traffic intensity?
**Answer:**
The system should be designed so that the traffic intensity does not exceed 1.


## 📂 Category: Traffic Management (3 cards)

### 🟢 Junior Level

#### 1. What happens if the output link is busy in FIFO queuing?
**Answer:**
Packets arriving while the output link is busy must wait in the queue until the link is free to transmit them.


### 🟡 Mid Level

#### 1. What happens if the arrival rate of packets to a router (or output capacity exceeded) causes network congestion?
**Answer:**
Congestion occurs, causing packets to queue in the output buffer, leading to increased delays and potential packet loss.


### 🔴 Senior Level

#### 1. What is bufferbloat?
**Answer:**
Bufferbloat is a phenomenon where excessive buffering in routers leads to high latency and poor user experience, even when the throughput is high.


## 📂 Category: Traffic Management & Quality of Service (1 cards)

### 🟡 Mid Level

#### 1. What is the impact of larger buffers on packet queuing?
**Answer:**
While larger buffers can reduce packet loss by accommodating fluctuations in packet arrival rates, they can also increase queuing delays, affecting real-time applications negatively.


## 📂 Category: Traffic Management & Queuing (1 cards)

### 🟡 Mid Level

#### 1. Why can high throughput near link capacity lead to increased delays?
**Answer:**
As sending rates approach link capacity, the average delay increases significantly due to packet queuing.


## 📂 Category: Transport & Network Layers (1 cards)

### 🟢 Junior Level

#### 1. What foundational protocols control the sending and receiving of information on the Internet?
**Answer:**
Transmission Control Protocol (TCP) for reliable transport and Internet Protocol (IP) for network-layer routing. RFCs define these alongside application protocols like HTTP and SMTP.


## 📂 Category: Transport / Data Link Protocols (1 cards)

### 🔴 Senior Level

#### 1. What is the maximum size of the window in a Selective Repeat protocol relative to the sequence number space?
**Answer:**
The window size must be less than or equal to half the size of the sequence number space ($N \le 2^{(k-1)}$ for $k$-bit sequence numbers) to avoid confusion between retransmissions and new packets.


## 📂 Category: Transport Layer (203 cards)

### 🟢 Junior Level

#### 1. Can TCP connections support multicasting?
**Answer:**
No, TCP connections are point-to-point and can only connect one sender to one receiver.

#### 2. Describe the nature of UDP as a transport protocol
**Answer:**
UDP is a connectionless and lightweight transport protocol that provides minimal services without handshaking before communication.

#### 3. Describe the role of the transport layer on the sending side of communication.
**Answer:**
It converts application-layer messages into transport-layer segments, possibly breaking them into smaller chunks, and adds a transport-layer header to each chunk.

#### 4. Describe the three segments involved in the TCP handshake.
**Answer:**
The client sends a SYN segment, the server responds with a SYN-ACK segment, and the client sends an ACK segment.

#### 5. Does UDP include a congestion-control mechanism?
**Answer:**
No, UDP does not include a congestion-control mechanism, allowing sending processes to transmit data at any rate.

#### 6. How are acknowledgment numbers used in TCP?
**Answer:**
Acknowledgment numbers indicate the next byte that a sender expects to receive, facilitating reliable data transfer and flow control.

#### 7. How are sockets identified in the transport layer?
**Answer:**
Each TCP or UDP socket is uniquely identified by a tuple consisting of source IP, source port, destination IP, and destination port (or a local port/IP pair for listening server sockets).

#### 8. How do application developers choose between UDP and TCP?
**Answer:**
They specify the desired transport protocol when instantiating network sockets, choosing based on application requirements such as reliability, ordering, latency tolerance, and framing.

#### 9. How do application processes utilize the transport layer?
**Answer:**
They send and receive messages across logical sockets without needing to manage or understand the underlying physical infrastructure, routing, or link-layer framing details.

#### 10. How do web servers handle segments from multiple clients?
**Answer:**
They distinguish between segments using the source IP addresses and source port numbers since all segments will have the same destination port (e.g., port 80).

#### 11. How does TCP differ from UDP in terms of service guarantees?
**Answer:**
TCP provides a connection-oriented service with guaranteed, uncorrupted, ordered delivery without gaps or duplication, alongside flow control. UDP offers a connectionless service without reliability or flow control.

#### 12. How does TCP estimate the round-trip time (RTT)?
**Answer:**
By measuring the time between sending a segment and receiving its acknowledgment, known as SampleRTT.

#### 13. How does TCP infer that the network is not congested?
**Answer:**
By receiving acknowledgments (ACKs) for previously unacknowledged segments, which signals that data is successfully traversing the network path.

#### 14. How does TCP manage flow control to prevent overflowing the receiver's buffer?
**Answer:**
TCP uses buffers and a receive window (rwnd) advertised in packet headers to inform the sender how much free buffer space is currently available at the receiver.

#### 15. How does TCP's congestion-control mechanism differ from UDP's operation?
**Answer:**
TCP throttles the sender's transmission rate dynamically based on network congestion, whereas UDP does not implement any congestion control or flow control, allowing for immediate, unmanaged data transmission.

#### 16. How does UDP handle data between the application process and the network layer?
**Answer:**
UDP takes messages from the application, adds header fields for multiplexing/demultiplexing, and passes the segment directly to the network layer without establishing a connection.

#### 17. How does parallelism affect the retrieval of objects in non-persistent connections?
**Answer:**
Browsers can open multiple TCP connections to retrieve different objects simultaneously, potentially shortening response time.

#### 18. How does the Go-Back-N (GBN) protocol handle lost or delayed packets, and what are its similarities to TCP?
**Answer:**
When a timeout occurs, the sender retransmits all unacknowledged packets currently in flight. GBN shares core mechanisms with TCP, including sequence numbers, cumulative acknowledgments, and retransmission timeouts.

#### 19. How does the transport layer handle multiple application processes?
**Answer:**
By using unique socket identifiers and examining port numbers for multiplexing and demultiplexing.

#### 20. How is a specific application process identified on a host when multiple services are running concurrently?
**Answer:**
By utilizing destination port numbers bound to transport layer sockets, uniquely identifying the target process on the host.

#### 21. How is throughput affected in the presence of heavy intervening traffic?
**Answer:**
Throughput is determined not only by the transmission rates of the individual links but also by the volume of other concurrent traffic sharing those intermediate links.

#### 22. Name the four primary dimensions along which transport-layer services can be classified.
**Answer:**
Reliable data transfer, throughput, timing, and security.

#### 23. Name two transport-layer protocols commonly used on the Internet.
**Answer:**
TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

#### 24. What action does the receiver perform upon receiving a packet in rdt1.0?
**Answer:**
It removes the data from the packet and delivers it to the upper layer.

#### 25. What are the key components of a TCP segment?
**Answer:**
A TCP segment consists of a header and a data field, with the header containing fields like sequence number, acknowledgment number, and flags.

#### 26. What are the three guiding principles for TCP sender rate adjustments?
**Answer:**
Decrease rate upon loss, increase rate upon acknowledgment, and probe for bandwidth.

#### 27. What are the two broad approaches to congestion control in networking?
**Answer:**
End-to-end congestion control and network-assisted congestion control.

#### 28. What are the two types of TCP connections used in client-server communication?
**Answer:**
Non-persistent connections and persistent connections.

#### 29. What are transport-layer segments, and what is their role in Internet terminology?
**Answer:**
Transport-layer packets (known as segments) created by converting application-layer messages into smaller chunks with added headers.

#### 30. What does "connection-oriented" mean in the context of TCP?
**Answer:**
It means that a virtual connection (via a handshake) must be established between two application processes before application-layer data can be sent.

#### 31. What does UDP stand for and what are its key characteristics?
**Answer:**
User Datagram Protocol; it is a connectionless, unreliable transport-layer protocol that offers no flow control, error recovery, or ordering guarantees.

#### 32. What does it mean that UDP provides an unreliable data transfer service?
**Answer:**
There is no guarantee that messages sent through UDP will reach the receiving process, acknowledgments are not used, flow/congestion control is absent, and packets may arrive out of order or duplicated.

#### 33. What does multiplexing and demultiplexing entail at the transport layer?
**Answer:**
Multiplexing involves gathering data chunks from different application sockets, encapsulating them with header information (ports) to create segments, and passing them to the network layer. Demultiplexing is the reverse process of delivering received segments to the correct socket.

#### 34. What does the sender do upon receiving a NAK in the rdt2.0 protocol?
**Answer:**
It immediately retransmits the last corrupted or unacknowledged packet.

#### 35. What fields does a typical UDP header include?
**Answer:**
A UDP header includes source port number, destination port number, length, and checksum.

#### 36. What happens if a transport-layer protocol does not provide reliable data transfer?
**Answer:**
Some data sent by the sending process may not arrive at the receiving process, which is acceptable for loss-tolerant applications like multimedia.

#### 37. What happens if multiple UDP segments have the same destination IP address and port number?
**Answer:**
They are directed to the same destination process via the same socket.

#### 38. What happens to the end-system view when a packet is lost in the network?
**Answer:**
It appears as if the packet was transmitted but never reached the destination.

#### 39. What happens to the transport-layer segment at the receiving end?
**Answer:**
The network layer extracts the transport-layer segment from the datagram and passes it up to the transport layer, which then processes it for the receiving application.

#### 40. What happens when a transport-layer segment arrives at a host?
**Answer:**
The transport layer examines the segment's destination port number to direct it to the correct socket.

#### 41. What happens when an ACK is received in the Go-Back-N (GBN) protocol?
**Answer:**
The ACK serves as a cumulative acknowledgment, indicating that all packets up to that sequence number have been received.

#### 42. What is TCP?
**Answer:**
TCP (Transmission Control Protocol) is a connection-oriented, reliable transport protocol used in the Internet.

#### 43. What is a defining characteristic of UDP compared to TCP?
**Answer:**
UDP is a connectionless protocol, meaning it does not establish a handshake or connection before sending data, offering lower overhead at the cost of reliability.

#### 44. What is a segment in the transport layer?
**Answer:**
A segment is the transport-layer packet used to transport application-layer messages, created by protocols like TCP or UDP.

#### 45. What is guaranteed delivery in the context of network services?
**Answer:**
A network service guarantee that ensures a packet sent by a source host will eventually arrive at the destination host.

#### 46. What is meant by a full-duplex connection in TCP?
**Answer:**
A full-duplex connection allows both processes to send messages to each other simultaneously over the same connection.

#### 47. What is one major disadvantage of using UDP for multimedia applications?
**Answer:**
The lack of congestion control can lead to high packet loss and potential network congestion if many applications send high-bit-rate streams without regulation.

#### 48. What is reliable data transfer?
**Answer:**
A service provided by protocols (like TCP) ensuring that data sent by the application layer on one end is delivered correctly, completely, and in the correct order to the application layer on the other end, recovering from packet loss, corruption, and reordering.

#### 49. What is the Internet checksum and how is it calculated?
**Answer:**
A checksum calculated over all fields of the TCP and UDP headers and data fields, which is verified by the receiver.

#### 50. What is the concept of pipelining in data transfer protocols?
**Answer:**
Pipelining allows the sender to transmit multiple packets without waiting for acknowledgments, increasing utilization.

#### 51. What is the function of acknowledgment (ACK) in TCP?
**Answer:**
ACK is used by the receiver to inform the sender that a packet has been received correctly.

#### 52. What is the header size of UDP compared to TCP?
**Answer:**
UDP has an 8-byte header, whereas TCP has a 20-byte header.

#### 53. What is the primary cause of network congestion?
**Answer:**
Too many data sources attempting to send packets into the network at too high a rate, exceeding link capacities and buffer limits.

#### 54. What is the primary focus and mechanism of the rdt3.0 protocol?
**Answer:**
It provides reliable data transfer over an unreliable channel that can corrupt, drop, or lose packets, utilizing stop-and-wait semantics, sequence numbers, timers, and acknowledgments (ACKs).

#### 55. What is the primary function of a transport-layer protocol?
**Answer:**
To provide logical communication between application processes running on different hosts, abstracting the network layer details to make distinct hosts appear directly connected.

#### 56. What is the primary purpose of the checksum in the rdt2.0 data transfer protocol?
**Answer:**
To allow the receiver to detect when bit errors have occurred in received packets.

#### 57. What is the purpose of TCP's timeout/retransmit mechanism?
**Answer:**
To reliably recover from lost segments or dropped ACKs in a TCP connection by resending unacknowledged data once a retransmission timer expires.

#### 58. What is the purpose of flow control in TCP?
**Answer:**
Flow control matches the rate at which the sender transmits data with the rate at which the receiver can process and read the data, preventing buffer overflows.

#### 59. What is the purpose of the FIN bit in TCP?
**Answer:**
The FIN bit is used to indicate that a side of the TCP connection wants to close the connection.

#### 60. What is the purpose of the TCP three-way handshake?
**Answer:**
To establish parameters for the data transfer between a client and a server by exchanging three special segments.

#### 61. What is the purpose of the countdown timer in rdt3.0?
**Answer:**
To manage the timing of packet retransmissions in stop-and-wait reliable data transfer protocols.

#### 62. What is the purpose of the handshaking procedure in TCP?
**Answer:**
The handshaking procedure allows the client and server to exchange transport-layer control information (like sequence numbers and window size) before the application-level messages begin to flow.

#### 63. What is the purpose of the sequence number field in a TCP segment?
**Answer:**
The sequence number indicates the byte-stream number of the first byte in the segment, used for ensuring ordered delivery of data.

#### 64. What is the purpose of the source port number in a segment?
**Answer:**
It serves as part of the return address for response segments sent back to the original sender.

#### 65. What is the role of a socket in network applications?
**Answer:**
A socket serves as the interface between the application process and the transport-layer protocol.

#### 66. What is the role of the receive buffer in TCP?
**Answer:**
The receive buffer stores incoming segments until the application reads the data.

#### 67. What is the role of the transport layer in the Internet protocol stack?
**Answer:**
The transport layer is responsible for transporting application-layer messages between application endpoints, using protocols like TCP and UDP.

#### 68. What is the significance of using sequence numbers in reliable data transfer protocols like rdt2.1?
**Answer:**
They help the receiver distinguish between new packets and retransmissions.

#### 69. What is the simplest reliable data transfer protocol for a perfectly reliable channel?
**Answer:**
rdt1.0

#### 70. What is the socket interface in the Internet?
**Answer:**
The socket interface is a set of rules that specify how a program on one end system asks the Internet to deliver data to a program on another end system.

#### 71. What minimal services do both UDP and TCP provide?
**Answer:**
Process-to-process data delivery and error checking.

#### 72. What must an application do after finishing sending messages via TCP?
**Answer:**
The application must tear down the TCP connection.

#### 73. What network inefficiency occurs when a sender prematurely retransmits a packet?
**Answer:**
The routers waste precious link bandwidth by forwarding both the original packet and the unnecessarily retransmitted duplicate.

#### 74. What parameters uniquely identify a TCP socket?
**Answer:**
A TCP socket is identified by a four-tuple: (source IP address, source port number, destination IP address, destination port number).

#### 75. What potential issue arises from the retransmission mechanism in stop-and-wait protocols like rdt3.0?
**Answer:**
The possibility of duplicate data packets entering the sender-to-receiver channel due to premature timeouts or delayed acknowledgments.

#### 76. What role does the checksum play in reliable data transfer protocols like SR?
**Answer:**
The checksum is used to detect bit errors in a transmitted packet.

#### 77. What role does the receive window field play in TCP?
**Answer:**
The receive window field is used for flow control, indicating the number of bytes a receiver is willing to accept.

#### 78. What services are not provided by both TCP and UDP?
**Answer:**
Both TCP and UDP do not provide guarantees for throughput or timing.

#### 79. What services can transport protocols provide even if the underlying network layer is unreliable?
**Answer:**
Transport protocols can provide reliable data transfer (via acknowledgments and retransmissions) and encryption for confidentiality.

#### 80. What two additional concerns must be addressed in rdt3.0 beyond bit errors, and what two transport protocols are primarily available on the Internet?
**Answer:**
rdt3.0 must detect and recover from packet loss (beyond bit errors). The two primary Internet transport protocols are User Datagram Protocol (UDP) and Transmission Control Protocol (TCP).

#### 81. What two pieces of information are needed to identify a receiving process on the Internet?
**Answer:**
The address of the host (IP address) and an identifier for the receiving process (port number).

#### 82. What type of service does TCP provide?
**Answer:**
A reliable, connection-oriented service.

#### 83. What type of service does UDP provide?
**Answer:**
An unreliable, connectionless service.

#### 84. What types of applications typically prefer UDP?
**Answer:**
Real-time applications such as streaming multimedia, Internet telephony, and online gaming prefer UDP because they can tolerate some packet loss.

#### 85. What types of applications typically require reliable data transfer?
**Answer:**
Applications such as electronic mail, file transfer, remote host access, Web document transfers, and financial applications.

#### 86. Where is the transport layer implemented in the networking model?
**Answer:**
The transport layer is implemented in the end systems, not in the network routers.

#### 87. Why do developers of Internet telephony applications often prefer UDP over TCP?
**Answer:**
Because UDP tolerates minor data loss while avoiding the head-of-line blocking, connection setup overhead, and aggressive congestion control of TCP, ensuring real-time delivery.

#### 88. Why does UDP include a checksum?
**Answer:**
To provide error detection for the UDP header and payload to catch potential corruption that may occur during transmission.

#### 89. Why does a receiving process need an explicit transport-layer address (port)?
**Answer:**
To ensure messages arriving at a host are demultiplexed and handed off to the correct specific target application process.

#### 90. Why does the Go-Back-N (GBN) protocol discard out-of-order packets?
**Answer:**
To avoid the need for complex buffering at the receiver; the receiver only needs to keep track of the next expected packet sequence number.

#### 91. Why does the sender in the Go-Back-N (GBN) protocol need to limit the number of unacknowledged packets?
**Answer:**
To enforce flow control and prevent overwhelming the receiver's capacity or congesting network queues.

#### 92. Why is it important to set the timeout interval appropriately in transport protocols?
**Answer:**
To minimize unnecessary retransmissions while ensuring timely retransmissions for lost segments.

#### 93. Why is managing TCP connections a burden for web servers with non-persistent connections?
**Answer:**
Each new connection requires allocating TCP buffers and maintaining state variables for potentially hundreds of clients simultaneously.

#### 94. Why must an application developer explicitly choose a transport-layer protocol?
**Answer:**
Because different transport-layer protocols (such as TCP and UDP) provide varying guarantees regarding reliability, ordering, and flow control that may or may not match the specific application's requirements.


### 🟡 Mid Level

#### 1. Can applications using UDP still achieve reliable data transfer?
**Answer:**
Yes, reliability can be implemented at the application layer, but this requires additional mechanisms such as acknowledgment and retransmission.

#### 2. Can the transport layer rely on the network layer to deliver packets to their destination?
**Answer:**
Yes, but the service model determines the reliability of this delivery.

#### 3. Describe the sender's behavior in GBN when it receives an ACK for packet n.
**Answer:**
The sender considers all packets up to and including packet n as acknowledged and slides the window forward to allow new packets to be sent.

#### 4. Explain the sawtooth behavior observed in TCP's congestion control.
**Answer:**
The sawtooth behavior represents the cycle of linearly increasing cwnd until a loss occurs (resulting in a decrease), followed by another linear increase, and so on.

#### 5. How can UDP traffic affect overall network performance in comparison to TCP?
**Answer:**
Since UDP does not adjust its transmission rate based on congestion control, it can crowd out TCP traffic, potentially leading to severely degraded performance for TCP connections sharing the same bottleneck link.

#### 6. How do gaps in Ethernet frames affect applications using UDP and TCP differently?
**Answer:**
UDP applications see gaps directly, while TCP handles gaps by retransmitting lost data, ensuring data integrity.

#### 7. How does GBN utilize timers in its operation?
**Answer:**
A timer is set for the oldest unacknowledged packet; if the timer expires, all unacknowledged packets are retransmitted.

#### 8. How does Selective Repeat (SR) differ from Go-Back-N (GBN) in handling packet retransmissions?
**Answer:**
SR retransmits only those packets that are suspected to be lost or corrupted, avoiding unnecessary retransmissions of other packets.

#### 9. How does TCP adjust the timeout interval after a retransmission?
**Answer:**
The timeout interval is doubled after each retransmission.

#### 10. How does TCP deal with packet errors and losses?
**Answer:**
TCP uses checksums for error detection and retransmits packets that are lost or corrupted. It detects losses via timeouts or duplicate acknowledgments.

#### 11. How does TCP demultiplex incoming segments compared to UDP?
**Answer:**
In TCP, two arriving segments with different source IP addresses or source port numbers will be directed to different sockets based on a four-tuple (source IP, source port, destination IP, destination port). UDP uses only the destination port number for demultiplexing.

#### 12. How does TCP determine when to increase cwnd during the congestion-avoidance phase?
**Answer:**
TCP increases cwnd by MSS bytes whenever a new acknowledgment (ACK) arrives.

#### 13. How does TCP handle segment retransmission upon detecting duplicate ACKs?
**Answer:**
TCP retransmits the missing segment before the segment's timer expires when it detects packet loss through duplicate ACKs.

#### 14. How does rdt3.0 ensure reliable data transmission over a lossy channel?
**Answer:**
By using checksums for error detection, sequence numbers to avoid confusion over duplicates, and timers for retransmitting packets after a timeout when no ACK is received.

#### 15. How does the Selective Repeat protocol handle out-of-order packets received by the receiver?
**Answer:**
Out-of-order packets are buffered until any missing packets are received, after which a batch of consecutive packets can be delivered in order.

#### 16. How does the rdt3.0 sender handle lost versus delayed packets?
**Answer:**
It cannot definitively differentiate between them; it assumes packet loss if the corresponding ACK is not received within a specified timeout interval.

#### 17. How many RTTs are typically involved in establishing a TCP connection and receiving an HTML file in non-persistent connections?
**Answer:**
Approximately two RTTs are involved: one for establishing the connection and one for the request and response.

#### 18. How many states do the sender and receiver FSMs have in the rdt1.0 and rdt2.1 protocols?
**Answer:**
In rdt1.0, both sender and receiver have one state each. In rdt2.1, both sender and receiver have two states each to handle sequence numbers and ACKs/NAKs.

#### 19. How often does TCP compute SampleRTT measurements?
**Answer:**
Typically, only one SampleRTT measurement at a time, approximately once every RTT.

#### 20. In what scenario can a server correctly demultiplex TCP/UDP connections that share the same source port number?
**Answer:**
If the source IP addresses are different, the server can differentiate the connections using the 4-tuple (source IP, source port, dest IP, dest port) even if the source port numbers are identical.

#### 21. Name two classic versions of TCP that have been used since the late 1980s.
**Answer:**
TCP Tahoe and TCP Reno.

#### 22. Under what condition does a TCP receiver send a duplicate ACK?
**Answer:**
A duplicate ACK is sent when an out-of-order segment with a higher-than-expected sequence number is received, indicating a gap in the data stream.

#### 23. What action does the GBN (Go-Back-N) receiver take upon receiving a correctly sequenced packet?
**Answer:**
The receiver sends an ACK for that packet and delivers the data to the upper layer.

#### 24. What action does the sender take after transmitting a packet in the rdt3.0 protocol?
**Answer:**
It starts a countdown timer to monitor for an acknowledgment (ACK) and handles potential timeout events for retransmission.

#### 25. What advantage does UDP offer in terms of handling multiple concurrent clients?
**Answer:**
UDP allows servers to support many more active clients since it does not maintain per-connection state tables or require kernel resources for connection management.

#### 26. What approach does rdt2.2 take to handle acknowledgments?
**Answer:**
It sends duplicate ACKs for the last correctly received packet instead of using NAKs.

#### 27. What are some of the issues researchers have identified with TCP in wireless networks?
**Answer:**
Issues include high bit error rates and the inability of TCP to distinguish between congestion and wireless link errors.

#### 28. What are the components that play crucial roles in the operation of rdt3.0?
**Answer:**
Checksums, sequence numbers, timers, and positive/negative acknowledgment packets.

#### 29. What are the key variables tracked in the sender side of the GBN (Go-Back-N) protocol?
**Answer:**
The key variables are "base" (sequence number of the oldest unacknowledged packet) and "nextseqnum" (smallest unused sequence number).

#### 30. What are the three major components of the TCP congestion-control algorithm?
**Answer:**
Slow start, congestion avoidance, and fast recovery.

#### 31. What control does an application developer have over the transport layer when using sockets?
**Answer:**
The developer can choose the transport protocol and potentially adjust parameters like maximum buffer and segment sizes.

#### 32. What defines a "loss event" for a TCP sender?
**Answer:**
A timeout or the receipt of three duplicate ACKs.

#### 33. What do ACK packets in rdt2.1 include to help the sender?
**Answer:**
The sequence number of the packet being acknowledged.

#### 34. What does a TCP connection-establishment request segment include?
**Answer:**
It includes the destination port number (e.g., 12000), a SYN (connection-establishment) bit set, and a randomly chosen source port number selected by the client.

#### 35. What does a UDP socket require for identification?
**Answer:**
A two-tuple consisting of a destination IP address and a destination port number.

#### 36. What features does QUIC provide that are beneficial for HTTP?
**Answer:**
Message multiplexing, per-stream flow control, and low-latency connection establishment.

#### 37. What happens if the receiver gets a packet with a sequence number higher than the expected one (e.g., Go-Back-N)?
**Answer:**
The receiver discards that packet and resends an ACK for the last correctly received packet.

#### 38. What happens if the sender's window is full in TCP?
**Answer:**
The sender must wait until it receives ACKs for previously sent packets before it can send more data.

#### 39. What happens to data sent from a client process in TCP?
**Answer:**
The data is passed to the TCP send buffer, from which TCP sends chunks of data to the network layer at its discretion.

#### 40. What happens to the congestion window during the slow start phase?
**Answer:**
It begins at a small value (1 MSS) and doubles every time a transmitted segment is acknowledged.

#### 41. What happens to the timer when a new packet is sent in rdt3.0?
**Answer:**
The timer is started or reset.

#### 42. What happens when TCP receives out-of-order segments?
**Answer:**
TCP implementations typically keep out-of-order segments until the missing segments are received, rather than discarding them.

#### 43. What happens when a TCP server receives a connection-request segment?
**Answer:**
The server locates the process waiting on the specified port, creates a new socket, and uses the four values from the segment to identify this socket.

#### 44. What happens when a packet is received with a sequence number equal to the base of the receive window in Selective Repeat (SR)?
**Answer:**
The received packet and any consecutively numbered buffered packets are delivered to the upper layer.

#### 45. What is Round-Trip Time (RTT) and SampleRTT in TCP connections?
**Answer:**
RTT is the total time it takes for a small packet to travel from client to server and back, including queue, propagation, and processing delays. SampleRTT specifically measures the exact elapsed time from when a specific TCP segment is transmitted until its acknowledgment (ACK) is received.

#### 46. What is a 'timeout event' in Go-Back-N (GBN) and rdt3.0 protocols, and what is the sender's action?
**Answer:**
A timeout event occurs when the sender does not receive an acknowledgment for a packet within a specified period. In response, the sender retransmits the unacknowledged packet(s).

#### 47. What is a challenge posed by applications that use multiple parallel TCP connections?
**Answer:**
Applications using multiple parallel connections can gain a disproportionate share of bandwidth in congested networks, leading to unfair allocations among users.

#### 48. What is a guaranteed available throughput service in transport protocols?
**Answer:**
A service where the application can request a specific minimum throughput rate, and the transport protocol ensures that this rate is met throughout the connection's lifetime.

#### 49. What is an exponential weighted moving average (EWMA)?
**Answer:**
A statistical average that gives more weight to recent samples, used in the calculation of EstimatedRTT.

#### 50. What is congestion control in TCP?
**Answer:**
A mechanism to prevent excessive traffic from overwhelming network links and routers.

#### 51. What is demultiplexing in the transport layer?
**Answer:**
Delivering incoming transport-layer segments to the appropriate application process based on the segment's fields.

#### 52. What is the Maximum Segment Size (MSS) in TCP and how does it relate to MTU?
**Answer:**
The MSS is the maximum amount of application-layer data that can be sent in a single TCP segment, typically set based on the network path's Maximum Transmission Unit (MTU) minus IP and TCP header sizes.

#### 53. What is the advantage of using cumulative acknowledgments in GBN (Go-Back-N)?
**Answer:**
It simplifies the acknowledgment process, as only the highest acknowledged packet needs to be confirmed.

#### 54. What is the effect of a shared bottleneck link on throughput and network congestion?
**Answer:**
A shared bottleneck link reduces throughput by equally dividing its total capacity among multiple competing data transfers. Packet loss often results when router buffers overflow due to this congestion.

#### 55. What is the impact of pipelining on the range of sequence numbers in reliable data transfer protocols?
**Answer:**
The range of sequence numbers must be increased to allow multiple in-transit packets to have unique identifiers.

#### 56. What is the main characteristic of end-to-end congestion control?
**Answer:**
The network layer provides no explicit support to the transport layer; congestion must be inferred from network behavior such as packet loss or delay.

#### 57. What is the main issue with timeout-triggered retransmissions in TCP?
**Answer:**
The timeout period can be relatively long, leading to increased end-to-end delay and idle link capacity when a segment is lost.

#### 58. What is the minimum time the sender must wait to be certain that a packet has been lost?
**Answer:**
At least the round-trip delay plus processing time at the receiver.

#### 59. What is the operational behavior of the sender when its transmission window is full in Go-Back-N (GBN)?
**Answer:**
The sender cannot transmit any new packets and must wait for an acknowledgment (ACK) for one of the outstanding unacknowledged packets to slide the window forward.

#### 60. What is the primary behavior of TCP in the congestion-avoidance state regarding the congestion window (cwnd)?
**Answer:**
In congestion-avoidance, TCP increases the congestion window (cwnd) linearly by 1 MSS (Maximum Segment Size) for each round-trip time (RTT).

#### 61. What is the purpose of the welcoming socket in a TCP server?
**Answer:**
The welcoming socket listens for connection-establishment requests from clients on a specified port (e.g., port 12000).

#### 62. What is the role of congestion-control protocols?
**Answer:**
Congestion-control protocols in end systems control the rate at which packets are transmitted between sender and receiver.

#### 63. What is the role of the congestion window (cwnd) in TCP?
**Answer:**
It limits the amount of unacknowledged data that can be sent, influencing the sending rate.

#### 64. What is the sender's action in response to a timer interrupt in rdt3.0?
**Answer:**
The sender retransmits the data packet.

#### 65. What is the significance of the "window" in the GBN (Go-Back-N) protocol?
**Answer:**
The window represents the range of sequence numbers that can be used for unacknowledged packets and slides forward as ACKs are received.

#### 66. What is the term used to describe TCP's congestion control algorithm that consists of linear increase and multiplicative decrease?
**Answer:**
This approach is known as Additive Increase, Multiplicative Decrease (AIMD).

#### 67. What mechanism does TCP use to maintain an average of SampleRTT values?
**Answer:**
A weighted moving average called EstimatedRTT.

#### 68. What primary mechanism does TCP include to manage network efficiency and flow control?
**Answer:**
TCP includes a congestion-control mechanism (using AIMD, slow start, and congestion windows) to manage data flow and prevent network congestion collapse.

#### 69. What problem does the Go-Back-N (GBN) protocol face when the window size and bandwidth-delay product are both large?
**Answer:**
GBN causes unnecessary retransmissions of many healthy packets following a single packet error, resulting in severe network performance degradation.

#### 70. What role do ACK packets play in the rdt3.0 reliable data transfer protocol?
**Answer:**
They inform the sender whether a specific data packet (identified by sequence numbers 0 or 1) was received correctly and uncorrupted.

#### 71. What triggers the TCP sender to perform a fast retransmit?
**Answer:**
The sender performs a fast retransmit upon receiving three duplicate ACKs for the same segment, indicating that the segment following the acknowledged one has likely been lost.

#### 72. Why does TCP not compute SampleRTT for retransmitted segments?
**Answer:**
To avoid ambiguities and inaccuracies in round-trip time estimation caused by the Karn's/Partridge's algorithm when distinguishing original from retransmitted segments.

#### 73. Why is TCP considered a distributed approach to congestion control?
**Answer:**
Because each TCP sender adjusts its rate based on local feedback without explicit coordination with other senders.

#### 74. Why is buffering necessary in the Selective Repeat (SR) receiver?
**Answer:**
To hold out-of-order packets temporarily until all preceding missing packets are received, allowing the network stack to deliver data in-order to upper layers.

#### 75. Why is it important for the Selective Repeat (SR) receiver to acknowledge already received packets?
**Answer:**
To prevent the sender from retransmitting packets that have already been received correctly, which would otherwise prevent the sender's window from moving forward.

#### 76. Why is it important that QUIC is implemented as an application-layer protocol?
**Answer:**
It allows for faster updates and changes compared to TCP or UDP, which have longer update cycles tied to operating systems.

#### 77. Why should the TCP retransmission timeout interval be larger than the estimated round-trip time (RTT)?
**Answer:**
To avoid premature timeouts and unnecessary retransmissions of segments that are still in transit.


### 🔴 Senior Level

#### 1. Describe the "split-connection" approach in TCP.
**Answer:**
The split-connection approach breaks the end-to-end connection into two parts: one between the mobile host and the wireless access point, and the other from the access point to the communication endpoint.

#### 2. Describe the difference in TCP's response to a triple duplicate ACK event compared to a timeout, and the effect on its transmission rate.
**Answer:**
On a triple duplicate ACK, TCP halves cwnd, adds 3 MSS, sets ssthresh to half the cwnd value at the time of the loss, and enters fast recovery. This cuts the transmission rate in half, after which it increases linearly until the next loss event.

#### 3. How do HTTP/1.1 and QUIC differ in addressing Head-of-Line (HOL) blocking?
**Answer:**
HTTP/1.1 encounters HOL blocking over pipelined TCP connections where a single blocked request halts all subsequent ones. QUIC operates over UDP and allows multiplexing streams independently, avoiding transport-layer HOL blocking.

#### 4. How does QUIC differ from TCP and manage multiple streams?
**Answer:**
QUIC uses UDP as its underlying transport protocol and is designed to provide improved performance, including multiplexing several application-level streams through a single connection to eliminate head-of-line blocking.

#### 5. How does TCP CUBIC improve upon TCP Reno's congestion control mechanism?
**Answer:**
TCP CUBIC increases cwnd based on the cube of the time since the last loss, allowing for a quicker ramp-up to the previous maximum rate before adjusting cautiously.

#### 6. How does the buffer size requirement change with multiple TCP flows?
**Answer:**
For many independent TCP flows, the buffer requirement scales with the aggregate traffic, often expressed as B = RTT × C / √N.

#### 7. How is the TCP timeout interval derived?
**Answer:**
It is calculated using EstimatedRTT (exponentially weighted moving average of round-trip time) and DevRTT (delay variance measurement).

#### 8. In Selective Repeat (SR), what can occur if the sender and receiver do not synchronize their views of packet acknowledgment?
**Answer:**
The sender may retransmit packets that have already been received correctly due to window state discrepancies, causing inefficiencies.

#### 9. What action does a TCP sender take upon detecting three duplicate ACKs?
**Answer:**
It immediately performs a fast retransmit of the lost segment and enters the fast recovery state to maintain throughput.

#### 10. What actions does a TCP sender take upon receiving a congestion indication through ECN (Explicit Congestion Notification)?
**Answer:**
The sender halves its congestion window and sets the Congestion Window Reduced (CWR) bit in the header of the next TCP segment.

#### 11. What are some approaches to improve TCP performance in wireless environments?
**Answer:**
Approaches include local recovery protocols, TCP sender awareness of wireless links, and split-connection techniques.

#### 12. What are some strategies implemented to improve congestion control in data centers?
**Answer:**
Data center-specific TCP variants and Remote Direct Memory Access (RDMA) technologies.

#### 13. What complications can arise from packet reordering in network communications?
**Answer:**
Old or delayed copies of packets can reappear with overlapping sequence numbers, leading to ambiguity, state corruption, or improper handling by the transport/application layer receiver.

#### 14. What critical flaw exists in the rdt2.0 reliable data transfer protocol?
**Answer:**
It assumes that ACK and NAK control messages can never be corrupted; it lacks a mechanism to handle corrupted acknowledgement packets.

#### 15. What does DevRTT represent in TCP?
**Answer:**
DevRTT represents the variability of the round-trip time, serving as an EMA (Exponential Moving Average) estimating how much SampleRTT deviates from EstimatedRTT.

#### 16. What happens to the timeout interval when new data or an ACK is received?
**Answer:**
The timeout interval is recalculated based on the most recent EstimatedRTT and DevRTT values.

#### 17. What happens when the receiver's buffer is full and the receive window (rwnd) is zero?
**Answer:**
The sender continues to send segments with one byte of data to inform the receiver of its status, allowing the receiver to eventually update the rwnd value.

#### 18. What is QUIC and how does it relate to UDP?
**Answer:**
QUIC (Quick UDP Internet Connections) is an application-layer transport protocol that runs on top of UDP. It implements advanced transport-layer services such as reliable data transfer, stream multiplexing, and cryptographic security (TLS 1.3 built-in) to improve performance for secure HTTP traffic.

#### 19. What is a commonly studied AQM algorithm?
**Answer:**
Random Early Detection (RED) is one widely studied Active Queue Management (AQM) algorithm used for congestion avoidance in routers.

#### 20. What is one major feature of QUIC that enhances connection establishment?
**Answer:**
It combines connection state establishment with authentication and encryption, requiring fewer round trips than TCP.

#### 21. What is required from the receiver in a Selective Repeat protocol?
**Answer:**
The receiver must individually acknowledge correctly received packets regardless of their arrival order, buffering out-of-order packets until missing preceding packets arrive to deliver an in-order stream to the upper layer.

#### 22. What is the "slow start threshold" (ssthresh) in TCP congestion control?
**Answer:**
The congestion window parameter set to half of the current congestion window (cwnd) when a loss event occurs, marking the transition point from exponential slow start to linear congestion avoidance.

#### 23. What is the difference between the sender's and receiver's views in a TCP connection?
**Answer:**
The sender and receiver may have asynchronous views on what data has been acknowledged and window sizes, as acknowledgments or segments in transit can be delayed, reordered, or dropped.

#### 24. What is the purpose of Explicit Congestion Notification (ECN) in network-assisted congestion control?
**Answer:**
ECN allows routers to mark IP packet headers to signal congestion directly to TCP senders before packet loss actually occurs, enabling proactive adjustment of sending rates.

#### 25. What is the purpose of the fast recovery phase in TCP?
**Answer:**
In fast recovery, cwnd is increased by 1 MSS for every duplicate ACK received until the missing segment is acknowledged, at which point it transitions to congestion avoidance.

#### 26. What is the relationship between a TCP connection's throughput, congestion window size (W), and round-trip time (RTT) in steady-state?
**Answer:**
Throughput is roughly approximated by W / RTT, representing the average rate of data transfer constrained by the congestion window and latency.

#### 27. What is the significance of the initial sequence numbers in the TCP connection establishment process?
**Answer:**
Initial sequence numbers are needed to ensure that both the client and server can track the data flow accurately and to prevent certain types of attacks (like sequence prediction or spoofing).

#### 28. What mechanism is used to ensure packets can be retransmitted correctly without confusion?
**Answer:**
A maximum packet lifetime is assumed to prevent sequence numbers from being reused until any previous packets have expired.

#### 29. What parameters determine the ramp-up speed of cwnd in TCP CUBIC?
**Answer:**
Parameters include Wmax (the size of the congestion window when the last loss occurred) and K (the point in time when cwnd is expected to reach Wmax).

#### 30. What role does the concept of "probing for bandwidth" play in TCP's congestion control?
**Answer:**
TCP "probes" for additional available bandwidth by increasing cwnd until a loss event occurs, thereby optimizing the transmission rate without overwhelming the network.

#### 31. Why is the maximum packet lifetime important in TCP?
**Answer:**
It prevents the reuse of sequence numbers until it is certain that all stray packets with that number are no longer lingering in the network.

#### 32. Why was the QUIC protocol developed?
**Answer:**
To meet the needs of modern applications that require more security and congestion control services than UDP provides, but without the strict head-of-line blocking and rigid feature set of TCP.


## 📂 Category: Transport Layer & Reliable Data Transfer (1 cards)

### 🟡 Mid Level

#### 1. What happens to packets within the sender's window when an ACK is received for a packet?
**Answer:**
If the ACK corresponds to the packet at the send base, the window base is moved forward to the next unacknowledged packet.


## 📂 Category: Transport Layer & TCP Congestion Control (1 cards)

### 🔴 Senior Level

#### 1. What happens to cwnd and ssthresh during a timeout event in TCP?
**Answer:**
On a timeout, cwnd is set to 1 MSS, and ssthresh is updated to half the value of cwnd prior to the loss.


## 📂 Category: Transport Layer & TCP/IP (1 cards)

### 🔴 Senior Level

#### 1. What is the formula for setting the TCP timeout interval and updating EstimatedRTT?
**Answer:**
EstimatedRTT = (1 – α) * EstimatedRTT + α * SampleRTT (α = 0.125 typically). TimeoutInterval = EstimatedRTT + 4 * DevRTT, where DevRTT accounts for RTT variance.


## 📂 Category: Transport Layer (TCP) (3 cards)

### 🟢 Junior Level

#### 1. Why are TCP timers necessary?
**Answer:**
Timers are used to manage retransmissions for lost packets and ensure timely delivery of segments.


### 🟡 Mid Level

#### 1. Why are duplicate packets a concern in TCP, and how are sequence numbers related?
**Answer:**
Duplicate packets can occur due to retransmissions and can confuse the receiver if not managed properly. Sequence numbers are randomly chosen at the start of a TCP connection specifically to prevent confusion between segments from old connections and new connections that might use the same port numbers.

#### 2. Why can frequent creation and closing of sockets impact web server performance?
**Answer:**
It can severely affect performance due to the overhead associated with setting up and tearing down connections, particularly in busy servers.


## 📂 Category: Transport Layer / Congestion Control (3 cards)

### 🟡 Mid Level

#### 1. How does a TCP sender adjust its sending rate dynamically?
**Answer:**
By maintaining and adjusting a congestion window (cwnd) alongside the receiver's advertised window (rwnd). The sender limits unacknowledged data in flight to the minimum of cwnd and rwnd, scaling cwnd up during additive increase/slow start and scaling it down upon detecting packet loss or congestion.


### 🔴 Senior Level

#### 1. How does a router indicate congestion using Explicit Congestion Notification (ECN)?
**Answer:**
A router sets specific bits (e.g., bits 11 and 12 in the Differentiated Services field of the IPv4 header or Traffic Class field in IPv6) to indicate congestion. This mark is mirrored back to the sender by the receiver via TCP ACK segments (using the CWR/ECE flags).

#### 2. Why do traditional TCP congestion control protocols struggle in modern data centers?
**Answer:**
Data center networks feature low-loss, ultra-low latency environments where traditional additive-increase/multiplicative-decrease (AIMD) reacts too slowly or inappropriately to buffer occupancies.


## 📂 Category: Transport Layer / Reliable Data Transfer (4 cards)

### 🟢 Junior Level

#### 1. How does the sender detect a lost packet in rdt3.0?
**Answer:**
By using a timer; if an ACK is not received within a specified time, the sender retransmits the data packet.


### 🟡 Mid Level

#### 1. How does the rdt2.0 protocol ensure reliability over a channel with bit errors?
**Answer:**
By implementing error detection, positive acknowledgments (ACKs), and negative acknowledgments (NAKs).


### 🔴 Senior Level

#### 1. How does the Selective Repeat (SR) protocol deal with packet loss and handle ACKs?
**Answer:**
Each packet has its own timer for retransmission; if a packet times out, only that specific packet is resent. The SR sender marks the acknowledged packet, moves the window forward if the packet's sequence number equals the send base, and transmits any new packets that are now within the window.

#### 2. How does the receiver handle out-of-order packets in rdt2.1?
**Answer:**
It sends a positive acknowledgment for the packet it has received.


## 📂 Category: Transport Layer / TCP (1 cards)

### 🟡 Mid Level

#### 1. Why does TCP double its retransmission timeout (RTO) interval after successive timeouts?
**Answer:**
To implement exponential backoff, preventing the sender from flooding an already congested network with repeated retries.


## 📂 Category: Transport Layer Protocols (3 cards)

### 🟡 Mid Level

#### 1. How is DevRTT calculated?
**Answer:**
DevRTT = (1 – β) * DevRTT + β * |SampleRTT – EstimatedRTT|, with β typically set to 0.25

#### 2. How is the TCP MSS determined?
**Answer:**
The MSS is determined by the largest link-layer frame size minus the TCP/IP header length to ensure it fits within a single link-layer frame.

#### 3. How is the UDP checksum calculated?
**Answer:**
By taking the one's complement of the sum of all 16-bit words in the segment, including the checksum field itself.


## 📂 Category: Virtualization & Mobility (1 cards)

### 🔴 Senior Level

#### 1. What major challenges arise from host mobility and VM migration in network architectures?
**Answer:**
Host mobility requires locating mobile nodes, addressing, and ensuring uninterrupted data routing during handovers. VM migration struggles with standard Ethernet/IP limitations in maintaining active connections across servers.


## 📂 Category: Web Caching (1 cards)

### 🟢 Junior Level

#### 1. Why can web caching reduce costs for institutions?
**Answer:**
By minimizing traffic to external networks, institutions can delay upgrading their bandwidth capacity, thereby saving operational costs.


## 📂 Category: Web Security (1 cards)

### 🟢 Junior Level

#### 1. What is a potential privacy concern associated with cookies?
**Answer:**
Websites can track user behavior and potentially sell collected information to third parties.


## 📂 Category: Web Security & Protocols (1 cards)

### 🟢 Junior Level

#### 1. What happens if a user returns to a website after a long period with respect to cookies?
**Answer:**
The user's browser will still send the Cookie header containing the identification number, allowing the website to recognize the user session.


## 📂 Category: Wireless & Error Control (1 cards)

### 🟡 Mid Level

#### 1. What is included in the cyclic redundancy check (CRC) of an 802.11 frame?
**Answer:**
A 32-bit Frame Check Sequence (FCS) value used for detecting bit errors in the received wireless frame.


## 📂 Category: Wireless & Mobile (1 cards)

### 🔴 Senior Level

#### 1. What are the key challenges in implementing CDMA?
**Answer:**
Key challenges include the careful selection of CDMA codes and managing varying received signal strengths from different senders.


## 📂 Category: Wireless & Mobile Networks (32 cards)

### 🟢 Junior Level

#### 1. What are two common authentication methods used in 802.11 wireless networks?
**Answer:**
MAC address-based access and username/password authentication.

#### 2. What are wireless hosts?
**Answer:**
Wireless hosts are end-system devices that run applications, including smartphones, tablets, laptops, and IoT devices like sensors and appliances.

#### 3. What is the major architectural standard implemented by 4G networks, and what are their typical real-world speeds?
**Answer:**
4G implements Long-Term Evolution (LTE) and offers real-world download speeds of up to 60 Mbps.

#### 4. What is the primary advantage of 4G cellular networks compared to WiFi access points?
**Answer:**
4G networks provide pervasive wide-area coverage, allowing users to access the Internet continuously, even while on the move across vast distances.

#### 5. What mechanism does 802.11 use to confirm the successful receipt of a data frame?
**Answer:**
Link-layer acknowledgments.

#### 6. Why is millimeter wave technology not suitable for long-range rural deployments?
**Answer:**
It has a much shorter range, requiring denser deployments primarily suited for urban areas.


### 🟡 Mid Level

#### 1. How does 4G network connectivity compare with 3G networks?
**Answer:**
4G networks can seamlessly peer with 3G cellular voice/data networks for backward compatibility and interworking.

#### 2. How does 802.11 rate adaptation adjust transmission rates?
**Answer:**
If two frames are sent without acknowledgment, the transmission rate decreases; if 10 consecutive frames are acknowledged, the rate increases.

#### 3. How does a centralized controller discover nearby Bluetooth devices?
**Answer:**
By broadcasting inquiry messages on different frequency channels to find devices within transmission range.

#### 4. How does a mobile device provide its identity to the base station during association?
**Answer:**
By sending its International Mobile Subscriber Identity (IMSI) or a temporarily assigned identifier (like a GUTI/TMSI) to the base station.

#### 5. How does a wireless station (H1) maintain its IP address when roaming between two BSSs?
**Answer:**
If the Basic Service Sets (BSSs) are connected to the same Layer 2 access network (flat subnet without an intervening router boundary), the station can roam between access points while retaining its IP address and maintaining active higher-layer TCP connections.

#### 6. What causes signal interference and what unique challenge does TCP face in wireless networks?
**Answer:**
Interference is caused by competing radio sources and environmental electromagnetic noise. TCP faces the challenge of misinterpreting wireless bit errors or handover losses as network congestion, triggering inappropriate congestion control responses.

#### 7. What characterizes multi-hop, infrastructure-less networks (such as MANETs and VANETs)?
**Answer:**
Nodes must dynamically relay messages across multiple intermediate nodes to reach a destination without a centralized infrastructure, often while mobile.

#### 8. What is the function of a DHCP discovery message in 802.11 wireless networks?
**Answer:**
To obtain an IP address from the local subnet via DHCP after successfully associating with a wireless access point.

#### 9. What is the function of a base station in a cellular network?
**Answer:**
It manages wireless radio resources, coordinates device authentication, allocates resources, and facilitates communication between mobile devices and the core network.

#### 10. What is the primary architecture type used in 4G LTE?
**Answer:**
An all-IP architecture separating the control plane and user plane.

#### 11. What must a mobile node (e.g., H1) do to switch from AP1 to AP2?
**Answer:**
H1 disassociates from AP1 and associates with AP2 while retaining its IP address and ongoing TCP sessions.

#### 12. Why is collision avoidance critical in the 802.11 protocol?
**Answer:**
Because wireless medium contention and hidden terminals mean undetected collisions lead to severe frame loss and wasted transmissions, drastically degrading wireless throughput and performance.

#### 13. Why is handover management critically important in 5G networks?
**Answer:**
Due to the higher density of cells and the demand for low latency in real-time applications.

#### 14. Why is it important for the mobile device to maintain its connection while moving between networks?
**Answer:**
To minimize datagram loss and ensure continuous communication with the correspondent as the device roams.

#### 15. Why is the home network considered a valuable coordination point for mobile devices?
**Answer:**
It serves as a single location for persistent information about the device and facilitates communication while roaming.

#### 16. Why might a handover be initiated from a source base station to a target base station?
**Answer:**
Due to signal deterioration, network congestion, or based on periodic radio measurements of nearby base stations.


### 🔴 Senior Level

#### 1. How does a base station decide to perform a handover?
**Answer:**
By assessing the quality of the signal (e.g., RSSI/RSRP), current cell loads, and other metrics reported from the mobile device and nearby base stations.

#### 2. What architectural commonalities exist between Mobile IP and 4G/5G network architectures?
**Answer:**
Both utilize home networks, foreign networks, home agents, and employ indirect forwarding mechanisms utilizing tunneling for data transmission.

#### 3. What assumption does CDMA make about the signals from multiple senders?
**Answer:**
CDMA assumes that the signals from interfering senders are additive, meaning they can be summed together during transmission.

#### 4. What complicates the handover process when a mobile device roams across multiple provider networks?
**Answer:**
Cross-provider coordination, authentication handshakes, and roaming agreements are required, significantly increasing signaling overhead and latency.

#### 5. What is adaptive modulation and coding in wireless networks?
**Answer:**
A technique that adjusts the modulation scheme and coding rate dynamically based on real-time wireless channel conditions to optimize throughput while maintaining an acceptable Bit Error Rate (BER).

#### 6. What is the function of a foreign agent in Mobile IP?
**Answer:**
A foreign agent advertises mobility services to mobile devices, provides a care-of-address, assists in registering the device with the home agent, and forwards datagrams to the mobile node.

#### 7. What is the outcome after the handover process is complete for a mobile device?
**Answer:**
The target base station begins delivering datagrams to the mobile device and can forward outgoing datagrams to the Serving Gateway.

#### 8. What must the visited network do in relation to the home network's HSS in mobile cellular networks?
**Answer:**
The visited network must register the mobile device's location with the Home Subscriber Server (HSS) for tracking and authentication purposes.

#### 9. Why is careful selection of CDMA codes important?
**Answer:**
Properly orthogonal codes ensure that receivers can mathematically isolate and decode the intended sender's transmitted data stream from combined wireless signals without cross-talk.

#### 10. Why is research ongoing in mobile ad hoc networks (MANETs)?
**Answer:**
Research is focused on developing protocols that manage the challenges of connectivity and routing among mobile nodes in the absence of a fixed infrastructure.


## 📂 Category: Wireless Communications (1 cards)

### 🟢 Junior Level

#### 1. What is path loss in the context of wireless communication?
**Answer:**
Path loss refers to the reduction in signal strength (attenuation) as the distance between the sender and receiver increases.


## 📂 Category: Wireless Networking (3 cards)

### 🟢 Junior Level

#### 1. What is the purpose of the Service Set Identifier (SSID) in a wireless network?
**Answer:**
To identify the access point and enable wireless devices to connect to the correct network.


### 🟡 Mid Level

#### 1. What is the process called when a centralized controller invites Bluetooth clients to join the piconet?
**Answer:**
Bluetooth paging.

#### 2. What is the purpose of the RTS/CTS mechanism?
**Answer:**
To reserve the channel and avoid collisions, especially in scenarios involving hidden terminals.


## 📂 Category: Wireless Networks (74 cards)

### 🟢 Junior Level

#### 1. How can wireless networks be classified based on the number of hops?
**Answer:**
Wireless networks can be classified as single-hop (one direct wireless link to an access point/base station) or multi-hop (packets traverse multiple intermediate wireless nodes to reach a destination).

#### 2. How many active devices can be in a Bluetooth piconet?
**Answer:**
Up to eight active devices.

#### 3. How many non-overlapping channels are there in the 2.4 GHz band, and which are they?
**Answer:**
Three non-overlapping channels: 1, 6, and 11.

#### 4. What analogy is used to describe the functionality of CDMA?
**Answer:**
CDMA is likened to partygoers speaking in multiple languages, where individuals focus on their preferred conversation while filtering out others.

#### 5. What are Bluetooth networks also referred to as?
**Answer:**
Wireless Personal Area Networks (WPANs) or piconets.

#### 6. What are single-hop, infrastructure-less networks?
**Answer:**
These networks lack a base station, but one node may coordinate the transmissions of other nodes, such as in Bluetooth networks.

#### 7. What are some applications enabled by the ubiquity of 4G Internet access?
**Answer:**
HD video streaming, videoconferencing, IoT applications like shared bike and scooter systems, mobile payments, and Internet-based messaging.

#### 8. What are some key characteristics of wireless links?
**Answer:**
Key characteristics include transmission rates and coverage ranges, which can vary based on distance, channel conditions, and user load.

#### 9. What are the implications of wireless networks on application-layer protocols?
**Answer:**
Applications must treat bandwidth as a scarce resource, often leading to less image-rich content for mobile users compared to wired connections.

#### 10. What characterizes single-hop, infrastructure-based wireless networks?
**Answer:**
These networks have a base station connected to a wired network, with all communication occurring over a single wireless hop (e.g., 802.11 Wi-Fi and 4G/5G cellular networks).

#### 11. What connects a user’s mobile device to their home network in a cellular architecture?
**Answer:**
A 4G base station.

#### 12. What distinguishes 5G networks from their 4G predecessors?
**Answer:**
5G networks incorporate advanced technologies to improve speed, capacity, and connectivity compared to 4G.

#### 13. What does "5G NR" stand for?
**Answer:**
5G New Radio.

#### 14. What does a wireless LAN user need to transmit and receive packets in infrastructure mode?
**Answer:**
An access point connected to the enterprise or home network, where hosts connect through a base station providing traditional network services like routing and address assignment.

#### 15. What impact does wireless network mobility have on software application design?
**Answer:**
It enables the creation of location-aware and context-aware applications, significantly enriching user experience and expanding real-time contextual functionality.

#### 16. What is 5G fixed wireless?
**Answer:**
5G fixed wireless is a high-speed Internet access technology that uses wireless data transmission from a provider's base station to a home modem.

#### 17. What is a "WiFi jungle"?
**Answer:**
A physical location where a wireless device receives strong signals from multiple access points.

#### 18. What is a base station in a wireless network?
**Answer:**
A base station is responsible for sending and receiving data between wireless hosts and the larger network, coordinating communication for associated hosts.

#### 19. What is the broadest definition of a mobile device in a wireless network?
**Answer:**
A mobile device is one that changes its point of attachment to the network over time.

#### 20. What is the fundamental building block of an 802.11 wireless LAN architecture?
**Answer:**
The Basic Service Set (BSS), which typically includes one or more wireless stations and a central access point (AP).

#### 21. What is the maximum data rate and range for the 802.11b standard?
**Answer:**
Maximum data rate of 11 Mbps and a range of 30 meters.

#### 22. What is the shared transmission rate for WiFi (IEEE 802.11) today?
**Answer:**
Up to more than 100 Mbps.

#### 23. What is the typical operational transmission range for a user from a wireless LAN access point?
**Answer:**
A few tens of meters.

#### 24. What role do wireless links play in a wireless network?
**Answer:**
Wireless links connect hosts to base stations or other wireless hosts, facilitating communication through various wireless transmission technologies.

#### 25. What technique does Bluetooth use to avoid interference?
**Answer:**
Frequency-Hopping Spread Spectrum (FHSS), changing channels in a pseudo-random manner.

#### 26. Why do some 802.11 standards operate in the 5 GHz frequency band instead of 2.4 GHz?
**Answer:**
To significantly reduce interference from common consumer devices operating in the congested 2.4 GHz band, such as microwaves and Bluetooth devices.


### 🟡 Mid Level

#### 1. Describe how a node indicates it will go to sleep in an 802.11 network.
**Answer:**
The node sets the power-management bit in the header of an 802.11 frame to 1, indicating it will sleep and not receive frames.

#### 2. Describe the initial step H1 takes when moving from BSS1 to BSS2.
**Answer:**
H1 detects a weakening signal from AP1, scans for a stronger signal, and receives beacon frames from AP2.

#### 3. Describe the process a station follows before transmitting a frame in CSMA/CA.
**Answer:**
1. Senses the channel.
2. Waits for a DIFS.
3. If busy, selects a random backoff value and counts down.
4. If the counter reaches zero, transmits the frame.

#### 4. How do 802.11 wireless stations associate with an access point?
**Answer:**
By scanning channels and selecting an AP based on the signal strength and service set identifier (SSID) contained in the periodic beacon frames sent out by the AP.

#### 5. How do RTS and CTS frames function in mitigating the hidden terminal problem in wireless networks?
**Answer:**
An RTS (Request to Send) frame is sent by a node to request channel access, and the CTS (Clear to Send) frame is broadcast by the access point/receiver to reserve the channel, forcing hidden nodes to defer transmission.

#### 6. How do base stations interact among themselves in a cellular network?
**Answer:**
They coordinate to manage the radio spectrum and minimize interference between cells.

#### 7. How do mobile networks interconnect with each other?
**Answer:**
Via the public Internet or an Internet Protocol Packet eXchange (IPX) network.

#### 8. How does an AP handle the conversion between Ethernet and 802.11 frames?
**Answer:**
The AP converts Ethernet frames to 802.11 frames and vice versa, filling in the appropriate address fields as necessary.

#### 9. How does fading affect wireless communication?
**Answer:**
Fading causes signal strength to vary, which can result in undetectable collisions at the receiver, complicating multiple access in wireless networks.

#### 10. How does the RTS/CTS mechanism improve performance in 802.11?
**Answer:**
It reduces the chances of collision by reserving the channel before a longer DATA frame is sent.

#### 11. How does the Radio Link Control (RLC) protocol ensure reliable data transfer?
**Answer:**
By using an ACK/NAK-based Automatic Repeat reQuest (ARQ) protocol.

#### 12. How many address fields does an 802.11 frame contain, and what are they used for?
**Answer:**
Four address fields; typically used for source and destination MAC addresses, and for routing through an access point (AP) and a router interface.

#### 13. How will future 5G networks enhance handover management compared to 4G networks?
**Answer:**
5G networks will be denser with smaller cell sizes, requiring lower handover latency for real-time applications.

#### 14. In the discontinuous reception state, how often does the mobile device wake up to check for transmissions?
**Answer:**
At scheduled intervals, typically several hundred milliseconds apart, to conserve battery power.

#### 15. What applications does URLLC target?
**Answer:**
Highly latency-sensitive applications like factory automation and autonomous driving.

#### 16. What are RTS and CTS frames used for in 802.11?
**Answer:**
RTS (Request to Send) reserves the channel, and CTS (Clear to Send) provides permission for the transmission, helping to mitigate hidden terminal problems.

#### 17. What defines multi-hop, infrastructure-based networks?
**Answer:**
These networks have a base station connected to the larger network, but some wireless nodes relay communication through other wireless nodes.

#### 18. What do the type and subtype fields in the 802.11 frame control field specify?
**Answer:**
They distinguish between different management and control frame types such as association requests, RTS (Request to Send), CTS (Clear to Send), ACK, and data frames.

#### 19. What does eMBB focus on in the context of 5G?
**Answer:**
eMBB (enhanced Mobile Broadband) focuses on increased bandwidth for higher download/upload speeds and moderate latency reduction.

#### 20. What does power management in 802.11 wireless networks aim to achieve?
**Answer:**
It minimizes the time mobile device radio circuitry needs to be actively powered on (e.g., via Doze mode and beacon intervals), extending battery life while buffering frames at the Access Point.

#### 21. What does the Address 2 field in an 802.11 MAC frame represent?
**Answer:**
The MAC address of the station transmitting the frame onto the wireless medium.

#### 22. What does the term "collision-avoidance" imply in 802.11?
**Answer:**
Techniques are implemented to minimize the chances of data frame collisions during transmission in wireless local area networks.

#### 23. What happens during the wakeup process of a node in an 802.11 network?
**Answer:**
The node wakes up just before the AP sends its beacon frame to check for buffered frames.

#### 24. What impact does fading have on the performance of 802.11 wireless networks?
**Answer:**
It can limit the signal ranges of stations and contribute to hidden terminal issues.

#### 25. What information is contained in address 3 of an 802.11 frame?
**Answer:**
The MAC address of the router interface for the subnet.

#### 26. What is a "home network" in the context of mobility management?
**Answer:**
A home network is the cellular provider network that stores subscriber information and supports roaming.

#### 27. What is binary exponential backoff used for in 802.11?
**Answer:**
To choose a random backoff value when the channel is busy, helping to avoid collisions.

#### 28. What is mMTC primarily designed for?
**Answer:**
Massive Machine Type Communications (mMTC) is designed for sensing, metering, and monitoring applications with IoT devices.

#### 29. What is multipath propagation?
**Answer:**
Multipath propagation occurs when portions of an electromagnetic wave reflect off objects, resulting in varying signal paths and blurring of the received signal.

#### 30. What is the hidden terminal problem in wireless networks?
**Answer:**
The hidden terminal problem occurs when two transmitting stations cannot detect each other's signals due to obstructions, leading to potential interference at the receiver.

#### 31. What is the maximum length of the payload in an 802.11 frame?
**Answer:**
Up to 2,312 bytes, though typically it is fewer than 1,500 bytes.

#### 32. What is the purpose of rate adaptation in 802.11 wireless networks?
**Answer:**
Rate adaptation allows dynamic selection of modulation and coding schemes (MCS) based on real-time channel conditions to maintain a low bit error rate (BER) and optimize throughput.

#### 33. What role does the WEP field play in the 802.11 frame?
**Answer:**
It indicates whether encryption is being used for the transmitted frame.

#### 34. What role does the centralized controller play in a Bluetooth piconet?
**Answer:**
It controls the piconet’s clock, frequency hopping, client device entry, and polls clients for permission to transmit.

#### 35. What wireless technologies do 5G and LTE use for spectral efficiency and channel multiplexing?
**Answer:**
5G uses MIMO (Multiple Input Multiple Output) technology to improve spectral efficiency, while LTE uses Orthogonal Frequency Division Multiplexing (OFDM) for downstream channel multiplexing.

#### 36. When is the RTS/CTS exchange typically used in 802.11 networks?
**Answer:**
It is used for longer data frames when the RTS threshold is set above the maximum frame length.

#### 37. Why can't 802.11 wireless networks use collision detection (CSMA/CD) like Ethernet?
**Answer:**
Because wireless devices cannot simultaneously send and transmit signals effectively due to the heavily attenuated received signal strength compared to transmitted power.


### 🔴 Senior Level

#### 1. How does CDMA encode data and partition the communication medium?
**Answer:**
In CDMA, each data bit is multiplied by a unique code (chipping rate) that changes at a faster rate. It partitions the codespace instead of time or frequency, assigning each node a distinct code for communication.

#### 2. How is the capacity of a 5G network defined?
**Answer:**
Capacity = cell density * available spectrum * spectral efficiency.

#### 3. How often can slot (re)allocation occur in LTE?
**Answer:**
As often as once every millisecond.

#### 4. In a CDMA system, how is the output received at the receiver expressed?
**Answer:**
The received signal is the linear superposition (sum) of the transmitted signals from all simultaneous senders, scaled by channel coefficients and separated using orthogonal spreading codes.

#### 5. What are the four major steps involved when a mobile user connects to a visited 4G/5G network?
**Answer:**
1) Base station association, 2) Control-plane configuration, 3) Data-plane configuration, 4) Mobile device handover.

#### 6. What happens during the handover process for a mobile device?
**Answer:**
The device changes its association from one base station to another, which may involve reconfiguring the Serving-Gateway-to-base-station tunnel.

#### 7. What impact does varying received signal strength have on CDMA?
**Answer:**
Variations in received signal strength can complicate the recovery of data, as receivers may struggle to differentiate between signals from different senders.

#### 8. What is Code Division Multiple Access (CDMA)?
**Answer:**
A protocol where each node is assigned a unique code to encode data, allowing simultaneous transmissions.

#### 9. What is the primary issue that arises when multiple Basic Service Sets (BSSs) are deployed within the same IP subnet?
**Answer:**
The challenge of seamless mobility, requiring protocols to handle handoffs so wireless stations can roam between access points without dropping active TCP connections or requiring IP address changes.

#### 10. What is the purpose of scheduling algorithms in cellular networks like LTE?
**Answer:**
To dynamically allocate radio resources and determine which mobile devices can transmit in given time-frequency resource blocks based on instantaneous channel quality and QoS profiles.

#### 11. Which IEEE 802.11 standard introduced centralized scheduling by the access point?
**Answer:**
802.11ax.


## 📂 Category: Wireless Networks & Switching (1 cards)

### 🟡 Mid Level

#### 1. How do switches handle device mobility between different Basic Service Sets (BSSs)?
**Answer:**
Switches automatically update their MAC forwarding tables based on new port locations when a client roams, though rapid mobility can disrupt active transport-layer connections like TCP.


## 📂 Category: Wireless Security (2 cards)

### 🟢 Junior Level

#### 1. Why do packet sniffers pose a security risk in wireless environments?
**Answer:**
In wireless environments, passive sniffers can intercept radio-frequency transmissions over the air, potentially capturing sensitive unencrypted data such as passwords and personal messages.


### 🟡 Mid Level

#### 1. What is the purpose of the RADIUS protocol in 802.11 networks?
**Answer:**
To facilitate communication between the access point and an authentication server for user access.


## 📂 Category: Wireless and Mobile Networks (9 cards)

### 🟢 Junior Level

#### 1. What are the performance metrics of 5G compared to 4G?
**Answer:**
5G offers roughly a 10x increase in peak bitrate and a 10x decrease in latency compared to 4G LTE networks.

#### 2. What happens when a mobile device is connected to a visited network?
**Answer:**
The device is said to be roaming, requiring coordination between the home network and the visited network.


### 🟡 Mid Level

#### 1. What is a handoff or handover in wireless networks?
**Answer:**
Handoff refers to the process where a mobile host changes its point of attachment to the network by disassociating from one base station and associating with a different one when moving out of range.

#### 2. What is the DIFS in the context of 802.11 CSMA/CA?
**Answer:**
DIFS stands for Distributed Inter-frame Space; it is a mandatory short wait period that a station must sense the wireless channel to be idle before attempting to transmit data.

#### 3. What is the difference between passive scanning and active scanning in 802.11 networks?
**Answer:**
Passive scanning involves listening for beacon frames sent periodically by access points (APs). Active scanning involves broadcasting a probe request frame and waiting for probe response frames from APs.

#### 4. What is the first step a mobile device takes when attaching to a visited network?
**Answer:**
The mobile device scans for and associates with a base station (access point or cell tower) in the visited network.

#### 5. What is the significance of the pre-allocation of resources in the handover process?
**Answer:**
It allows the mobile device to quickly associate with the new base station without going through a lengthy base-station association protocol.


### 🔴 Senior Level

#### 1. Describe the sequence of actions that occur after the target base station accepts a handover request.
**Answer:**
The target base station pre-allocates resources, acknowledges the request to the source base station, and the mobile device is informed to switch to the new base station.

#### 2. What happens when a mobile device moves to a new visited network in the context of direct routing?
**Answer:**
Additional mechanisms are needed to ensure the correspondent is informed of the mobile device's new visited network, as the HSS is only queried at the start of the session.

