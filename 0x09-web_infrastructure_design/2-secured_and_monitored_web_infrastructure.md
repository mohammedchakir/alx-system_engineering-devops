## *Secured and Monitored Web Infrastructure:*

<img width="754" alt="Screenshot 2023-12-25 at 16 22 10" src="https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/c3055021-6978-4041-bbcf-946047736f9d">


### Description

This architecture encompasses a trio of web servers, characterized by enhanced security, continuous monitoring, and encrypted data transmission.

### Infrastructure Highlights

- **Function of Firewalls**: The firewalls serve as a defensive barrier, shielding the web servers from unauthorized and undesirable network traffic. They act as intermediaries between internal and external networks, selectively obstructing traffic that fails to meet set security criteria.
- **Role of SSL Certificates**: SSL certificates play a crucial role in securing data flow between the web servers and external networks. They thwart man-in-the-middle (MITM) attacks and network eavesdropping, thereby safeguarding sensitive information. These certificates are instrumental in ensuring confidentiality, data integrity, and authentication.
- **Monitoring Client Objectives**: Monitoring clients scrutinize server performance and network interactions. They assess server health, promptly notify administrators of any deviations from expected performance levels, and offer comprehensive metrics on server operations. These tools autonomously verify server accessibility, track response times, and signal various anomalies, including file corruption, security breaches, and other potential complications.

### Infrastructure Challenges

- **SSL Termination at Load Balancer**: Positioning SSL termination at the load balancer results in unencrypted data transmission between the load balancer and web servers, posing a security risk.
- **Single MySQL Server Limitations**: The solitary MySQL server presents scalability challenges and constitutes a single point of failure within the web infrastructure.
- **Homogeneous Server Components**: Uniformity in server components leads to resource competition (CPU, memory, I/O), potentially degrading performance. This setup complicates problem diagnosis and hampers scalability.
