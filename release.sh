git add --all
git commit -m "$1"
git push && git push --mirror https://github.com/blairg23/fabricon-website
git status