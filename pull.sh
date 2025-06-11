#!/bin/bash

# 当前所在分支
current_branch=$(git rev-parse --abbrev-ref HEAD)

echo "🔄 Fetching all remote changes..."
git fetch --all --prune

# 获取所有本地分支
branches=$(git for-each-ref --format='%(refname:short)' refs/heads/)

echo "🔁 Pulling all local branches..."
for branch in $branches; do
    echo "📥 Switching to branch: $branch"
    git checkout "$branch" >/dev/null 2>&1

    # 检查是否有 upstream 远程追踪
    tracking=$(git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null)

    if [ -z "$tracking" ]; then
        echo "⚠️  Branch '$branch' has no upstream. Attempting to set to origin/$branch..."
        git branch --set-upstream-to=origin/$branch "$branch" 2>/dev/null
    fi

    echo "⬇️  Pulling latest for $branch..."
    git pull --ff-only
done

echo "🔙 Returning to original branch: $current_branch"
git checkout "$current_branch" >/dev/null 2>&1

echo "✅ All branches updated."
