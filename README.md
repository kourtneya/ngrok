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

6. Execute the following command to run NGROK. This will create a temporary public URL that will point to a web service running on the port specified. Replace `<your_ngrok_token>` with the token you copied from NGROK in the steps above.
    ```bash 
    docker run -it --rm -e NGROK_AUTHTOKEN=<your_ngrok_token> ghcr.io/kourtneya/ngrok http host.docker.internal:8084
    ```

7. You should see similar results below. This docker container must be running for request to tunnel to your local service

    