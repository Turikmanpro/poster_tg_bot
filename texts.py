# texts.py
start = "👋🏼 Приветствую!\n\n\
🔻 Используйте кнопки ниже для управления каналами:"

add_channel = '📢 Перешлите мне сообщение с канала где бот является администратором:'

have_access_to_post_on_channel = '✅ Канал <b>{}</b> успешно добавлен в авто-постинг!'

dont_have_access_to_post_on_channel = '❗️ Бот не может делать публикации в <b>{}</b>!'

reply_is_not_from_channel = '📢 Пожалуйста, перешлите сообщение только из канала!'

autoposting_message_to_channel = '✅ Авто-постинг включен!'


channel_already_exist = '❗️ Данный канал уже используется для авто-постинга!'

channel_info = '📢 Канал: {}\n\
👤 Владелец: {}\n\n\
⚙️ Доноры канала: '

donors_channels = '🔍 Донорские каналы для публикаций:'

add_donor = '📢 Перешлите мне сообщение с донорского канала: '

channel_private_error = '⛔️ Это приватный канал и бот не имеет доступа к созданию публикаций!'

donor_already_added = '❗️ Данный донор уже подвязан к этому каналу!'

success_added_donor = '✅ Донор <b>{}</b> успешно добавлен для канала <b>{}</b>.'

add_signatures = 'Введите текст и ссылку новой сигнатуры:\n\n\
Пример:\n\
Подпишитесь на наш канал:\n\n\
Введите "**D**" что бы удалить сигнатуру полностью.'

signature_success_added = 'Сигнатура для данного канала успешно обновлена!'

signature_error = 'Данный формат не подходит!'

select_language = 'Выберите язык на который будут переводится все посты:'

ad_keyword_added = '"**{}**" - теперь в списке фильтров рекламы.'

donors_settings = 'Настройки донора:\n\n\
Имя донора: **{}**\n\n\
ID: **{}**'


MESSAGES = {
    'start': start,
    'add_channel' : add_channel,
    'have_access_to_post_on_channel': have_access_to_post_on_channel,
    'dont_have_access_to_post_on_channel': dont_have_access_to_post_on_channel,
    'reply_is_not_from_channel': reply_is_not_from_channel,
    'autoposting_message_to_channel': autoposting_message_to_channel,
    'channel_already_exist': channel_already_exist,
    'channel_info': channel_info,
    'donors_channels': donors_channels,
    'add_donor': add_donor,
    'channel_private_error': channel_private_error,
    'donor_already_added': donor_already_added,
    'success_added_donor': success_added_donor,
    'add_signatures': add_signatures,
    'signature_success_added': signature_success_added,
    'signature_error': signature_error,
    'select_language': select_language,
    'ad_keyword_added': ad_keyword_added,
    'donors_settings': donors_settings
}