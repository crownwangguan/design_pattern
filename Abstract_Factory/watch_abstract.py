##Defining the abstract factory class
from abc import ABCMeta as ABC,abstractmethod

class ApplicationsFactory:
	__metaclass__=ABC

	def __init__(self):
		super(ApplicationsFactory,self)

	@abstractmethod
	def getMusicPlayer(self):
		pass

	@abstractmethod
	def getPhotoViewer(self):
		pass

## Defining Concrete Factory Classes 

class AppleApplicationsFactory(ApplicationsFactory):

	def __init__(self):
		super(AppleApplicationsFactory,self)

	def getMusicPlayer(self):
		return AppleMusicPlayer()

	def getPhotoViewer(self):
		return ApplePhotoViewer()


class AndroidApplicationsFactory(ApplicationsFactory):

	def __init__(self):
		super(AndroidApplicationsFactory,self)

	def getMusicPlayer(self):
		return AndroidMusicPlayer()

	def getPhotoViewer(self):
		return AndroidPhotoViewer()


def getPlatformFactory(plat):
	## We need a function which returns factory based on which platform we are
	factory_dict={
        "Android":AndroidApplicationsFactory(),
        "Apple":AppleApplicationsFactory()
	}
	return factory_dict[plat]


platform="Android"
app_factory=getPlatformFactory(platform)
music_player=app_factory.getMusicPlayer()
print(music_player.playMusic("Cheap Thrills"))