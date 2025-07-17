# RavyAPI.py [![codecov](https://codecov.io/github/GoogolGenius/RavyAPI.py/graph/badge.svg?token=KOQWEG60MZ)](https://codecov.io/github/GoogolGenius/RavyAPI.py)

> According to an update from Hazel, the Ravy API will no longer be in operation. The maintenance status of this library is currently in jeopardy.

A simple and dynamic asynchronous Python wrapper for the Ravy API.

## Features

- Easy usability
- 100% API coverage
- Unit tested (soon™️)
- Pyright type compatible

## Installation

- Compatible with Python 3.8+
- Not yet available on PyPI

```bash
python3 -m pip install git+https://github.com/GoogolGenius/RavyAPI.py
```

## Usage

```python
# Import required packages
import asyncio

import ravyapi


async def main() -> None:
    # Construct a ravyapi client object
    client = ravyapi.Client("token")  # Replace "token" with your API key

    # Make a simple request to get token information
    token_info = await client.tokens.get_token()
    print(token_info.token_type)  # Print the token type: "ravy" | "ksoft"

    # Close and teardown the client
    await client.close()


# Start the event loop and run the main function
asyncio.run(main())
```

## Contributing

Feel free to create pull requests and issues. Just be civil, kind, and respectful.

This is my first library, so if you have any suggestions or questions, please let me know! Reach out via GitHub Issues or Discord `@googolgenius`.
