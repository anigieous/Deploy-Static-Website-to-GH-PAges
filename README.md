# Deploy Website To GitHub Pages

This action Deploys your static website and Dynamic code Github Pages.

## How to Setup this action in your Workflow:

### Deploy Static Website to Github Pages

<!-- start usage -->
```yaml
- uses: anigieous/Deploy-Static-Website-to-GH-PAges/static@version
  with:
    # Repository name 
    # Default: ${{ github.repository }}
    repo_name: ''

    # you_personal_access_token for deploying your code
    token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}

```
<!-- end usage -->

### Deploy Dynamic Website to Github Pages
#### It build your website first using npm and than deploys your code to GitHub Pages

<!-- start usage -->
```yaml
- uses: anigieous/Deploy-Static-Website-to-GH-PAges/Dynamic@version
      with:
        # GitHub Username for making commit
        username: your_github_username

        # Email for making commit
        email: your_email_id

        # you_personal_access_token for deploying your code
        GITHUB_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}

```
<!-- end usage -->
