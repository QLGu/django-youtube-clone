import ftplib
class Amazon_Videos:

	def getVideos():

		ftp_address="push-13.cdn77.com"
		ftp_username="user_qzc1ty23"
		ftp_password="iY4Lv91TDCims0G12dT7"

		ftp = ftplib.FTP(ftp_address, ftp_username, ftp_password)

		ftp.cwd("/www")

		files = ftp.retrlines('NLST')

		print files
		

		

	if __name__ == '__main__':
		getVideos()