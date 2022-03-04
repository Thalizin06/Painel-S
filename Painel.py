# Imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random
from decouple import config
import json
import requests
os.system('cls' if os.name == 'nt' else 'clear')

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

# Inicio
bot = commands.Bot("-")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Painel-S v2.10.7", url="https://www.twitch.tv/thalizin06"))
    print(CYAN + f"Logado como: " + RED + f"{bot.user}" + CYAN + "!" )
    print(RED + '''______         _               _      _____ 
| ___ \       (_)             | |    /  ___|
| |_/ /  __ _  _  _ __    ___ | |    \ `--. 
|  __/  / _` || || '_ \  / _ \| |     `--. |
| |    | (_| || || | | ||  __/| |    /\__/ /
\_|     \__,_||_||_| |_| \___||_|    \____/ .cc
                                            
                                            ''')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)


# Comando convite
@bot.command(name="invite", help="Cria um convite de servidor")
async def send_server(ctx):
    server = "https://discord.gg/xQGvng4TBH"

    response = "**Convite: **" + server
    
    await ctx.send(response)

# Comando Kiny-Painel
@bot.command(name="painel", help="abre o kiny painel (O meu é melhor é claro)")
async def embed(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="**Kiny Painel v2.3.1**", color=0x4B0082)
    
    embed.set_author(name="Painel-S by Thaliz", url="https://www.twitch.tv/thalizin06", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ2Ba_Vfca2eMC6dEkSKKLp50X3UCMdTC2BA&usqp=CAU")

    embed.add_field(name="DOWNLOAD", value="https://github.com/Kiny-Kiny/Kiny-Painel", inline=False)

    embed.set_image(url="https://github.com/Kiny-Kiny/Kiny-Painel/raw/main/IMG_20210815_155210_616.jpg")

    embed.set_footer(icon_url=ctx.author.avatar_url, text="Information requested by: {}".format(ctx.author.display_name))

    await ctx.send(embed=embed)

# Comando Otimizar-pc
@bot.command(name="otimizar", help="Abre um otimizador testado e de otima qualidade")
async def embed(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="**Pc Otimizer v1.13.1**", color=0xE6E6FA)
    
    embed.set_author(name="Painel-S by Thaliz", url="https://www.twitch.tv/thalizin06", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ2Ba_Vfca2eMC6dEkSKKLp50X3UCMdTC2BA&usqp=CAU")

    embed.add_field(name="DOWNLOAD", value="https://cdn.discordapp.com/attachments/935532000725594122/946153784185352222/otimizar.rar", inline=False)

    embed.set_image(url="https://cdn.discordapp.com/attachments/935532000725594122/946154248255729744/unknown.png")

    embed.set_footer(icon_url=ctx.author.avatar_url, text="Information requested by: {}".format(ctx.author.display_name))

    await ctx.send(embed=embed)

# Apagar mensagem (apaga 10 mensagens)
@bot.command(name='cls', help='Apaga 10 msgs')
async def clear(ctx, amount = 11):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send('Você não tem permissão!')

# Apagar mensagem (apaga 100 mensagens) OBS: Pode causar lag e erros.
@bot.command(name='cls0', help='Apaga 100 msgs OBS: Podem ocorrer problemas.')
async def clear(ctx, amount = 101):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send('Você não tem permissão!')

# Apagar mensagem (apaga 50 mensagens) OBS: Pode causar lag.
@bot.command(name='cls1', help='Apaga 50 msgs OBS: Podem ocorrer problemas.')
async def clear(ctx, amount = 51):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send('Você não tem permissão!')

# Comando gerar senha (até 10 caracteres)
@bot.command(name="senha", help= "Gera senhas aleatorias")
async def senha(ctx):
    await ctx.message.delete()
    senha = random.randrange(10000000000)
    msg = "**Senha gerada!:** " 
    await ctx.send(msg)
    await ctx.send(senha)

# Dados gratis pra quem quiser
@bot.command(name="dados")
async def dados(ctx):

    dados = (
        
    [
        {
            "nome": "Bryan Pietro Brito",
            "idade": 64,
            "cpf": "132.648.650-09",
            "rg": "14.456.898-6",
            "data_nasc": "16/01/1958",
            "sexo": "Masculino",
            "signo": "Capricórnio",
            "mae": "Hadassa Rosa Emily",
            "pai": "Luís Raul Sérgio Brito",
            "email": "bryan_pietro_brito@comercialrafael.com.br",
            "senha": "Flwifft0wZ",
            "cep": "71090-545",
            "endereco": "Colônia Agrícola Águas Claras Chácara 44",
            "numero": 555,
            "bairro": "Guará I",
            "cidade": "Brasília",
            "estado": "DF",
            "telefone_fixo": "(61) 2912-7621",
            "celular": "(61) 99247-9786",
            "altura": "1,90",
            "peso": 60,
            "tipo_sanguineo": "O+",
            "cor": "vermelho"
        }
    ]

    )

    await ctx.send(dados)

# Painel-IP (API)
@bot.command(name="ip", help="Consulta um ip")
async def embed(ctx):
    await ctx.message.delete()
    name = ctx.message.content

    str = name
    result1 = str.replace('-ip ', '')

    site = 'http://ipwhois.app/json/'

    consultar = site + result1


    response = requests.get(consultar)

    data = response.json()
    ip = data.get("ip")
    cnt = data.get("continent")
    pais = data.get("country")
    success = data.get("success")
    type = data.get("type")
    continent = data.get("continent_code")
    countryc = data.get("country_code")
    countryf = data.get("country_flag")
    countrycp = data.get("country_capital")
    countryp = data.get("country_phone")
    countryn = data.get("country_neighbours")
    region = data.get("region")
    city = data.get("city")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    asn = data.get("asn")
    org = data.get("org")
    timezone = data.get("timezone")
    currency = data.get("currency")
    currencyc = data.get("currency_code")
    timezoneg = data.get("timezone_gmt")



    embed=discord.Embed(title="**Painel-IP v1.10.7**", color=0xFF5733)
    embed.set_author(name="Painel-S by Thaliz", url="https://www.twitch.tv/thalizin06", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ2Ba_Vfca2eMC6dEkSKKLp50X3UCMdTC2BA&usqp=CAU")

    embed.add_field(name="IP:", value=ip, inline=True)
    embed.add_field(name="CONTINENTE:", value=cnt, inline=True)
    embed.add_field(name="PAÍS:", value=pais, inline=True)
    embed.add_field(name="SUCCESS:", value=success, inline=True)
    embed.add_field(name="TYPE:", value=type, inline=True)
    embed.add_field(name="CONTINENT COD:", value=continent, inline=True)
    embed.add_field(name="COUNTRY COD:", value=countryc, inline=True)
    embed.add_field(name="BANDEIRA:", value=countryf, inline=True)
    embed.add_field(name="CAPITAL:", value=countrycp, inline=True)
    embed.add_field(name="COUNTRY PN:", value=countryp, inline=True)
    embed.add_field(name="COUNTRY NGB:", value=countryn, inline=True)
    embed.add_field(name="REGIÃO:", value=region, inline=True)
    embed.add_field(name="CIDADE:", value=city, inline=True)
    embed.add_field(name="LATITUDE:", value=latitude, inline=True)
    embed.add_field(name="LONGITUDE:", value=longitude, inline=True)
    embed.add_field(name="ASN:", value=asn, inline=True)
    embed.add_field(name="ORG:", value=org, inline=True)
    embed.add_field(name="TIMEZONE:", value=timezone, inline=True)
    embed.add_field(name="CURRENCY:", value=currency, inline=True)
    embed.add_field(name="CURRENCY CD:", value=currencyc, inline=True)
    embed.add_field(name="TIMEZONE GMT:", value=timezoneg, inline=True)

    embed.set_image(url=countryf)

    embed.set_footer(icon_url=ctx.author.avatar_url, text="Information requested by: {}".format(ctx.author.display_name))

    await ctx.send(embed=embed)

# Painel-DDD (API)
@bot.command(name="ddd", help="Consulta um ddd")
async def send_hello(ctx):
    await ctx.message.delete()
    name = ctx.message.content

    str = name
    result1 = str.replace('-ddd ', '')

    site = 'https://brasilapi.com.br/api/ddd/v1/'

    consultar = site + result1

    response = requests.get(consultar)
    data = response.json()

    result0 = data.get("state")
    result1 = data.get("cities")
    res0 = '**Estado: **'
    res1 = '**Cidades: **'

    await ctx.send(res0)
    await ctx.send(result0)
    await ctx.send(res1)
    await ctx.send(result1)

# Painel-CEP (API)
@bot.command(name="cep", help="Consulta um cep")
async def cep(ctx):
    await ctx.message.delete()
    name = ctx.message.content

    str = name
    result = str.replace('-cep ', '')

    site = 'https://brasilapi.com.br/api/cep/v1/'

    consultar = site + result

    response = requests.get(consultar)
    data = response.json()

    cep2 = data.get("cep")
    state2 = data.get("state")
    city2 = data.get("city")
    neighborhood2 = data.get("neighborhood")
    street2 = data.get("street")
    service2 = data.get("service")

    embed=discord.Embed(title="**Painel-CEP v1.13.7**", color=0xB0E0E6)
    embed.set_author(name="Painel-S by Thaliz", url="https://www.twitch.tv/thalizin06", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ2Ba_Vfca2eMC6dEkSKKLp50X3UCMdTC2BA&usqp=CAU")

    embed.add_field(name="CEP:", value=cep2, inline=True)
    embed.add_field(name="ESTADO:", value=state2, inline=True)
    embed.add_field(name="CIDADE:", value=city2, inline=True)
    embed.add_field(name="LOCAL:", value=neighborhood2, inline=True)
    embed.add_field(name="ENDEREÇO:", value=street2, inline=True)
    embed.add_field(name="SERVIÇO:", value=service2, inline=True)

    embed.set_footer(icon_url=ctx.author.avatar_url, text="Information requested by: {}".format(ctx.author.display_name))

    await ctx.send(embed=embed)


# Area de Testes



# Iniciar Bot
TOKEN = config("TOKEN")
bot.run(TOKEN)
