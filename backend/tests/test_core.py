from backend.core.registry import registry
from backend.core.config import settings

def test_registry():
    registry.register("test-key", 123)
    assert registry.exists("test-key")
    assert registry.get("test-key") == 123
    registry.unregister("test-key")
    assert not registry.exists("test-key")

def test_settings():
    assert settings.PROJECT_NAME == "SyntharaOS"
    assert isinstance(settings.DEBUG, bool)