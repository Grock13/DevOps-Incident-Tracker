# Incident Report — INC-3001

## Incident Summary

A deployment configuration issue caused the AWS-hosted Incident API to become unavailable.

**Environment:** AWS EC2, Docker Compose, FastAPI, PostgreSQL

**Severity:** High — simulated training incident

## Symptoms

Describe what happened when you attempted to access the application.

## Investigation

1. Checked the EC2 instance and Docker container status.
2. Examined FastAPI application logs.
3. Verified PostgreSQL service health.
4. Inspected Docker networking.
5. Compared database connection settings with the running configuration.

## Root Cause

Document the incorrect database hostname and explain why the application failed.

## Resolution

Describe the configuration rollback and container recreation.

## Validation

- API health endpoint returned HTTP 200.
- Database connectivity was restored.
- Existing incident records remained available.
- Automated smoke tests passed.

## Prevention

- Validate application configuration before deployment.
- Add automated smoke tests after deployment.
- Maintain documented rollback procedures.
- Monitor container health and application logs.

## Lessons Learned

Verify logs for the diffeerent components to understand where the issue is.
