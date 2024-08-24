# GameStats

Visualize your stats from your favorite games on Steam!

## Usage
### Live Demo
Coming soon...

### Supported Games
| Game Name | Steam ID |
| - | - |
| Counter-Strike 2 | 730 |

Request a game (create an issue)

## Development
### Roadmap
- [x] Home Page
    - [x] Make pretty
    - [x] Highlight key reasons to use this app
    - [x] Showcase features and functionality through videos/animation.
    - [x] Show supported games list
    - [x] Allow users to sign in
    - [x] Allow users to request a game
    - [x] Allow users to give feedback

- [x] Sign-in Page
    - [x] Make pretty
    - [x] Allow users to sign in using their Steam account.
    - [x] Display toast errors when login fails.

- [x] Dashboard
    - [x] Make pretty
    - [x] Display supported games that user has in a list, where games are clickable

- [ ] Game Stats Page (per game)
    - [ ] Make pretty
    - [ ] Show game info
    - [ ] Show stats for selected game (from Steam WebAPI)
    - [ ] Search/filter stats using user input

- [ ] Feedback Form
    - [ ] Make pretty
    - [ ] Send email to me

- [ ] Game Request Form
    - [ ] Make pretty
    - [ ] Send email to me

- [ ] Error Pages
    - [x] Make pretty
    - [ ] Email Support

### CI
```sh
# `os` can be one of the following
# linux-arm64 
# linux-armv7 
# linux-x64 
# macos-arm64 
# macos-x64 
# windows-arm64.exe
# windows-x64.exe
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-{os}
chmod +x tailwindcss-{os}
mv tailwindcss-{os} tailwindcss
```

### Compile TailwindCSS
```sh
.\tailwindcss.exe -c tailwind.config.js -i tailwind.css -o public/css/styles.css
```

### Environment Variables
| Name | Description |
| - | - |
| `HOST_URL` | URL of the web server |
| `ENABLE_DEBUG` | Whether to enable debug mode (Starlette error are shown on `500 Internal Server Error` instead of using custom exception handler) |
| `STEAM_SECRET` | Steam API key, available [here](https://steamcommunity.com/dev/apikey) |