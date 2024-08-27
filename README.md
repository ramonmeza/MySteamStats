# MySteamStats

Visualize your stats from your favorite games on Steam!

## Usage
### Live Demo
Coming soon...

### Supported Games
| Game Name | Steam ID |
| - | - |
| Counter-Strike 2 | 730 |

Request a game (create an issue)

## Developer
### Environment Variables
| Name | Description |
| - | - |
| `HOST_URL` | URL of the web server (needed for Steam API authentication callback) |
| `ENABLE_DEBUG` | Whether to enable debug mode (Starlette error are shown on `500 Internal Server Error` instead of using custom exception handler) |
| `STEAM_SECRET` | Steam API key, available [here](https://steamcommunity.com/dev/apikey) |

### CI
#### Compile TailwindCSS
```sh
.\tailwindcss.exe -c tailwind.config.js -i tailwind.css -o public/css/styles.css
```
#### Docker Build
```sh
docker build . --tag mysteamstatsapp
```

#### Docker Run
Steam authentication may not work when ran within a Docker container. This is because the callback url (HOST_URL) isn't an address that Steam can verify, or something.

```sh
docker run -e HOST_URL="" -e STEAM_SECRET="" -p 8000:8000 mysteamstatsapp
```
