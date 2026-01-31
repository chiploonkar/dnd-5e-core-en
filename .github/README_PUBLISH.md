# Publishing to PyPI via GitHub Actions

This repository includes a GitHub Actions workflow `.github/workflows/publish.yml` that will build and upload the package to PyPI when a tag matching `v*.*.*` is pushed (for example `v0.4.3`).

Steps to configure and use:

1. Create a PyPI API token:
   - Go to https://pypi.org/manage/account/#api-tokens and create a new token with an appropriate scope (preferably restricted to this project).
   - Copy the token once (it won't be shown again).

2. Add the token to GitHub secrets:
   - Go to your repository settings -> Secrets -> Actions
   - Create a new repository secret named `PYPI_API_TOKEN` and paste the token value.

3. Create and push a tag to trigger the release:
```bash
# from your local clone
git checkout main
git pull origin main
# bump version in pyproject.toml and dnd_5e_core/__init__.py
git add pyproject.toml dnd_5e_core/__init__.py CHANGELOG.md
git commit -m "Release 0.4.3"
git tag -a v0.4.3 -m "Release 0.4.3"
git push origin main
git push origin v0.4.3
```

4. Monitor the Actions tab on GitHub to see the workflow run and publication status.

Security note:
- Never store the token in the repository or paste it in chat. Use GitHub secrets.
- Revoke and rotate tokens if they are ever exposed.
