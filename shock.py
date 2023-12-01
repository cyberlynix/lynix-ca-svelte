import asyncio
import websockets
import json

# Dictionary to map auth codes to WebSocket clients
auth_clients = {}

async def echo(websocket, path):
    try:
        # Wait for the initial auth message
        auth_message = await websocket.recv()
        auth_data = json.loads(auth_message)
        auth = auth_data.get("auth_key", "")

        # Add the client to the auth_clients dictionary
        auth_clients[auth] = websocket

        print(f"Client with auth code '{auth}' connected")

        async for message in websocket:
            print("MSG RX:", message)

            try:
                # Parse the JSON message
                data = json.loads(message)
                # Auth Code
                auth_code = data.get("auth")

                # Extract values from the JSON
                action = data.get("action", "")
                duration = data.get("duration", "")
                intensity = data.get("intensity", "")
                pingDelay = data.get("pingDelay", "")

                # Construct the desired format without including the auth code
                formatted_message = f"{action};Duration:{duration}:{intensity};Pingdelay:{pingDelay}"

                # Send the formatted message only to the authenticated client
                if auth_code in auth_clients:
                    print("Auth Request")
                    await auth_clients[auth_code].send(formatted_message)

            except json.JSONDecodeError:
                print("Invalid JSON format")

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client with auth code '{auth}' disconnected")
    finally:
        # Remove the client from the auth_clients dictionary when they disconnect
        if auth in auth_clients:
            del auth_clients[auth]

async def main():
    server = await websockets.serve(echo, 'localhost', 8765)
    await server.wait_closed()
    
asyncio.run(main())