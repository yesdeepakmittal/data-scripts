'Need Improvement'
# '''
# Generate API KEY - https://github.com/yesdeepakmittal/data-scripts/blob/main/API.md#generating-api-key
# SET-UP ENV - https://github.com/yesdeepakmittal/data-scripts/blob/main/API.md#setting-up-virtual-environment
# '''

# from apiclient.discovery import build
# import csv

# YOUTUBE_API_KEY = ''
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"
# rows = []
# maxResults = 100

# obj = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
#                         developerKey = YOUTUBE_API_KEY)
# params = "id,snippet"
# id = '--write mentions text here--'
# search_result = obj.search().list(q=id,part = params,
#                                 maxResults = maxResults).execute()

# for result in search_result.get('items',[]):
#     if result.get('id').get('kind') == 'youtube#video' and result.get('snippet').get('channelId') != id:
#         channelTitle = result.get('snippet').get('channelTitle')
#         channelId = result.get('snippet').get('channelId')
#         videoTitle = result.get('snippet').get('title')
#         videoId = result.get('id').get('videoId')
#         videoDescription = result.get('snippet').get('description')
#         publishTime = result.get('snippet').get('publishTime')

#         row = {
#             'channelTitle':channelTitle,
#             'channelId':channelId,
#             'videoTitle':videoTitle,
#             'videoId':videoId,
#             'videoDescription':videoDescription,
#             'publishTime':publishTime
#         }

#         rows.append(row)


# with open('../Other_mentions.csv' ,'w',encoding='utf-8') as f:
#     features = ['channelTitle','channelId','videoTitle','videoId','videoDescription','publishTime']
#     file = csv.DictWriter(f,fieldnames=features)
#     file.writeheader()
#     for row in rows:
#         file.writerow(row)