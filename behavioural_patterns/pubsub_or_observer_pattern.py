"""
Category: Observer/Pubsub pattern

Intent: The pattern lets us define a subscription mechanism to notify multiple
objects about any events that happen to the object they are observing.

Real-world analogy:
    If we subscribe to a Youtube channel, we no longer need to go to the store
    to check if the next video is available. Instead, the subject (aka the pulisher)
    sends notifications directly to observers' (aka subscriber) mailbox.

    The publisher maintains a list of subscribers and knows which channel they're
    interested in. The subscribers can leave the list at any time and stop the pub-
    lisher from sending notifications.
"""


class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = list()

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.send_notification(self.name, event)


from abc import ABC, abstractmethod


class YoutubeSubscriber(ABC):
    @abstractmethod
    def send_notification(self, event):
        pass


class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def send_notification(self, channel, event):
        print(f"User {self.name} receives notification from {channel}: {event}")


if __name__ == '__main__':
    youtube_channel = YoutubeChannel("KL")
    youtube_user1 = YoutubeUser("user1")
    youtube_user2 = YoutubeUser("user2")
    youtube_user3 = YoutubeUser("user3")
    for yt_user in (youtube_user1, youtube_user2, youtube_user3):
        youtube_channel.subscribe(yt_user)
    youtube_channel.notify("A new video has been issued.")
