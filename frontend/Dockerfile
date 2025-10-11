FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy project files
COPY . .

# Debug: list files and contents
RUN ls -la
RUN ls -la src
RUN ls -la public

# Build the app with verbose output
RUN npx react-scripts build

# Debug: list build contents
RUN ls -la build/

# Install serve
RUN npm install -g serve

# Expose port
EXPOSE 3000

# Start the app in production mode
CMD ["npx", "serve", "-s", "build", "-p", "3000"]
