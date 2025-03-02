# Implementing of Slicing-UPF/SMF-UEs in 5G Core Network Deployment

<!-- PROJECT LOGO -->
<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/main/resources/images/FRA-UAS_Logo_rgb.jpg" width="450"/>
</p>

<h1 align="center">Team nyzers</h1>
<p align="center">
    <h3 align="center">Master of Engineering</h3>
    <h3 align="center">Information Technology</h3>
    <h5 align="center">Nabeela Maham (1400502)</h5> 
    <h5 align="center">Saad Jamil (1427200)</h5> 
    <h5 align="center">Zaka Ahmed  (1436851) </h5>
    <h5 align="center">Muhammad Haris (1440274) </h5>
    <h5 align="center">Yatish Sharma (1457597) </h5>
</p>

<a id="toc"></a>


## Table of Contents:
1. [Introduction](Introduction)
2. [Literature Review](Literature_Review)
   2.1 [Overview of Open5GS and 5G Core Networks](Overview_of_Open5GS_and_5G_Core_Networks)
   2.2 [Key Components of Open5GS](Key_Components_of_Open5GS)
    2.2.1 [AMF (Access and Mobility Management_Function)](AMF_(Access_and_Mobility_Management_Function))
    2.2.2 [SMF (Session Management Function)](SMF_(Session_Management_Function))
    2.2.3 [UPF (User Plane Function)](UPF_(User_Plane_Function))
    2.2.4 [NRF (Network_Repository_Function)](NRF_(Network_Repository_Function))
    2.2.5 [PCF (Policy Control Function)](PCF_(Policy_Control_Function))
   2.3 [Why Network Slicing?](Why Network Slicing?)
   2.4 [Role of NFs in Slicing](Why_Network_Slicing?)
   
4. Architecture Overview
   3.1 [Topology Design and Slicing Based on Application](Topology_Design_and_Slicing)
   3.2 [Design Challenges and Limitations](Design_Challenges_and_Limitations)

5. Requirements and Planning
   4.1 [Hardware and Development Requirements](Hardware_and_Development_Requirements)
   4.2 [Milestones and Issues](Milestones_and_Issues)

6. Development and Deployment
   5.1 [Setting Up the Docker Environment](Setting_Up_Docker_Environment)
   5.2 [Repo Clone and Test Deployments](Repo_Clone_and_Test_Deployments)
   5.3 [Creating Multiple NFs](Creating_Multiple_NFs)
   5.4 [PDU Session Creation](PDU_Session_Creation)
   5.5 [Multiple Slicing](Multiple_Slicing)
   5.6 [Completion of Network Architecture](Completion_of_Network_Architecture)
   5.7 [Adding Prometheus and Grafana](Adding_Prometheus_and_Grafana)
   5.8 [Alert Manager](Alert_Manager)
   5.9 [Webhook](Webhook)
   5.10 [Communication b/w Dockers](Communication_between_Dockers)
   5.11 [Python Script and Flask Application](Python_Script_and_Flask_Application)
   5.12 [Deploying Webhook Package under Project Docker](Deploying_Webhook_Package)
   5.13 [cAdvisor](cAdvisor)

7. Management and Orchestration
   6.1 [Adding all NFs in Prometheus](Adding_NFs_in_Prometheus)
   6.2 [Dashboards in Grafana](Dashboards_in_Grafana)
   6.3 [Database Connectivity, Storage, and Processing](Database_Connectivity_Storage_Processing)
   6.4 [Creating an Alert](Creating_an_Alert)
   6.5 [Triggering Alert and Webhook Communication](Triggering_Alert_and_Webhook_Communication)
   6.6 [Python Script Container Deployment](Python_Script_Container_Deployment)
   6.7 [Limitation of Docker Compose](Limitation_of_Docker_Compose)
   6.8 [Docker Swarm and Limitations](Docker_Swarm_and_Limitations)
   6.9 [Restart Policy and Other Policies](Restart_Policy_and_Other_Policies)
   6.10 [Management and Orchestration Workflow](Management_and_Orchestration_Workflow)

8. Testing Script
   7.1 [iperf3 Testing of UEs](iperf3_Testing_of_UEs)
   7.2 [Registering Multiple UEs and Establishing PDU Sessions](Registering_Multiple_UEs_and_Establishing_PDU_Sessions)
   7.3 [Network Slicing Verification](Network_Slicing_Verification)
   7.4 [Packetrusher](Packetrusher)
   7.5 [Performance Testing (Throughput & Latency)](Performance_Testing_Throughput_Latency)
   7.6 [Failure Recovery Test](Failure_Recovery_Test)

9. [Conclusion](Conclusion)
10. [References](References)


## 1. Introduction
This document is a guide on designing, initializing, and verifying a 5G network slice scenario with Open5GS, UERANSIM, and Docker. The overall goal in this project is network slicing, which supports multiple virtual networks on a common 5G infrastructure. The goal is realized with seamless UE (User Equipment) connectivity with Open5GS core network as well as monitoring, automation, scaling, and resiliency.

The document is about 5G network configuration and integration with critical 5G network elements, describing their functions in 5G slicing architecture. The paper also encompasses stepwise deployment instructions, methods of performance evaluation, and methods of optimization to achieve effective allocation of resources, reduced-latency communications, and high reliability. Using Docker as a means of containerized deployment and simulating the interactions with a UE via UERANSIM, this project is intended to develop a scalable and dynamic 5G slicing platform optimized towards real-world deployments.


## 2. Literature Review

### 2.1 Overview of Open5GS and 5G Core Networks
The 5G Core (5GC) is the foundational infrastructure for fifth-generation networks that is marked by a service-based architecture (SBA), which supports high-speed, reduced-latency, and scalable connectivity. In comparison with preceding network generations, 5GC allows network slicing, making it possible for multiple virtual networks on a shared infrastructure with varied usages, such as improved Mobile Broadband (eMBB), Ultra-Reliable Low Latency Communication (URLLC), as well as massive Machine-Type Communication (mMTC). The core network consists of multiple functional blocks, i.e., the Access and Mobility Management Function (AMF), Session Management Function (SMF), User Plane Function (UPF), as well as the Network Repository Function (NRF), which work in tandem with each other to efficiently manage authentication, mobility, as well as data traffic.

Open5GS is an open source 5G and 4G LTE core network implementation that allows researchers, developers, and companies to test and deploy 5G networks in a highly customizable environment. Open5GS supports both non-standalone (NSA) and standalone (SA) 5G architecture, making it a preferred platform for private 5G networks, research labs, and testbeds. Open5GS consists of all necessary core network functions and supports simulating User Equipment (UE) and base stations with UERANSIM. The possibility of containerizing Open5GS with Docker and orchestrating with Kubernetes means that scaling can be highly efficient, making Open5GS a preferred platform in 5G scenarios for network slice testing, network automation, as well as 5G network performance assessment.

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/main/Images/Haris_screenshots/Project%20Network%20Architecture/5gcorenetwork.png" width="450"/>
	 <p align="center">Figure 2.1: 5G Core Network </p>
</p>

## 2.2 Key Components of Open5GS

### 2.2.1 AMF (Access & Mobility Management Function)
The **AMF** is responsible for user equipment (UE) accessibility and mobility in the system. One among its most important responsibilities is:

- **Connection Management & Mobility** → Controls UE registration, connection setup, and mobility during customers cell changes.
- **Authentication Coordination** → Works in coordination with Authentication Server Function (AUSF) to authorize and validate UEs.
- **Security Context Management** → Maintains security parameters for UEs to enable secure communication.

In **Open5GS**, AMF is interacting with other core network entities to offer these services to support seamless connection and handovers in UE.

### 2.2.2 SMF (Session Management Function)
The **SMF** is required to manage session-related contexts with the **User Plane Function (UPF)**

- **Session Initiation, Modifying, and Closing** → Initializes sessions, modifies, and closes in order to transfer data.
- **IP Address Assignment** → assigns IP addresses to UEs to facilitate communication.
- **Policy Enforcer** → Enforces **QoS policies** and applies rules according to policy in the network.

In **Open5GS**, UPF is used in conjunction with SMF to realize efficient handling of session data and policy enforcement.

### 2.2.3 UPF (User Plane Function)
The **UPF** is used as the data plane to handle **user data traffic** between the external data networks and the UE. Core responsibilities:

- **Data Routing & Forwarding** → Routes user traffic in an optimum manner based upon session context.

- **Packet Handling & Inspection of QoS** → Provides appropriate handling of traffic & **enforcement of QoS**.

- **Anchor Point to Mobility** → Offers seamless handovers to maintain continuous sessions in data.

In **Open5GS**, UPF is used to run in ideal synchronization with SMF in order to achieve **minimum delay and ideal transmission**.

### 2.2.4 NRF (Network Repository Function)

The **NRF** is tasked to provide an **NF repository** and to aid in service discovery. 
Among these tasks: 
- **NF Registration** → Allows networking functions to register capabilities and services.
- **Service Discovery** → Enables NFs to **discover** and **interact** dynamically among each other.
- **Load Balance support** → Offers support to forward network traffic to multiple NFs efficiently.
In **Open5GS**, NRF offers an interface to ensure each **core network element is communicating efficiently** to make **service-based architecture (SBA) dynamic** and **scalable**. ---

### 2.2.5 PCF (Policy Control Function)
The **PCF** is responsible for **policy management and policy control** in the core in 5G.
Some among these responsibilities:
- **Policy Decision** → Implements Quality of Service (QoS) policy, consumption policy, and access policy in the network.
- **Session Management Support** → Enables SMF to dynamically apply policy to user sessions.
- **Charging Rules Provisioning** → Defines and applies charging rules for data usage and service prioritization.
In **Open5GS**, PCF also offers an interface to have every core network entity communicating efficiently in an effort to render service-based architecture (SBA) dynamic and scalable just like NRF.

### 2.3 Network Slicing in 5G and Open5GS
Network slicing is one of the most significant features of 5G networks that allows for several virtual networks to operate over a shared physical infrastructure. Every slice represents an individual, end-to-end logical network tailored to specific applications or services. This allows operators to allocate network resources effectively and meet various requirements of different industries, such as IoT, autonomous vehicles, smart cities, and enterprise networks.

Open5GS, an open-source implementation of a 5G core network, supports network slicing by providing support for creating and managing multiple slices with some specific characteristics. The AMF selects the requested slice of the UE, and the SMF assigns the session to the appropriate slice. The UPF (User Plane Function) ensures traffic is channeled in the correct slice, and NRF (Network Repository Function) is responsible for offering slice-related services and their subscription.

A Single Network Slice Selection Assistance Information (S-NSSAI) is used to characterize each network slice, and it consists of two parameters:

**Slice Service Type (SST)** → Specifies the type of service provided by the slice.
**Slice Differentiator (SD)** → Separates additional slices in a provided SST.
The table below outlines average SST values and their applications:

| **SST (Slice Service Type)** | **Service Category** | **Use Cases** |  
|-----------------------------|---------------------|--------------|  
| **1** | Enhanced Mobile Broadband (eMBB) | High-speed internet, video streaming, AR/VR |  
| **2** | Massive Machine-Type Communication (mMTC) | IoT, smart cities, sensor networks |  
| **3** | Ultra-Reliable Low Latency Communication (uRLLC) | Autonomous vehicles, industrial automation |  
| **4** | Private/Enterprise Network | Dedicated enterprise solutions, smart factories | 

In order to implement network slicing in Open5GS, the AMF, SMF, and UPF components must be configured to support multiple slices. Each slice is assigned a specific S-NSSAI in the configuration files (amf.yaml, smf.yaml) such that UEs connect to their own slice based on their subscription and requirements. Additionally, test tools like UERANSIM help validate if UEs are correctly connecting to the intended network slice.

With the help of network slicing, Open5GS allows operators to create flexible, secure, and scalable 5G networks for different use cases. This optimizes resource utilization, quality of service (QoS), and performance, leading to more effective and versatile 5G networks for future growth.
### 2.4 Docker and Containerization for Open5GS

Containerization is a lightweight virtualization method whereby applications are executed within their own segregated environments in order to provide consistency across several deployment platforms. Docker is the most widely used containerization technology that facilitates seamless packaging and execution of applications with all dependencies required. Containerizing Open5GS 5GC components renders the deployment modular and scalable in nature.

With Docker, Open5GS can be executed as a set of isolated Network Functions (NFs) such as AMF, SMF, UPF, and NRF each in its own container. The components are assured isolation from each other, networking is simpler in terms of slicing, and system resource management gets optimized. Even multi-container setups can be established and controlled using Docker Compose, and subsequently, get a full-fledged 5G Core Network up and running in no time.

Using Docker in Open5GS presents several benefits including portability, automation, and scalability. With Docker, operators can dynamically scale different components depending on the load of the network and deploy the services efficiently at the edge and cloud infrastructure. Docker-based installations also make Continuous Integration and Deployment (CI/CD) attainable, hence faster updates and automated testing.

When Open5GS is containerized, every network core function works in its own container. A typical Docker-based Open5GS deployment includes:

| **Container** | **Function** | **Description** |
|----------------------|--------------------------------------------------|-----------------------------------------------------------|
| **open5gs-amf** | Access and Mobility Management Function (AMF) | Manages UE registration, mobility, and authentication. |
| **open5gs-smf** | Session Management Function (SMF) | User session and traffic policy management. |
| **open5gs-upf** | User Plane Function (UPF) | Routes user traffic to external networks. |
| **open5gs-nrf** | Network Repository Function (NRF) | Maintains service registry for network functions. |
| **open5gs-ausf** | Authentication Server Function (AUSF) | Provides authentication services for UEs. |
| **open5gs-udm** | Unified Data Management (UDM) | Handles subscription data and policies. |
| **open5gs-pcf** | Policy Control Function (PCF) | Applies policy and QoS rules to network traffic. |
| **open5gs-mongodb** | Database | Stores subscriber information and fundamental network settings.
| **ueransim-gnb** | gNB (Base Station) | A simulated 5G base station for testing. |
| **ueransim-ue** | User Equipment (UE) | Emulates a cellular device to test networks. |

Several studies have highlighted the impact of containerization on 5G network deployments, emphasizing its use in resource optimization, fault tolerance, and operational efficiency. Compared to the traditional monolithic deployments, a containerized Open5GS system offers greater flexibility and facilitates the integration of network slicing, and hence it is the preferred choice for today's 5G network implementations.

### 2.5 Challenges in Deploying Open5GS in a Virtualized Environment

Deploying Open5GS to a virtualized setup has various issues related to performance, resource allocation, security, and integration. The issues below are the major ones and how they are impacted:

| **Challenge** | **Description** |
|------------------------------|------------------------------------------------------------|
| **Performance Overhead** | Virtualization layers impose **latency** and **reduction of throughput**, causing detrimental real-time packet processing. |
| **Network Latency Problems** | Virtual networks are plagued by **non-deterministic performance**, leading to **packet forwarding delays**. |
| **Resource Allocation** | Ineffective **CPU pinning, memory allocation, and scaling inefficiencies** lead to service bottlenecks. |
| **Integration Complexity** | Issues with compatibility with **UERANSIM, MongoDB, and orchestration tools** lead to deployment challenges.
| **Security and Isolation** | **Data leakage risk, access control risk, and multi-tenant isolation** require strong security. |
| **Scalability Constraints** | Dynamically scaling **network functions** based on traffic variations continues to be problematic.

By overcoming these challenges through better resource management, network acceleration techniques, and proper orchestration, Open5GS can be deployed successfully in a virtualized 5G Core Network.

## 2.3 Why network slicing?

Network slicing is one key feature in **5G networks** and allows for multiple virtual networks to operate on top of a universal underlying network. It accommodates **custom service** for each application, and **more efficient, flexible, and scalable** network management is possible.

### Key Drivers for Network Slicing

| **Reason** | **Description** |
|----------------------|----------------|
| **Efficient Resource Allocation** | Segmenting and differentiating service functions and assigning them exclusive resource without interference optimizes performance. |
| **Service Customization** | Enables operators to provide application-specific connectivity for use in instances such as IoT, autonomous vehicles, and ultra-reliable and low-latency communications (URLLC). |
| **Enhanced Security** | Independent and each one secures security threats as traffic is segmented away from traffic in another slice. |
| **Scalability and Flexibility** | The operators are able to resize and scale slices as and when required for better adaptability. |
| **QoS (Quality of Service) Assurance** | Guarantees some performance metrics like bandwidth, latency, and reliability for different applications.
| **Cost Optimization** | Optimizes telco resource utilization and saves telcos CAPEX and OPEX. |

### Real-World Use Cases

1. **IoT Devices** – A dedicated slice for IoT allows optimized low-power connectivity for smart sensors.
2. **Autonomous Cars** – A dedicated traffic slice optimized for latency gives real-time response.

3. **Smart Cities** – Various slivers target **public safety**, **transportation**, and **medical networks** in unique capacities.

4. **Industrial Automation** – High-reliability cuts provide highly efficient performance for smart factories.

## 2.4 Role of NFs in Slicing


In **5G Core (5GC)**, **Network Functions (NFs)** play a central role in providing **network slicing**. Each **NF** is responsible for some functions in a specific **slice** for optimized **traffic management, resource allotment, and service differentiation**.

### Key Network Functions (NFs) in Network Slicing

| **Network Function (NF)** | **Role in Network Slicing** |
|--------------------------|---------------------------|
| **AMF (Access and Mobility Management Function** | It governs user authentication, mobility, and continuity in sessions across slices.
| **SMF (Session Management Function** | Controls and assigns IP addresses and session resources on a per-slice basis. |
| **UPF (User Plane Function)** | Routes and forwards user traffic in accordance with policies based on slices. |
| **NRF (Network Repository Function** | It is holding a catalog for available NFs and offering service discovery for a specified slice.
| **NSSF (Network Slice Selection Function** | It selects appropriate network slicing based on user/service need.
| **PCF (Policy Control Function** | Defines policies for charging, security, and quality of service (QoS) at a slice level. |
| **AUSF (Authentication Server Function)** | Ensures secure user authentication for each slice. |
| **UDM (Unified Data Management)** | It is used for holding subscribers and permission for accesses. |

### How NF Enable Network Slicing

1. **Slice Registration and Slice Selection**
- When a subscriber is logged in, **NSSF** chooses appropriate slicing based on subscription and service conditions.
- **AMF** maintains mobility and access control in selected slice.

2. **Traffic Routing and Resource Allocation**


- **UPF** forwards traffic based on policies and rules related to slices.

- **SMF** assigns session parameters based on the slice’s QoS requirements.

3. **Security and Authentication** - **AUSF** and **UDM** authenticate a user in a slice and secure information.
4. **Dynamic Policy Enforcing** - **PCF** applies policies such as band limits, priorities, and security policies at a slice level.


## 3. Architecture Overview

### 3.1. Topology Design and Slicing Based on Application
The project implements a 5G Standalone (SA) Core Network with Network Slicing using Open5GS. It consists of multiple logical and physical components orchestrated via Docker to provide flexibility, scalability, and resilience.
<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/main/Images/Yatish-Screenshots/Architecture/2.%205G%20Network-3-3-3.drawio.png" width="450"/>
	 <p align="center">Figure 2.1: 5G Network Architecture</p>
</p>

The 5G Core Slicing architecture is implemented to facilitate multiple virtual networks, also known as network slices, over common 5G infrastructure. The network operator is free to allocate resources as a function of varying application as well as service requirements. The architecture is primarily made up of User Equipment (UE), which is smartphone, IoT sensors, industrial machines; gNB (Next-Generation Node B), which is 5G base station that links UEs with core network; as well as 5G Core Network (5GC) functions that are responsible for connections, authentications, as well as data plane. The functions included in the core network are AMF (Access as well as Mobility Management Function), which is responsible for registration, mobility, as well as session management; SMF (Session Management Function), which is responsible for session policies as well as allocating a network path with suitable user traffic; as well as UPF (User Plane Function), which sends data plane into suitable Data Network (DN).

Network slicing is implemented with the aid of the Network Slice Selection Function (NSSF), which allocates a suitable slice on a UE in terms of slice attributes like Slice Service Type (sst), as well as Slice Differentiator (sd). The slice attributes specify slice attributes compatible with varying use cases. For example, a high-speed internet browsing as well as media streaming optimized slice is eMBB (Enhanced Mobile Broadband), a power-efficient IoT device with minimal data requirement optimized slice is mMTC (Massive Machine-Type Communications), a critical application scenario optimized slice is uRLLC (Ultra-Reliable Low-Latency Communications), which is suitable for autonomous driving as well as remote surgery. Each slice is equipped with a corresponding set of AMF, as well as SMF, as well as UPF, DN, which ensures that traffic is isolated as well as optimized in terms of requirements in terms of bandwidth, as well as latency, as well as reliability.

In an Open5GS 5G network, network slicing is established by specifying the target UE profile with corresponding values of sst and sd. The NSSF maps these values into a corresponding slice, which directs the UE towards a target AMF, which in turn allocates suitable SMF and UPF to establish a connection towards a target Data Network. There can be parallel multiple slices on a common shared infrastructure, making efficient utilization and discrimination in terms of service viable. Network operators can realize customized strategies in Open5GS-based network slicing to meet a variety of different application requirements, with optimized performance and scale in 5G deployments these days.

Below is a tabular representation based on its UE IMSI numbers, its SST, its SD, its Network Slice Type, and its 5G Core elements such as gNB, UPF, AMF, and Data Network (DN).

| **UE IMSI**          | **SST (Slice Service Type)** | **SD (Slice Differentiator)** | **Network Slice Type**                      | **gNB** | **AMF** | **SMF** | **UPF** | **Data Network (DN)** |
|----------------------|---------------------------|-----------------------------|-----------------------------------|--------|------|------|------|----------------|
| 262011234567890     | 1                         | 0x000001                    | eMBB (Enhanced Mobile Broadband) | gNB 1  | AMF 1 | SMF 1 | UPF 1 | Data Network 01 |
| 262011234567891     | 1                         | 0x000002                    | eMBB (Enhanced Mobile Broadband) | gNB 1  | AMF 1 | SMF 1 | UPF 1 | Data Network 01 |
| 262011234567892     | 1                         | 0x000003                    | eMBB (Enhanced Mobile Broadband) | gNB 2  | AMF 1 | SMF 1 | UPF 1 | Data Network 01 |
| 262011234567893     | 2                         | 0x000001                    | mMTC (Massive Machine-Type Communications) | gNB 3  | AMF 1 | SMF 2 | UPF 2 | Data Network 02 |
| 262011234567894     | 2                         | 0x000002                    | mMTC (Massive Machine-Type Communications) | gNB 3  | AMF 1 | SMF 2 | UPF 2 | Data Network 02 |
| 262011234567895     | 2                         | 0x000003                    | mMTC (Massive Machine-Type Communications) | gNB 3  | AMF 1 | SMF 2 | UPF 2 | Data Network 02 |
| 262011234567896     | 3                         | 0x000001                    | uRLLC (Ultra-Reliable Low Latency Communication) | gNB 4  | AMF 2 | SMF 3 | UPF 3 | Data Network 03 |
| 262011234567897     | 3                         | 0x000002                    | uRLLC (Ultra-Reliable Low Latency Communication) | gNB 4  | AMF 2 | SMF 3 | UPF 3 | Data Network 03 |
| 262011234567898     | 3                         | 0x000003                    | uRLLC (Ultra-Reliable Low Latency Communication) | gNB 4  | AMF 2 | SMF 3 | UPF 3 | Data Network 03 |
| 262011234567899     | 4                         | 0x000001                    | Private/Enterprise Network Slice | gNB 5  | AMF 3 | SMF 4 | UPF 4 | Data Network 04 |
| 262011234567900     | 4                         | 0x000002                    | Private/Enterprise Network Slice | gNB 5  | AMF 3 | SMF 4 | UPF 4 | Data Network 04 |
| 262011234567901     | 4                         | 0x000003                    | Private/Enterprise Network Slice | gNB 5  | AMF 3 | SMF 4 | UPF 4 | Data Network 04 |

## Explanation of Columns:
- **UE IMSI** → All devices with a single identity.
- **SST (Slice Service Type)** - Defines network slice type:
  - **1** = eMBB (High-speed data transfer)
  - **2** = mMTC (IoT, energy-efficient devices)
  - **3** = uRLLC (Ultra-low-latency application
  - **4** = Enterprise/Industrial Use case - Private Network Slice-
- **SD (Slice Differentiator)** → Additional identifier to slice-distinguish in a similar SST.
- **Network Slice Category →** The target application (for instance, broadband, IoT, mission-critical, private network).
- **gNB (Base Station)** → The specific base station handling UE connections.
- **AMF (Access Mobility Management Function)** → Responsible for UE authentication, mobility, and also session management.
- **SMF (Session Management Function)** - Controls the session state and assigns users' traffic policies.
- **UPF (User Plane Function)** steers UE (User Equipment) traffic into a corresponding data network.
- **Data Network (DN) →** The destination network that finally terminates UE traffic (for example, public internet, enterprise networks, etc.).

## 3.2. Design Challenges and Limitations

### 1. **Network Slicing Complexity**
   - Implementing 5G core slicing requires sophisticated orchestration and management.
   - Ensuring seamless interoperability between different slices is challenging.
   - Dynamic allocation and reallocation of network resources increase complexity.

### 2. **Security and Isolation Risks**
   - While slices are logically separated, vulnerabilities in one slice could impact others.
   - Ensuring complete isolation between slices for critical applications (e.g., healthcare, autonomous vehicles) remains a challenge.

### 3. **Performance Overhead**
   - Slicing introduces additional processing and signaling overhead.
   - Maintaining low latency while managing multiple slices is complex.

### 4. **Scalability Issues**
   - The increasing number of UEs and services demands efficient scaling mechanisms.
   - The orchestration of numerous slices with different QoS requirements is resource-intensive.

### 5. **Resource Allocation Challenges**
   - Efficiently allocating compute, storage, and network resources per slice is difficult.
   - Over-provisioning wastes resources, while under-provisioning leads to service degradation.

### 6. **Interoperability with Legacy Networks**
   - Ensuring smooth interaction with existing 4G LTE and non-standalone 5G networks.
   - Differences in network architectures and protocols create compatibility issues.

### 7. **Regulatory and Standardization Challenges**
   - Variations in regulatory policies across regions impact network slicing deployment.
   - Lack of universal standards may lead to vendor lock-in and fragmentation.

### 8. **Cost and Deployment Complexity**
   - Deploying and maintaining a sliced 5G core network involves significant cost.
   - Small network operators may struggle with investment and operational expertise.

These challenges highlight the key considerations in designing and deploying an efficient 5G core slicing architecture.


## Minimum Hardware Requirements  

| Component       | Minimum Requirement   | Recommended Requirement |
|----------------|----------------------|-------------------------|
| **CPU**        | x86_64, 4 Cores       | At least 8 Cores       |
| **RAM**        | 8GB                   | 16GB or more           |
| **Storage**    | 50GB SSD              | NVMe SSD (256GB+)      |
| **Network**    | NIC at 1 Gbps         | NIC at 10 Gbps         |
| **GPU (Optional)** | Not required, but recommended for AI-based surveillance |

## Programming Languages for Orchestration  
- **Python** – For scripting, automation, and API integration  
- **Bash/Shell Scripting** – For deployment, automation, and configuration  

## Local Software Requirements  
- **Database Management**: `db-desktop` (For subscriber database maintenance)  
- **Containerization**:  
  - Docker & Docker Compose (For managing and deploying network services)  
  - Kubernetes (Optional, for large-scale network slicing and orchestration)  

## Network Tools  
- **iperf3** – For network performance testing and bandwidth measurement  
- **Prometheus** – For real-time monitoring of network functions  
- **Grafana** – For visualizing network statistics and performance metrics  

These requirements ensure optimal performance, scalability, and efficient orchestration of the 5G core slicing architecture.


### 4.2. Milestones and Issues

### Milestones  

The project was structured into key milestones, each contributing to the successful implementation of 5G core slicing.  

#### **Milestone 1: Project Understanding**  
- **Tasks Completed:**
  - Setup GitHub repository and navigated project requirements.
  - Studied deployment templates and network slicing architecture.
  - Understood 5G slicing concepts and functions.  

#### **Milestone 2: Research**  
- **Tasks Completed:**
  - Researched 5G core slicing, UPF, and SMF.
  - Studied network slicing and orchestration principles.  

#### **Milestone 3: Environment Setup**  
- **Tasks Completed:**
  - Installed and configured Linux VMs.
  - Set up Docker, Docker Compose, and Kubernetes.
  - Installed Open5GS, WebUI, and UE simulation tools.  

#### **Milestone 4: Deploy Open5GS Core**  
- **Tasks Completed:**
  - Deployed Open5GS core network with an initial network slice.
  - Configured key network components and validated functionality.
  - Updated documentation and realigned project goals.  

#### **Milestone 5: Deploy UERANSIM**  
- **Tasks Completed:**
  - Deployed and integrated UERANSIM for UE connectivity.
  - Ensured connectivity between UERANSIM and Open5GS core.  

#### **Milestone 6: Simulate UEs & Expand Network Slices**  
- **Tasks Completed:**
  - Registered multiple UEs and tested network slicing.
  - Configured multiple UPF instances for different slices.
  - Scaled network slices based on S-NSSAI requirements.  

#### **Milestone 7: Testing and Performance Validation & Documentation**  
- **Tasks Completed:**
  - Measured throughput and latency for each slice.
  - Monitored UE registration and PDU session performance.
  - Created detailed documentation and final project presentation.  

#### **Milestone 8: Management and Orchestration**  
- **Tasks Completed:**
  - Integrated orchestration logic with Docker for automated slice management.
  - Developed a complete architecture for dynamic slice allocation.  
 
---

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/main/Images/Haris_screenshots/Milistones/Milistone.png" width="1050"/>
	 <p align="center">Figure 6.9:Milistones</p>
</p>

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/main/Images/Haris_screenshots/Milistones/Issues.png" width="1050"/>
	 <p align="center">Figure 6.9: Issue with an Milistones</p>
</p>

### Issues and Resolutions  

The following challenges were encountered and addressed during the project:  

| **Issue** | **Description** | **Resolution** |  
|-----------|----------------|---------------|  
| **Network Connectivity Issues** | UEs failed to register with Open5GS. | Debugged configuration files and adjusted APN settings. |  
| **UERANSIM Integration Challenges** | Packet loss and unstable connectivity. | Tuned network parameters and ensured compatibility with Open5GS. |  
| **Slice Isolation Problems** | UEs connected to incorrect slices. | Implemented precise mapping between UEs and S-NSSAI identifiers. |  
| **High Latency in Some Slices** | Performance inconsistencies observed. | Optimized UPF routing and improved network resource allocation. |  
| **Orchestration Automation** | Manual management was inefficient. | Integrated Docker-based orchestration for dynamic slice management. |  

This structured approach ensured smooth project execution, overcoming challenges while meeting all key milestones.  

  
## 5. Development and Deployment 
This section will detail step-by-step deployment of the 5G slicing system.

### 5.1. Setting Up the Docker Environment
- Install Docker and Docker Compose on your system.
- Ensure Docker daemon is running.
- Verify installation using:
  ```
   docker --version
   docker-compose --version

 - Configure necessary environment variables and required permissions.

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/main/Images/Zaka_Screenshoots/1.%20Docker%20build%20%26%20Installation/Docker%20Installated.png" width="1050"/>
	 <p align="center">Figure 5.1: Docker Installation </p>
</p>
   
### 5.2. Repo Clone and Test Deployments
 - Clone the repository:
   ```
   git clone https://github.com/Borjis131/docker-open5gs.git
   cd docker-open5gs
 - Deploy a test container to verify setup:
   ```
   docker compose -f compose-files/network-slicing/docker-compose.yaml --env-file=.env up -d
 - Check running containers:
   ```
   docker ps

   <p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/main/Images/Zaka_Screenshoots/2.%20Containers%20Build%20%26%20Running%20Basic/docker%20desktop%20images%20.png" width="1050"/>
	 <p align="center">Figure 5.2: Docker Desktop </p>
</p>
     

## 5.3. Creating Multiple Network Functions (NFs)  

To enable multiple slices, additional Network Functions (NFs) such as **SMFs** and **UPFs** are required to handle the traffic for different slices. Each NF instance operates independently, serving a specific slice.  

The following **YAML configuration** defines **SMF2** as a separate NF instance with its own configuration file and container:  

### YAML Breakdown  

```yaml
smf2:
  container_name: slicing-upf_smf_ues-smf-2  # Unique container name for SMF instance
  image: "ghcr.io/borjis131/smf:${OPEN5GS_VERSION}"  # Docker image reference
  command: "-c /etc/open5gs/custom/smf2.yaml"  # Custom configuration file
  networks:
    open5gs:
      aliases:
        - smf2.open5gs.org  # Alias for internal DNS resolution
  configs:
    - source: smf2_config  # Configuration source
      target: /etc/open5gs/custom/smf2.yaml  # Target location inside the container
  depends_on:
    - nrf  # Ensures NRF is active before starting SMF
    - upf2  # Ensures UPF is active before starting SMF


### 5.4. Modifying MCC and MNC 

As part of our setup, we updated the Mobile Country Code (MCC) and Mobile Network Code (MNC) to 262-01, based on the professor’s(project) requirements. The MCC (262) corresponds to Germany, and the MNC (01) is typically assigned to a specific mobile network operator. These values are crucial as they define the identity of our network within the 5G core and ensure proper registration and connectivity of UEs.

By adjusting these parameters, we ensured that our test environment aligns with the required specifications, allowing for accurate testing and validation of network functions. This change is especially important for simulating real-world scenarios and ensuring compatibility with other components in the Open5GS setup.

# MCC and MNC Configuration

| **Parameter** | **Value** | **Description** |
|--------------|----------|----------------|
| **MCC**      | 262      | Mobile Country Code (Germany) |
| **MNC**      | 01       | Mobile Network Code (Operator-Specific) |



### 5.5. PDU Session Creation

A PDU session is required to establish connectivity between the UE (User Equipment) and the 5G Core network. The session setup process involves several steps, including UE registration, authentication, and session establishment.

#### **Steps to Establish a PDU Session**
1. UE scans and selects the PLMN (`262/01`).
2. UE registers with the AMF (Access and Mobility Management Function).
3. The SMF (Session Management Function) establishes the PDU session.
4. The network assigns an IP address to the UE.
5. The session is validated through logs.

#### **Sample Logs from UERANSIM**
```logs
2025-03-01 16:28:32 UERANSIM v3.2.6
2025-03-01 16:28:32 [2025-03-01 15:28:32.980] [nas] [info] UE switches to state [MM-DEREGISTERED/PLMN-SEARCH]
2025-03-01 16:28:33 [2025-03-01 15:28:33.030] [rrc] [debug] New signal detected for cell[1], total [1] cells in coverage
2025-03-01 16:28:33 [2025-03-01 15:28:33.151] [nas] [info] Selected plmn[262/01]
2025-03-01 16:28:33 [2025-03-01 15:28:33.151] [rrc] [debug] New signal detected for cell[2], total [2] cells in coverage
2025-03-01 16:28:35 [2025-03-01 15:28:35.472] [rrc] [info] Selected cell plmn[262/01] tac[1] category[SUITABLE]
2025-03-01 16:28:35 [2025-03-01 15:28:35.473] [nas] [info] UE switches to state [MM-DEREGISTERED/PS]
2025-03-01 16:28:35 [2025-03-01 15:28:35.473] [nas] [info] UE switches to state [MM-DEREGISTERED/NORMAL-SERVICE]
2025-03-01 16:28:35 [2025-03-01 15:28:35.473] [nas] [debug] Initial registration required due to [MM-DEREG-NORMAL-SERVICE]
2025-03-01 16:28:35 [2025-03-01 15:28:35.475] [nas] [debug] UAC access attempt is allowed for identity[0], category[MO_sig]
2025-03-01 16:28:35 [2025-03-01 15:28:35.475] [nas] [debug] Sending Initial Registration
2025-03-01 16:28:35 [2025-03-01 15:28:35.501] [rrc] [debug] Sending RRC Setup Request
2025-03-01 16:28:35 [2025-03-01 15:28:35.507] [nas] [info] UE switches to state [MM-REGISTER-INITIATED]
2025-03-01 16:28:35 [2025-03-01 15:28:35.525] [rrc] [info] RRC connection established
2025-03-01 16:28:35 [2025-03-01 15:28:35.529] [rrc] [info] UE switches to state [RRC-CONNECTED]
2025-03-01 16:28:35 [2025-03-01 15:28:35.529] [nas] [info] UE switches to state [CM-CONNECTED]
2025-03-01 16:28:36 [2025-03-01 15:28:36.302] [nas] [debug] Authentication Request received
2025-03-01 16:28:36 [2025-03-01 15:28:36.502] [nas] [debug] Security Mode Command received
2025-03-01 16:28:36 [2025-03-01 15:28:36.504] [nas] [debug] Selected integrity[2] ciphering[0]
2025-03-01 16:28:36 [2025-03-01 15:28:36.725] [nas] [debug] Registration accept received
2025-03-01 16:28:36 [2025-03-01 15:28:36.727] [nas] [info] UE switches to state [MM-REGISTERED/NORMAL-SERVICE]
2025-03-01 16:28:36 [2025-03-01 15:28:36.732] [nas] [debug] Sending Registration Complete
2025-03-01 16:28:36 [2025-03-01 15:28:36.733] [nas] [info] Initial Registration is successful
2025-03-01 16:28:36 [2025-03-01 15:28:36.738] [nas] [debug] Sending PDU Session Establishment Request
2025-03-01 16:28:36 [2025-03-01 15:28:36.753] [nas] [debug] UAC access attempt is allowed for identity[0], category[MO_sig]
2025-03-01 16:28:36 [2025-03-01 15:28:36.922] [nas] [debug] Configuration Update Command received
2025-03-01 16:28:37 [2025-03-01 15:28:37.131] [nas] [debug] PDU Session Establishment Accept received
2025-03-01 16:28:37 [2025-03-01 15:28:37.134] [nas] [info] PDU Session establishment is successful PSI[1]
2025-03-01 16:28:38 [2025-03-01 15:28:38.378] [app] [info] Connection setup for PDU session[1] is successful, TUN interface[uesimtun0, 10.45.0.5] is up.


### 5.6. Multiple Slicing

Network slicing allows different types of traffic to be handled using separate logical networks within the same physical infrastructure. This ensures optimized performance for different use cases such as enhanced mobile broadband (eMBB), ultra-reliable low-latency communications (URLLC), and massive machine-type communications (mMTC).

#### **Steps to Implement Network Slicing**
1. **Modify Configuration Files**  
   - Define network slices in the `smf` and `amf` configuration files.  
   - Assign slices to specific traffic types (eMBB, URLLC, mMTC).  
   
2. **Deploy and Verify Slicing**  
   - Restart the network functions after updating the configurations.  
   - Use the following command to access the network function (NF) container and verify the slicing setup:  
   ```bash
   docker exec -it <nf-container> sh

### 5.7. Completion of Network Architecture (iperf3)
  Installation of IPERF3 and then show the output of the amf and other communicating with iperf3. 
  

### 5.8. Adding Prometheus and Grafana
  - Install Grafana and configure it to visualize Prometheus data.

'amf sessions'
   ```bash
amf_session{instance="amf1.open5gs.org:9090", job="amf1"}
```

'gnb sessions on AMF'
   ```bash
{__name__="gnb", instance="amf1.open5gs.org:9090", job="amf1"}
```

'AMF Authentication task'

   ```bash
fivegs_amffunction_amf_authreq{job="amf1"}
```

'PCF successful Policies'

   ```bash
fivegs_pcffunction_pa_policysmassosucc
```

'Active UEs in SMF'
   ```bash
{__name__="ues_active", instance="smf1.open5gs.org:9090", job="smf1"}

 ```   
    
### 5.9. Alert Manager

Deploying Alert Manager discuss little bit about alert manager

```yaml
alertmanager:
   container_name: alertmanager
   image: prom/alertmanager:v0.25.0
   deploy:
      mode: replicated
      replicas: 1  # Initial replicas
   networks:
    open5gs:
      aliases:
        - alertmanager.open5gs.org
   volumes:
    - /Users/zakaahmedchishti/Downloads/docker-open5gs-main/configs/slicing-upf_smf_ues/:/etc/alertmanager
   ports:
    - "0.0.0.0:9093:9093/tcp"
   depends_on:
      - prometheus
      - webhook  
```
      
# WebUI Service Configuration (YAML)

This section provides an overview of the `webui` service configuration using YAML within a Docker Compose setup. YAML (Yet Another Markup Language) is widely used for configuration files due to its readability and support for complex data structures.

---

## YAML Configuration

```yaml
 webui:
    container_name: webui
    image: "webui:${OPEN5GS_VERSION}"
    deploy:
      mode: replicated
      replicas: 1  # Initial replicas
      restart_policy:
        condition: on-failure
      update_config:
        parallelism: 1
        delay: 10s
    restart: always
    environment:
      - DB_URI=mongodb://db.open5gs.org/open5gs
      - PORT=9999
      - HOSTNAME=0.0.0.0
      - NODE_ENV=dev
      - COMPOSE_PROJECT_NAME=slicing-upf_smf_ues
    command: "run dev"
    networks:
      open5gs:
        aliases:
          - webui.open5gs.org
    ports:
      - "0.0.0.0:9999:9999/tcp"
    depends_on:
    - prometheus


### **5.10. Network Testing tools installations (iperf3 etc.)**

For our project, we have installed various network testing tools such as mgen, iperf3, and flowgrind. These tools help in evaluating network performance, generating traffic, and analyzing slicing efficiency. The installation process is simple and quick.

```bash
sudo apt update && sudo apt install -y flowgrind
sudo apt update && sudo apt install -y iperf3
sudo apt update && sudo apt install -y mgen
```
To avoid repetitive installations, we have added these tools directly to our local Docker containers. This ensures that every container has the necessary dependencies for testing. Below is an example of how we included them in our Dockerfile:

```bash
RUN apt-get update && apt-get install -y \
    libgnutls28-dev libgcrypt-dev libtalloc-dev \
    libnghttp2-dev libmicrohttpd-dev libcurl4-gnutls-dev \
    libyaml-dev libsctp-dev ethtool iperf3
```


### 5.12. Deploying Webhook Package under Project Docker
 We have integrated our python code for Orchestration also inside the container. So that as soon as webhook receives an alert. It will trigger our python script to scale. 
 
```bash
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    lsb-release \
    gnupg \
    && echo "Docker installation started at $(date)" \
    && curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh get-docker.sh \
    && rm get-docker.sh \
    && curl -L "https://github.com/docker/compose/releases/download/v2.6.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && echo "Docker installation completed at $(date)"

WORKDIR /app

# Copy the Flask webhook script into the container
COPY webhook_listener.py /app/webhook_listener.py

RUN echo "Flask and requests installation started at $(date)" \
    && pip install Flask requests \
    && echo "Flask and requests installation completed at $(date)"

# Expose the port the webhook service will listen on
EXPOSE 5001

# Define the command to run when the container starts
CMD ["sh", "-c", "echo 'nameserver 8.8.8.8' > /etc/resolv.conf && \
    echo 'nameserver 8.8.4.4' >> /etc/resolv.conf && \
    python /app/webhook_listener.py"]

```
As we discussed our webhook_listener script under the Orchestration part. 


### 5.13. cAdvisor
  We have faced the challenge of monitoring all container's system utilization. so we have added a cadvisor. To better monitor the performance of our Docker containers, such as the AMF and other NFs, we have integrated cAdvisor into the system. cAdvisor provides real-time metrics on container performance, including CPU utilization, memory usage, and network statistics. By using cAdvisor, we can easily track how much CPU each container is consuming, ensuring that the resources are being efficiently utilized and identifying any potential performance bottlenecks.

This integration allows us to continuously monitor the health of the containers and make adjustments if any container, like AMF, is consuming more resources than expected. It’s a valuable tool for maintaining optimal system performance and ensuring the stability of our network slicing and other services running within Docker containers.
```yaml
cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    container_name: cadvisor
    networks:
      - open5gs
    ports:
    - 8080:8080
    volumes:
    - /:/rootfs:ro
    - /var/run:/var/run:rw
    - /sys:/sys:ro
    - /var/lib/docker/:/var/lib/docker:ro
    depends_on:
    - redis

  redis:
    image: redis:latest
    container_name: redis
    ports:
    - 6379:6379

```
    
# **6. Orchestration and Management**

Efficient management and orchestrating are essential for **network slicing** in a dynamic manner in Open5GS. The following explains how **monitoring, alerting, and automation** are being managed based on **Prometheus, Grafana, and Docker** in achieving good performance and availability.


## **6.1. Summing up whole Network Functions (NFs) in Prometheus**
Prometheus is used for capturing and holding real-time metrics for Open5GS entities. The inner functions in Open5GS (AMF, SMF, UPF, NRF) are configured to expose CPU usage, active sessions, and network-related information. The metrics are periodically scraped from a configuration file in `prometheus.yaml`. The information is stored in Prometheus for real-time surveillance and analysis. 

Here is our 'Prometheus.yaml' configuration.

```yaml
scrape_configs:
  - job_name: amf1
    static_configs:
      - targets: ["amf1.open5gs.org:9090"]
  - job_name: pcf
    static_configs:
      - targets: ["pcf.open5gs.org:9090"]
  - job_name: smf1
    static_configs:
      - targets: ["smf1.open5gs.org:9090"]
  - job_name: smf2
    static_configs:
      - targets: ["smf2.open5gs.org:9090"]
  - job_name: smf3
    static_configs:
      - targets: ["smf3.open5gs.org:9090"]
  - job_name: smf4
    static_configs:
      - targets: ["smf4.open5gs.org:9090"]
  - job_name: upf1
    static_configs:
      - targets: ["upf1.open5gs.org:9090"]
  - job_name: upf2
    static_configs:
      - targets: ["upf2.open5gs.org:9090"]
  - job_name: upf3
    static_configs:
      - targets: ["upf3.open5gs.org:9090"]
  - job_name: upf4
    static_configs:
      - targets: ["upf4.open5gs.org:9090"] 
  - job_name: gnb1
    static_configs:
      - targets: ["gnb1.ueransim.org:9090"]
  - job_name: amf2
    static_configs:
      - targets: ["amf2.open5gs.org:9090"]
  - job_name: nssf
    static_configs:
      - targets: ["nssf.open5gs.org:9090"]
  - job_name: nrf
    static_configs:
      - targets: ["nrf.open5gs.org:9090"]
  - job_name: amf3
    static_configs:
      - targets: ["amf3.open5gs.org:9090"]
  - job_name: cadvisor
    static_configs:
      - targets: ["cadvisor:8080"]
   ```
We have access to all (amf, smf, upf) which are defined in our topology. As well as cadvisor, nrf other important components. Here we have shown the connection with Prometheus in the below screenshot. As we know it's still in the development process so, it doesn't support all functions of open5gs as stated on their webpage. The port:9090 is used by the NFs to send data to the Prometheus. 

## **6.2. Dashboards in Grafana**
Grafana is used for 'Prometheus' visualizations and real-time monitoring. These are the following dashboards, we have created multiple dashboards to visualize our Prometheus data. Which include data received from (amf, upf, pcf, smf, cadvisor).Here are details of the included dashboards:  

   - 'AMF Dashboard': This dashboard includes AM Initial Registration requests, AMF Authentication requests, AMF Active gnodeb's, AMF Actice Sessions.
   - 'PCF Dashboard':This dashboard includes Policy Successful, PCF SM Policy Association requests, PCF Function PA Sessionbr, Policy Asasso Request. 
   - 'SMF Dashboard': This dashboard includes PDU Session Creation Req across all slices, SMF Active Sessions, SMF PDU Session Create requests, and SMF PDU Session Creation Req. 
   - 'UPF Dashboard': This dashboard represent information regarding UPF number of QoS flows (upf1, upf2, upf3) and Alerts that are active on the alert manager.  
   - 'Processor Usage':As, this dashboard includes processor usage of (smf, upf, amf) as well as total docker container receiving. All containers CPU usage, this data mainly collected through cadvisor. 
  

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/cdd2d7e0b481d119b481cd680dbea7075a450636/Images/Zaka_Screenshoots/32.%20Grafana%20Dashboard%20Paremeters%20/Screenshot%202025-02-28%20at%2011.56.03%E2%80%AFPM.png" width="1050"/>
	 <p align="center">Figure 6.8: PCF Dashboard</p>
</p>

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/cdd2d7e0b481d119b481cd680dbea7075a450636/Images/Zaka_Screenshoots/32.%20Grafana%20Dashboard%20Paremeters%20/Screenshot%202025-02-28%20at%2011.56.18%E2%80%AFPM.png" width="1050"/>
<p align="center">Figure 6.9: UPF Dashboard</p>
</p>

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/cdd2d7e0b481d119b481cd680dbea7075a450636/Images/Zaka_Screenshoots/32.%20Grafana%20Dashboard%20Paremeters%20/Screenshot%202025-02-28%20at%2011.58.04%E2%80%AFPM.png" width="1050"/>
<p align="center">Figure 6.10: Processor Usage Dashboard</p>
</p>

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/cdd2d7e0b481d119b481cd680dbea7075a450636/Images/Zaka_Screenshoots/32.%20Grafana%20Dashboard%20Paremeters%20/Screenshot%202025-02-28%20at%2011.56.10%E2%80%AFPM.png" width="1050"/>
<p align="center">Figure 6.11: SMF Dashboard</p>
</p>

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/cdd2d7e0b481d119b481cd680dbea7075a450636/Images/Zaka_Screenshoots/32.%20Grafana%20Dashboard%20Paremeters%20/Screenshot%202025-02-28%20at%2011.55.55%E2%80%AFPM.png" width="1050"/>
<p align="center">Figure 6.11: AMF Dashboard</p>
</p>


## **6.3 Database Connectivity, Storage and Processing**

Database connectivity is mandatory for network-based information such as subscriber information, network slicing profiles, and performance logs. Secure connectivity is mandatory for smooth fetching and storing for authentication, sessions, and analytics.

'Database Connectivity'
- Establish a secure network database for information maintenance and storage.
- Handle subscriber authentication network slicing and performance logs.
- In the below, we show the presented screenshot of information stored on a database.
  
<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/main/Images/Zaka_Screenshoots/16.%20db%20connect%20to%20get%20access%20to%20data/Screenshot%202025-01-12%20at%204.30.41%E2%80%AFPM.png" width="1050"/>
	 <p align="center">Figure 6.8: Database Connectivity</p>
</p>

**Data in the database**
| **Data Type** | **Description** |
|-------------------------|-------------------------------------------------------|
| **Subscriber Data** | Stores IMSI, authentication credentials, and profiles. |
| **Network Slicing Information** | Consists of slicing configurations (SST, SD, policies). |
| **Traffic Logs** | Tracks traffic in and out of UPF and Data Network. | **Monitoring Metrics** | Stores real-time performance data from Prometheus. |

As the important role of Database is that:
- 'Authentication and Handling of Sessions:' The AMF pulls subscriber authentication information out of the database.
- 'Network Slicing Assignment:' The slicing parameters (SST/SD) are fetched when a UE connection request is obtained from the database.*


<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/ba0cc16a4b4bc035496227b0eef0b66aac685002/Images/Zaka_Screenshoots/16.%20db%20connect%20to%20get%20access%20to%20data/Screenshot%202025-03-01%20at%201.16.41%E2%80%AFPM.png" width="1050"/>
	 <p align="center">Figure 6.8: Current Active Sessions db</p>
</p>

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/ba0cc16a4b4bc035496227b0eef0b66aac685002/Images/Zaka_Screenshoots/16.%20db%20connect%20to%20get%20access%20to%20data/.Screenshot%202025-03-01%20at%201.17.22%E2%80%AFPM.png" width="1050"/>
	 <p align="center">Figure 6.8: Subcribers Inforamation</p>
</p>

## **6.4. Creating an Alert Rule**
To enhance the reliability and scalability of the Open5GS core network, we have implemented an alerting system using Prometheus Alert Rules. This setup ensures active reaction to key events in NF's (upf, smf) to prevent service disruptions and optimize resource allocation.

We have created three alerts from which first are our project requirements. First is UPF Scaling Alert (ScaleUPF) monitors the number of UEs registered to AMF2. If the ran_ue metric exceeds 5 UEs for more than 1 minute, an alert is triggered with a critical severity label, instructing the system to scale the UPF instance accordingly. Similarly, the SMF Scaling Alert (ScaleSMF) follows the same principle but triggers when more than 5 UEs are registered for 3 minutes, ensuring the SMF can handle increased session load.

Additionally, a Container Availability Alert (ContainerDown) has been configured to detect container failures. It evaluates the container_last_seen metric, and if a container remains unresponsive for more than 600 seconds (10 minutes), an alert is sent. As scaling and managing is a challenge using docker-compose, we are only using the above alerts which are set on AMF2 and SMF2. As we have introduced a maximum load on the AMF2, SMF2. So, the alert is set only on these NFs to test that the scaling is working. The limitations of docker-compose are discussed below. As the suggested approach is using Kubernetes or docker swarm. 

```yaml
 - name: upf-scaling-alerts
    rules:
      - alert: ScaleUPF
        expr: ran_ue{instance="amf2.open5gs.org:9090"} > 5
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Scale UPF instance"
          description: "More than 3 UEs registered for AMF2. Scale UPF."

  - name: smf-scaling-alerts
    rules:
      - alert: ScaleSMF
        expr: ran_ue{instance="amf2.open5gs.org:9090"} > 5
        for: 3m
        labels:
          severity: critical
        annotations:
          summary: "Scale SMF instance"
          description: "More than 3 UEs registered for AMF2. Scale SMF."

  - name: ContainerAlerts
    rules:
      - alert: ContainerDown
        expr: time() - container_last_seen > 600
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Container is down!"
          description: "The container {{ $labels.name }} has been missing for more than 600 seconds."

 `````


## **6.5. Triggering Notifications and Webhook Communication**

Here we need to understand the alert we have created now needs to be forwarded to the alert manager. Where we can collect and manage alerts from multiple Prometheus instances in a single place. Supports multiple receivers like email, Slack, PagerDuty, or webhooks, allowing flexible notification methods. As in our case we are using 'webhook'. Before reaching alert to the alert manager, alert has three modes shown below (Active, Pending, Firing): 

<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/ba0cc16a4b4bc035496227b0eef0b66aac685002/Images/Zaka_Screenshoots/23.%20Alert%20Firing/Screenshot%202025-03-01%20at%201.21.01%E2%80%AFPM.png" width="1050"/>
	 <p align="center">Figure 6.8: Alert in InActive Mode</p>
</p>


<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/ba0cc16a4b4bc035496227b0eef0b66aac685002/Images/Zaka_Screenshoots/23.%20Alert%20Firing/Screenshot%202025-03-01%20at%201.21.40%E2%80%AFPM.png"/>
	 <p align="center">Figure 6.8: Alert in Pending Mode</p>
</p>


<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/ba0cc16a4b4bc035496227b0eef0b66aac685002/Images/Zaka_Screenshoots/23.%20Alert%20Firing/Screenshot%202025-03-01%20at%201.23.48%E2%80%AFPM.png"/>
	 <p align="center">Figure 6.8: Alert in Firing Mode</p>
</p>


Now next step is the connectivity of Prometheus with the alert manager. We have also deployed an alert manager under the same container stack. 

 
<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/cdd2d7e0b481d119b481cd680dbea7075a450636/Images/Zaka_Screenshoots/19.%20Alert%20Manager%20with%20Prometheus%20Connected/2.%20Alert%20Manager%20Connected.png" width="1050"/>
	 <p align="center">Figure 6.8: Connectivity Between Alert Manager and Promotheus</p>
</p>

The below screenshot shows that after firing an alert alert reached alert manager management. 
 
<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/ba0cc16a4b4bc035496227b0eef0b66aac685002/Images/Zaka_Screenshoots/19.%20Alert%20Manager%20with%20Prometheus%20Connected/Screenshot%202025-03-01%20at%201.26.58%E2%80%AFPM.png" width="1050"/>
	 <p align="center">Figure 6.8: Recieved alerts at Alert Manager</p>
</p>


Once the alert is processed, Alertmanager forwards it to the webhook, which serves as an integration point for external systems. The webhook receives the alert payload in JSON format, containing crucial information such as the alert name, severity level, affected instance, and timestamps. This allows for automated responses, such as dynamically scaling UPF or SMF when the number of registered UEs exceeds the defined threshold, triggering incident response workflows to notify, or updating monitoring dashboards in real time.
Alertmanager enables seamless automation and integration within the Open5GS monitoring framework, ensuring efficient alert handling, quick response to network conditions, and enhanced reliability of the core network infrastructure.

```yaml
receivers:
  - name: "webhook"
    webhook_configs:
      - url: "http://webhook:5001/alert"
        send_resolved: false  # Prevents duplicate alerts when resolved
 `````
As our webhook is accessible at the 'http://webhook:5001/alert' so every request alert comes to the alert manager will be forwarded to the webhook. More details are also discussed in this document according to the requirement. 


## **6.6. Deploying Python Scripts in Containers**
The provided Python script implements a webhook using Flask to handle scaling alerts for Open5GS core network components, specifically the UPF (User Plane Function) and SMF (Session Management Function). When an alert is fired by Prometheus and forwarded to Alertmanager, it is sent to this webhook as a JSON payload containing alert details.Like shown logs of webhook.

The webhook processes incoming alerts asynchronously using a thread pool executor, ensuring scalability and non-blocking execution. Upon receiving a “ScaleUPF” or “ScaleSMF” alert, it dynamically retrieves the current count of running container instances using a Docker command and triggers an appropriate scaling action via Docker Compose. The scaling command instructs Docker Compose to increase the number of UPF or SMF instances while maintaining their operational state. To enhance stability, a short delay is introduced after scaling, allowing the new instances to initialize properly. By integrating this webhook with Alertmanager, automated service scaling is achieved, ensuring the Open5GS network can dynamically adapt to traffic demands. This automation optimizes resource utilization, prevents congestion, and enhances the reliability of the 5G core network, making it highly responsive to real-time network conditions.


```python
from flask import Flask, request, jsonify
import subprocess
import json
import time
import logging
import concurrent.futures

app = Flask(__name__)
docker_compose_file = "/app/Scaling.yaml"

logging.basicConfig(level=logging.INFO)
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

def get_container_count(service_name):
    cmd = f"docker ps --filter 'name={service_name}-' --format '{{{{.Names}}}}' | wc -l"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return int(result.stdout.strip() or 0) if result.returncode == 0 else 0

def scale_service(target_service, new_target_count):
    logging.info(f"Scaling {target_service}: New count -> {new_target_count}")
    scale_command = f"docker-compose -f {docker_compose_file} up -d --scale {target_service}={new_target_count} {target_service}"
    process = subprocess.Popen(scale_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
    stdout, stderr = process.communicate()
    time.sleep(10)

def handle_alert(data):
    if 'alerts' in data:
        for alert in data['alerts']:
            alert_name = alert['labels'].get('alertname')
            if alert_name == 'ScaleUPF':
                executor.submit(scale_service, "upf", get_container_count("upf") + 1)
            elif alert_name == 'ScaleSMF':
                executor.submit(scale_service, "smf", get_container_count("smf") + 1)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    logging.info(f"Received Alert: {json.dumps(data, indent=4)}")
    executor.submit(handle_alert, data)
    return jsonify({"status": "Scaling triggered"}), 200

@app.route('/')
def home():
    return "Scaling Webhook for UPF and SMF is Running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

```
---


This is the logs of webhook running as a flash application under same docker container project as under same network (open5gs). As the webhook is wait for the alert as soon as alert recieved, our the better visibity of the alert we have displayed the alert in the logs of the container. As the firing alert is regarding scaling to scale upf under the amf2. So, Fist out python code get the list of all active container and then check how many active upf are there suppose we have four active upf. then it creates a new upf with the name of 'slicing-upf_smf_ues-upf-5' and active it with the same configation under same network id '10.47.0.0'. Creation of new UPF-5 with dynamic scaling using python script logs shown below:


```logs

2025-03-01 13:20:49  * Tip: There are .env files present. Install python-dotenv to use them.
2025-03-01 13:20:49 INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
2025-03-01 13:20:49  * Running on all addresses (0.0.0.0)
2025-03-01 13:20:49  * Running on http://127.0.0.1:5001
2025-03-01 13:20:49  * Running on http://10.33.33.45:5001
2025-03-01 13:20:49 INFO:werkzeug:Press CTRL+C to quit
2025-03-01 13:23:29 INFO:root:Received Alert: {
2025-03-01 13:23:29     "receiver": "webhook",
2025-03-01 13:23:29     "status": "firing",
2025-03-01 13:23:29     "alerts": [
2025-03-01 13:23:29         {
2025-03-01 13:23:29             "status": "firing",
2025-03-01 13:23:29             "labels": {
2025-03-01 13:23:29                 "alertname": "ScaleUPF",
2025-03-01 13:23:29                 "instance": "amf2.open5gs.org:9090",
2025-03-01 13:20:49  * Serving Flask app 'webhook_listener'
2025-03-01 13:20:49  * Debug mode: off
2025-03-01 13:23:42 slicing-upf_smf_ues-upf-5
2025-03-01 13:23:29                 "job": "amf2",
2025-03-01 13:23:29                 "severity": "critical"
2025-03-01 13:23:29             },
2025-03-01 13:23:29             "annotations": {
2025-03-01 13:23:29                 "description": "More than 3 UEs registered for AMF2. Scale UPF.",
2025-03-01 13:23:29                 "summary": "Scale UPF instance"
2025-03-01 13:23:29             },
2025-03-01 13:23:29             "startsAt": "2025-03-01T12:22:29.362Z",
2025-03-01 13:23:29             "endsAt": "0001-01-01T00:00:00Z",
2025-03-01 13:23:29             "generatorURL": "http://7666dfd5eb35:9090/graph?g0.expr=ran_ue%7Binstance%3D%22amf2.open5gs.org%3A9090%22%7D+%3E+5&g0.tab=1",
2025-03-01 13:23:29             "fingerprint": "f01045c1d01fa02e"
2025-03-01 13:23:29         }
2025-03-01 13:23:29     ],
2025-03-01 13:23:29     "groupLabels": {},
2025-03-01 13:23:29     "commonLabels": {
2025-03-01 13:23:29         "alertname": "ScaleUPF",
2025-03-01 13:23:29         "instance": "amf2.open5gs.org:9090",
2025-03-01 13:23:29         "job": "amf2",
2025-03-01 13:23:29         "severity": "critical"
2025-03-01 13:23:29     },
2025-03-01 13:23:29     "commonAnnotations": {
2025-03-01 13:23:29         "description": "More than 3 UEs registered for AMF2. Scale UPF.",
2025-03-01 13:23:29         "summary": "Scale UPF instance"
2025-03-01 13:23:29     },
2025-03-01 13:23:29     "externalURL": "http://c43610a2cb52:9093",
2025-03-01 13:23:29     "version": "4",
2025-03-01 13:23:29     "groupKey": "{}:{}",
2025-03-01 13:23:29     "truncatedAlerts": 0
2025-03-01 13:23:29 }
2025-03-01 13:23:29 INFO:werkzeug:10.33.33.48 - - [01/Mar/2025 12:23:29] "POST /alert HTTP/1.1" 200 -
2025-03-01 13:23:30 INFO:root:Current container count for upf: 4
2025-03-01 13:23:30 INFO:root:Scaling upf: New count -> 5
2025-03-01 13:23:31 ERROR:root:Failed to scale upf: time="2025-03-01T12:23:31Z" level=warning msg="Found orphan containers ([alertmanager grafana webui webhook ue10 ue12 ue11 ue9 ue15 ue8 ue6 ue13 ue14 ue7 ue1 ue2 ue3 ue5 ue4 prometheus gnb5 gnb3 packetrusher gnb1 gnb2 gnb4 nssf amf3 slicing-upf_smf_ues-smf-4 slicing-upf_smf_ues-smf-1 udm slicing-upf_smf_ues-smf-3 slicing-upf_smf_ues-smf-2 amf2 bsf amf1 ausf udr nrf pcf db cadvisor slicing-upf_smf_ues-upf-3 slicing-upf_smf_ues-upf-2 slicing-upf_smf_ues-upf-4 slicing-upf_smf_ues-upf-1 redis iperf]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up."
2025-03-01 13:23:31 Container slicing-upf_smf_ues-upf-5  Creating
2025-03-01 13:23:31 Container slicing-upf_smf_ues-upf-2  Creating
2025-03-01 13:23:31 Container slicing-upf_smf_ues-upf-3  Creating
2025-03-01 13:23:31 Container slicing-upf_smf_ues-upf-1  Creating
2025-03-01 13:23:31 Container slicing-upf_smf_ues-upf-4  Creating
2025-03-01 13:23:31 Container slicing-upf_smf_ues-upf-5  Created
2025-03-01 13:23:31 Error response from daemon: Conflict. The container name "/slicing-upf_smf_ues-upf-3" is already in use by container "576cc6d2de5655a0bedd8009b38c6fdb002ffac8c59e53cf00dbbcc394f87cd3". You have to remove (or rename) that container to be able to reuse that name.
2025-03-01 13:23:31 
2025-03-01 13:23:41 INFO:root:Current running count for upf: 4
2025-03-01 13:23:41 WARNING:root:Some containers are not running for upf. Attempting to start them.
2025-03-01 13:23:42 INFO:root:Successfully started container slicing-upf_smf_ues-upf-5
```



As the logs shows that new UPF-5 has been created. And running. So, the goal of orchestration or scalability is achieved. But as this is not a good or recommended method of doing orchestration because docker compose only provide manual scaling. And docker compose does'nt provide automatic scaling. But we tried to make it automated. But because involemenet of differenet platform. It's make it complex and non-reliable for major use. It's only good for specific test cases. Well we have also tried docker swarm which is discussed below and also we discussed the limitstions of the docker swarm. 


## 6.7 Management and Orchestration Workflow

This procedure describes the use of **Prometheus, Grafana, and AlertManager** for monitoring and automation in **Open5GS network slicing**.

### Workflow Steps

1. **Metrics Collection**
- `cAdvisor` gathers system resource utilization (CPU, memory, disk).
- Metrics are forwarded to **Prometheus** for storage and analysis.
- **Redis** is utilized for caching temporary data.

2. **Visualization & Alerts**
- **Grafana** requests **Prometheus** for metrics to build dashboards.
- If a measure exceeds a threshold (e.g., high CPU usage), an **alert is raised**.

3. **Automation & Alert Handling** - **AlertManager** handles the alert and triggers a **Webhook notification**.
- A **Python script (running in a Docker container)** processes the webhook and responds to it.
- The script can **restart services, alter resources, or log the problem automatically**.
This arrangement facilitates **automating the management of network slicing** and allows for effective monitoring of **Open5GS**.

### Workflow Diagram

<p align="center">
  <img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/main/Images/Haris_screenshots/Managemnet%20and%20Orchestration/Management%26Orchestration.png" width="800"/>
  <p align="center">Figure 6.1: Management and Orchestration Workflow</p>
</p>


## **6.8. Docker Compose limitations**
In your project we are using Docker Compose, there are several limitations to consider. Docker Compose is designed to run on a single host, limiting its ability to scale across multiple machines, making it less ideal for distributed systems. While we can scale services, 'Docker Compose isn’t as efficient for large-scale deployments' or high availability as Kubernetes or Docker Swarm. It's ideal only for one or two containers creation. The networking model can become complex when managing multiple containers that need to communicate across various networks, and persistent storage for stateful applications can be challenging without careful handling of Docker volumes. Furthermore, Docker Compose doesn’t offer advanced configuration management or fine-grained resource controls, which can be limiting for more complex setups. Centralized logging and service discovery can require third-party tools, and upgrading services may lead to downtime. For larger or production-grade projects, Kubernetes or Docker Swarm would offer more robust solutions.

**limitations**:

| **Limitation** | **Impact on Open5GS** |
|--------------|-----------------|
| **No Built-in Auto-Scaling** | not able to dynamically **scale NFs** based on traffic load. |
| **Single-Host Deployment** | Limited to operating on **one machine**. |
| **Lack of Service Discovery** | need **manual linking of services**. |

For large-scale deployments, **Kubernetes or docker swarm** is proposed.

## **6.9. Docker Swarm and Disadvantages**
We have attempted to use Docker Swarm for orchestration, given its capabilities in multi-container orchestration, scalability, and load balancing for network functions. Docker Swarm would allow us to spread Open5GS components across hosts, balance UE traffic optimally, and perform rolling updates without disrupting services. However, due to the limitations of running Docker Swarm on a single laptop, it has not been feasible to implement. Additionally, the project description also restricts us to using Docker Compose, which, while functional, isn’t the most ideal solution for our needs. Docker Compose lacks the advanced networking features, granularity in resource allocation, and integration options that Docker Swarm or Kubernetes offer, making it less suitable for handling complex, large-scale deployments such as those required for Open5GS. For more advanced network slicing and enhanced orchestration, other solutions need to consider rather than Docker Compose. 


<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/ba0cc16a4b4bc035496227b0eef0b66aac685002/Images/Zaka_Screenshoots/17.%20Docker%20Swam/Screenshot%202025-01-19%20at%204.07.18%E2%80%AFPM.png" width="1050"/>
	 <p align="center">Figure 6.8: Recieved alerts at Alert Manager</p>
</p>


Docker Swarm supports **multi-container orchestration** through:
- **Scalability**: It spreads **network functions** across hosts.
- **Load Balancing**: It balances **UE traffic** optimally.
- **Rolling Updates**: Upgrade Open5GS components **non-disruptively**.

However, it is restricted.
| **Limitation** | **Influence on Open5GS** |
|--------------|-----------------|
| **Less Feature-Rich than Kubernetes** | Lacks **rich networking** features. |
| **No granularity level control** | Cannot reserve **each individual CPU/memory for each slice**.
| **Limited Integrations** | Fewer features for logs and monitoring. |

For advanced network slicing, **Kubernetes** is a superior option.


## **6.9. Restart_policy and Other Policies**
Docker Compose offers several options to ensure the reliability and stability of containers, particularly through restart policies and health checks. These policies help ensure that your services stay up and running, even in the event of failure or unexpected shutdowns. Here’s a breakdown of these options:

Docker’s restart policies control whether a container should automatically restart when it exits or fails. These policies are especially useful for ensuring the availability of critical services like Open5GS components. The key restart policies include:

Docker's **restart policies** ensure reliability for service:

| **Restart Policy** | **Behaviour** |
|--------------|-----------------|
| **Always** | Always restarts the container when it stops, regardless of the exit code. This is useful for long-running services that should always be running. |
| **Unless-Stopped** | Similar to Always, but the container won’t restart if it’s manually stopped. It’s ideal for services you want to run continuously, but with the option to stop them manually without triggering an automatic restart. |
| **On-Failure** | Restarts the container only if it exits with a non-zero exit code (indicating failure). This is useful for situations where you want the container to automatically restart after a failure but not for normal shutdowns.|

In your case, the 'restart: unless-stopped' policy is used to keep containers running unless manually stopped, ensuring the reliability of your services even during unexpected failures.

**Health Checks**

Health checks are another essential feature of Docker Compose that ensure your containerized services are functioning correctly. A health check periodically runs a command to check if the service inside the container is healthy and responsive. If the container fails the health check, Docker can restart it based on the restart policy.
Here’s an example of a health check configuration:

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:9090"]  # Checks if the UPF metrics endpoint is accessible
  interval: 30s  # Time between each health check
  retries: 3     # Number of consecutive failures before marking as unhealthy
  timeout: 10s   # Time to wait for the health check to complete
  start_period: 20s  # Time before starting health checks after container starts
```
In this configuration, the health check ensures that the UPF metrics endpoint (http://localhost:9090) is accessible, and Docker will attempt to restart the container if the health check fails 3 times in a row. The health check also starts after a delay of 20 seconds to allow the service to initialize.



# 7. Testing Script
This Portion describes the running network details, our results how we have achieved the goals, and the test we have conducted to evaluate ourselves. 


### **Open5gs Networks and Containers. 

As 'docker network ls' shows the current available networks and as we are using open5gs as a network under the network ID range '10.33.33.0/24'. and br-ogs specifies a custom name for the bridge network that Docker will create and use for the open5gs network. All container get a dynamic IP in the range of '10.33.33.0'. Which as a example in our case shown in below tables. 

show 'docker network ls'.
```bash
NETWORK ID     NAME                          DRIVER    SCOPE
1bf07b6a35a1   bridge                        bridge    local
8bbc0aab489f   docker_gwbridge               bridge    local
6cf38b6b3cfb   host                          host      local
525bc2c1ea4a   none                          null      local
2598b4048c2a   open5gs                       bridge    local
d2a1781256c4   slicing-upf_smf_ues_default   bridge    local
```

### **Core Network NFs**  
As shown below the dynamic IP assigned by the bridge network. Remember these are dynamic so, it changes again and again on every run. 

| Name   | Container ID        | IPv4 Address | Alias             |
|--------|---------------------|--------------|-------------------|
| amf1   | 1d3f99a12bc3        | 10.33.33.12  | amf1.open5gs.org  |
| amf2   | 2f4e88b2cd44        | 10.33.33.51  | amf2.open5gs.org  |
| amf3   | 3b7c99d1ef55        | 10.33.33.52  | amf3.open5gs.org  |
| ausf   | 0365a941dff0        | 10.33.33.16  | ausf.open5gs.org  |
| nssf   | 475df31241c1        | 10.33.33.14  | nssf.open5gs.org  |
| udm    | 635cc11da8aa        | 10.33.33.15  | udm.open5gs.org   |
| udr    | 917797133a9a        | 10.33.33.13  | udr.open5gs.org   |
| pcf    | 6a4c11e512a9        | 10.33.33.17  | pcf.open5gs.org   |
| nrf    | 9c2d5f34a8eb        | 10.33.33.19  | nrf.open5gs.org   |
| bsf    | f1f96ad98584        | 10.33.33.10  | bsf.open5gs.org   |


### **User Equipment (UE)**
| Name  | Container ID        | IPv4 Address | Alias             |
|-------|---------------------|--------------|-------------------|
| ue1   | 3a9f83b2b7a2        | 10.33.33.42  | ue1.ueransim.org  |
| ue2   | 7a4d32c5f9b6        | 10.33.33.53  | ue2.ueransim.org  |
| ue3   | 5c8f91d2ea73        | 10.33.33.54  | ue3.ueransim.org  |
| ue4   | 8b623b2561f6        | 10.33.33.41  | ue4.ueransim.org  |
| ue5   | 22b33761eaaf        | 10.33.33.40  | ue5.ueransim.org  |
| ue6   | 62ac86d45fff        | 10.33.33.38  | ue6.ueransim.org  |
| ue7   | d7e924c8b1f2        | 10.33.33.55  | ue7.ueransim.org  |
| ue8   | 490f88f7c56d        | 10.33.33.33  | ue8.ueransim.org  |
| ue9   | 0e192575726f        | 10.33.33.34  | ue9.ueransim.org  |
| ue10  | 87b151cab6a1        | 10.33.33.29  | ue10.ueransim.org |
| ue11  | 154137aaa082        | 10.33.33.30  | ue11.ueransim.org |
| ue12  | 00df815302a0        | 10.33.33.31  | ue12.ueransim.org |
| ue13  | 78d2acc4f9d2        | 10.33.33.35  | ue13.ueransim.org |
| ue14  | 50f11d8e49cf        | 10.33.33.32  | ue14.ueransim.org |
| ue15  | 8b9f8e613540        | 10.33.33.36  | ue15.ueransim.org |

### **gNB (Base Stations)**
| Name  | Container ID        | IPv4 Address | Alias             |
|-------|---------------------|--------------|-------------------|
| gnb1  | 4e6a8d2c9f71        | 10.33.33.25  | gnb1.ueransim.org |
| gnb2  | 89f7c5d12a30        | 10.33.33.26  | gnb2.ueransim.org |
| gnb3  | 2d4c9a3e78b1        | 10.33.33.28  | gnb3.ueransim.org |
| gnb4  | 74b1b642def9        | 10.33.33.24  | gnb4.ueransim.org |
| gnb5  | 2eca644530df        | 10.33.33.23  | gnb5.ueransim.org |

### **UPF & SMF (Network Functions)**
| Name                          | Container ID        | IPv4 Address | Alias            |
|-------------------------------|---------------------|--------------|------------------|
| slicing-upf_smf_ues-upf-1     | 1d2ca2892bd9        | 10.33.33.6   | upf1.open5gs.org |
| slicing-upf_smf_ues-upf-2     | 797e56acaeaa        | 10.33.33.2   | upf2.open5gs.org |
| slicing-upf_smf_ues-upf-3     | 576cc6d2de56        | 10.33.33.5   | upf3.open5gs.org |
| slicing-upf_smf_ues-upf-4     | d3e4f6c2b8a7        | 10.33.33.7   | upf4.open5gs.org |
| slicing-upf_smf_ues-upf-5     | 35b24c2ce179        | 10.33.33.49  | upf4.open5gs.org |
| slicing-upf_smf_ues-smf-1     | 8adfeb21c256        | 10.33.33.18  | smf1.open5gs.org |
| slicing-upf_smf_ues-smf-2     | 0e76cbf728a8        | 10.33.33.21  | smf2.open5gs.org |
| slicing-upf_smf_ues-smf-3     | a7b8c9d0e1f2        | 10.33.33.20  | smf3.open5gs.org |
| slicing-upf_smf_ues-smf-4     | 079b90ff1923        | 10.33.33.9   | smf4.open5gs.org |
| slicing-upf_smf_ues-smf-5     | 08cb90fhvd45        | 10.33.33.58  | smf5.open5gs.org |

### **Monitoring**
| Name        | Container ID        | IPv4 Address | Port Number | Alias                    |
|-------------|---------------------|--------------|-------------|--------------------------|
| prometheus  | 7666dfd5eb35        | 10.33.33.39  | 9090        | metrics.prometheus.org   |
| alertmanager| b1c2d3e4f5a6        | 10.33.33.50  | 9093        | alertmanager.open5gs.org |
| webhook     | 37264c95b29a        | 10.33.33.45  | 5001        | webhook.open5gs.org      |
| grafana     | d6e7f8g9h0i1        | 10.33.33.44  | 3000        | dashboard.grafana.org    |
| cadvisor    | 1c2d3e4f5g6h        | 10.33.33.56  | 8080        | cadvisor.open5gs.org     |

### **Other Services**
| Name        | Container ID        | IPv4 Address | Port Number | Alias             |
|-------------|---------------------|--------------|-------------|-------------------|
| packetrusher| 849800384bd8        | 10.33.33.27  | -           | packetrusher.org  |
| iperf       | 5e6f7g8h9i0j        | 10.33.33.57  | -           | test.iperf.org    |
| mongodb     | f5g6h7i8j9k0        | 10.33.33.48  | 27017       | db.open5gs.org    |
| webui       | 353fc21b675a        | 10.33.33.22  | 9999        | webui.open5gs.org |

## **Tunnel interfaces as per slicies**
| Slices              | Name                      | Network ID       | TUN interface IPv4 Address |
|---------------------|---------------------------|------------------|----------------------------|
| sst-1               | slicing-upf_smf_ues-smf-1 | 10.45.0.0/16     | -                          |
| sst-1, sd-0x000001  | ue1                       |                  | 10.45.0.2                  |
| sst-1, sd-0x000002  | ue2                       |                  | 10.45.0.3                  |
| sst-1, sd-0x000003  | ue3                       |                  | 10.45.0.4                  |
| sst-2               | slicing-upf_smf_ues-smf-2 | 10.46.0.0/16     | -                          |
| sst-2, sd-0x000001  | ue4                       |                  | 10.46.0.2                  |
| sst-2, sd-0x000002  | ue5                       |                  | 10.46.0.3                  |
| sst-2, sd-0x000003  | ue6                       |                  | 10.46.0.4                  |
| sst-3               | slicing-upf_smf_ues-smf-3 | 10.47.0.0/16     | -                          |
| sst-3, sd-0x000001  | ue7                       |                  | 10.47.0.2                  |
| sst-3, sd-0x000002  | ue8                       |                  | 10.47.0.3                  |
| sst-3, sd-0x000003  | ue9                       |                  | 10.47.0.4                  |
| sst-3, sd-0x000001  | ue13                      |                  | 10.47.0.5                  |
| sst-3, sd-0x000002  | ue14                      |                  | 10.47.0.6                  |
| sst-3               | slicing-upf_smf_ues-smf-5 | 10.47.0.0/16     | -                          |
| sst-3, sd-0x000003  | ue15                      |                  | 10.47.0.7                  |
| sst-4               | slicing-upf_smf_ues-smf-4 | 10.48.0.0/16     | -                          |
| sst-4, sd-0x000001  | ue10                      |                  | 10.48.0.2                  |
| sst-4, sd-0x000002  | ue11                      |                  | 10.48.0.3                  |
| sst-4, sd-0x000003  | ue12                      |                  | 10.48.0.4                  |


## 7.1. Iperf3 testing of UE's
To validate the functionality of network slicing, iPerf3 was used to conduct performance tests between the User Equipment (UE) and the Open5GS network. An iPerf3 server was created using a Docker container, which allowed for controlled and consistent testing of the network’s performance. Each UE was tested individually, sending traffic to the iPerf3 server to assess the throughput, latency, and packet loss under different conditions.

```bash
  iperf:
    container_name: iperf
    image: "mlabbe/iperf3:latest"
    networks:
      open5gs:
        aliases:
          - test.iperf.org
```

The tests helped ensure that the network slicing configurations were properly isolating traffic between different slices, allowing for distinct Quality of Service (QoS) for each slice. By using iPerf3, it was possible to monitor the network’s response to varying loads, check if traffic is being routed correctly through the right slices, and verify that the network is operating as expected without interference between slices. This testing methodology ensures that the slicing mechanisms are functioning effectively, providing optimized performance for different services running on the same network infrastructure.

Here are the testing results of UE's Iperf3. 


## 7.2. Multiple UEs Registration and PDU Session Establishment
- Several UEs are attached to the test system capacity.
- Ensures PDU sessions are correctly mapped to network slices.

## 7.3. Network Slicing Verification
- Directs traffic to the corresponding network slice depending on SST and SD values.
- Ensures appropriate implementation of QoS (Quality of Service) policies.

## 7.4. Packetrusher
- A packet generation tool is utilized for stress-testing the network.
- Assists in testing the 5G Core's ability to handle high volumes of packets.

## 7.5. Performance Testing (Throughput & Latency)

- Measures throughput (data transfer rate) and latency (delay) under varying loads.
- Facilitates evaluation of the network's performance under different conditions.
 
<p align="center">
<img src="https://github.com/MobileComputingWiSe24-25/mobcom-team_nyzers/blob/757322fe2455485f795395d61aedc5c69d9da5e8/Images/Yatish-Screenshots/Slicing(4%20sst_with_3%20sd)-AMF(3)_UPF_SMF(4)_UEs(12)/iperf_Throughput_test%20from%20ue11%20and%20ue7%20to%20ue2.png" width="1050"/>
	 <p align="center">Figure 7.4: Throughput Monitoring</p>
</p>

## 7.6. Failure Recovery Test - Simulates failures of critical components (e.g., AMF, UPF). 
- Monitors how the system automatically recovers and restores services.

These tests validate that Open5GS runs **reliably and correctly** within an environment of network slicing.

### System Objectives
- Ensure smooth UE connections and network slicing.
- Optimize session management and limit overload scenarios.

###  Task Handling
- Implement resource allocation strategies to prevent congestion.
- Monitor performance under different traffic loads.

This documentation will be available in Markdown format in the GitHub repository, ensuring proper formatting, readability, and consistency.
##  Additional Deployment Steps
- Deploy multiple gNodeBs for multiple UEs.
- Ensure successful connectivity between UERANSIM and Open5GS core.
- Register multiple UEs and establish PDU sessions.
- Add more slices based on S-NSSAI.
- Configure separate UPF instances for each slice.
- Map UEs to appropriate slices and validate PDU session establishment.
- Develop a system to monitor slice metrics (e.g., throughput, registration rate).
- Automate scaling of UPFs and SMFs based on UEs.
- Integrate orchestration logic with Docker to manage container lifecycles.
- Measure throughput and latency for each slice.
- Register up to 10 UEs and monitor slice performance under load.
- Simulate failures (e.g., UPF crash) and validate system recovery.
- Fine-tune deployment settings for optimal performance.

## 8. Conclusion

The implementation of a 5G core network with network slicing based on **Open5GS**, **Docker**, and **UERANSIM** was a solid and scalable solution for the telecommunication needs of today. Through the integration of **containerized network functions (NFs)**, i.e., **AMF**, **SMF**, **UPF**, and monitoring tools like **Prometheus** and **Grafana**, the project well demonstrated the features of **network slicing** in offering **customized and isolated network services**.

### Key Outcomes:
- **Dynamic Network Slicing:** Efficient resource allocation across multiple slices supporting diverse application demands such as **eMBB**, **mMTC**, and **uRLLC**.
- **Automation & Scalability:** Achieved through **Docker Compose**, **Alert Manager**, and a **Flask-based webhook**, allowing for auto-scaling of NFs based on real-time network demand.
- **Greater Monitoring & Resilience:** Through **Grafana dashboards** and **Prometheus alerts**, with high availability and rapid recovery on failure.
- **Performance Validation:** Testing included **low latency**, **high throughput**, and **effective failure recovery** across different network loads.

Overall, this project warrants the application of **containerized 5G core networks** for **efficient**, **future-proof**, and **flexible telecommunications infrastructure**, paving the way for **network slicing**'s broader applicability to both **consumer** and **enterprise applications**.

## 9. References
- 3GPP TS 23.501: System Architecture for the 5G System.
- Prometheus & Grafana Documentation.
- Open5GS Documentation: [https://open5gs.org/](https://open5gs.org/)
- UERANSIM Documentation: [https://github.com/aligungr/UERANSIM](https://github.com/aligungr/UERANSIM)
- Docker Documentation: [https://docs.docker.com/](https://docs.docker.com/)

