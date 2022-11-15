# shb_py_gui_auto_shutdown - Aplikasi yang dapat Men-Shutdown Komputer saat Mouse dan Keyboard Tidak Aktif

## Link-Link Penting

- Website Utama Saya: https://bit.ly/shb-main
- Akun GitHub Saya: https://bit.ly/shb-github
- Channel YouTube Saya: https://bit.ly/shb-channel
- Berikan Saya Uang Gratis (Traktir Saya): https://bit.ly/shb-traktir

## Software Apakah Ini?

Ini adalah aplikasi untuk shutdown secara otomatis setelah beberapa menit keyboard dan mouse tidak aktif.

## Screenshot

![ScreenShot](.readme-assets/shb_py_gui_auto_shutdown-1.png?raw=true)

## Cara Mencoba Kode Ini

Untuk menjalankan aplikasi ini, install Python3, masuk ke dalam foldernya via command line, lalu:

Buat virtual environment:

```
python -m venv venv
```

Untuk di windows agar venv bisa diaktifkan:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Aktifkan venv:

```
venv/Scripts/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Untuk menjalankannya dalam mode development:

```
python App.py
```

Untuk membuild exe:

```
pyinstaller --onefile App.py
```
