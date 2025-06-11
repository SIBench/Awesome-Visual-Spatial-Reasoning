#!/bin/bash

# 提示用户输入分支名
read -p "请输入要 pull 的分支名称: " branch

# 执行 git pull
git pull origin "$branch"

