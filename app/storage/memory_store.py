# storage/memory_store.py

class MemoryStore:
    """
    A simple in-memory key-value store.
    Useful for caching data or managing session state during runtime.
    Data is lost when the application stops.
    """
    def __init__(self):
        """
        Initializes the in-memory store.
        """
        self._data = {}
        print("In-memory store initialized.")

    def set(self, key: str, value):
        """
        Sets a value for a given key.

        Args:
            key: The key to store the data under.
            value: The data to store.
        """
        print(f"Setting value for key '{key}' in memory store.")
        self._data[key] = value

    def get(self, key: str):
        """
        Retrieves a value for a given key.

        Args:
            key: The key of the data to retrieve.

        Returns:
            The stored value, or None if the key does not exist.
        """
        print(f"Getting value for key '{key}' from memory store.")
        return self._data.get(key)

    def delete(self, key: str):
        """
        Deletes a key-value pair from the store.

        Args:
            key: The key to delete.
        
        Returns:
            True if the key existed and was deleted, False otherwise.
        """
        if key in self._data:
            print(f"Deleting key '{key}' from memory store.")
            del self._data[key]
            return True
        return False
        
    def list_keys(self):
        """
        Returns a list of all keys in the store.
        """
        return list(self._data.keys())

# Example of how to use the MemoryStore
if __name__ == '__main__':
    cache = MemoryStore()
    
    print("\nTesting memory store operations...")
    cache.set("user_session_1", {"username": "alice", "login_time": "2023-10-27T10:00:00Z"})
    cache.set("app_config", {"theme": "dark", "language": "en"})
    
    print(f"All keys: {cache.list_keys()}")
    
    session = cache.get("user_session_1")
    print(f"Retrieved session: {session}")
    
    cache.delete("user_session_1")
    print(f"Deleted 'user_session_1'. Keys are now: {cache.list_keys()}")
    
    session_after_delete = cache.get("user_session_1")
    print(f"Attempting to retrieve deleted session: {session_after_delete}")
