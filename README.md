# Ngrok
[Ngrok](https://ngrok.com) is a secure tunneling tool that lets you expose a local web server to the internet instantly. It creates a secure tunnel from a public URL to your local machine, allowing you to test webhooks, demo sites to clients, or access your apps remotely. With features like HTTPS support, traffic inspection, custom domains, and authentication, Ngrok is a powerful tool for developers working behind NATs, firewalls, or in private networks.


## Key Features:

* Instant public URLs for local servers
* HTTPS tunnels with valid SSL
* Webhook testing made easy
* Traffic inspection and replay
* Authentication and access control
* Custom subdomains and reserved domains


## Getting Started
1. Navigate to [Ngrok](https://ngrok.com)

2. Click the **`Sign In`** button
    - If you do not have an existing account, create a free account by clicking the **`Sign Up`** button

3. Once the `Welcome` page has loaded after a successful sign in, click the **`Your Token`** option in the left pane under `Getting Started`

4. On the `Your Token` page, click the **`Copy`** button to copy the NGROK Auth token. You will use this token when running ngrok in docker 

5. Open a Terminal window 
    - **MacOS** <br>
    Press <kbd>Command</kbd> + <kbd>Space</kbd> on the keyboard, type `Terminal` and press <kdb>Enter</kdb>

    - **Windows** <br>
    Click the **`Start`** button *(usually Windows icson)* at the bottom left corner of the screen. Type `cmd` and press <kdb>Enter</kdb>

### Source Code
1. Clone the repository to your local machine
    ```bash
    git clone https://github.com/kourtneya/ngrok.git 
    ```

2. Navigate to the cloned repository 
    ```
    cd ngrok
    ```

3. Open the project folder in a new VS Code Window by typing the following command 
    ```bash
    code .
    ```
    > **NOTE:** You can use any text editor

4. In the new VS Code window, open a `Terminal` window by clicking `View` at the top, then `Terminal`

5. In Python, it is best practice to create a virtual environment. A virtual environment in python is a self-contained directory that contains a the python interpreter and its installed dependencies. Having this virtual environment scopes the dependencies to this project, avoid conflicts with other projects, and keeps your global python installation clean. 

    Execute the following command to create the virtual environment for ngrok

    ```bash
    python -m venv my_ngrok
    ```

6. Next, enter in the following command to activate the virtual environment
    - MacOS
    ```bash
    source my_ngrok/bin/activate
    ```
    
    - Windows
    ```bash
    my_ngrok\Scripts\activate.bat
    ```

7. You need to install these dependencies in the virtual environment so that you can properly run the python application

    Install the projects dependencies by entering the following command in the terminal session. 

    ```bash 
    pip install -r requirements.txt
    ```
8. Open the `app.py` file and replace the `YOUR_NGROK_AUTH_TOKEN`, on the following line
    ```{.bash .no-copy hl_lines=""}
    ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")
    ```

9. Save `app.py` File
    - In the top left corner, click `File`, then `Save` in the drop down menu; <br>or<br>

    - Use the respective shortcuts to save the file 

        - MacOS <br>
        <kbd>Command</kbd> + <kbd>S</kbd>

        - Windows <br>
        <kbd>Ctrl</kbd> + <kbd>S</kbd>

10. Execute the following command to run NGROK. This will create a temporary public URL that will point to a web service running on the port specified. As of right now, you have not created a service running on this port yet. 
    ```bash
    python app.py
    ```

11. You should see a similar result below. This application must be running the entire time else Webex will not be able to route messages to the AI-powered service you will create later in the lab. The first url presented for forwarding *(highlighted)* is the public url Webex will need for the Webhook. Take note of this URL 
    ```{.bash .no-copy hl_lines="1"}
    Public URL:  NgrokTunnel: "https://c22c-172-98-16-94.ngrok-free.app" -> "http://localhost:8084"
    Press [Enter] to exit...
    ```

### Docker Setup

1. Execute the following command to run NGROK. This will create a temporary public URL that will point to a web service running on the port specified. Replace `<your_ngrok_token>` with the token you copied from NGROK in the steps above.
    ```bash 
    docker run -it --rm -e NGROK_AUTHTOKEN=<your_ngrok_token> ghcr.io/kourtneya/ngrok http host.docker.internal:8084
    ```

2. You should see similar results below. This docker container must be running for request to tunnel to your local service
    ```bash
    ngrok                                                                                                                              (Ctrl+C to quit)
                                                                                                                                                   
    🤖 Want to hang with ngrokkers on our new Discord? https://discord.gg/xvAfCpJG                                                                     
                                                                                                                                                    
    Session Status                online                                                                                                               
    Account                       kourtneya (Plan: Free)                                                                                               
    Update                        update available (version 3.22.1, Ctrl-U to update)                                                                  
    Version                       3.22.1                                                                                                               
    Region                        United States (us)                                                                                                   
    Latency                       421ms                                                                                                                
    Web Interface                 http://0.0.0.0:4040                                                                                                  
    Forwarding                    https://c6d8-173-38-117-89.ngrok-free.app -> http://host.docker.internal:8084                                        
                                                                                                                                                    
    Connections                   ttl     opn     rt1     rt5     p50     p90                                                                          
                                0       0       0.00    0.00    0.00    0.00 
    ```