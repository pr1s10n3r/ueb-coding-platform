# Frontend

This is the frontend application layer of the _UEB Coding Platform_.

## Setup Local Development Environment

You will need the last version of [Node](https://nodejs.org/en/) and [NPM](https://www.npmjs.com/).

1. Clone the project to your computer using git.
2. Move inside the `frontend` directory.
3. Install dependencies using `npm install`.
4. Run the project using `npm run dev`.

Also, you will need to create a local `.env.local` file for testing purposes. Here is the structure of that file:

```shell
# .env.local
BACKEND_BASE_URL=http://localhost:8000
```

## Build

```shell
# Build for staging
$ vite build --mode stating
# Build for production
$ vite build --mode prod
```
