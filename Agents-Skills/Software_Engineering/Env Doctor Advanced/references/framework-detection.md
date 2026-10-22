# Environment Configuration Framework Detection

## CI/CD Platforms

### GitHub Actions
- Config: `.github/workflows/*.yml`
- Env vars: `env:` block, `secrets.*`, `${{ secrets.* }}`
- Runners: `runs-on:` (ubuntu-latest, windows-latest, macos-latest)
- Version matrix: `strategy.matrix`

### CircleCI
- Config: `.circleci/config.yml`
- Env vars: `environment:` block, `<< pipeline.parameters.* >>`
- Executors: `docker:`, `machine:`, `macos:`

### GitLab CI
- Config: `.gitlab-ci.yml`
- Env vars: `variables:`, `$CI_*` predefined variables
- Runners: `tags:`, `image:`

## Container Environments

### Docker
- Dockerfile: `ENV`, `ARG`, `EXPOSE`
- docker-compose.yml: `environment:`, `env_file:`, `.env`
- .dockerignore: exclude `.env` from build context

### Kubernetes
- ConfigMaps: `kubectl create configmap`
- Secrets: `kubectl create secret`
- Pod specs: `env:`, `envFrom:`

## Runtime Detection

### Node.js
- Version: `package.json` → `engines.node`, `.nvmrc`, `.node-version`
- Env loading: `dotenv` package, `process.env`
- Scripts: `package.json` → `scripts`

### Python
- Version: `pyproject.toml` → `requires-python`, `.python-version`, `runtime.txt`
- Env loading: `python-dotenv`, `os.environ`, `os.getenv`
- Virtual env: `venv/`, `.venv/`, `Pipfile`

### Go
- Version: `go.mod` → `go X.Y`
- Env loading: `os.Getenv`, `os.LookupEnv`
- Build tags: `//go:build`
