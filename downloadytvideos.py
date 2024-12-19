import yt_dlp as youtube_dl

def descargar_video(url, ruta):
ydl_opts = {
'format’: 'best’,
'outtmpl’: f’{ruta}/%(title)s.%(ext)s’,
'nocheckcertificate’: True,
'ignoreerrors’: True,
'verbose’: True
}
try:
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
ydl.download([url])
print("Descarga completada.")
except Exception as e:
print(f"Error: {e}")

Example of use
url_video = input("Enter download link:  ")
ruta_descarga = r"PUT DOWNLOAD ROUTE"
descargar_video(url_video, ruta_descarga)