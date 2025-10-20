# SOWRL: Ren’Py Extension for Non-Linear Games

**SOWRL** is a Python extension for the Ren’Py visual novel engine that helps you build flexible **non-linear** stories with a semi-open world feel. Unlike strictly linear branching, players can freely move between locations and choose the order in which they pursue storylines. SOWRL provides a simple structure so you can focus on narrative and design instead of low-level navigation and state management.

The core idea is easy integration: to start, just copy the `OkiMVC` folder into your Ren’Py project. That folder contains the basic building blocks (models, views, controllers) and UI scaffolding needed to navigate locations.

## Features

- **Non-linear storytelling:** Build branching narratives and open areas to explore.
- **Semi-open world:** Let players decide where to go and which arcs to progress, instead of a fixed sequence.
- **Simple integration:** Drop the `OkiMVC` folder into the root of your Ren’Py game to enable the system.
- **MVC organization:** Separate game data, UI, and logic to keep things clear and maintainable.
- **Included examples:** The `example` directory shows how to define scenes and set up movement between locations.

## Getting Started

1. Create or open a Ren’Py project.
2. Copy the `OkiMVC` folder into your game’s root directory.
3. Review the sample projects in [`example`](https://github.com/MrHryhorii/SOWRL/tree/main/example) to see how components are arranged and how navigation works.
4. Define your own scenes and locations using the provided scaffolding.
5. Launch your game via the Ren’Py Launcher and verify location navigation.

## Examples

The `example` directory contains small demo projects, such as:

- Basic navigation between multiple locations with a movement menu.
- Multiple scenes and screens demonstrating different presentations.
- A simple data model setup for locations/characters.

These examples don’t cover every feature, but they’re a practical starting point to understand the approach and structure.

## Documentation

Further details and comments live in the library and example code. As the repository evolves, additional notes may appear.

## License

No license has been provided yet.

## Credits

Author: Hryhorii Chupryna (MrHryhorii)
