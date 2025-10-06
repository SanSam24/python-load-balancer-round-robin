servers = ["Server 1", "Server 2"]
index = 0

def route_request():
    global index
    print(f"Request routed to {servers[index]}")
    index = (index + 1) % len(servers)

# Test routing
for _ in range(4):
    route_request()
