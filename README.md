# Microservices Server
[![Version](https://img.shields.io/badge/LICENSE-Apache%20Modified%20License-green?style=flat&logoWidth=15&logo=.NET)](/LICENSE)

В этом репозитории представлены следующие компоненты:
* Сервер ([здесь](/Microservices-MicroServer))
* Отладчик коммуникации сервисов ([здесь](/MicroServer.Debugger))
* Клиент для C# ([здесь](/API-C%23))
* Клиент для Python ([здесь](/API-Python))
* Концептуальный пример реализации сервера ([здесь](/Microservices-PythonServer)) - *пример с множеством комментариев, который позволит легко разобраться в принципе работы сервера; на основе этого примера можно создать собственную реализацию сервера*
* Образ виртуальной машины с минималистичной установкой Windows 7 ([здесь](/Virtual%20Machine%20Package)) - *может быть полезен при организации портативной среды*

Помимо компонентов, в данном репозитории представлена документация для:
* Сервера - [здесь](https://github.com/michael2021-vlsu/Microservices-Server/blob/micromaster/Documentation%20Microservices-MicroServer.pdf)
* Отладчика - [здесь](https://github.com/michael2021-vlsu/Microservices-Server/blob/micromaster/Documentation%20MicroServer.Debugger.pdf)
* Клиента для Python - [здесь](https://github.com/michael2021-vlsu/Microservices-Server/blob/micromaster/Documentation%20API-Python.pdf)
* Клиента для C# - [здесь](https://github.com/michael2021-vlsu/Microservices-Server/blob/micromaster/Documentation%20API-C%23.pdf)

### Первое знакомство рекомендуется начать с документации клиента (например, для [Python](https://github.com/michael2021-vlsu/Microservices-Server/blob/micromaster/Documentation%20API-Python.pdf))

Присутствует демонстрационное видео, в котором виден пример работы микросервисной системы: 

https://user-images.githubusercontent.com/82028882/138525791-4b1e0e8b-80eb-4669-b743-316f083e3a3a.mp4

Видео в более высоком качестве лежит [здесь](https://github.com/michael2021-vlsu/Microservices-Server/blob/micromaster/Demo.mp4).

Стоит отметить, что в демонстрации приведён концептуальный пример (то есть, как в принципе в может работать микросервисная система). 
В приведённом примере использовано в 2 раза больше микросервисов, чем можно было бы (6 вместо 3-х).
В реальности так делать настоятельно не рекомендуется, однако, в примере это демонстрирует возможности системы в плане гибкости и возможности разнесения большого количества частей по разным исполняемым файлам для наибольшей независимости при разработке.

В демонстрации всё присходит без участия человека с момента запуска виртуальной машины до момента начала ручного ввода данных для рассчёта. 
Процесс зепуска микросервисной системы (всех сервисов и сервера) полностью автоматизирован.