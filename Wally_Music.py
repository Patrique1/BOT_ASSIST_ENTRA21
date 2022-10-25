import threading
from pytube import YouTube
import vlc
from time import sleep
import re, urllib.parse, urllib.request
import pyttsx3
import speech_recognition as sr


tts_engine = pyttsx3.init()


def speak(text):
  if tts_engine._inLoop:
    tts_engine.endLoop()
  tts_engine.say(text)
  tts_engine.runAndWait()


class MusicPlayerTask:
  def __init__(self):
    self.Instance = vlc.Instance()

    self._playing = False
    self.pause = False

  def stop_player(self):
    self._playing = False

  def toggle_pause_song(self):
    self.pause = not self.pause

  def reset(self):
    self._playing = False
    self.pause = False

  def play(self, music_url):
    Media = self.Instance.media_new(music_url)
    Media.get_mrl()

    player = self.Instance.media_player_new()
    player.set_media(Media)
    player.play()
    self._playing = True

    while self._playing:
      sleep(0.1)
      while player.is_playing():
        if not self._playing:
          player.stop()
          break
        if self.pause:
          player.pause()  # this leaves the loop, since player.is_playng == False
          break  # just to make sure (lol)

        sleep(0.1)
      if not self._playing:
        player.stop()
        break
      if not self.pause:
        player.play()

    self.reset()


music_player = MusicPlayerTask()


def get_music_youtube_link(music_name):

  query_string = urllib.parse.urlencode({"search_query": music_name})
  formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
  search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
  clip = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
  return clip


def play_music(music_name):
  clip = get_music_youtube_link(music_name)

  # get audio
  yt = YouTube(clip)
  music_url = yt.streams.filter(only_audio=True).first().url
  # out_file = yt.streams.filter(only_audio=True).first().download() # to download the music

  # start play music thread
  music_thread = threading.Thread(target=music_player.play, args=(music_url, ), daemon=True)
  music_thread.start()


def pause_music():
  music_player.toggle_pause_song()

def stop_music():
  music_player.stop_player()


def tocar_musica():
  while True:
    frase = input('\nQual música deseja ouvir? ')

    play_music(frase)

    comando = input('>>> ')
    if comando == 'sair':
      stop_music()
      break


