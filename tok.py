from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


#ВЫБОР_КЛАССА
intex = InlineKeyboardButton('10И', callback_data='intex')
ek = InlineKeyboardButton('10Э', callback_data='ek')
en = InlineKeyboardButton('10ЕН', callback_data='en')
gum = InlineKeyboardButton('10Г', callback_data='gum')
socgum = InlineKeyboardButton('10СГ', callback_data='socgum')

#ВОЗМОЖНОСТИ_ИНТЕХ
iRaspis= InlineKeyboardButton('Расписание ⏰', callback_data='iRaspis')
News = InlineKeyboardButton('Новости 📰', callback_data='News')
iResources = InlineKeyboardButton('Полезные ресурсы', callback_data='iResources')
iEGE = InlineKeyboardButton('ЕГЭ ✏', callback_data='iEGE')
iOlimp = InlineKeyboardButton('Олимпиады 🥇', callback_data='iOlimp')
iPostup = InlineKeyboardButton('Поступашки 🐦', callback_data='iPostup')

#РАСПИСАНИЕ_ИНТЕХ
iMon = InlineKeyboardButton('Понедельник', callback_data='iMon')
iTue = InlineKeyboardButton('Вторник', callback_data='iTue')
iWed = InlineKeyboardButton('Среда', callback_data='iWed')
iThu = InlineKeyboardButton('Четверг', callback_data='iThu')
iFri = InlineKeyboardButton('Пятница', callback_data='iFri')
iSat = InlineKeyboardButton('Суббота', callback_data='iSat')
iEvents = InlineKeyboardButton('Мероприятия', callback_data='iEvents')
iBack = InlineKeyboardButton('🔙', callback_data='iBack')

#EGE_ИНТЕХ
iDemoMath = InlineKeyboardButton("МАТЕМАТИКА'21", callback_data='iDemoMath')
iPersMath = InlineKeyboardButton("МАТЕМАТИКА'22", callback_data='iPersMath')
iDemoInf = InlineKeyboardButton("ИНФОРМАТИКА'21", callback_data='iDemoInf')
iDemoPh = InlineKeyboardButton("ФИЗИКА'21", callback_data='iDemoPh')
iPersPh = InlineKeyboardButton("ФИЗИКА'22", callback_data='iPersPh')
iDemoRus = InlineKeyboardButton("РУССКИЙ ЯЗЫК'21", callback_data='iDemoRus')
iPersRus = InlineKeyboardButton("РУССКИЙ ЯЗЫК'22", callback_data='iPersRus')
iBackEGE = InlineKeyboardButton('🔙', callback_data='iBackEGE')

school = InlineKeyboardButton('О школе 🏫', callback_data='school')
kontaktuch = InlineKeyboardButton('Контакты учителей 👩‍🏫', callback_data='kontuch')

klassi = InlineKeyboardMarkup(row_width=1).add(intex, ek, en, gum, socgum)
intex = InlineKeyboardMarkup(row_width=2).add(iRaspis, News, iResources, iEGE, iOlimp, iPostup).add(school)
week= InlineKeyboardMarkup(row_width=1).add(iMon, iTue, iWed, iThu, iFri, iSat, iEvents, iBack)
intexBack = InlineKeyboardMarkup(row_width=1).add(iBack)
egeintex = InlineKeyboardMarkup(row_width=2).add(iDemoMath, iPersMath, iDemoInf, iDemoPh, iPersPh, iDemoRus,iPersRus, iBack)
egeintexback = InlineKeyboardMarkup(row_width=1).add(iBackEGE)
kontaktuch_school = InlineKeyboardMarkup(row_width=1).add(kontaktuch)