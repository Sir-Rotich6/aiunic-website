# Quick Reference - Upload to GitHub

## Fastest Method: GitHub Web Interface

1. **Create Repository**
   - Go to: https://github.com/new
   - Name: `aiunic-website`
   - DON'T initialize with README
   - Click "Create repository"

2. **Upload Files**
   - Click "uploading an existing file"
   - Drag all 11 files
   - Commit message: "Initial commit"

3. **Create Workflow File**
   - Click "Add file" → "Create new file"
   - Name: `.github/workflows/deploy.yml`
   - Copy content from deploy.yml
   - Commit

4. **Enable GitHub Pages**
   - Settings → Pages
   - Source: gh-pages branch
   - Save

5. **Access Website**
   - Wait 2-3 minutes
   - Visit: https://USERNAME.github.io/aiunic-website/

## Files Checklist

- [ ] index.html
- [ ] styles.css
- [ ] script.js
- [ ] README.md
- [ ] LICENSE
- [ ] .gitignore
- [ ] CONTRIBUTING.md
- [ ] SETUP.md
- [ ] setup.sh
- [ ] setup.bat
- [ ] .github/workflows/deploy.yml

## Command Line (Alternative)

```bash
git init
git add .
git commit -m "Initial commit - AIUnic website"
git branch -M main
git remote add origin https://github.com/USERNAME/aiunic-website.git
git push -u origin main
```

## Your Live URL

https://YOUR-USERNAME.github.io/aiunic-website/

---
All files are ready. Upload now! 🚀
