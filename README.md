# software_testing 
Выбранное для тестирования ПО - Converter (проект по ТРПП со 2-ого курса)

Состав команды Frik Party:
+ [Погодин Вадим Витальевич](https://github.com/vadimmpog)
+ [Горбенко Артем Дмитриевич](https://github.com/Thunderbirrd)
+ [Ромайкин Игорь Дмитриевич](https://github.com/Ygrick)
+ [Игнатов Александр Евгеньевич](https://github.com/sancepan)

## Описание выбранного ПО
Приложение представляет собой конвертер валют по текущему курсу. Пользователю предлагается следующий функционал:

Предоставляется возможность обменивать средства со своего баланса на любую из представленных валют.
Присутствует возможность отслеживать историю своих обменов
Благодаря информативному дизайну главной страницы, можно видеть текущие котировки всех основных валют по отношению друг к другу
Возможен просмотр графиков конкретной пары валют, что позволяет отслеживать историю изменения котировок
<br> !!! Приложение предназначено для запуска с мобильного устройства !!!
## Диаграмма вариантов использования

<span align="center"><img src="https://sun9-67.userapi.com/impg/28SAr9rZ6NmXac5obHLshxf7qgCleDk_EhXKhg/IIQ-kqj1SuI.jpg?size=520x461&quality=96&sign=12dfdfe054e024d8dd92f3925023d19e&type=album" width="350dp"></span><br>
## Найденные методом чёрного ящика баги

##### Баг №1
<span align="center"><img src="https://sun9-45.userapi.com/impg/wLhFlpf8naXd9bJI2DWSSC3fsqgZ8jbte3vNDQ/hdNTTPUUUCI.jpg?size=800x1600&quality=96&sign=1089ba83b57df2a9b72c890f7dd8fb28&type=album" width="200dp"></span><br>
Невозможность использования конвертатора валют с нецелыми числами
Данная ошибка является ошибкой поля пользовательского ввода
 
##### Баг №2
<span align="center"><img src="https://sun9-12.userapi.com/impg/wtUvEA1YY6RgkGke7mYcEhheC53HNHMcHQl5yg/xcPaoYqP-dk.jpg?size=864x1920&quality=96&sign=0a468d55054a64fe890360ad00bb6d80&type=album" width="200dp"></span><br>
При нажатии на картинки во вкладке "Главная" на нижней части экрана устройств появляется неинформативная надпись "This is item in position 2"

##### Баг №3
<span align="center"><img src="https://sun9-55.userapi.com/impg/S33TjHXWA69IhphimrGh3kkafjaZ6TmVb8Xlzw/1h5krIU3JMM.jpg?size=486x1080&quality=96&sign=f95d5c8ec8a62cbec379856fb082f9fa&type=album" width="200dp"></span><br>
В интерфейсе регистрации в полях ввода логина и пароля вводимые буквы и цифры белого цвета на белом фоне.
Данная ошибка является ошибкой стилизации.

##### Баг №4
При вводе корректных данных для логина и пароля(но такой пользователь не зарегистрирован) и многократного нажатия на кнопку "log in" происходит ошибка и клиента "выкидывает" из приложения

##### Баг №5
<span align="center"><img src="https://sun1-83.userapi.com/impg/okrqjDw3NlIUW-DH2FWRoaKmQYmDF4TiI2I35w/dKuWbgkQS1w.jpg?size=800x1600&quality=96&sign=fa564c4ec7e3162f504a1d18e38ac406&type=album" width="200dp"></span><br>
При вводе неправильного логина сообщение об ошибке приходит в неправильной кодировке и клиент видит строку, состоящую из знаков вопроса

##### Баг №6
<span align="center"><img src="https://sun9-55.userapi.com/impg/O97D9eWa3_dcHDZpk_k1kVOz8546-kFWWFlxQw/UO6QYLqu1Ik.jpg?size=800x1600&quality=96&sign=7b50e49bed2dda5fe83115e5111fc3d2&type=album" width="200dp"></span><br>
На странице регистрации поля для ввода пароля и его повторения не скрывают своё содержимое
