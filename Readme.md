# VoltaicGRiD's Recipe Manager
Intended to be used with Newsboat as a 'run-all' solution to recipe management from RSS feeds, my Recipe Manager (RM) can download a recipe into a JSON file (named '.recipe' in my code for easier visibility).

My Recipe Manager is an all-console solution, no GUI is implemented, and none is in the works.

From the downloaded recipe, the 'RecipeManager.py' script can perform a few functions:
- Open the recipe card in your browser from 'JustTheRecipe.com'
- Perform ingredient and measurement combination from multiple recipes using GPT-4 AI (Needs your own API key)
    - **INFO**: GPT-4 is far superior to GPT-3.5 for this task
    - TODO: Implement custom, built-in solution to do this instead, **in progress**
- Output the recipe in a quick, easily-readable format to the console

## Usage with Newsboat
I've implemented this custom 'set browser' macro that binds to the 'r' key in newsboats configuration file found here:

`~/.newsboat/config`

`macro r set browser "cd ~ & python Recipes/Voltaic_Recipe_Manager/DownloadRecipe.py %u" ; open-in-browser ; set browser "xdg-open %u"`


Make sure you create the directory 'Recipes' in your primary working / %home% directory before cloning this repo into that folder.
`cd ~ & mkdir Recipes`

In the end, your directory tree should look like this:

```bash
(~) %HOME%
 └ Recipes
    └ Voltaic_Recipe_Manager
        ├ RecipeManager.py
        ├ DownloadRecipe.py
        └ Readme.md
```

## GPT-4 Prommpt
My currently (relatively well-engineered, so-far) prompt for use with GPT-4 is as follows:

> You are a professional grocery shopper, making the most efficient, time-saving lists in the whole world. Remain brief and highly-efficient.
> Only use these categories: Produce, Canned Goods, Dairy, Meat, Deli, Seafood, Condiments & Spices, Bakery, Grains
> Substitution suggestions should always be output with their measurements.
> Never output fine-grained details about the ingredients. (For example, do not include "zested" or "peeled, cored, and sliced", or similar)

In testing, I found these values to be reasonable and provide "best-case results";

- `openai_tokens : 1000`
- `openai_temp : 0.1`

## Configuration
At the moment, there aren't a lot of configuration options, but more will come. I am primarily developing this solution for myself, but requests and contributions are always welcome.

**OpenAI API Key**
*No longer stored in an environment variable*
Presently, all configuration is stored in the `config` file that is included with the repo.

The configuration loads data line-by-line, using the buffer ` : ` (1-wide spacing after the key and before the value required)


## Planned Features
- [ ] Integration of custom solution for ingredient consolidation and measurement conversion
- [ ] Implementation of 'Send to Printer' method for the basic recipe card (no plans to support images)
- [ ] Documentation updates to cleanup the code
- [ ] Additional configuration options
