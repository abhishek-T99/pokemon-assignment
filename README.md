# Pokemon Listing API

## Setting up the Project for Development

### Installation Steps

1. **Clone the repository**:

```bash
git clone https://github.com/abhishek-T99/pokemon-assignment.git
cd pokemon-assignment
```

2. **Install Python dependencies**:

```bash
pip install -r requirements.txt
```

3. **Create and configure the `.env` file.**:

   Create a `.env` file in the project root directory. A sample file `.env.example` is provided. Copy its content to `.env` and update the configuration variables accordingly.

```bash
cp .env.sample .env
```

4. **Run the database migration**:

```bash
alembic upgrade heads
```

5. **Run the FastAPI Project**:

   Start the FastAPI server with:

```bash
uvicorn app.main:app --reload
```

## API Workings

### Overview

The Pokemon Listing API is designed to fetch Pokemon data from an external API, store it in a local database, and serve requests from the database. This reduces the need to repeatedly call the external API and improves performance.

### Endpoints

1. **List Pokemon**

   - **Endpoint**: `/api/v1/pokemons/`
   - **Method**: `GET`
   - **Description**: Retrieves a paginated list of Pokemon from the database and fetches Pokemon data from the external API and store it in the database if database is  empty.

   ```bash
   curl http://localhost:8000/api/v1/pokemon?limit=10
   ```