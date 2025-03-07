import platform
import socket
import os
import sys

print(f"\n Machine Type: {platform.machine()}")
print(f"\n Processor Type: {platform.architecture()}")

socket.setdefaulttimeout(50)
print(f"\Default Timeout for Socket: {socket.getdefaulttimeout()}")

print(f"\nOS Type: {os.name}")
print(f"\nOS Name: {platform.system()}")
print(f"\n Current PID: {os.getpid()}")

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os, os.O_RDWR | os.O_CREAT)
file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Some string to write to this file")
file_object_TextIO.flush()

pid = 0
if pid == 0:
    print(f"\n[Child PID: {os.getpid()}], [Parent PID: {os.getpid()}]")
    os.lseek(file_handle, 0, 0)
    print(f"\n[Child PID: {os.getpid()}], [Parent PID: {os.read(file_handle, 100).decode()}]")
    os.close(file_handle)
    sys.exit(0)
else: 
    print(f"\n[Parent PID: {os.getpid()}], [Parent PID: {os.getpid()}]")
    print("Wait for child")
    os.waitpid(pid, 0)
    print("child finished")
    file_object_TextIO.close()
    sys.exit(10)
