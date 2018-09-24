import socket
import time
import subprocess

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

task_list = [0]

connections = subprocess.check_output("tail -1 server1.txt", shell=True)

print 'Serving HTTP on port %s ...' % PORT
while True:
    current_time = int(time.time())
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    for task in task_list:
        if task <= current_time:
            task_list.remove(task)

    # Add a delay to give the illusion of processing.
    delay = 10
    delay += current_time
    task_list.append(delay)

    task_id = 1
    task_string = "\n"
    for task in task_list:
        task_string = task_string + "\n" + str(task_id) + "\t" + str(task)
        task_id += 1

    log_tasks = open("server1.txt", "w")
    log_tasks.write(str(len(task_list)))

    http_response = """\
HTTP/1.1 200 OK

""" + "Server running on port: " + str(PORT) + " has " + str(len(task_list)) + " connection(s).\nTask\tCompletion time" + task_string

    client_connection.sendall(http_response)
    client_connection.close()
