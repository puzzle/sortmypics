# sortmypics
sorts your pics in a /yyyy/month manner reading the exif data of your pics

# Installation:
Für das Script ist folgende Python Extension ExifRead erforderlich. Diese kann direkt von pypi.org bezogen werden: https://pypi.org/project/ExifRead/ Die Installation kann mittels `pip install exifread` erfolgen. Sollte python-pip noch nicht auf dem System sein, kann dies mittels `sudo apt install python-pip` installiert werden.

# Verwendung:
`python sortmypics.py`
Als Option muss das Verzeichnis mit den zu sortierenden Bildern mit `-d` angegeben werden. Das Zielverzeichnis wird mittels `-p` definiert
Beispiel: `python sortmypics.py -d '/home/user/Downloads/CameraUploads/' -p '/home/user/Pictures/'`

Bilder oder auch andere Dokumente, welche keine ExIf Metadaten haben, werden in den Zielverzeichnis `/sortyourself/` abgelegt.

# Know bugs/Features:
* Leerzeichen in Verzeichnissen oder Dateinamen sind zur Zeit noch nicht zugelassen. Als Workaround hilft: `ls -1 | while read i; do mv "$i" "`echo $i | tr -d " "`"; done`
* Header in den Dateien
* Beschreibung übersetzten
* GUI für die Applikation
