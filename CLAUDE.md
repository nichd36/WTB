# Introduction

This repo is for a project called WTB (Where's the Bus) API where we will pull data from Prasarana's GTFS Open API and then process it.

This repo is strictly for the backend/API. It is a FastAPI app and we are deploying it as a serverless API via Vercel.

Keep comments concise, only put if needed, to explain your intention, and not how it works. Keep code comments simple, and easy to understand.

# Features to be included

1. To serve information regarding Prasarana's bus stops in Klang Valley.
2. To serve information regarding Prasarana's bus routes in Klang Valley.
3. To serve information on buses's latest location.
4. To serve the ETA of bus arrival.

# Pull Request Convention

Changes are not allowed to be commited directly to main branch, rather, we will need to raise a PR, directed to main branch.

When creating a PR, its title should be: `<type>([optional scope]): <description>`

## Type

`build` - Changes that affect the build system or external dependencies (dependencies update)
`ci` - Changes to our CI configuration files and scripts (basically directory .github/workflows)
`docs` - Documentation only changes
`feat` - A new feature
`fix` - A bug fix
`chore` - Changes which does not touch the code (ex. manual update of release notes). It will not generate release notes changes
`refactor` - A code change that contains refactor
`style` - Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
`test` - Adding missing tests or correcting existing tests and also changes for our test app

# Technical Details

1. FastAPI app
2. To use Python 3.14
3. Serverless