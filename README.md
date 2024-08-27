# MySteamStats

Visualize your stats from your favorite games on Steam!

## Usage
### Live Demo
https://www.MySteamStats.com/


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

## Roadmap
This is a changing list of things I need to do.

- [ ] **Make forms functional**

- [ ] Utilize Steam API to personalize menu with Steam icon and Steam nickname

- [ ] About Page
    - [ ] Make it pretty
    - [ ] describe the platform and it's purpose
    - [ ] talk about me a bit 👉👈

- [ ] Contact Page (this could just be the feedback from? unsure yet)

- [ ] "Market"
    - [ ] Make social media accounts
        - [ ] twitter
        - [ ] tiktok
    - [ ] bring up to friends and family
    - [ ] hit up the discord servers