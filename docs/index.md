# Index

::: plane
    options:
        show_root_heading: true

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

## Contributing

Feel free to make a pull request in the [GitHub repository](https://github.com/GoogleGenius/plane)! Make sure to report any bugs or issues as well.

## About

Created by [GoogleGenius](https://github.com/GoogleGenius). Licensed under the GNU General Public License v3.0. Please check the [LICENSE](https://github.com/GoogleGenius/plane/blob/main/LICENSE) file for more information about the license as well as this project's basis in some elements from the [ksoftapi.py](https://github.com/KSoft-Si/ksoftapi.py) wrapper.
