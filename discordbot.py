import discord
from discord.ext import commands, tasks
import os
import sys
import asyncio
import re
client = discord.Client()
bot=commands.Bot(command_prefix='k!')
client =commands.Bot(command_prefix='k!')
bot.remove_command('help')
       
@client.command()
async def addgchat(ctx):
    await ctx.send('>>> グローバルチャットを有効にします。\n``コロッケーグローバル`` というチャンネルを作成して下さい。')
@bot.command()
async def addgchat2(ctx):
    await ctx.send("まず``コロッケーグローバル2``を作成しウェブフックを押しウェブフックを作成を押して名前``コロッケーグローバル2``というウェブフックを作るとできます。")

@client.command()
async def inviteベータ(ctx):
    await ctx.send("BOTベータ版の招待リンクです。https://discord.com/api/oauth2/authorize?client_id=707799417356419124&permissions=8&scope=bot")



@client.command()
async def invite(ctx):
    await ctx.send('>>> BOTの招待URLです。\nhttps://discordapp.com/oauth2/authorize?client_id=707790237463478292&permissions=8&scope=bot')



@client.command()
async def lookup(ctx, user):
    user = await client.fetch_user(user)
    if user.bot == True:
        bots = "はい"
    elif user.bot == False:
        bots = "いいえ"
    else:
        bots = "指定されたIDは見つかりませんでした。"
    embed = discord.Embed(title=f"ユーザーの情報(id:{user.id})", description=f"**・ユーザー名**\n {user.name}\n \n**・タグ**\n {user.discriminator}\n \n**・ユーザーID**\n {user.id}\n \n**・アバターURL**\n {user.avatar_url}\n \n**・BOT**\n {bots}\n")
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    await ctx.send(embed=embed)

        



@client.command()
async def status(ctx):
    await ctx.send(f"サーバー数:{len(client.guilds)}\nユーザー数:{len(client.users)}") 

servers = print('グローバルチャット利用可能になりました')

@client.event
async def on_message(message):
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return
    GLOBAL_CH_NAME = "コロッケーグローバル" # グローバルチャットのチャンネル名

    if message.channel.name == GLOBAL_CH_NAME:
        # コロッケーグローバルの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        # channelsはbotの取得できるチャンネルのイテレーター
        # global_channelsはコロッケーグローバル の名前を持つチャンネルのリスト

        embed = discord.Embed(title="コロッケーグローバル",
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name,
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        # Embedインスタンスを生成、投稿者、投稿場所などの設定

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)



@bot.command()
async def Linkedserverlist(ctx):
    await ctx.send('制作者@くけけ \n説明:みなさんもコロッケサーバーで雑談やゲームの話やBOTの話をしよう\nhttps://discord.gg/xmJT5As\n作成者ゆうゆう\n説明犯人はこいつだぁ！(入るとわかる)https://discord.gg/p6BRh5p\nGame Base Station Black Serverこのサーバーはいろんなゲームをやっています例えばみんな大好きMinecraftを専門にやっていますがフォートナイトやアスファルト9などをやっていますhttps://discord.gg/RbgTbT3')
    await ctx.send('')


@client.command()
async def info(ctx):
    await ctx.send(f"サーバー数:{len(client.guilds)}")
    for guild in client.guilds:
        await ctx.author.send(f"{guild.name}(id:{guild.id})")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="やっほー。コロッケBOT作成者のくけけだよ", description="新しくなったhelpへようこそ", color=0x00bfff)
    embed.add_field(name="k!help", value="今表示してるのがk!helpだよ", inline=False)
    embed.add_field(name="k!inviteベータ", value="ベータ版BOTの招待リンクを送るよ", inline=False)
    embed.add_field(name="k!invite", value="BOTの招待リンクを送るよ", inline=False)
    embed.add_field(name="k!addgchat2", value="Webhookバージョンでのグローバルチャットを追加します。",inline=False)
    embed.add_field(name="k!info", value="サーバー数と人数を確認するコマンドだよ", inline=False)
    embed.add_field(name="k!addgchat", value="グローバルチャットを追加します", inline=False)
    embed.add_field(name="k!set", value="開発者のサポートサーバーや連絡先を表示します", inline=False)
    embed.add_field(name="k!lookup <ID>", value="IDを使って相手の情報を確認できます", inline=False)
    embed.add_field(name="k!Linkedserverlist", value="連携サーバーリストを表示します(連携サーバー登録はくけけのTwitterのDMかDiscordのDMまで)", inline=False)
    await ctx.send(embed=embed)




@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name='k!help | 起動3.64秒 |　くけけ#5351'))
bot.run(token)
