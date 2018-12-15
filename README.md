# sortmypics
sorts your pics in a /yyyy/month manner reading the exif data of your pics

English version see below.

## Installation
Für das Script ist folgende Python Extension ExifRead erforderlich. Diese kann direkt von pypi.org bezogen werden: https://pypi.org/project/ExifRead/ Die Installation kann mittels `pip install exifread` erfolgen. Sollte python-pip noch nicht auf dem System sein, kann dies mittels `sudo apt install python-pip` installiert werden.

## Verwendung
`python sortmypics.py`
Als Option muss das Verzeichnis mit den zu sortierenden Bildern mit `-d` angegeben werden. Das Zielverzeichnis wird mittels `-p` definiert
Beispiel: `python sortmypics.py -d '/home/user/Downloads/CameraUploads/' -p '/home/user/Pictures/'`

Bilder oder auch andere Dokumente, welche keine ExIf Metadaten haben, werden in den Zielverzeichnis `/sortyourself/` abgelegt.

## Know bugs/Features
* Leerzeichen in Verzeichnissen oder Dateinamen sind zur Zeit noch nicht zugelassen. Als Workaround hilft: `ls -1 | while read i; do mv "$i" "`echo $i | tr -d " "`"; done`
* Header in den Dateien
* Beschreibung übersetzten
* GUI für die Applikation

---

# English

## Installation
The following Python Extension ExifRead is required for the script. This can be obtained directly from pypi.org: https://pypi.org/project/ExifRead/ The installation can be done with `pip install exifread`. If python-pip is not yet on the system, this can be installed with `sudo apt install python-pip`.

## Usage
`python sortmypics.py`
As an option, the directory with the images to be sorted must be specified with `-d`. The target directory is defined with `-p`.
Example: `python sortmypics.py -d '/home/user/Downloads/CameraUploads/' -p '/home/user/Pictures/'`

Images or other documents without ExIf metadata are stored in the target directory `/sortyourself/`.

## Know bugs/features
* Spaces in directories or file names are currently not allowed. As workaround helps: `ls -1 | while read i; do mv "$i" "`echo $i | tr -d " "`""; done`
* Header in the files
* Description translated
* GUI for the application
