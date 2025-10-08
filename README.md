

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

---

## 🚀 Steps to Run

1. Install dependencies:

   ```bash
   pip install flask requests
   ```
2. Run both servers in separate terminals:

   ```bash
   python server1.py
   python server2.py
   ```
3. Run the load balancer:

   ```bash
   python load_balancer.py
   ```



---

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
```

