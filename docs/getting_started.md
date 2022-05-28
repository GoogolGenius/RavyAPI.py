# Getting Started

## Quick Example

```python
# Import required packages
import asyncio

import plane


async def main() -> None:
    # Construct a plane client object
    client = plane.Client("token")  # Replace "token" with your API key

    # Make a simple request to get token information
    token_info = await client.tokens.get_token()
    print(token_info.type)  # Print the token type: "ravy" | "ksoft"

    # Close and teardown the client
    await client.close()


# Start the event loop and run the main function
asyncio.run(main())
```

## More Information

Check the API reference for more information as well as the official Ravy API documentation:

[Reference](./reference/client.md){ .md-button .md-button--primary }
[Ravy Docs](https://ravy.org/docs){ .md-button }
