# lasier-poc

## Setup

```sh
poetry install
poetry shell
docker-compose up -d

# Wait docker-compose setup and run the command below
inv init-unleash
```

## Run

```sh
# Open in another terminal
inv run --app=provider

# Open in another terminal
inv run --app=proxy

# Open in another terminal
int run --app=client
```

## Visualize

Open [Unleash Dashboard](http://127.0.0.1:4242/) and [Redis Commander
Dashboard](http://127.0.0.1:8081/).
