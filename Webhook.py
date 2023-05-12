"""Making a post request to Webhook, without using discord.py"""

import aiohttp

webhook_url = "your_webhook's_url" # URL of the Webhook (make sure NOT TO SHARE IT WITH ANYONE.)

# JSON data to send to the Webhook.
# You can find the data payload at https://discord.com/developers/docs/resources/webhook#execute-webhook
data = {
    'content': 'Hello, world!',
    'username': 'MyWebhook',
    'avatar_url': 'https://example.com/my_avatar',
    'embeds': [ # A list of Embed Objects you need to send through the Webhook (maximum of 10 embeds)
                # You can find embed object payload at https://discord.com/developers/docs/resources/channel#embed-object
        {
            'title': 'My Embed',
            'description': 'This is an embed sent by Webhook',
        },
    ]
}

# Make a POST request to the Webhook
async with aiohttp.ClientSession() as session:
    async with session.post(webhook_url, json=data) as resp: # Make a POST Request to the Webhook URL with
                                                             # the JSON payload you created earlier
        resp.raise_for_status() # Raise the status in case the request Fails (Optional)
        print(resp.json()) # Print the response returned by the API.
                           # The returned Data payload will be like - https://discord.com/developers/docs/resources/webhook#webhook-object


"""Use discord.Embed instead of raw payload to create embeds"""
# Don't want to create Emebds like this and instead use native discord.py library?

from discord import Embed

embed = Embed(title='My Embed', description='This is an embed sent by Webhook') # Create an Embed object
embed.set_author(name='My Webhook', icon_url='https://example.com/my_avatar')
embed.add_field(name='Some Field', value='Some Value'))
my_dict = embed.to_dict() # This returns the dict form of the Embed you just created
                          # Just use this dict as an Element of the list of Embed objects you need to send through the Webhook
data = {
    'embeds': [
        my_dict,
    ],
}
# and then send it using the same process above.




"""Use discord.py to send a message through the Webhook"""

from discord import Webhook, AsyncWebhookAdapter
import aiohttp

webhook_url = "your_webhook's_url" # To be kept Confidential

@bot.command()
async def send_webhook(ctx):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session)) # Make a webhook object with the URL of the Webhook.
        content = 'Hello, World!'
        embed = discord.Embed(title='My Embed', description='An Embed sent using Webhooks') # Create an Embed Object with discord.Embed()

        await webhook.send(content=content, embed=embed)
        # for sending multiple embeds, you can use embeds kwarg which accepts a list of upto 10 embeds
        # Like `await webhook.send(content=content, embeds=[embed1, embed2, ...])`
