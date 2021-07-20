# 简介

## Fork

### Procedure

![procedure](https://github.com/dtcokr/v2ray-rules-dat/raw/master/procedure.png)

### Custom

- 加入大量自定义黑名单域名

  - DEVELOPERDAN_ADS_TRACKING

  https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt

  - POLISHFILTERSTEAM_KADHOSTS

  https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt

  - VELESILA_YHOSTS

  https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts

  - MATOMO_REFERRER_SPAM

  https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt

  - WINHELP2002

  https://winhelp2002.mvps.org/hosts.txt

  - NEOFELHZ_NEOHOSTS

  https://v.firebog.net/hosts/neohostsbasic.txt

  - ROONEYMCNIBNUG_SNAFU

  https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt

  - PAULGB_BARBBLOCK

  https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt

  - ADAWAY

  https://adaway.org/hosts.txt

  - LANIKSJ_ADMIRAL

  https://v.firebog.net/hosts/Admiral.txt

  - ANUDEEPND_BLACKLIST

  https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt

  - DISCONNECT_ADS

  https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt

  - HOSTSVN

  https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts

  - JDLINGYU_ADWARS

  https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts

  - EASYPRIVACY

  https://v.firebog.net/hosts/Easyprivacy.txt

  - FABRICEPRIGENT_ADS

  https://v.firebog.net/hosts/Prigent-Ads.txt

  - FADEMIND_TRACKERS

  https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts

  - GEOFFREYFROGEYE_FIRSTPARTY

  https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt

  - KEES1958_TOP_ADS_TRACKERS

  https://raw.githubusercontent.com/Kees1958/W3C_annual_most_used_survey_blocklist/master/TOP_EU_US_Ads_Trackers_HOST

  - GEOFFREYFROGEYE_MULTIPARTY

  https://hostfiles.frogeye.fr/multiparty-trackers-hosts.txt

  - PERFLYST_ANDROID_TRACKERS

  https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt

  - PERFLYST_SMARTTV

  https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt

  - QUIDSUP_TRACKERS

  https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt

  - DANDELIONSPROUT_ANTI_MALWARE

  https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt

  - DIGITALSIDE_THREATINTEL

  https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt

  - FABRICEPRIGENT_CRYPTOJACKING

  https://v.firebog.net/hosts/Prigent-Crypto.txt

  - DISCONNECT_MALVERTISING

  https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt

  - MANDIANT_APT1_REPORT

  https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt

  - PHISHINGARMY_EXTENDED

  https://phishing.army/download/phishing_army_blocklist_extended.txt

  - QUIDSUP_MALICIOUS

  https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt

  - SHALLA_MALICIOUS

  https://v.firebog.net/hosts/Shalla-mal.txt

  - SPAM404

  https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt

  - FADEMIND_RISKY_HOSTS

  https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts

  - URLHAUS_MALICIOUS

  https://urlhaus.abuse.ch/downloads/hostfile/

  - ZERODOT1_COINBLOCKLISTS

  https://zerodot1.gitlab.io/CoinBlockerLists/hosts_browser

  - ANUDEEPND_FACEBOOK

  https://raw.githubusercontent.com/anudeepND/blacklist/master/facebook.txt

  - PRIVACYPROTECTIONTOOLS_ANTIAD

  https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-domains.txt

  - DEVINEENGINE_HIJACKING

  https://raw.githubusercontent.com/DivineEngine/Profiles/master/Quantumult/Filter/Guard/Hijacking.list

  - DEVINEENGINE_ADVERTISING

  https://raw.githubusercontent.com/DivineEngine/Profiles/master/Quantumult/Filter/Guard/Advertising.list

  - DEVINEENGINE_PRIVACY

  https://raw.githubusercontent.com/DivineEngine/Profiles/master/Quantumult/Filter/Guard/Privacy.list

  - EHPO1_LIBY

  https://raw.githubusercontent.com/eHpo1/Rules/master/QuantumultX/Filter/Liby.txt

  - GEQ1AN_ADBLOCK

  https://raw.githubusercontent.com/GeQ1an/Rules/master/QuantumultX/Filter/AdBlock.list

  - NOBYDA_ADBLOCK

  https://raw.githubusercontent.com/NobyDa/ND-AD/master/QuantumultX/AD_Block.txt

  - NOBYDA_ADBLOCK_PLUS

  https://raw.githubusercontent.com/NobyDa/ND-AD/master/QuantumultX/AD_Block_Plus.txt

  - URLHAUS_MALICIOUS_FULL

  https://curben.gitlab.io/malware-filter/urlhaus-filter-hosts.txt
  
  - 移动、联通、电信、极验一键登录 / 后台获取手机号

    ```
    114dev.com
    cmpassport.com
    id6.me
    nishub1.10010.com
    opencloud.wostore.cn
    onepass.geetest.com
    ```
  
  - JiGuang Push / JPush / 极光推送
  
    ```
    jpush.cn
    easytomessage.com
    jpush.io
    jiguang.cn
    ```
    
  https://www.icsi.berkeley.edu/pubs/privacy/TR-20-001.pdf
  
  - BLUESKYXN_AGHR
  
  https://github.com/BlueSkyXN/AdGuardHomeRules

  - StevenBlack-fakenews-gambling

  https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts

  - NOTRACKING_BLOCKLISTS

  https://raw.githubusercontent.com/notracking/hosts-blocklists/master/dnscrypt-proxy/dnscrypt-proxy.blacklist.txt

  - HOSHSADIQ_NOCOIN

  https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt

---

[**V2Ray**](https://github.com/v2fly/v2ray-core) 路由规则文件加强版，可代替 V2Ray 官方 `geoip.dat` 和 `geosite.dat`，兼容 [Shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows)、[Xray-core](https://github.com/XTLS/Xray-core)、[Trojan-Go](https://github.com/p4gefau1t/trojan-go) 和 [leaf](https://github.com/eycorsican/leaf)。利用 GitHub Actions 北京时间每天早上 6 点自动构建，保证规则最新。

## 规则文件生成方式

### geoip.dat

- 通过仓库 [@Loyalsoldier/geoip](https://github.com/Loyalsoldier/geoip) 生成
- 其中全球 IP 地址（IPv4 和 IPv6）来源于 [MaxMind GeoLite2](https://dev.maxmind.com/geoip/geoip2/geolite2/)，`CN`（中国大陆）类别下的 IPv4 地址来源于 [ipip.net](https://github.com/17mon/china_ip_list)
- 新增 `geoip:telegram` 类别，方便黑名单模式用户使用

> 希望定制 `geoip.dat` 文件？查看仓库 [@Loyalsoldier/geoip](https://github.com/Loyalsoldier/geoip)。

### geosite.dat

- 基于 [@v2fly/domain-list-community/data](https://github.com/v2fly/domain-list-community/tree/master/data) 数据，通过仓库 [@Loyalsoldier/domain-list-custom](https://github.com/Loyalsoldier/domain-list-custom) 生成
- **加入大量中国大陆域名、Apple 域名和 Google 域名**：
  - [@felixonmars/dnsmasq-china-list/accelerated-domains.china.conf](https://github.com/felixonmars/dnsmasq-china-list/blob/master/accelerated-domains.china.conf) 加入到 `geosite:cn` 类别中
  - [@felixonmars/dnsmasq-china-list/apple.china.conf](https://github.com/felixonmars/dnsmasq-china-list/blob/master/apple.china.conf) 加入到 `geosite:geolocation-!cn` 类别中（如希望本文件中的 Apple 域名直连，请参考下面 [geosite 的 Routing 配置方式](https://github.com/Loyalsoldier/v2ray-rules-dat#geositedat-1)）
  - [@felixonmars/dnsmasq-china-list/google.china.conf](https://github.com/felixonmars/dnsmasq-china-list/blob/master/google.china.conf) 加入到 `geosite:geolocation-!cn` 类别中（如希望本文件中的 Google 域名直连，请参考下面 [geosite 的 Routing 配置方式](https://github.com/Loyalsoldier/v2ray-rules-dat#geositedat-1)）
- **加入 GFWList 域名**：
  - 基于 [@gfwlist/gfwlist](https://github.com/gfwlist/gfwlist) 数据，通过仓库 [@cokebar/gfwlist2dnsmasq](https://github.com/cokebar/gfwlist2dnsmasq) 和 [@pexcn/gfwlist-extras](https://github.com/pexcn/gfwlist-extras) 生成
  - 加入到 `geosite:gfw` 类别中，供习惯于 PAC 模式并希望使用 [GFWList](https://github.com/gfwlist/gfwlist) 的用户使用
  - 同时加入到 `geosite:geolocation-!cn` 类别中
- **加入 Greatfire Analyzer 检测到的屏蔽域名**：
  - 通过仓库 [@Loyalsoldier/cn-blocked-domain](https://github.com/Loyalsoldier/cn-blocked-domain) 获取 [Greatfire Analyzer](https://zh.greatfire.org/analyzer) 检测到的在中国大陆被屏蔽的域名
  - 加入到 `geosite:greatfire` 类别中，可与上面的 `geosite:gfw` 类别同时使用，以达到域名黑名单的效果
  - 同时加入到 `geosite:geolocation-!cn` 类别中
- **加入 EasyList 和 EasyListChina 广告域名**：通过 [@AdblockPlus/EasylistChina+Easylist.txt](https://easylist-downloads.adblockplus.org/easylistchina+easylist.txt) 获取并加入到 `geosite:category-ads-all` 类别中
- **加入 AdGuard DNS Filter 广告域名**：通过 [@AdGuard/DNS-filter](https://kb.adguard.com/en/general/adguard-ad-filters#dns-filter) 获取并加入到 `geosite:category-ads-all` 类别中
- **加入 Peter Lowe 广告和隐私跟踪域名**：通过 [@PeterLowe/adservers](https://pgl.yoyo.org/adservers) 获取并加入到 `geosite:category-ads-all` 类别中
- **加入 Dan Pollock 广告域名**：通过 [@DanPollock/hosts](https://someonewhocares.org/hosts) 获取并加入到 `geosite:category-ads-all` 类别中
- **加入 Windows 操作系统相关的系统升级和隐私跟踪域名**：
  - 基于 [@crazy-max/WindowsSpyBlocker](https://github.com/crazy-max/WindowsSpyBlocker/tree/master/data/hosts) 数据
  - [**慎用**] Windows 操作系统使用的隐私跟踪域名 [@crazy-max/WindowsSpyBlocker/hosts/spy.txt](https://github.com/crazy-max/WindowsSpyBlocker/blob/master/data/hosts/spy.txt) 加入到 `geosite:win-spy` 类别中
  - [**慎用**] Windows 操作系统使用的系统升级域名 [@crazy-max/WindowsSpyBlocker/hosts/update.txt](https://github.com/crazy-max/WindowsSpyBlocker/blob/master/data/hosts/update.txt) 加入到 `geosite:win-update` 类别中
  - [**慎用**] Windows 操作系统附加的隐私跟踪域名 [@crazy-max/WindowsSpyBlocker/hosts/extra.txt](https://github.com/crazy-max/WindowsSpyBlocker/blob/master/data/hosts/extra.txt) 加入到 `geosite:win-extra` 类别中
  - 关于这三个类别的使用方式，请参考下面 [geosite 的 Routing 配置方式](https://github.com/Loyalsoldier/v2ray-rules-dat#geositedat-1)
- **加入更多代理域名**：通过仓库 [@lhie1/Rules](https://github.com/lhie1/Rules/tree/master) 获取更多代理域名，并加入到 `geosite:geolocation-!cn` 类别中
- **可添加自定义直连、代理和广告域名**：由于上游域名列表更新缓慢或缺失某些域名，所以引入**需要添加的域名**列表。[`hidden 分支`](https://github.com/Loyalsoldier/v2ray-rules-dat/tree/hidden)里的三个文件 `direct.txt`、`proxy.txt` 和 `reject.txt`，分别存放自定义的需要添加的直连、代理、广告域名，最终分别加入到 `geosite:cn`、`geosite:geolocation-!cn` 和 `geosite:category-ads-all` 类别中
- **可移除自定义直连、代理和广告域名**：由于上游域名列表存在需要被移除的域名，所以引入**需要移除的域名**列表。[`hidden 分支`](https://github.com/Loyalsoldier/v2ray-rules-dat/tree/hidden)里的三个文件 `direct-need-to-remove.txt`、`proxy-need-to-remove.txt` 和 `reject-need-to-remove.txt`，分别存放自定义的需要从 `direct-list`（直连域名列表）、`proxy-list`（代理域名列表）和 `reject-list`（广告域名列表） 移除的域名


## 参考配置

### geoip.dat

跟 V2Ray 官方 `geoip.dat` 配置方式相同。

**Routing 配置方式**：

```json
"routing": {
  "rules": [
    {
      "type": "field",
      "outboundTag": "Direct",
      "ip": [
        "223.5.5.5/32",
        "119.29.29.29/32",
        "180.76.76.76/32",
        "114.114.114.114/32",
        "geoip:cn",
        "geoip:private"
      ]
    },
    {
      "type": "field",
      "outboundTag": "Proxy",
      "ip": [
        "1.1.1.1/32",
        "1.0.0.1/32",
        "8.8.8.8/32",
        "8.8.4.4/32",
        "geoip:us",
        "geoip:ca",
        "geoip:telegram"
      ]
    }
  ]
}
```

### geosite.dat

跟 V2Ray 官方 `geosite.dat` 配置方式相同。相比官方 `geosite.dat` 文件，本项目特有的类别：

- `geosite:apple-cn`：包含 [@felixonmars/dnsmasq-china-list/apple.china.conf](https://github.com/felixonmars/dnsmasq-china-list/blob/master/apple.china.conf) 文件里的域名，供希望 Apple 域名直连（不走代理）的用户使用。
- `geosite:google-cn`：包含 [@felixonmars/dnsmasq-china-list/google.china.conf](https://github.com/felixonmars/dnsmasq-china-list/blob/master/google.china.conf) 文件里的域名，供希望 Google 域名直连（不走代理）的用户使用。
- [**慎用**]`geosite:win-spy`：包含 [@crazy-max/WindowsSpyBlocker/hosts/spy.txt](https://github.com/crazy-max/WindowsSpyBlocker/blob/master/data/hosts/spy.txt) 文件里的域名，供希望屏蔽 Windows 操作系统隐私跟踪域名的用户使用。
- [**慎用**]`geosite:win-update`：包含 [@crazy-max/WindowsSpyBlocker/hosts/update.txt](https://github.com/crazy-max/WindowsSpyBlocker/blob/master/data/hosts/update.txt) 文件里的域名，供希望屏蔽 Windows 操作系统自动升级的用户使用。
- [**慎用**]`geosite:win-extra`：包含 [@crazy-max/WindowsSpyBlocker/hosts/extra.txt](https://github.com/crazy-max/WindowsSpyBlocker/blob/master/data/hosts/extra.txt) 文件里的域名，供希望屏蔽 Windows 操作系统附加隐私跟踪域名的用户使用。

> ⚠️ 注意：在 Routing 配置中，类别越靠前（上），优先级越高，所以 `geosite:apple-cn` 和 `geosite:google-cn` 要放置在 `geosite:geolocation-!cn` 前（上）面才能生效。

#### 高级用法

v2fly/domain-list-community 项目 [data](https://github.com/v2fly/domain-list-community/tree/master/data) 目录中某些列表里的规则会被标记诸如 `@cn` 的 attribute（如下所示），意为该域名在中国大陆有接入点，可直连。

```
steampowered.com.8686c.com @cn
steamstatic.com.8686c.com @cn
```

对于玩 Steam 国区游戏，想要直连的用户，可以设置类别 `geosite:steam@cn` 为直连，意为将 [steam](https://github.com/v2fly/domain-list-community/blob/master/data/steam) 列表内所有被标记了 `@cn` attribute 的规则（域名）设置为直连。同理，由于 [category-games](https://github.com/v2fly/domain-list-community/blob/master/data/category-games) 列表包含了 `steam`、`ea`、`blizzard`、`epicgames` 和 `nintendo` 等常见的游戏厂商。设置类别 `geosite:category-games@cn` 为直连，即可节省大量服务器流量。

> ⚠️ 注意：在 Routing 配置中，类别越靠前（上），优先级越高，所以 `geosite:category-games@cn` 等所有带有 `@cn` attribute 的规则都要放置在 `geosite:geolocation-!cn` 前（上）面才能生效。
> 
> `category-games` 列表内的规则（域名）可能会有疏漏，请留意规则命中情况。如发现遗漏，欢迎到项目 v2fly/domain-list-community 提 [issue](https://github.com/v2fly/domain-list-community/issues) 反馈。

#### 配置参考下面 👇👇👇

**白名单模式 Routing 配置方式**：

```json
"routing": {
  "rules": [
    {
      "type": "field",
      "outboundTag": "Reject",
      "domain": [
        "geosite:category-ads-all"
      ]
    },
    {
      "type": "field",
      "outboundTag": "Direct",
      "domain": [
        "geosite:private",
        "geosite:apple-cn",
        "geosite:google-cn",
        "geosite:tld-cn",
        "geosite:category-games@cn"
      ]
    },
    {
      "type": "field",
      "outboundTag": "Proxy",
      "domain": [
        "geosite:geolocation-!cn"
      ]
    },
    {
      "type": "field",
      "outboundTag": "Direct",
      "domain": [
        "geosite:cn"
      ]
    },
    {
     "type": "field",
     "outboundTag": "Proxy",
     "network": "tcp,udp"
    }
  ]
}
```

**黑名单模式 Routing 配置方式：**

```json
"routing": {
  "rules": [
    {
      "type": "field",
      "outboundTag": "Reject",
      "domain": [
        "geosite:category-ads-all"
      ]
    },
    {
      "type": "field",
      "outboundTag": "Proxy",
      "domain": [
        "geosite:tld-!cn",
        "geosite:gfw",
        "geosite:greatfire"
      ]
    },
    {
      "type": "field",
      "outboundTag": "Proxy",
      "ip": [
        "geoip:telegram"
      ]
    },
    {
     "type": "field",
     "outboundTag": "Direct",
     "network": "tcp,udp"
    }
  ]
}
```

**DNS 配置方式**：

```json
"dns": {
  "servers": [
    {
      "address": "114.114.114.114",
      "port": 53,
      "domains": [
        "geosite:cn",
        "geosite:category-games@cn"
      ],
      "expectIPs": [
        "geoip:cn"
      ]
    },
    {
      "address": "https://1.1.1.1/dns-query",
      "domains": [
        "geosite:geolocation-!cn"
      ]
    },
    "https+local://223.5.5.5/dns-query",
    "119.29.29.29"
  ]
}
```


## 致谢

- [@v2fly/geoip](https://github.com/v2fly/geoip)
- [@Loyalsoldier/geoip](https://github.com/Loyalsoldier/geoip)
- [@v2fly/domain-list-community](https://github.com/v2fly/domain-list-community)
- [@Loyalsoldier/domain-list-custom](https://github.com/Loyalsoldier/domain-list-custom)
- [@felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)
- [@gfwlist/gfwlist](https://github.com/gfwlist/gfwlist)
- [@pexcn/gfwlist-extras](https://github.com/pexcn/gfwlist-extras)
- [@cokebar/gfwlist2dnsmasq](https://github.com/cokebar/gfwlist2dnsmasq)
- [@Loyalsoldier/cn-blocked-domain](https://github.com/Loyalsoldier/cn-blocked-domain)
- [@lhie1/Rules](https://github.com/lhie1/Rules/tree/master)
- [@AdblockPlus/EasylistChina+Easylist.txt](https://easylist-downloads.adblockplus.org/easylistchina+easylist.txt)
- [@AdGuard/DNS-filter](https://kb.adguard.com/en/general/adguard-ad-filters#dns-filter)
- [@PeterLowe/adservers](https://pgl.yoyo.org/adservers)
- [@DanPollock/hosts](https://someonewhocares.org/hosts)
- [@crazy-max/WindowsSpyBlocker](https://github.com/crazy-max/WindowsSpyBlocker)
