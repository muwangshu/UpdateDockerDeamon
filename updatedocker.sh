sudo mkdir -p /etc/docker
# 写入配置文件
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [
    "hub.fast360.xyz",
    "hub.rat.dev",
    "hub.littlediary.cn",
    "docker.kejilion.pro",
    "dockerpull.cn",
    "docker-0.unsee.tech",
    "docker.tbedu.top",
    "docker.1panelproxy.com",
    "docker.melikeme.cn",
    "cr.laoyou.ip-ddns.com",
    "hub.firefly.store",
    "docker.hlmirror.com",
    "docker.m.daocloud.io",
    "docker.1panel.live",
    "image.cloudlayer.icu",
    "docker.1ms.run"
  ]
}
EOF
# 重启docker服务
sudo systemctl daemon-reload && sudo systemctl restart docker
