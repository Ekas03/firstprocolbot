from config import TOKEN
import tok as kb
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic
from aiogram.types import ParseMode
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
iMon = 'https://sun9-47.userapi.com/impg/cP_00RUsxyUwr6tG0KXdilgah8AFjyJGlUrWkQ/RlDE9EaN-M0.jpg?size=1262x602&quality=96&sign=77b72914dfcffdd646a021bd3848cb5f&type=album'
iTue = 'https://sun9-14.userapi.com/impg/6H2395Mrg794lI9jzV1N3MpSo8wznLHrHj5Cng/5bAgkMFdJIo.jpg?size=1262x600&quality=96&sign=540ef88ba8bdf76e3c4724e681523c2a&type=album'
iWed = 'https://sun9-47.userapi.com/impg/Uhji_XYrf5tWL8EF19ok9Y1UizK3rV936W3kDw/PMpBkpCAu5Q.jpg?size=1262x598&quality=96&sign=698c06e179ad167794e07a8f66ed8358&type=album'
iThu = 'https://sun9-50.userapi.com/impg/o4cQSHZa1sWmsJWOW6GNw2jiCHsb_-Tv4p3cuA/URKdnOWFVbA.jpg?size=1262x638&quality=96&sign=7cb7becacbe892a2e0683a3a2a412d54&type=album'
iFri = 'https://sun9-67.userapi.com/impg/J8p_61LorRe7urjTqkjl5TUr0x9b8IE83o1GwA/jJVRK5S-9S8.jpg?size=1259x638&quality=96&sign=98924615f1c456085c9c91b133b28961&type=album'
iSat = 'https://sun9-17.userapi.com/impg/7kO-d_aFAo_7wo5Gy4Vdxc6dyx0sSjIYJGYrHQ/kW3CDkvUmTw.jpg?size=1260x599&quality=96&sign=beaac28d700ecc391f1b7228812101e3&type=album'

@dp.message_handler(commands=['start'])
async def process_class_command(message: types.Message):
    await message.reply("Выбери, пожалуйста, свой класс: ",  reply_markup=kb.klassi)

@dp.message_handler(commands=['grade'])
async def process_class_command_2(message: types.Message):
    await message.reply("Выбери, пожалуйста, свой класс:", reply_markup=kb.klassi)

@dp.callback_query_handler(lambda c: c.data == 'intex')
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Что бы ты хотел(-а) узнать?", reply_markup=kb.intex)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('ek'))
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔒 К сожалению, данный класс ещё находится в разработке ☹")

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('en'))
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔒 К сожалению, данный класс ещё находится в разработке ☹")

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('gum'))
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔒 К сожалению, данный класс ещё находится в разработке ☹")

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('socgum'))
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔒 К сожалению, данный класс ещё находится в разработке ☹")

@dp.message_handler(lambda message: message.text == "Вернуться к выбору класса")
async def process_class_command_3(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери, пожалуйста, свой класс:", reply_markup=kb.klassi)

#РАСПИСАНИЕ_ИНТЕХ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iRaspis'))
async def process_week(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Выбери день недели", reply_markup=kb.week)

#ДНИНЕДЕЛИ_ИНТЕХ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iMon'))
async def process_iMon(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Расписание на понедельник: ")
    await bot.send_photo(callback_query.from_user.id, iMon)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iTue'))
async def process_iTue(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Расписание на вторник: ")
    await bot.send_photo(callback_query.from_user.id, iTue)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iWed'))
async def process_iWed(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Расписание на среду: ")
    await bot.send_photo(callback_query.from_user.id, iWed)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iThu'))
async def process_iThu(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Расписание на четверг: ")
    await bot.send_photo(callback_query.from_user.id, iThu)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iFri'))
async def process_iFri(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Расписание на пятницу: ")
    await bot.send_photo(callback_query.from_user.id, iFri)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iSat'))
async def process_iSat(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Расписание на субботу: ")
    await bot.send_photo(callback_query.from_user.id, iSat)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iEvents'))
async def process_iEvents(callback_query: types.CallbackQuery):
    message_text = text(bold('МЕРОПРИЯТИЯ 📌'),
                        '\n\n1. Спортивное программирование', italic('\nКогда: каждую пятницу в 16:00', '\nГде: 13 кабинет'),
                        '\n\n2. Открытие', italic('\nКогда: каждую пятницу в 17:30', '\nГде: 13 кабинет'),
                        '\n\n3. Командный турнир ЦДЮТТ', italic('\nКогда: в конце апреля'))
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iBack'))
async def process_iBack(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Что бы ты хотел(-а) узнать?", reply_markup=kb.intex)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iRaspis'))
async def process_iRaspis(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Выбери день недели", reply_markup=kb.week)

#ПОЛЕЗНЫЕРЕСУРСЫ_ИНТЕХ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iResources'))
async def process_iResources(callback_query: types.CallbackQuery):
    message_text = text(bold('ПОЛЕЗНЫЕ РЕСУРСЫ 💡'),
                        '\n\nИНТЕРНЕТ-РЕСУРСЫ:',
                        '\nwelcome.stepik.org - онлайн-курсы от ведущих вузов и компаний страны',
                        '\nkpolyakov.spb.ru - сайт Полякова по информатике',
                        '\ncodeforces.com - соревнования и олимпиады по информатике',
                        '\nvsenauka.ru - бесплатная научная литература'
                        '\nsilvertests.ru - портал обучения информатике'
                        '\nege.sdamgia.ru - образовательный портал для подготовки к экзаменам'
                        '\nolimpiada.ru - всё об олимпиадах для школьников'
                        '\npostypashki.ru - лучшая подготовка к олимпиадам, ЕГЭ и ДВИ'
                        '\nmathus.ru - материалы по математике: подготовка к олимпиадам и ЕГЭ'
                        '\n\nЧАТ-БОТЫ:'
                        '\n@mybookbot - поиск книг по всему интернету на всех языках'
                        '\n@ias16bot - бот-учитель со множеством различных функций'
                        '\n@Wikipedia_voice_bot - бот с функцией голосового поиска по «Википедии»'
                        '\n@AndyRobot - чат-бот, который поможет выучить английский язык')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.intexBack)

#ЕГЭ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iEGE'))
async def process_iEGE(callback_query: types.CallbackQuery):
    message_text = text(bold('ПОЛЕЗНЫЕ РЕСУРСЫ ДЛЯ ПОДГОТОВКИ К ЕГЭ 💡'),
                        '\n\nege.sdamgia.ru - образовательный портал для подготовки к экзаменам'
                        '\nkpolyakov.spb.ru - сайт Полякова по информатике'
                        '\nfipi.ru - методическая копилка заданий ЕГЭ'
                        '\nmathege.ru - открытый банк математических задач ЕГЭ'
                        '\nneznaika.info - позволяет подготовиться к ЕГЭ и ОГЭ'
                        '\nfoxford.ru - онлайн-школа'
                        '\nshkolkovo.net - образовательный портал для подготовки к ЕГЭ, ОГЭ, и олимпиадам'
                        '\n4ege.ru - всё самое важное о ЕГЭ'
                        '\nmathus.ru - материалы по математике: подготовка к олимпиадам и ЕГЭ'
                        '\ndisk.yandex.ru/d/jvNVv6OfEAqftw - приложения для подготовки к ЕГЭ по русскому языку'
                        '\n\nЕсть много каналов на YouTube. Например: '
                        '\nпо математике - Борис Трушин, Пифагор, Математик МГУ, Школково и др.'
                        '\nпо информатике - Информатик БУ, Школково и др.'
                        '\nпо физике - ЕГЭ/ОГЭ Физика, Павел ВИКТОР, Школково и др.'
                        '\n\nТакже Вы можете посмотреть демоверсии ЕГЭ 2021 и перспективную модель на 2022 год:')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.egeintex)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iDemoMath'))
async def process_iDemoMath(callback_query: types.CallbackQuery):
    with open('data/demo-pro-math-2021.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iPersMath'))
async def process_iPersMath(callback_query: types.CallbackQuery):
    with open('data/ma-11-ege-pm2022-demo (5).pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iDemoInf'))
async def process_iDemoInf(callback_query: types.CallbackQuery):
    with open('data/demo-inf-2021.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iDemoPh'))
async def process_iDemoPh(callback_query: types.CallbackQuery):
    with open('data/demo-fiz-2021.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iPersPh'))
async def process_iPersPh(callback_query: types.CallbackQuery):
    with open('data/fi-11-ege-pm2022-demo (1).pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iDemoRus'))
async def process_iDemoRus(callback_query: types.CallbackQuery):
    with open('data/demo-rus-2021.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iPersRus'))
async def process_iPersRus(callback_query: types.CallbackQuery):
    with open('data/ru-11-ege-pm2022-demo (1).pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

#ОЛИМПИАДЫ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iOlimp'))
async def process_iOlimp(callback_query: types.CallbackQuery):
    message_text =text('❗Участие в олимпиадах даёт право поступления в ВУЗ без вступительных испытаний или школьник получает 100 баллов по профильному предмету олимпиады.',
                        bold('\n\nПОЛЕЗНЫЕ РЕСУРСЫ ДЛЯ ПОДГОТОВКИ К ОЛИМПИАДАМ 💡'),
                        '\nolimpiada.ru - всё об олимпиадах для школьников'
                        '\npostypashki.ru - подготовка к олимпиадам, ЕГЭ и ДВИ'
                        '\nfoxford.ru - онлайн-школа'
                        '\nshkolkovo.net - образовательный портал для подготовки к ЕГЭ, ОГЭ, и олимпиадам'
                        '\nmathus.ru - материалы по математике: подготовка к олимпиадам и ЕГЭ',
                        bold('\n\nБЛИЖАЙШИЕ ОЛИМПИАДЫ:'),
                             '\n1. Командный турнир ЦДЮТТ (по 3 человека)', italic('\nКогда: в конце апреля'))
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.intexBack)

#ПОСТУПАШКИ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iPostup'))
async def process_iPostup(callback_query: types.CallbackQuery):
    message_text = text(bold('РЕСУРСЫ ДЛЯ ВЫБОРЫ ВУЗА'),
                         '\n\npostupi.online, \nucheba.ru, \nvuzopedia.ru, \ntabiturient.ru',
                         bold('\n\nТОП ТЕХНИЧЕСКИХ ВУЗОВ'), '\nМГУ им. Ломоносова - msu.ru', '\nСПБГУ - spbu.ru'
                                                                            '\nМФТИ - mipt.ru'
                                                                            '\nИТМО - itmo.ru'
                                                                            '\nМАИ - mai.ru'
                                                                            '\nМГТУ им. Баумана -bmstu.ru '
                                                                            '\nНИЯУ МИФИ - mephi.ru'
                                                                            '\nНИТУ МИСиС - misis.ru')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.intexBack)

#НОВОСТИ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('News'))
async def process_News(callback_query: types.CallbackQuery):
    message_text = text(bold('НОВОСТИ 📍'), '\n\n1. Рособрнадзор перенес сроки итогового сочинения для 11-х классов.','\n\nВместо 5 апреля итоговое сочинение ученики 11 классов будут писать 15 апреля. Те, кто будут писать сочинения повторно, либо не явившиеся вовремя по уважительной причине смогут сдать его 21 апреля и 5 мая.')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN)

#О ШКОЛЕ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('school'))
async def process_school(callback_query: types.CallbackQuery):
    message_text = text(bold('ИНФОРМАЦИЯ О ШКОЛЕ'),
                        '\n\nПолное название: \nГосударственное общеобразовательное учреждение Ярославской области «Средняя школа «Провинциальный колледж» (сокращенно - ГОУ ЯО СШ «Провинциальный колледж»)'
                        '\n\nАдрес: Большая Октябрьская ул., 79, Ярославль'
                        '\n\nКонтакты: \n(4852) 30-33-38 (приемная, директор)'
                        '\n20-12-42 (Центр дополнительного образования детей "Открытие")'
                        '\n48-60-54 (учительская)'
                        '\n21-23-85 (зам.директора по учебной работе)'
                        '\nФакс: (4852) 30-33-38'
                        '\n\nПочта: yarprovcol@yandex.ru'
                        '\n\nСайт: pcollege.edu.yar.ru'
                        '\n\nТакже Вы можете узнать контакты учителей:')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.kontaktuch_school)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('kontuch'))
async def process_kontuch(callback_query: types.CallbackQuery):
    with open('data/kontakti_uchiteley.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document, parse_mode=ParseMode.MARKDOWN)

#НЕИЗВЕСТНАЯ КОМАНДА
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text('Я не знаю, что это значит 🤨'
                        '\nДля того, чтобы узнать, что я могу, выбери класс 👉 /grade')
    await msg.reply(message_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)