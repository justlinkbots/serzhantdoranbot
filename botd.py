#! /usr/bin/env python
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import os
PREFIX = '%'
client = commands.Bot(command_prefix = PREFIX )
client.remove_command('help')

trigeret_words = ['сержант','сержант доран','серж','доран']
ser_words = ['сэр доран','сэр']
ne_words = ['не хочу этого делать','не буду этого делать','нахуй оно мне надо','нахуя']
pot_words = ['потерял','посеял']
help_words = ['команды','-help']

@client.event
async def on_ready():
	print ('Бот Сержант Доран запущен! ВНИМАНИЕ! Копируя данный программный код без согласия разработчика, вы нарушаете авторские права!')
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="-help"))
#@client.command()
#async def help(ctx):
#	emb = discord.Embed( title = 'На что реагирует бот', description ='Рофлан бот))) Регистр не важен!' , colour = discord.Color.blue() )
#	emb.set_footer(text = 'Created by 𝓙𝓾𝓼𝓽 𝓛𝓲𝓷𝓴 ♥#3337 ©')
#	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
#	emb.add_field( name = 'Серж, Доран, Сержант Доран', value = '• Сержант Доран сагриться на вас) • ', inline=False)
#	emb.add_field( name = 'Сэр, Сэр доран', value = '• Сержант Доран сагриться на вас) • ', inline=False)
#	emb.add_field( name = 'Потерял, Посеял', value = '• Сержант Доран сагриться на вас) • ', inline=False)
#	await ctx.send( embed = emb)

@client.event
async def on_message( message ):
	msg = message.content.lower()
	if msg in trigeret_words:
		await message.channel.send('** Если ты мне понравишься, можешь звать меня «серж». Но знаешь что? ТЫ МНЕ НЕ НРАВИШЬСЯ!!! ПОНЯТНО?!?**')
	if msg in ser_words:
		await message.channel.send('**Я вам не сэр. Я сам зарабатываю себе на жизнь, и-ди-от. Будете звать меня «сержант», или «сержант Дорнан». Ты меня по-ни-ма-ешь?**')
	if msg in ne_words:
		await message.channel.send('** И-ди-от, не сметь обсуждать приказы начальства! Скажу прыгать, будешь прыгать! Скажу драться, будешь драться! Скажу умереть за Родину, умрёшь без разговоров! Я ясно излагаю?**')
	if msg in pot_words:
		await message.channel.send('**Вот как? И вы думаете, я этому поверю, салага? Вот она правда: вы допустили потерю дорогостоящего обмундирования. Его стоимость будет вычтена из вашего жалованья, и вы будете служить, пока вам не исполнится 510, потому что вам понадобится именно столько лет, чтобы оплатить комплект Силовой боевой брони модель II, который вы потеряли! Доложите об этом в арсенале, получите новый комплект, а потом вернитесь и доложите мне, рядовой! Свободны!**')
	if msg in help_words:	
		await message.channel.send('**Тригерет слова, на которые отвечает бот**')
		await message.channel.send('Cержант, Cержант доран, Cерж, Доран')
		await message.channel.send('Не хочу этого делать, Не буду этого делать, Нахуй оно мне надо, Нахуя')
		await message.channel.send('Потерял, Посеял')


#'**Тригерет слова, на которые отвечает бот**'
#'Cержант, Cержант доран, Cерж, Доран'
#'Не хочу этого делать, Не буду этого делать, Нахуй оно мне надо, Нахуя'
#'Потерял, Посеял'
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
