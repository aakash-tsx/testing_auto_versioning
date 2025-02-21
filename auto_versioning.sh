#!/bin/bash

# ✅ Step 1: Get the latest Git tag
LATEST_TAG=$(git tag --sort=-v:refname | head -n 1)

# ✅ Step 2: Set initial version if no tag exists
if [[ -z "$LATEST_TAG" ]]; then
  NEW_VERSION="v1.0.0"  # Start from version 1.0.0
else
  # ✅ Step 3: Extract version numbers
  VERSION_NUM=$(echo "$LATEST_TAG" | sed 's/v//')
  MAJOR=$(echo "$VERSION_NUM" | cut -d. -f1)
  MINOR=$(echo "$VERSION_NUM" | cut -d. -f2)
  PATCH=$(echo "$VERSION_NUM" | cut -d. -f3)

  # ✅ Step 4: Auto-increment version based on commit message
  if git log -1 --pretty=%B | grep -q "#major"; then
    MAJOR=$((MAJOR + 1))
    MINOR=0
    PATCH=0
  elif git log -1 --pretty=%B | grep -q "#minor"; then
    MINOR=$((MINOR + 1))
    PATCH=0
  else
    PATCH=$((PATCH + 1))
  fi

  NEW_VERSION="v$MAJOR.$MINOR.$PATCH"
fi

# ✅ Step 5: Export new version to GitHub Actions
echo "NEW_VERSION=$NEW_VERSION" >> $GITHUB_ENV
echo "New Version: $NEW_VERSION"

# ✅ Step 6: Create a new Git tag and push
git tag -a $NEW_VERSION -m "Version $NEW_VERSION"
git push origin $NEW_VERSION
