import sys
import os
import logging
from bson import ObjectId

# sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'services'))
# from logger_track import events_logger

from datetime import datetime
import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'schema/documents')))

class CommonJsonSchema:

    schema = {
        'title': '',
        'description': '',
        'tags': [],
        'created_at': 0,
        'updated_at': 0,
    }

    def __init__(self, video_meta_info):

        tags = video_meta_info['tags'] + video_meta_info['categories']
        currentDateAndTime = datetime.now()

        CommonJsonSchema.schema['title'] = video_meta_info.get('title', None)
        CommonJsonSchema.schema['description'] = video_meta_info['description']
        CommonJsonSchema.schema['tags'] = tags
        CommonJsonSchema.schema['created_at'] = currentDateAndTime
        CommonJsonSchema.schema['updated_at'] = currentDateAndTime

    def common_schema(self):

        common_data = {
            **CommonJsonSchema.schema
        }
        return common_data

class Video(CommonJsonSchema):
    
    video_schema = {
        "video_id": '',
        "article_ref_ids": [],
        "video": { "url": ''},
        "author": '',
        "views": 0,
        "rating": 0.0,
        "subscribers": 0,
        "thumbnail": '',
        "images": ''
    }

    def __init__(self, video_meta_info):
        super().__init__(video_meta_info)
        Video.video_schema["video_id"] = video_meta_info['uploader_id']
        Video.video_schema["video"]['url'] = video_meta_info['webpage_url']
        Video.video_schema["author"] = video_meta_info['uploader']
        Video.video_schema["views"] = video_meta_info['view_count']
        Video.video_schema["thumbnail"] = video_meta_info['thumbnail']
        Video.video_schema["images"] = video_meta_info['thumbnail']

    def video(self) -> dict:
        video_doc = {
            **self.common_schema(),
            **Video.video_schema
        }
        return video_doc

class Article(CommonJsonSchema):
    
    schema = {
        "content": '',
        "article_id": '',
        "summary": '',
        "author": '',
        "thumbnail": '',
        "images": '',
        "topic_ref_ids": [],
        "video_ref_ids": []
    }

    def __init__(self, video_inserted_id, video_meta_info):
        super().__init__(video_meta_info)

        author_tuple = video_meta_info['uploader_id'], video_meta_info['uploader']
        author_info = ' / '.join(author_tuple)

        Article.schema["content"] = str()
        Article.schema["article_id"] = video_meta_info['uploader_id']
        Article.schema["summary"] = video_meta_info['description']
        Article.schema["author"] = author_info
        Article.schema["thumbnail"] =  video_meta_info['thumbnail']
        Article.schema["images"] = video_meta_info['thumbnail']
        Article.schema["video_ref_ids"] = [ ObjectId(video_inserted_id) ]# .append(video_inserted_id)
        Article.schema["topic_ref_ids"] = []
        
        
    def article_schema(self) -> dict:

        json_schema = {
            **self.common_schema(),
            **Article.schema
        }

        return json_schema

class Topic(CommonJsonSchema):
    
    schema = {
        "topic_id": '',
        "article_ref_ids": [],
        "video_ref_ids": [],
        "audio_ref_ids": [],
        "subcategory_ref_ids": []
    }

    def __init__(self, video_inserted_id, article_inserted_id, video_meta_info):
        super().__init__(video_meta_info)
        Topic.schema["topic_id"] = video_meta_info['uploader_id']
        Topic.schema["video_ref_ids"]  = [ ObjectId(video_inserted_id) ]
        Topic.schema["article_ref_ids"] = [ ObjectId(article_inserted_id) ]

    def topic_schema(self) -> dict:
        topic_doc = {
            **self.common_schema(),
            **Topic.schema
        }
        return topic_doc
  
    

# if __name__ == "__main__":
    
#     video_meta_info = {
#         'title': 'This is video_title ',
#         'description': 'This is any item description',
#         'tags': 'This is tags',
#         'created_at': 10,
#         'updated_at': 20,
#         "article_ref_ids": [],
#         "video_ref_ids": [],
#         "audio_ref_ids": [],
#         "subcategory_ref_ids": [],
#         "webpage_url": "This is webpage_url",
#         "uploader": 'uploader author',
#         "view_count": 90000,
#         "rating": 0.0,
#         "subscribers": 0,
#         "thumbnail": 'images thumbnail'
#     }

#     objClass = Article(1234,video_meta_info)
#     dict_doc= objClass.article()
#     pprint.pprint(dict_doc)
    