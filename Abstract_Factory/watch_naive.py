## We need to design a Watch OS which runs custom utilities like  playing music,displaying photos etc using the platforms Default Music Player

from abc import ABCMeta as ABC,abstractmethod
## Define Product Abstract Classses
class MusicPlayer:
	__metaclass__ = ABC

	def __init__(self):
		super(MusicPlayer,self).__init__()
	
	@abstractmethod
	def playMusic(self):
		pass

class PhotoGallery:
	__metaclass__=ABC
	def __init__(self):
		super().__init__()
	
	@abstractmethod
	def showPhotos(self):
		pass


##Define Product Concrete Classes

class AppleMusicPlayer(MusicPlayer):

	def __init__(self):
		super(AppleMusicPlayer,self).__init__();

	def playMusic(self,song):
		return "Running "+song+" on iTunes"

class AndroidMusicPlayer(MusicPlayer):

	def __init__(self):
		super(AndroidMusicPlayer,self).__init__();

	def playMusic(self,song):
		return "Running "+song+" on Google Play Music"

class ApplePhotoViewer(PhotoGallery):

	def __init__(self):
		super().__init__();

	def showPhotos(self,img):
		return "Displaying "+img+" on Photos"

class AndroidPhotoViewer(PhotoGallery):

	def __init__(self):
		super().__init__();

	def showPhotos(self,img):
		return "Displaying "+img+" on Google Photos"

## The most raw approach


class Applications:
	'Provides you with UI strings in a given language'

	def __init__(self,plat):
		self.platform=plat

	def getMusicPlayer(self):
		music_dict={
		"Apple":AppleMusicPlayer(),
		"Android":AndroidMusicPlayer()
		}
		return music_dict[self.platform]

	def getPhotoViewer(self):
		photo_dict={
		"Apple":ApplePhotoViewer(),
		"Android":AndroidPhotoViewer()
		}
		return photo_dict[self.platform]

## Now we generate objects for it 

watch_apple=Applications("Apple")
music_player=watch_apple.getMusicPlayer()
print(music_player.playMusic("Dusk Till Dawn"))