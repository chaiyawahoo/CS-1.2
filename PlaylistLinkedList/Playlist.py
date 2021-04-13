from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None
    self.__length = 0

  def add_song(self, title):
    new_song = Song(title)
    self.__length += 1
    if self.__first_song is None:
      self.__first_song = new_song
    else:
      current = self.__first_song
      while current.get_next_song() is not None:
        current = current.get_next_song()
      current.set_next_song(new_song)

  def find_song(self, title):
    if self.__length < 1:
      return -1
    elif self.__first_song.get_title() == title:
      return 0
    else:
      current = self.__first_song
      index = 0
      while current.get_next_song() is not None:
        current = current.get_next_song()
        index += 1
        if current.get_title() == title:
          return index
      else:
        return -1

  def remove_song(self, title):
    if self.__length < 1:
      return
    elif self.__first_song.get_title() == title:
      self.__first_song = self.__first_song.get_next_song()
      self.__length -= 1
    else:
      current = self.__first_song
      prev = self.__first_song
      while current is not None:
        prev = current
        current = current.get_next_song()
        if current.get_title() == title:
          prev.set_next_song(current.get_next_song())
          self.__length -= 1
          return


  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    return self.__length


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current = self.__first_song
    counter = 1
    while current is not None:
      print(f"{counter}. {str(current)}")
      counter += 1
      current = current.get_next_song()