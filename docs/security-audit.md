# Incident API — Container Security Audit

## Objective

Improve the security and reliability of the Dockerized FastAPI and PostgreSQL application.

## Security Review

| Area | Improvement |
|---|---|
| Image security | Scanned the container image for known vulnerabilities |
| Container user | Configured the API to run as a non-root user |
| File permissions | Enabled a read-only application filesystem |
| Linux capabilities | Dropped unnecessary container capabilities |
| Privilege escalation | Enabled `no-new-privileges` |
| Secrets management | Moved the database password to a Docker Compose secret |
| Resource usage | Applied CPU and memory limits |
| Network access | Kept PostgreSQL accessible through the private Docker network |

## Validation Performed

- Verified application and database health checks
- Tested existing API endpoints
- Confirmed database records were preserved
- Verified that application directories could not be modified
- Confirmed authorized temporary file writes still worked
- Checked that the database password was no longer exposed as an environment variable
- Ran automated API tests

## Vulnerability Scan Results

Document the actual Docker Scout findings and any remaining remediation work.

## Lessons Learned

Container security requires controlling user permissions, secrets, filesystem access, resources, and vulnerable dependencies. Security controls should be tested to ensure they do not prevent legitimate application behavior.
