#!/bin/bash

# 检查是否提供了提交消息和分支名称
if [ -z "$1" ]; then
  echo "请提供提交消息。用法: ./git_commit_push.sh '你的提交消息' '分支名称'"
  exit 1
fi

if [ -z "$2" ]; then
  echo "请提供分支名称。用法: ./git_commit_push.sh '你的提交消息' '分支名称'"
  exit 1
fi

# 执行 git 命令
git add .
git commit -m "$1"
git push origin "$2"
