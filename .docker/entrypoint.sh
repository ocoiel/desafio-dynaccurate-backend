#!/bin/sh
export PATH="/opt/poetry/bin:$PATH"

#!/bin/bash
set -e

# Wait for the database to be ready
# ./wait-for-it.sh -t 60 db:5432

# Set up the database
echo "Setting up the database..."
prisma db push --schema src/infrastructure/database/prisma/schema.prisma

# Run the app
exec "$@"
