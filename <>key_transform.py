"""key_transform.py: Utility for deriving service-specific tokens from a master API key."""

import hashlib
import hmac

def derive_key(master_key: str, service: str) -> str:
    """
    Derives a service-specific key from the master API key using HMAC-SHA256.

    Args:
        master_key (str): The master API key.
        service (str): Service identifier (e.g., 'ai', 'docker', 'mcp').

    Returns:
        str: Derived hex-encoded service key.
    """
    return hmac.new(master_key.encode(), service.encode(), hashlib.sha256).hexdigest()

if __name__ == "__main__":
    # Example usage
    master = "abcd1234-efgh5678-ijkl9012"
    for srv in ["ai", "docker", "mcp"]:
        print(f"{srv} token:", derive_key(master, srv))
