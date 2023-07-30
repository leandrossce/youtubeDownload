from pytube import YouTube
from youtubesearchpython import VideosSearch
import os

def download_video(url, output_path):
    try:
        # Criando um objeto YouTube
        video = YouTube(url)

        # Selecionando a melhor resolução disponível
        stream = video.streams.get_highest_resolution()

        # Iniciando o download
        print(f"Baixando: {video.title}...")
        stream.download(output_path)
        print("Download concluído!")

    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")




def download_audio(url, output_path):
    try:
        # Criando um objeto YouTube
        video = YouTube(url)

        # Selecionando o stream de áudio (formato MP4 com apenas áudio)
        audio_stream = video.streams.filter(only_audio=True, file_extension='mp4').first()

        # Definindo o nome do arquivo MP3
        mp3_file = f"{video.title}.mp3"

        # Baixando o stream de áudio
        print(f"Baixando o áudio de: {video.title}...")
        audio_stream.download(output_path)

        # Renomeando o arquivo para o formato MP3
        os.rename(os.path.join(output_path, audio_stream.default_filename), os.path.join(output_path, mp3_file))

        print("Download de áudio concluído!")

    except Exception as e:
        print(f"Ocorreu um erro durante o download do áudio: {e}")


def get_video_url_by_name(search_query):
    try:
        # Realizando a pesquisa por nome
        videos_search = VideosSearch(search_query, limit=1)

        # Obtendo a URL do primeiro vídeo da pesquisa
        if videos_search.result()['result']:
            video_url = videos_search.result()['result'][0]['link']
            return video_url

        print("Nenhum vídeo encontrado.")
        return None

    except Exception as e:
        print(f"Ocorreu um erro durante a pesquisa: {e}")
        return None



#fará o download da música Tears For Fears - Everybody Wants To Rule The World salvando em C:\Users\Leandro\Downloads\teste\
download_audio((get_video_url_by_name("Tears For Fears - Everybody Wants To Rule The World")),"C:\\Users\\Leandro\\Downloads\\teste\\")
