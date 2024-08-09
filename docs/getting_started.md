# Getting Started

## Quick Example

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

## KSoft Tokens

If you have a KSoft token, you can simply pass it to the constructor for the `ravyapi.client.Client`. Please note that KSoft tokens are not compatible with any endpoints other than `ksoft` and `tokens`.

## Phisherman Token

You might have noticed there is no available kwarg to set the phisherman.gg token using the `urls` endpoint. This is because you can instead set it directly to the `ravyapi.client.Client` using the `ravyapi.client.Client.set_phisherman_token()` method. This also returns the `ravyapi.client.Client` object so you can chain calls.

```python
# Assume boilerplate is already set up
client = ravyapi.Client("token").set_phisherman_token("phisherman_token")
website_info = await client.urls.get_website("https://example.com")
```

## Permissions

The API wrapper automatically validates your token's permissions upon the first method call. If you attempt to use an API method that you do not have permission to use, the library will raise a `ravyapi.api.errors.AccessException`. This information is currently stored internally, but not publicly accessible. To manually check for permissions, call the `ravyapi.client.Client.tokens.get_token()` method and use the `access` property.

```python
# Assume boilerplate is already set up
token_info = await client.tokens.get_token()
permissions = token_info.access
```

## Error Handling

You can catch the defined errors in the `ravyapi.api.errors` module and handle them appropriately.

```python
# Assume boilerplate is already set up
try:
    token_info = await client.tokens.get_token()
except ravyapi.HTTPException as e:  # Generic HTTP error
    if e.status == 429:
        print(f"Encountered {e.status}: we are being ratelimited by Cloudflare!")
    else:
        print(f"Encountered HTTP error: ({e.status}) - {e.exc_data}!")

try:
    website_info = await client.urls.get_website("https://example.com")
except ravyapi.AccessException as e:  # Access denied
    print(f"This errored as the endpoint route needed {e.required} permission!")
```

## More Information

Check the API reference for more information as well as the official Ravy API documentation:

[Reference](./reference/client.md){ .md-button .md-button--primary }
[Ravy Docs](https://ravy.org/docs){ .md-button }
