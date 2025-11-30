import zmq
import time

context = zmq.Context()

print("Connecting to get-file microservice")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")

print("\n--- Test 1: Read valid file ---")
socket.send(b"get!example.txt")
message = socket.recv()
print("Expected: file contents")
print("Received:", message.decode())
print()

time.sleep(1)

print("\n--- Test 2: Invalid filename ---")
socket.send(b"get!bad file!.txt")  # fails regex
message = socket.recv()
print("Expected: filename error")
print("Received:", message)
print()

time.sleep(1)

print("\n--- Test 3: Unsupported operation ---")
socket.send(b"read!example.txt")
message = socket.recv()
print("Expected: error message")
print("Received:", message)
print()
