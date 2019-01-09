#!/bin/bash

echo "优化Github访问速度"

echo "151.101.72.249 github.global.ssl.fastly.net" >> /etc/hosts
echo "192.30.253.112 github.com" >> /etc/hosts

echo "安装软件包"
yum install -y vim tmux epel-release git
yum install -y python36 python36-devel


echo "调整系统配置"
sed -i "s/#UseDNS yes/UseDNS no/" /etc/ssh/sshd_config
systemctl reload sshd


echo "增加自定义设置"
echo "alias ..='cd ..'" >> /root/.bashrc
echo "export TERM=xterm-256color" >> /root/.bash_profile
