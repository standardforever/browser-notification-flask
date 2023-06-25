from fastapi import FastAPI, WebSocket
import websockets

app = FastAPI()
connected_clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            await websocket.receive_text()  # Handle incoming messages if needed
    finally:
        connected_clients.remove(websocket)


@app.post("/process_request")
async def process_request(request_data: dict):
    # Process the request data as needed
    
    # Broadcast the message to all connected clients
    message = "New request: " + str(request_data)
    for client in connected_clients:
        await client.send_text(message)
    
    return {"message": "Request processed successfully"}


import uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
