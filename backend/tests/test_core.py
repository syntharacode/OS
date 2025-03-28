# Import the Synthara OS registry (a global key-value store)
from backend.core.registry import registry

# Import Synthara OS system settings (from .env or defaults)
from backend.core.config import settings

# Unit test for validating the dynamic registry behavior
def test_registry():
    # Register a key-value pair
    registry.register("test-key", 123)

    # Ensure the key exists
    assert registry.exists("test-key")

    # Ensure the value is retrievable and correct
    assert registry.get("test-key") == 123

    # Remove the key
    registry.unregister("test-key")

    # Ensure the key no longer exists
    assert not registry.exists("test-key")

# Unit test for checking global system settings
def test_settings():
    # Ensure the project name matches expected default
    assert settings.PROJECT_NAME == "SyntharaOS"

    # Ensure the DEBUG flag is a boolean type
    assert isinstance(settings.DEBUG, bool)
