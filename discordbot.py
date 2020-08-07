import discord
from discord.ext import commands, tasks
import os
import sys
import asyncio
import re
import tlaceback

token = os.environ['DISCORD_BOT_TOKEN']

client =commands.Bot(command_prefix='k!')
bot=commands.Bot(command_prefix='k!')

client = discord.Client()

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
    await ctx.send('制作者@くけけ \n説明:みなさんもコロッケサーバーで雑談やゲームの話やBOTの話をしよう\nhttps://discord.gg/zzd4r2P\n作成者ゆうゆう\n説明犯人はこいつだぁ！(入るとわかる)https://discord.gg/p6BRh5p\nGame Base Station Black Serverこのサーバーはいろんなゲームをやっています例えばみんな大好きMinecraftを専門にやっていますがフォートナイトやアスファルト9などをやっていますhttps://discord.gg/RbgTbT3')
    await ctx.send('')
@bot.command()
async def Mainserver(ctx):
    await ctx.send('新型コロッケサーバーです\nhttps://discord.gg/pfGHf3X')
@bot.command()
async def addgchat(ctx):
    await ctx.send('グローバルチャットを有効にします\nコロッケーグローバルと入力してチャンネルを作成してください')

@bot.command()
async def set(ctx):
    await ctx.send('>>>  開発者の連絡先とサーバーです。\n・コロッケBOTサポートサーバー招待コードhttps://discord.gg/bB49bPR \nコロッケ公式Twitter：https://twitter.com/korokkekousiki\n開発者のTwitter：')

@bot.command()
async def botsetベータ(ctx):
    await ctx.send("当BOTベータ版の招待リンクだよhttps://discord.com/api/oauth2/authorize?client_id=707799417356419124&permissions=8&scope=bot")

@bot.command()
async def botset(ctx):
    await ctx.send("当BOTの招待リンクだよhttps://discord.com/api/oauth2/authorize?client_id=707790237463478292&permissions=8&scope=bot")

@bot.command()
async def やっはろー(ctx):
    await ctx.send("曲のダウンロードリンクだよ　https://d.kuku.lu/86c8543e80")



@client.command()
async def addgban(ctx):
    await ctx.send('>>> グローバルBANを有効にします。\n``コロッケ-gbans`` というチャンネルを作成して下さい。')

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="やっほー。コロッケBOT作成者のくけけだよ", description="新しくなったhelpへようこそ", color=0x00bfff)
    embed.add_field(name="k!help", value="今表示してるのがk!helpだよ", inline=False)
    embed.add_field(name="k!botsetベータ", value="ベータ版BOTの招待リンクを送るよ", inline=False)
    embed.add_field(name="k!botset", value="BOTの招待リンクを送るよ", inline=False)
    embed.add_field(name="k!やっはろー", value="やっはろーという曲のダウンロードリンクだよ", inline=False)
    embed.add_field(name="k!info", value="サーバー数と人数を確認するコマンドだよ", inline=False)
    embed.add_field(name="k!addgchat", value="グローバルチャットを追加します", inline=False)
    embed.add_field(name="k!adminhelp", value="運営専用ヘルプです。",inline=False)
    embed.add_field(name="k!set", value="開発者のサポートサーバーや連絡先を表示します", inline=False)
    embed.add_field(name="k!Mainserver", value="開発者のメインサーバーを表示します", inline=False)
    embed.add_field(name="k!Linkedserverlist", value="連携サーバーリストを表示します(連携サーバー登録はくけけのTwitterのDMかDiscordのDMまで)", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def adminhelp(ctx):
    embed = discord.Embed(title="コロッケBOT：運営用ヘルプ", description="このコマンドは全て運営専用だよ。みんなは使えないから気を付けてね。", color=0x00bfff)
    embed.add_field(name="k!link <サーバーID>", value="サーバーの招待リンクを作成します", inline=False)
    embed.add_field(name="k!gban <ID>", value="選択したユーザーをグローバルBANします", inline=False)
    embed.add_field(name="k!ungban <ID>", value="選択したユーザーのグローバルBANを解除します", inline=False)
    embed.add_field(name="k!導入サーバー", value="DMに導入サーバー名とサーバーIDを送ります", inline=False)
    embed.add_field(name="k!botexit <サーバーID>", value="指定したサーバーからBOTを退出させます", inline=False)
    await ctx.send(embed=embed)

with open("./admins.txt") as f:
    admins = f.read()


@tasks.loop(seconds=200)
async def gban_update():
    with open("./bans.txt", mode="r", encoding="utf-8") as f:
        users = f.read()
        f.close()
    for user in list(users.split(',')):
        try:
            user = await client.fetch_user(user)
            for guild in client.guilds:
                await guild.ban(user, reason="globalban")
        except discord.Forbidden:pass

@client.command()
async def lookup(ctx, user):
    user = await client.fetch_user(user)
    if user.bot == True:
        bots = "BOT"
    elif user.bot == False:
        bots = "ユーザー" 
    else:
        bots = "(指定されたIDのユーザは検索できませんでした別のIDをお試しください)"
    embed = discord.Embed(title=f"ユーザーの情報(id:{user.id})", description=f"・ユーザー名**\n {user.name}\n \n**・タグ**\n {user.discriminator}\n \n**・アカウントの種類**\n {bots}\n \n**・ユーザーID**\n {user.id}\n \n**・アカウント作成時刻(UTC)**\n {user.created_at}\n", color=0x00bfff)
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def link(ctx, guild):
    if re.search(f"{ctx.author.id}", f"{admins}") != None:
        run = "no"
        for guilds in client.guilds:
            if f"{guilds.id}" == f"{guild}":
                msg = await ctx.send(f"{guilds.name}の招待コードを作成中です...")
                channel = guilds.channels[0]
                invite = await channel.create_invite(reason=None, max_age=30)
                await msg.edit(content=f"招待の作成が完了しました。\n{invite}")
                run = "y"
        if run == "no":
            await ctx.send("そのidのサーバーが見つかりませんでした。")
    else:
        msg = await ctx.send("運営のみが実行可能なコマンドです。")

@client.command()
async def botexit(ctx,serverid=None):
    if re.search(f"{ctx.author.id}", f"{admins}") == None:
        await ctx.send("管理者以外は実行できません。")
        return
    if serverid == None:
        await ctx.send("エラー: サーバーIDが入力されていません。")
        return
    status = await ctx.send(content=f"退出を準備しています...")
    try:
        guild = await client.fetch_guild(serverid)
        status = await ctx.send(content=f"{guild.name}から退出しています...")
        await guild.leave()
        await status.edit(content=f"{guild.name}から退出しました。")
    except discord.Forbidden as e:
        await status.edit(content=f"エラーが発生しました。\n```{e}```")

@client.command()
async def gban(ctx, user):
    if re.search(f"{ctx.author.id}", f"{admins}") != None:
        if re.search(f"{user}", f"{admins}") != None:
            await ctx.send(" 運営ををGBANすることはできません")
            return
        user = await client.fetch_user(user)
        with open('./bans.txt', mode='r', encoding="utf-8") as f:
            oldbans = f.read()
            f.close()
        with open('./bans.txt', mode='w', encoding="utf-8") as f:
            f.write(f"{oldbans},{user.id}")
            f.close()                                                     
        status = await ctx.send(f"{user.name}をGBANしています...")
        try:
            for guild in client.guilds:
                await guild.ban(user, reason="コロッケBOTによるGBANです。")
                for channel in guild.channels:
                    if channel.name == "コロッケ-gbans":
                        await channel.send(f"> **● 新規GBANが発行されました**\n> \n> ・GBANされたアカウントのユーザー名:\n> {user.name}\n> \n> タグ:{user.discriminator}\n> \n>")
        except discord.Forbidden:pass
        await status.edit(content=f"{user.name}のGBANが完了しました。")
    else:
        await ctx.send("運営のみが実行可能なコマンドです。")


@client.command()
async def ungban(ctx, user):
    if re.search(f"{ctx.author.id}", f"{admins}") != None:
        user = await client.fetch_user(user)
        status = await ctx.send(f"{user.name}のGBANを解除しています...")
        try:
            for guild in client.guilds:
                await guild.unban(user, reason="コロッケBOTによるGBANです。")
        except discord.Forbidden:pass
        await status.edit(content=f"{user.name}のGBAN解除が完了しました。")
    else:
        await ctx.send("運営のみが実行可能なコマンドです")


@client.command()
async def 導入サーバー(ctx):
    await ctx.send(f"サーバー数:{len(client.guilds)}")
    for guild in client.guilds:
        await ctx.author.send(f"{guild.name}(id:{guild.id})")


@client.event
async def on_ready():
    channel = client.get_channel(707566403699605575)
    await channel.send("起動完了:メイン      グローバルチャットとコマンドを利用できます ")
    await client.change_presence(activity=discord.Game(name='k!help |くけけ#5351|24時間作動中'))



bot.run('token')
client.run('token')
