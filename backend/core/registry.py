# Central dynamic registry for Synthara OS
# 
# This module provides a lightweight key-value store that can be used
# across the system to register models, services, metadata, or runtime states.

class SyntharaRegistry:
    def __init__(self):
        # Internal dictionary to hold registered items
        self._registry = {}

    # Register a new key-value pair into the registry
    def register(self, key: str, value):
        self._registry[key] = value

    # Retrieve a value by its key
    def get(self, key: str):
        return self._registry.get(key)

    # Check if a key exists in the registry
    def exists(self, key: str) -> bool:
        return key in self._registry

    # Remove a specific key from the registry
    def unregister(self, key: str):
        if key in self._registry:
            del self._registry[key]

    # Clear the entire registry (use with caution)
    def clear(self):
        self._registry = {}

# Global instance of the registry, accessible system-wide
registry = SyntharaRegistry()
