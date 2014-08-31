'''
	Google driveyi cdn olarak kullanabilmek için;
	1) Google Drivede bir klasör oluşturun. Örnek: public_cdn
	2) Sharing ayarlarından klasörü public yapın
	3) https://www.googledrive.com/host/klasör_id/fikret.mp4 klasör_id yerine klasörün id'sini yapıştırın. Videolarınızın linki hazır :)
'''
from apiclient import errors
# ...

def retrieve_all_files(service):
  """Retrieve a list of File resources.

  Args:
    service: Drive API service instance.
  Returns:
    List of File resources.
  """
  result = []
  page_token = None
  while True:
    try:
      param = {}
      if page_token:
        param['pageToken'] = page_token
      files = service.files().list(**param).execute()

      result.extend(files['items'])
      page_token = files.get('nextPageToken')
      if not page_token:
        break
    except errors.HttpError, error:
      print 'An error occurred: %s' % error
      break
  return result