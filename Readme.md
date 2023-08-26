# VoltaicGRiD's Recipe Manager
Intended to be used with Newsboat as a 'run-all' solution to recipe management from RSS feeds, my Recipe Manager (RM) can download a recipe into a JSON file (named '.recipe' in my code for easier visibility).

My Recipe Manager is an all-console solution, no GUI is implemented, and none is in the works.

From the downloaded recipe, the 'RecipeManager.py' script can perform a few functions:
- Open the recipe card in your browser from 'JustTheRecipe.com'
- Perform ingredient and measurement combination from multiple recipes using GPT-4 AI (Needs your own API key)
    - **INFO**: GPT-4 is far superior to GPT-3.5 for this task
    - TODO: Implement custom, built-in solution to do this instead, **in progress**
- Output the recipe in a quick, easily-readable format to the console

## Configuration
At the moment, there aren't a lot of configuration options, but more will come. I am primarily developing this solution for myself, but requests and contributions are always welcome.

**OpenAI API Key**
- `os.environ['OPENAI_API']`
- Create an environment variable that matches `OPENAI_API' with your OpenAI Key
    - If you're interested in usage of this application for yourself and cannot / do not have an API key, create an issue here or email me at `dustin@dustinconlon.com`, and I may be able to work with you on integration without it or with my personal Key

## Planned Features
- [ ] Integration of custom solution for ingredient consolidation and measurement conversion
- [ ] Implementation of 'Send to Printer' method for the basic recipe card (no plans to support images)
- [ ] Documentation updates to cleanup the code
- [ ] Additional configuration options
