

class EventDispatcher:


    def __init__(self):
        self.events = {}

    def subscribe(self, event_type: str, callback: callable):

        if event_type not in self.events:
            self.events[event_type] = []

        self.events[event_type].append(callback)

    def unsubscribe(self, event_type: str, callback: callable):
        """Remove a registered callback."""
        if event_type in self.events:
            if callback in self.events[event_type]:
                self.events[event_type].remove(callback)

    def dispatch(self, event_type: str, *args, **kwargs):

        callbacks = self.events.get(event_type, [])

        for callback in callbacks:
            try:
                callback(*args, **kwargs)
            except Exception as error:
                print(f"Error in callback: {error}")


# Example callbacks
def first_listener(message):
    print(f"First listener: {message}")


def second_listener(message):
    print(f"Second listener: {message}")


def faulty_listener(message):
    raise Exception("Something went wrong in faulty listener")


if __name__ == "__main__":
    dispatcher = EventDispatcher()

    dispatcher.subscribe("message", first_listener)
    dispatcher.subscribe("message", faulty_listener)
    dispatcher.subscribe("message", second_listener)

    print("Dispatching event:")
    dispatcher.dispatch("message", "Hello, Observer Pattern!")

    print("\nUnsubscribing first listener:")
    dispatcher.unsubscribe("message", first_listener)
    dispatcher.dispatch("message", "Second dispatch")