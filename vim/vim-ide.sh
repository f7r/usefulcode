#! /bin/bash
yum install -y http://mirror.ghettoforge.org/distributions/gf/gf-release-latest.gf.el7.noarch.rpm

# enable gf-plus
sed -i "13s/0/1/" /etc/yum.repos.d/gf.repo

yum makecache
yum install -y vim-enhanced vim-minimal cmake python34-devel kernel-devel

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

mv vimrc ~/.vimrc
mv pylintrc ~/.pylintrc

vim +PluginInstall +qall
~/.vim/bundle/YouCompleteMe/install.py

echo "export TERM=xterm-256color" >> ~/.bashrc
#pip install pylint flake8
