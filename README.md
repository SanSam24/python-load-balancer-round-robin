
# Python Round Robin Load Balancer

## Overview

This project simulates a Round Robin load balancer in Python using Flask, distributing incoming requests to 6 backend servers. Each server is a standalone Flask app, and a central load balancer (also in Flask) routes requests sequentially among them.

## Project Structure

```
server1.py
server2.py
server3.py
server4.py
server5.py
server6.py
load_balancer.py
launcher.py
requirements.txt
README.md
```

## Setup Instructions

1. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

2. **Start backend servers**

   - Option 1: **Manually**  
     Open 6 terminals and run each:
     ```
     python server1.py
     python server2.py
     ...
     python server6.py
     ```
   - Option 2: **Automatically**  
     Use the launcher script to start all servers in parallel:
     ```
     python launcher.py
     ```
     (Keep this terminal open to keep the servers running.)

3. **Start the load balancer**

   Open a new terminal and run:
   ```
   python load_balancer.py
   ```

4. **Access the load balancer**

   Open your browser and go to:  
   [http://127.0.0.1:6000/](http://127.0.0.1:6000/)

   Refresh the page multiple times—you'll see the response rotate among the 6 servers.

5. **Check request statistics (optional)**

   Visit [http://127.0.0.1:6000/stats](http://127.0.0.1:6000/stats) to see how many requests each server has handled.

## Scalability

To add/remove servers, simply edit the `BACKEND_SERVERS` list in `load_balancer.py` and update the `server_scripts` list in `launcher.py`.

## Sample Output

### Browser Requests

Refreshing the browser multiple times at [http://127.0.0.1:6000/](http://127.0.0.1:6000/) will cycle through:

```
Hello from Server 1
Hello from Server 2
Hello from Server 3
Hello from Server 4
Hello from Server 5
Hello from Server 6
Hello from Server 1
...
```

### Load Balancer Console

The load balancer will log which server each request is routed to:

```
2025-10-09 09:55:42 [INFO] Routing request to http://127.0.0.1:5001 (Server 1), Request count: 1
2025-10-09 09:55:44 [INFO] Routing request to http://127.0.0.1:5002 (Server 2), Request count: 1
...
```

### Request Statistics

Visiting `/stats` endpoint on load balancer:

```
Server 1: 4 requests
Server 2: 3 requests
Server 3: 3 requests
Server 4: 3 requests
Server 5: 3 requests
Server 6: 3 requests
```

## Notes

- All servers and the load balancer must be running for proper routing.
- If a backend server is down, the load balancer returns `502 Backend server unreachable` for requests routed to it.
- The design makes it easy to add/remove backend servers by editing a single list.

---
Enjoy experimenting with round robin load balancing!
=======


#  Simple Load Balancer using Round Robin (Python)

## 📘 Project Overview

This project demonstrates a **basic load balancer** that distributes requests **evenly between two backend servers** using the **Round Robin algorithm**.
The goal is to simulate how real-world load balancers share traffic to improve performance and prevent any single server from being overloaded.

---

## ⚙️ How It Works

1. Two backend servers (`server1.py` and `server2.py`) are created using **Flask**.

   * Server 1 returns “Hello from Server 1!”
   * Server 2 returns “Hello from Server 2!”
2. The **load balancer script** (`load_balancer.py`) keeps a list of both server URLs.
3. Using `itertools.cycle()`, requests are sent alternately to each server in a **round-robin** pattern:

   ```
   Request 1 → Server 1  
   Request 2 → Server 2  
   Request 3 → Server 1  
   Request 4 → Server 2  
   ```
4. This ensures that both servers handle an equal share of requests.

---

## 💻 Tools Used

* **Python 3**
* **Flask** (for creating the servers)
* **Requests** (for sending HTTP requests)
* **itertools** (for round robin logic)


##  Key Concept

**Round Robin Algorithm** – Distributes requests one by one to each server in sequence, looping back to the first after the last.

---

## ✅ Output Example

```
Request 1 → http://localhost:5001
Response 1: Hello from Server 1!
Request 2 → http://localhost:5002
Response 2: Hello from Server 2!
Request 3 → http://localhost:5001
Response 3: Hello from Server 1!
