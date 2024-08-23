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
- [ ] Home Page
    - [ ] Make pretty
    - [x] Highlight key reasons to use this app
    - [x] Showcase features and functionality through videos/animation.
    - [x] Show supported games list
    - [x] Allow users to sign in
    - [ ] Allow users to request a game
    - [ ] Allow users to give feedback

- [ ] Sign-in Page
    - [ ] Make pretty
    - [x] Allow users to sign in using their Steam account.
    - [x] Display toast errors when login fails.

- [ ] Dashboard
    - [ ] Make pretty
    - [x] Display supported games that user has in a list, where games are clickable

- [ ] Game Stats Page (per game)
    - [ ] Make pretty
    - [ ] Show game info
    - [ ] Show stats for selected game (from Steam WebAPI)
    - [ ] Search/filter stats using user input

### Environment Variables
| Name | Description |
| - | - |
| `HOST_URL` | URL of the web server |
| `ENABLE_DEBUG` | Whether to enable debug mode (Starlette error are shown on `500 Internal Server Error` instead of using custom exception handler) |
| `STEAM_SECRET` | Steam API key, available [here](https://steamcommunity.com/dev/apikey) |