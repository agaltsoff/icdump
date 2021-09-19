# icdump

Выгрузка начального состояния и изменений конфигурации 1С типовыми средствами 

**ЦЕЛЬ**

Видеть в Git изменения текста модулей не выгружая в Git всю конфигурацию.
        
**ОПРЕДЕЛЕНИЯ**

|Имя|Описание|
|---|---|
|Эталон|Конфигурация 1С, подключённая к хранилищу конфигураций, которая только обновляется из хранилища.|
|Разработка|База для разработки, подключённая к хранилищу, которая обновляется из хранилища и в которой разработчик изменяет объекты.|

**ФАЙЛЫ**

| Имя          | Описание                                                     |
| ------------ | ------------------------------------------------------------ |
| icdump.py    | Использование: icdump.py COMMAND [--config CONFIG]  <br />COMMAND Команда <br />--config CONFIG Файл настроек в формате json, по умолчанию config.json |
| icdumplib.py | Инициализация и вспомогательные функции.                     |
| config.json  | Настройки                                                    |

**КОМАНДЫ**

|Имя|Описание|
|---|---|
|setup|Выгружает эталон |
|update|Выгружает изменения эталона|
|precommit|Выгружает различия между разработкой и эталоном.|
|master|Файлы, которые есть в репозитории, но нет в выгрузке разработки, удаляет из репозитория.<br />Файлы, которые есть в выгрузке разработки, но нет в репозитории, копирует из выгрузки эталона в репозиторий.|
|develop|Копирует файлы из выгрузки разработки в репозиторий|

**ПОРЯДОК РАБОТЫ**

|Действие|Команда|Результат|
|---|---|---|
|**Перед началом работы**|||
| Выгрузить эталон|setup|Начальная выгрузка эталона|
|**После захвата и изменения объектов**|||
|Обновить выгрузку эталона|update|В выгрузке эталона изменения сделанные другими во время изменения объектов|
|Выгрузить разработку|precommit|В выгрузке разработки изменённые объекты|
|Обновить эталон в репозитории|master|Оригиналы изменённых объектов в репозитории|
|Git Commit||Оригиналы изменённых объектов в Git|
|Обновить разработку в репозитории|develop|Изменённые объекты в репозитории|
|Git Commit||Изменённые объекты в Git|

Таким образом при каждой выгрузке, когда появились новые изменённые объекты, сначала в Git будут выгружены их оригиналы, затем их изменения. В результате можно будет сравнивать изменения с оригиналами, не выгружая в Git всю конфигурацию.

При использовании git-flow *master* делать в ветку ***master***, *develop* в ветку ***develop*** или в ветку ***feature*** для этих изменений и перед *develop* делать объединять (merge) эту ветку и ветку ***master***.

**Примечания**

Работало в 8.3.13. В 8.3.12 precommit выгружает ВСЮ конфигурацию, хотя в файлах ConfigDumpInfo.xml Kdiff3 показывает различия только в нескольких строках реально изменённых объектов.
