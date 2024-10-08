Если на вашем компьютере с Windows не установлены Git и Python, вам нужно сначала установить их. Вот шаги для установки и запуска Python-скрипта:

### Шаг 1: Установка Python

1. **Скачайте установочный файл Python**:
   - Перейдите на официальный сайт Python: [python.org](https://www.python.org/).
   - Перейдите на страницу загрузок и выберите последнюю версию Python для Windows.

2. **Запустите установочный файл**:
   - Убедитесь, что выбрана опция **"Add Python to PATH"** перед тем, как нажать **"Install Now"**. Это добавит Python в системный PATH, чтобы вы могли запускать его из командной строки.

3. **Проверьте установку**:
   - Откройте командную строку (Cmd) и введите:
     ```bash
     python --version
     ```
   - Вы должны увидеть установленную версию Python.

### Шаг 2: Установка Git

1. **Скачайте установочный файл Git**:
   - Перейдите на официальный сайт Git: [git-scm.com](https://git-scm.com/).
   - Перейдите на страницу загрузок и выберите версию Git для Windows.

2. **Запустите установочный файл** и следуйте инструкциям на экране:
   - В большинстве случаев можно использовать настройки по умолчанию. Убедитесь, что опция **"Git Bash Here"** включена, чтобы иметь возможность открывать Git Bash из контекстного меню проводника.

3. **Проверьте установку**:
   - Откройте командную строку (Cmd) и введите:
     ```bash
     git --version
     ```
   - Вы должны увидеть установленную версию Git.

### Шаг 3: Запуск Python-скрипта

1. **Создайте или поместите свой Python-скрипт** в удобное место на вашем компьютере.

2. **Откройте командную строку (Cmd)** и перейдите в каталог, где находится ваш скрипт:
   ```bash
   cd путь\к\вашему\скрипту
   ```

3. **Запустите скрипт**:
   ```bash
   python ваш_скрипт.py
   ```
   Замените `ваш_скрипт.py` на имя вашего Python-скрипта.

Теперь ваш Python-скрипт должен выполниться в командной строке. Если у вас есть дополнительные зависимости, установите их с помощью `pip`, командного менеджера пакетов Python:
```bash
pip install имя_пакета
```
