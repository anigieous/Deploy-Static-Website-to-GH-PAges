# Deploy Website To GitHub Pages

This action Deploys your static website and Dynamic code Github Pages.

## How to Setup this action in your Workflow:

### Deploy Static Website to Github Pages

<!-- start usage -->
```yaml
- name: Deploy to GitHub Pages
  uses: anigieous/Deploy-Website-to-GH-Pages/Static@version
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
#### Note*
Make sure you have this script in your package.json file.
```
"deploy": "gh-pages -d build -t -r https://$npm_config_token@github.com/your_username/your_repo_name.git"
```

<!-- start usage -->
```yaml
- name: Deploy and Build
  uses: anigieous/Deploy-Website-to-GH-Pages/Dynamic@version
  with:
    # GitHub Username for making commit
    username: your_github_username

    # Email for making commit
    email: your_email_id

    # you_personal_access_token for deploying your code
    GITHUB_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}

```
<!-- end usage -->

## Requirements
### For Deploying Static Website you should enable deploy from your Repository setting:
Steps:
- Move to Setting of your Repository.
- Move to Pages.
- Select source as Github Action.

### For Deploying Dynamic Website you should enable deploy from your Repository setting:
Steps:
- Move to Setting of your Repository.
- Move to Pages.
- Select source as Deploy from Branch.

