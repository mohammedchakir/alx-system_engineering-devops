## *Distributed Web Infrastructure:*

<img width="750" alt="Screenshot 2023-12-25 at 15 31 28" src="https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/22ed3e8e-6990-4792-8256-5fab9902a404">


### Description

This architecture features a distributed web infrastructure designed to mitigate traffic on the primary server by offloading some tasks to a secondary, replica server. This is facilitated through a load-balancing server that allocates workload between the primary and replica servers.

### Infrastructure Details

- **Load Balancing Algorithm**: The HAProxy load balancer employs the Round Robin algorithm, which systematically allocates server requests in a sequential and equitable manner, based on server weights. This dynamic approach allows for real-time adjustments in server weighting.
- **Load Balancer Configuration**: The HAProxy facilitates an Active-Passive configuration, differing from Active-Active setups where workloads are evenly distributed across all nodes. In this scenario, not all nodes are concurrently active, with passive nodes ready to take over should the active node become unavailable.
- **Primary-Replica Database Dynamics**: In this setup, the Primary server handles both read and write operations, while the Replica server is limited to read-only tasks. Synchronization occurs following write operations on the Primary server.
- **Application Role of Nodes**: The Primary node manages all write-related tasks for the site, while the Replica node is tasked with read operations, thereby reducing the read load on the Primary node.

### Infrastructure Challenges

- **Single Points of Failure**: Multiple vulnerabilities exist, such as the potential for site dysfunction if the Primary MySQL database is down, affecting site modifications. Additionally, the server hosting the load balancer and the application server linked to the primary database are also critical points.
- **Security Concerns**: Without SSL encryption, data transmission is vulnerable to interception. The absence of firewalls across servers further exacerbates the risk of unauthorized access.
- **Lack of Monitoring**: The absence of a server monitoring system means there is no real-time awareness of each server's status.
