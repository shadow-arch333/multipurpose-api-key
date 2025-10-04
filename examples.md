# Examples and Workflow

## Key Derivation Example

Given a master API key:  
`abcd1234-efgh5678-ijkl9012`

### Python Usage

```python
from key_transform import derive_key

master_key = "abcd1234-efgh5678-ijkl9012"

ai_token = derive_key(master_key, "ai")
docker_token = derive_key(master_key, "docker")
mcp_token = derive_key(master_key, "mcp")

print("AI token:", ai_token)
print("Docker token:", docker_token)
print("MCP token:", mcp_token)
```

## Security Workflow

- The master key is never exposed to service endpoints.
- Only derived keys are sent to respective APIs.
- Revoking the master key disables all derived tokens.

## Extending for More Services

Simply pass a new service string:

```python
custom_token = derive_key(master_key, "custom_service")
```

## Notes

- For production, consider enhancing with time-based salts or using server-side token exchange.
- You can adapt the code for other languages or as a backend service.
