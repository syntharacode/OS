# Central dynamic registry for Synthara OS

class SyntharaRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, key: str, value):
        self._registry[key] = value

    def get(self, key: str):
        return self._registry.get(key)

    def exists(self, key: str) -> bool:
        return key in self._registry

    def unregister(self, key: str):
        if key in self._registry:
            del self._registry[key]

    def clear(self):
        self._registry = {}

# Global instance
registry = SyntharaRegistry()