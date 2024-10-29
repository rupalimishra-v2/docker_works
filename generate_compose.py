import os

def generate_docker_compose():
    base_path = os.path.dirname(os.path.abspath(__file__))
    plugins_path = os.path.join(base_path, 'plugins')
    
    services = []

    # Iterate through each directory in plugins
    for plugin in os.listdir(plugins_path):
        plugin_path = os.path.join(plugins_path, plugin)
        if os.path.isdir(plugin_path):
            service_definition = f"""
  {plugin}:
    build:
      context: {plugin_path}
      dockerfile: Dockerfile
    environment:
      - SERVICE_API_KEY=${{SERVICE_API_KEY}}
    ports:
      - "800{len(services)}:8000"  # Assign unique ports for each service
    volumes:
      - {plugin_path}:/app
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
            """
            services.append(service_definition)

    # Combine all services into the final docker-compose.yml
    final_compose = "version: '3.8'\nservices:\n" + ''.join(services)
    
    # Write the docker-compose.yml file
    with open(os.path.join(base_path, 'docker-compose.yml'), 'w') as f:
        f.write(final_compose)
        print("docker-compose.yml generated successfully.")

if __name__ == "__main__":
    generate_docker_compose()
