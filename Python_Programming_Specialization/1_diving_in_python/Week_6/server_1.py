

"""
async text tcp server for metrics
"""


import asyncio
import json


DATABASE = {}
SUCCESS = 'ok\n\n'
WRONG = 'error\nwrong command\n\n'
ALLOWED = ('put', 'get', 'DATABASE')



def get_handler(recv_data):
    command_list = recv_data.split()
    if len(command_list) != 2:
        return WRONG

    key = command_list[1]    
    answer = 'ok\n'
    for k, value in DATABASE.items():
        if k == key or key == '*':
            for val in value:
                answer += f'{k} {val[1]} {val[0]}\n'
    answer += '\n'
    return answer    

def parse_request(recv_data):
    if len(recv_data) > 4 and (recv_data[:3] in ALLOWED or recv_data[:7] in ALLOWED): 
        if recv_data[:3] == ALLOWED[0]:
            return put_handler(recv_data)
        elif recv_data[:3] == ALLOWED[1]:
            return get_handler(recv_data)
        elif recv_data[:7] == ALLOWED[2]:
            return DATABASE_handler()
        else:
            return WRONG
    else:    
        return WRONG

def put_handler(recv_data):        
    try:
        metric, value, timestamp = recv_data.split()[1:]
        if metric not in DATABASE.keys():
            DATABASE[metric] = []            
        
        l = DATABASE.get(metric)
        updated = False
        for element in l:
            if element[0] == int(timestamp):
                element[1] = float(value)
                updated = True
        if not updated:
            DATABASE[metric].append([int(timestamp), float(value)])

        return SUCCESS
    except Exception as e:
        print(e)        
        return WRONG    



async def handle_echo(reader, writer):
    recv_data = await reader.read(1024)
    client_answer = parse_request(recv_data.decode())

    print(f'Received {recv_data} from {writer.get_extra_info("peername")}')
    print(f'Send to client {client_answer.encode()}')
    
    writer.write(client_answer.encode())
    await writer.drain()
    
    writer.close()


    
def DATABASE_handler():
    return str(DATABASE)



class ClientServerProtocol(asyncio.Protocol):
    def data_received(self, data):
        resp = parse_request(data.decode())
        self.transport.write(resp.encode())
        
    def connection_made(self, transport):
        self.transport = transport



def run_server(host, port):        
    
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()    
