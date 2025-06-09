from pyngrok import ngrok

ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")

public_url = ngrok.connect(8084)

print("Public URL: ", public_url)
input("Press [Enter] to exit...\n")