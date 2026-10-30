## CI/CD Pipeline — GitHub Actions

The project uses GitHub Actions to automatically validate, test, and build the application when code is pushed to GitHub or submitted through a pull request.

### Pipeline stages

1. **Source validation:** Checks Python and Bash syntax.
2. **Integration testing:** Runs automated pytest tests against a temporary PostgreSQL database.
3. **Docker build:** Builds the FastAPI application image using Docker Buildx.
4. **Image verification:** Confirms that the image includes the required dependencies and application files and is configured to run as a non-root user.

### Build caching

The pipeline uses GitHub Actions caching to reuse unchanged Docker build layers and reduce repeated build work.

### Troubleshooting

The project includes simulated CI failures involving application behavior and Dockerfile configuration, with successful recovery verified through subsequent pipeline runs.
