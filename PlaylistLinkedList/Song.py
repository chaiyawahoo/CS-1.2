class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None

  def get_title(self):
    return self.__title

  def set_title(self, title):
    if isinstance(title, str):
      self.__title = title
    else:
      raise TypeError()

  def get_next_song(self):
    return self.__next_song

  def set_next_song(self, next_song):
    if isinstance(next_song, Song) or next_song is None:
      self.__next_song = next_song
    else:
      raise TypeError()

  def __str__(self):
    return self.__title

  def __repr__(self):
    return f"{str(self)} -> {str(self.__next_song)}"
