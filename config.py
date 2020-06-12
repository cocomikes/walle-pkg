#!/usr/bin/python  
#-*-coding:utf-8-*-

#keystore信息
#Windows 下路径分割线请注意使用\\转义
keystorePath = "../signature/xxx.jks"
keyAlias = "app"
keystorePassword = "123456"
keyPassword = "123456"

#加固后的源文件名（未重签名）每次发布新版时务必更新名称
protectedSourceApkName = "xxx_legu.apk"
#加固后的源文件所在文件夹路径(...path),注意结尾不要带分隔符，默认在此文件夹根目录
protectedSourceApkDirPath = ""
#渠道包输出路径，默认在此文件夹channels目录下
channelsOutputFilePath = ""
#渠道名配置文件路径，只支持渠道写入, 默认在此文件夹根目录
channelFilePath = ""
#额外信息配置文件（绝对路径，例如/Users/mac/Desktop/walle360/config.json）
#配置信息示例参看https://github.com/Meituan-Dianping/walle/blob/master/app/config.json
extraConfigFilePath = ""
#Android SDK buidtools path , please use above 25.0+
sdkBuildToolPath = "/Users/mikes/Library/Android/sdk/build-tools/28.0.3"
