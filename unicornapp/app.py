from flask import Flask, request
import requests  # <-- Add this import

app = Flask(__name__)

# Function to retrieve EC2 instance ID (only works if running on EC2)
def get_instance_id():
    try:
        # Query EC2 instance metadata
        instance_id = requests.get('http://169.254.169.254/latest/meta-data/instance-id', timeout=1).text
    except requests.RequestException:
        instance_id = "N/A (Not running on EC2)"
    return instance_id

@app.route('/')
def hello():
    # Get client IP address
    client_ip = request.remote_addr
    
    # Get EC2 instance ID
    instance_id = get_instance_id()

    # Unicorn ASCII Art
    unicorn_art = '''
                               /
                    __       //
                    -\\= \\=\\ //
                  --=_\\=---//=--
                -_==/  \\/ //\\/--
                 ==/   /O   O\\==--
    _ _ _ _     /_/    \\  ]  /--
   /\\ ( (- \\    /       ] ] ]==-
  (\\ _\\_\\_\\-\\__/     \\  (,_,)--
 (\\_/                 \\     \\-
 \\/      /       (   ( \\  ] /)
 /      (         \\   \\_ \\./ )
 (       \\         \\      )  \\
 (       /\\_ _ _ _ /---/ /\\_  \\
  \\     / \\     / ____/ /   \\  \\
   (   /   )   / /  /__ )   (  )
   (  )   / __/ '---`       / /
   \\  /   \\ \\             _/ /
   ] ]     )_\\_         /__\\/
   /_\\     ]___\\
  (___)

Unicorn.Rentals Reservation Entry API
Copyright 2019
    '''

    # Simple HTML with the unicorn ASCII art and text
    return f'''
        <html>
            <head><title>Unicorn App</title></head>
            <body style="text-align: center; white-space: pre;">
                <h1>Hello! Your IP is {client_ip}. The instance ID is {instance_id}.</h1>
                <pre>{unicorn_art}</pre>
            </body>
        </html>
    '''

if __name__ == '__main__':
    # Run Flask app on all interfaces on port 80
    app.run(host='0.0.0.0', port=80)
