This script is a rough script to allow you to get the raw data of twitch chat messages. 

The purpose of posting this script is to invite other developers to build some ideas on how to use the new Twitch points redemption system (without using a webhook).
I am sure Twitch will soon release some API for this purpose some time in the future. Meanwhile, the only way I can see that would allow integrating (in parts) the redemption system with third-parties is through the use of a tag in the raw data (and webhooks). This tag is called "custom-reward-id", and is unique to the reward. The problem is: the reward MUST include a message, otherwise it cannot be detected. At the moment streamers (and developers) cannot control the points (thus, any idea that includes giving the viewers extra points will not work at the moment). But this tag in the raw data can be used to automate redemptions (e.g. playing a sound, entering a raffle, voting, etc.). This script is a simple script to be able to know the custom-reward-id.

The script would cause the bot to spam raw data. So to start collecting raw data, send !startrawdata in chat, then immediately redeem the reward, and !endrawdata to end the nightmare of spam. Find the tag called "custom-reward-id", the long number after it is the reward id. This is best done when not streaming.

If you have any ideas on how this can be used, contact me here, or on twitter: @yaz123211, discord: Yaz12321#5267, twitch.tv/yaz12321, or by email: yaz1232112321@gmail.com
