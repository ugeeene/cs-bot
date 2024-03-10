import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

global i
global s
global x1
global x2
global x3
global x4
global a
global ans
i=' '
s=' '
x1=0
x2=0
x3=0
x4=0
a=0
ans=0
def tobase(num,base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b=alpha[num % base]
    while num>= base :
        num //=base
        b+= alpha[num % base]
    return b[::-1] 


button_hi= KeyboardButton('Wassup')
button_help= KeyboardButton('/help')
button_go= KeyboardButton('Less go')
button_plus= KeyboardButton('+')
button_minus= KeyboardButton('-')
button_multiply= KeyboardButton('*')
button_divide1= KeyboardButton('//')
button_divide2= KeyboardButton('%')
button_stepen= KeyboardButton('^')
button_getsum= KeyboardButton('Get the answer')
button_getrazn= KeyboardButton('Get the answer')
button_getpr= KeyboardButton('Get the answer')
button_again= KeyboardButton('Try again')
button_back= KeyboardButton('Go back')

TOKEN: str = os.environ.get("bot-token")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('shjsnf',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi))

    
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("""Dude just press the less go button""")

@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    global i
    global s
    global x1
    global x2
    global x3
    global x4
    global a
    global ans
    if message.text == 'Wassup':
        await message.answer(f"""...""",reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_help,button_go))
    elif message.text == 'Try again' or message.text == 'Less go':
        await message.answer('Chose',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True)
                            .add(button_plus,button_minus)
                            .add(button_multiply)
                            .add(button_divide2)
                            .add(button_divide3)
                            .add(button_stepen))
    elif message.text =='+':
        s='+'
        await message.answer('first number',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
        i='x1'
    elif message.text =='-':
        s='-'
        await message.answer('first number',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
        i='x1'
    elif message.text =='*':
        s='*'
        await message.answer('first number',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
        i='x1'
    elif message.text =='//':
        s='//'
        await message.answer('first number',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
        i='x1'
    elif message.text =='%':
        s='%'
        await message.answer('first number',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
        i='x1'
    elif message.text =='^':
        s='^'
        await message.answer('first number',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
        i='x1'
    elif message.text== 'Get the answer':
        await message.answer(ans,reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_again))
    elif message.text =='Go back':
        if i=='x1':
            await message.answer('choose',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True)
                            .add(button_plus,button_minus)
                            .add(button_multiply)
                            .add(button_divide2)
                            .add(button_divide3)
                            .add(button_stepen))
        elif i=='x2':
            i='x1'
            if s=='+':
                await message.answer('first number.')
            elif s=='-':
                await message.answer('first number.')
            elif s=='*':
                await message.answer('first number.')
             elif s=='//':
                await message.answer('first number.')
             elif s=='%':
                await message.answer('first number.')
             elif s=='^':
                await message.answer('first number.')
        elif i=='x3':
            i='x2'
            if s=='+':
                await message.answer('first number system')
            elif s=='-':
                await message.answer('first number system')
            elif s=='*':
                await message.answer('first number system')
            elif s=='//':
                await message.answer('first number systme')
            elif s=='%':
                await message.answer('first number system')
            elif s=='^':
                await message.answer('first number systme')
        elif i=='x4':
            i='x3'
            if s=='+':
                await message.answer('second number')
            elif s=='-':
                await message.answer('second number')
            elif s=='*':
                await message.answer('second number')
            elif s=='//':
                await message.answer('second number')
            elif s=='%':
                await message.answer('second number')
            elif s=='^':
                await message.answer('second number')
        elif i=='a':
            i='x4'
            if s=='+':
                await message.answer('second number system')
            elif s=='-':
                await message.answer('second number system')
            elif s=='*':
                await message.answer('second number system')
            elif s=='//':
                await message.answer('second number system')
            elif s=='%':
                await message.answer('second number system')
            elif s=='^':
                await message.answer('second number system')
        elif i=='ans':
            i='a'
            if s=='+':
                await message.answer('answer number system',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
            elif s=='-':
                await message.answer('answer number system',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
            elif s=='*':
                await message.answer('answer number system',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
            elif s=='//':
                await message.answer('answer number system',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
            elif s=='%':
                await message.answer('answer number system',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
            elif s=='^':
                await message.answer('answer number system',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_back))
    elif s=='+' or s=='-' or s=='*' or s=='//' or s=='%' or s=='^':
        if i=='x1':
            x1=message.text
            i='x2'
            if s=='+':
                await message.answer('first number system')
            elif s=='-':
                await message.answer('first number sysytem')
            elif s=='*':
                await message.answer('first number system')
            elif s=='//':
                await message.answer('first number system')
            elif s=='%':
                await message.answer('first number sysytem')
            elif s=='^':
                await message.answer('first number system')
        elif i=='x2':
            try:
                x2=int(message.text)
                try:
                    x1=int(str(x1),x2)
                    i='x3'
                    if s=='+':
                        await message.answer('second number')
                    elif s=='-':
                        await message.answer('second number')
                    elif s=='*':
                        await message.answer('second number')
                    elif s=='//':
                        await message.answer('second number')
                    elif s=='%':
                        await message.answer('second number')
                    elif s=='^':
                        await message.answer('second number')
                except ValueError:
                    i='x1'
                    if s=='+':
                        await message.answer('there\'s an error\nTry again')
                    elif s=='-':
                        await message.answer('there\'s an error\nTry again')
                    elif s=='*':
                        await message.answer('there\'s an error\nTry again')
                    elif s=='//':
                        await message.answer('there\'s an error\nTry again')
                    elif s=='%':
                        await message.answer('there\'s an error\nTry again')
                    elif s=='^':
                        await message.answer('there\'s an error\nTry again')
            except ValueError:
                if s=='+':
                    await message.answer('there\'s an error\nTry again')
                elif s=='-':
                    await message.answer('there\'s an error\nTry again')
                elif s=='*':
                    await message.answer('there\'s an error\nTry again')
                elif s=='//':
                    await message.answer('there\'s an error\nTry again')
                elif s=='%':
                    await message.answer('there\'s an error\nTry again')
                elif s=='^':
                    await message.answer('there\'s an error\nTry again')
        elif i=='x3':
            x3=message.text
            i='x4'
            if s=='+':
                await message.answer('second number system')
            elif s=='-':
                await message.answer('second number system')
            elif s=='*':
                await message.answer('second number system')
            elif s=='//':
                await message.answer('second number system')
            elif s=='%':
                await message.answer('second number system')
            elif s=='^':
                await message.answer('second number systme')
        elif i=='x4':
            try:
                x4=int(message.text)
                try:
                    x3=int(str(x3),x4)
                    i='a'
                    if s=='+':
                        await message.answer('answer number system')
                    elif s=='-':
                        await message.answer('answer number system')
                    elif s=='*':
                        await message.answer('answer number system')
                    elif s=='//':
                        await message.answer('answer number system')
                    elif s=='%':
                        await message.answer('answer number system')
                    elif s=='^':
                        await message.answer('answer number system')
                except ValueError:
                    i='x3'
                    if s=='+':
                        await message.answer('there\'s an error\nTry again')
                    elif s=='-':
                        await message.answer('there\'s an error\nTry again')
                    if s=='*':
                        await message.answer('there\'s an error\nTry again')
                    elif s=='//':
                        await message.answer('there\'s an error\nTry again')
                    elif s=='%':
                        await message.answer('there\'s an error\nTry again')
                    if s=='^':
                        await message.answer('there\'s an error\nTry again')
            except ValueError:
                if s=='+':
                    await message.answer('there\'s an error\nTry again')
                elif s=='-':
                    await message.answer('there\'s an error\nTry again')
                elif s=='*':
                    await message.answer('there\'s an error\nTry again')
                if s=='//':
                    await message.answer('there\'s an error\nTry again')
                elif s=='%':
                    await message.answer('there\'s an error\nTry again')
                elif s=='^':
                    await message.answer('there\'s an error\nTry again')
        elif i=='a':
            try:
                a=int(message.text)
                b=int('1',a)
                i='ans'
                if s=='+':
                    ans=x1+x3
                    ans=tobase(ans,a)
                    await message.answer('answer is ready',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_getsum,button_back))
                elif s=='-':
                    ans=x1-x3
                    if ans<0:
                        ans=int(tobase(0-ans,a))
                        ans=0-ans
                    else:
                        ans=tobase(ans,a)
                    await message.answer('answer is ready',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_getrazn,button_back))
                elif s=='*':
                    ans=x1*x3
                    ans=tobase(ans,a)
                    await message.answer('answer is ready',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_getpr,button_back))
                elif s=='//':
                    ans=x1//x3
                    ans=tobase(ans,a)
                    await message.answer('answer is ready',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_getpr,button_back))
                elif s=='%':
                    ans=x1%x3
                    ans=tobase(ans,a)
                    await message.answer('answer is ready',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_getpr,button_back))
                elif s=='^':
                    ans=x1**x3
                    ans=tobase(ans,a)
                    await message.answer('answer is ready',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(button_getpr,button_back))
            except ValueError:
                if s=='+':
                    await message.answer('there\'s an error\nTry again')
                elif s=='-':
                    await message.answer('there\'s an error\nTry again')
                elif s=='*':
                    await message.answer('there\'s an error\nTry again')
                elif s=='//':
                    await message.answer('there\'s an error\nTry again')
                elif s=='%':
                    await message.answer('there\'s an error\nTry again')
                elif s=='^':
                    await message.answer('there\'s an error\nTry again')
    else:
        await message.answer('there\'s an error\nTry again')


if __name__ == '__main__':
    executor.start_polling(dp)


