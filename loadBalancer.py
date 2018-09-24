import webbrowser
import socket
import subprocess

HOST, PORT = '', 8887

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

total_connections = 0

#task_list = []

server_address = {
    "server1": 8888,
    "server2": 8889,
    "server3": 8890
}

print 'Serving HTTP on port %s ...' % PORT

while True:
    server1_connections = subprocess.check_output("tail -1 server1.txt", shell=True)
    server2 = subprocess.check_output("tail -1 server2.txt", shell=True)
    server3 = subprocess.check_output("tail -1 server3.txt", shell=True)

    try:
        least_number_connections = int(server1_connections)
        least_server_connection_name = "server1"
    except:
        least_number_connections = 0
        least_server_connection_name = "server1"

    try:
        server2_connections = int(server2)
    except:
        server2_connections = 0

    try:
        server3_connections = int(server3)
    except:
        server3_connections = 0

    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    connections = {
        "server1": least_number_connections,
        "server2": server2_connections,
        "server3": server3_connections
    }

    for conn in connections:
        print conn + " " + str(connections[conn])

    for conn in connections:
        if int(connections[conn]) < least_number_connections:
            least_server_connection_name = conn
            least_number_connections = connections[conn]


    print "Sending connection to: " + least_server_connection_name
    http_response = """\
HTTP/1.1 200 OK
""" + "Sending request to server: " + least_server_connection_name
    print http_response

    #response=conn.getresponse()

    webbrowser.open_new_tab("http://localhost:" + str(server_address[least_server_connection_name]))

    client_connection.sendall(http_response)
    client_connection.close()
