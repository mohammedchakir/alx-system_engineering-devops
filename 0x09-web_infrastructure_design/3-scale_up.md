## *Scaled Up Web Infrastructure:*

<img width="689" alt="Screenshot 2023-12-26 at 01 16 31" src="https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/33b6a4cd-c0a7-457c-91e2-18db833c11a0">


### Description

This enhanced web infrastructure represents an evolved version of the previously detailed setup, found in [this document](2-secured_and_monitored_web_infrastructure.md). In this iteration, all Single Points Of Failure (SPOFs) have been eliminated. Key components, namely the web, application, and database servers, now independently operate on separate GNU/Linux servers. SSL protection extends beyond the load-balancer, with each server's network fortified by firewalls and subject to continuous monitoring.

### Infrastructure Enhancements

- **Dedicated Firewalls for Each Server**: Individual firewalls for each server enhance security, shielding against unauthorized access and undesirable traffic for each component, as opposed to a singular point of defense.

### Infrastructure Challenges

- **Elevated Maintenance Costs**: Segmenting major components across multiple servers necessitates additional expenditures. This includes the initial investment in extra servers and the consequent increase in electricity consumption. The financial implications extend to both purchasing new hardware and sustaining the operational costs of the expanded server array.
