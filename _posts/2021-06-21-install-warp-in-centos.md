---
layout:     post
title:      "在CentOS上安装并使用WARP代理出口ip (解锁Netflix IP限制）"
subtitle:   "How to install WARP in CentOS"
date:       2021-06-21 15:01:31
author:     "xxxbrian"
catalog: true
header-img: "img/in-post/2021-06-21-install-warp-in-centos/bg-Netflix.png"
header-mask: 0.4
tags:
  - 笔记
  - CentOS
  - Netflix
  - 梯子
---

## WARP

Cloudflare WARP 是 Cloudflare 推出的一项网络隐私保护服务, 通过添加WARP出口可以绕过Netflix等流媒体对代理ip的封锁。([Cloudefare官方中文介绍](https://blog.cloudflare.com/zh-cn/warp-for-desktop-zh-cn/))

## WGCF

[WGCF](https://github.com/ViRb3/wgcf)是WARP的非官方cli客户端。

通过WGCF可以VPS添加ipv4，ipv6代理,以达到解锁Netflix的目的。

### 安装wgcf

执行以下命令：

```shell
mkdir wgcf
cd wgcf
wget -O wgcf https://github.com/ViRb3/wgcf/releases/download/v2.2.4/wgcf_2.2.4_linux_amd64
chmod +x wgcf
```

初次使用需要注册用户并生成配置文件：

```shell
./wgcf register
./wgcf generate
```

随后就可以在程序目录中找到`wgcf-account.toml`和`wgcf-profile.conf`两个新生成的文件。

### 配置wgcf

`wgcf-account.toml`是你的WARP账户信息，如果你有WARP+账户可以替换成你自己的账户; `wgcf-profile.conf`是WireGuard的配置文件，下载到本地保存。

#### 修改wgcf-profile.conf

**WG连接后是内核层级的软件，会建立自己的虚拟网卡，且WARP客户端均为内网NAT地址，当双栈流量均被WG接管后我们就无法再从原有的IP连接到服务器了。因此在IPv4与IPv6之间必须做一个取舍，以防这样的情况发生。**

可以自己把`engage.cloudflareclient.com`解析成IP，对Endpoint修改成ipv4或者ipv6保存即可。

修改配置文件就两种情况：

* 最后一行`Endpoint=engage.cloudflareclient.com：2048`修改为`162.159.192.1:2408`,删除`AllowedIPs = 0.0.0.0/0`接管本地IPv4路由。
* 最后一行`Endpoint=engage.cloudflareclient.com：2048`修改为`[2606:4700:d0::a29f:c001]:2408`,删除`AllowedIPs = ::/0`接管本地IPv6路由。

### 安装Wireguard客户端

CentOS7：

```shell
sudo yum install epel-release elrepo-release
sudo yum install yum-plugin-elrepo
sudo yum install kmod-wireguard wireguard-tools
```

其它系统的命令可以参考[官方网站](https://www.wireguard.com/install/)

安装完成后，**重启VPS**。

### 配置Wireguard

把刚刚修改好的配置文件wgcf-profile.conf上传至`/etc/wireguard`,并重命名为`wgcf.conf`。

```shell
cp wgcf-profile.conf /etc/wireguard/wgcf.conf
```

### 启动wgcf

```shell
#加载内核模块
modprobe wireguard
#检查WG模块加载是否正常
lsmod | grep wireguard
```

开关隧道的命令为：

```shell
#开启隧道
sudo wg-quick up wgcf
#关闭隧道
sudo wg-quick down wgcf
```

如果VPS出口没有走ipv6的话，需要这编辑`/etc/gai.conf` 文件（没有的话就新建），修改为以下内容：

```text
label ::1/128 0
label ::/0 1
label fd01::/16 1
label 2002::/16 2
label ::/96 3
label ::ffff:0:0/96 4
label fec0::/10 5
label fc00::/7 6
label 2001:0::/32 7
precedence ::1/128 50
precedence ::/0 40
precedence fd01::/16 40
precedence 2002::/16 30
precedence ::/96 20
precedence ::ffff:0:0/96 10
```

检测是否可以观看Netflix：

```shell
wget -O nf https://github.com/sjlleo/netflix-verify/releases/download/2.6/nf_2.6_linux_amd64 && chmod +x nf && clear && ./nf
```

检测结果：

![Netflix-verify](/img/in-post/2021-06-21-install-warp-in-centos/netflix-verify.png)
