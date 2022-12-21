#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContentItem(object):

    def __init__(self):
        self._author_fans = None
        self._author_id = None
        self._author_level = None
        self._author_name = None
        self._cate = None
        self._cate_cnt = None
        self._collect_cnt = None
        self._collection = None
        self._comment_cnt = None
        self._content = None
        self._copyright_end = None
        self._copyright_start = None
        self._create_time = None
        self._detail_pic_num = None
        self._detail_url = None
        self._expire_time = None
        self._id = None
        self._key_word = None
        self._location_tag = None
        self._mini_app_id = None
        self._pic_url = None
        self._praise_cnt = None
        self._pub_time = None
        self._rating = None
        self._related_goods_ids = None
        self._share_cnt = None
        self._source_id = None
        self._status = None
        self._tags = None
        self._title = None
        self._topic_tag = None
        self._type = None
        self._update_time = None
        self._video_duration = None
        self._video_url = None

    @property
    def author_fans(self):
        return self._author_fans

    @author_fans.setter
    def author_fans(self, value):
        self._author_fans = value
    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        self._author_id = value
    @property
    def author_level(self):
        return self._author_level

    @author_level.setter
    def author_level(self, value):
        self._author_level = value
    @property
    def author_name(self):
        return self._author_name

    @author_name.setter
    def author_name(self, value):
        self._author_name = value
    @property
    def cate(self):
        return self._cate

    @cate.setter
    def cate(self, value):
        self._cate = value
    @property
    def cate_cnt(self):
        return self._cate_cnt

    @cate_cnt.setter
    def cate_cnt(self, value):
        self._cate_cnt = value
    @property
    def collect_cnt(self):
        return self._collect_cnt

    @collect_cnt.setter
    def collect_cnt(self, value):
        self._collect_cnt = value
    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, value):
        self._collection = value
    @property
    def comment_cnt(self):
        return self._comment_cnt

    @comment_cnt.setter
    def comment_cnt(self, value):
        self._comment_cnt = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def copyright_end(self):
        return self._copyright_end

    @copyright_end.setter
    def copyright_end(self, value):
        self._copyright_end = value
    @property
    def copyright_start(self):
        return self._copyright_start

    @copyright_start.setter
    def copyright_start(self, value):
        self._copyright_start = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def detail_pic_num(self):
        return self._detail_pic_num

    @detail_pic_num.setter
    def detail_pic_num(self, value):
        self._detail_pic_num = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, value):
        if isinstance(value, list):
            self._key_word = list()
            for i in value:
                self._key_word.append(i)
    @property
    def location_tag(self):
        return self._location_tag

    @location_tag.setter
    def location_tag(self, value):
        self._location_tag = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def praise_cnt(self):
        return self._praise_cnt

    @praise_cnt.setter
    def praise_cnt(self, value):
        self._praise_cnt = value
    @property
    def pub_time(self):
        return self._pub_time

    @pub_time.setter
    def pub_time(self, value):
        self._pub_time = value
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
    @property
    def related_goods_ids(self):
        return self._related_goods_ids

    @related_goods_ids.setter
    def related_goods_ids(self, value):
        self._related_goods_ids = value
    @property
    def share_cnt(self):
        return self._share_cnt

    @share_cnt.setter
    def share_cnt(self, value):
        self._share_cnt = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def topic_tag(self):
        return self._topic_tag

    @topic_tag.setter
    def topic_tag(self, value):
        self._topic_tag = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def video_duration(self):
        return self._video_duration

    @video_duration.setter
    def video_duration(self, value):
        self._video_duration = value
    @property
    def video_url(self):
        return self._video_url

    @video_url.setter
    def video_url(self, value):
        self._video_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.author_fans:
            if hasattr(self.author_fans, 'to_alipay_dict'):
                params['author_fans'] = self.author_fans.to_alipay_dict()
            else:
                params['author_fans'] = self.author_fans
        if self.author_id:
            if hasattr(self.author_id, 'to_alipay_dict'):
                params['author_id'] = self.author_id.to_alipay_dict()
            else:
                params['author_id'] = self.author_id
        if self.author_level:
            if hasattr(self.author_level, 'to_alipay_dict'):
                params['author_level'] = self.author_level.to_alipay_dict()
            else:
                params['author_level'] = self.author_level
        if self.author_name:
            if hasattr(self.author_name, 'to_alipay_dict'):
                params['author_name'] = self.author_name.to_alipay_dict()
            else:
                params['author_name'] = self.author_name
        if self.cate:
            if hasattr(self.cate, 'to_alipay_dict'):
                params['cate'] = self.cate.to_alipay_dict()
            else:
                params['cate'] = self.cate
        if self.cate_cnt:
            if hasattr(self.cate_cnt, 'to_alipay_dict'):
                params['cate_cnt'] = self.cate_cnt.to_alipay_dict()
            else:
                params['cate_cnt'] = self.cate_cnt
        if self.collect_cnt:
            if hasattr(self.collect_cnt, 'to_alipay_dict'):
                params['collect_cnt'] = self.collect_cnt.to_alipay_dict()
            else:
                params['collect_cnt'] = self.collect_cnt
        if self.collection:
            if hasattr(self.collection, 'to_alipay_dict'):
                params['collection'] = self.collection.to_alipay_dict()
            else:
                params['collection'] = self.collection
        if self.comment_cnt:
            if hasattr(self.comment_cnt, 'to_alipay_dict'):
                params['comment_cnt'] = self.comment_cnt.to_alipay_dict()
            else:
                params['comment_cnt'] = self.comment_cnt
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.copyright_end:
            if hasattr(self.copyright_end, 'to_alipay_dict'):
                params['copyright_end'] = self.copyright_end.to_alipay_dict()
            else:
                params['copyright_end'] = self.copyright_end
        if self.copyright_start:
            if hasattr(self.copyright_start, 'to_alipay_dict'):
                params['copyright_start'] = self.copyright_start.to_alipay_dict()
            else:
                params['copyright_start'] = self.copyright_start
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.detail_pic_num:
            if hasattr(self.detail_pic_num, 'to_alipay_dict'):
                params['detail_pic_num'] = self.detail_pic_num.to_alipay_dict()
            else:
                params['detail_pic_num'] = self.detail_pic_num
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.key_word:
            if isinstance(self.key_word, list):
                for i in range(0, len(self.key_word)):
                    element = self.key_word[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_word[i] = element.to_alipay_dict()
            if hasattr(self.key_word, 'to_alipay_dict'):
                params['key_word'] = self.key_word.to_alipay_dict()
            else:
                params['key_word'] = self.key_word
        if self.location_tag:
            if hasattr(self.location_tag, 'to_alipay_dict'):
                params['location_tag'] = self.location_tag.to_alipay_dict()
            else:
                params['location_tag'] = self.location_tag
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.praise_cnt:
            if hasattr(self.praise_cnt, 'to_alipay_dict'):
                params['praise_cnt'] = self.praise_cnt.to_alipay_dict()
            else:
                params['praise_cnt'] = self.praise_cnt
        if self.pub_time:
            if hasattr(self.pub_time, 'to_alipay_dict'):
                params['pub_time'] = self.pub_time.to_alipay_dict()
            else:
                params['pub_time'] = self.pub_time
        if self.rating:
            if hasattr(self.rating, 'to_alipay_dict'):
                params['rating'] = self.rating.to_alipay_dict()
            else:
                params['rating'] = self.rating
        if self.related_goods_ids:
            if hasattr(self.related_goods_ids, 'to_alipay_dict'):
                params['related_goods_ids'] = self.related_goods_ids.to_alipay_dict()
            else:
                params['related_goods_ids'] = self.related_goods_ids
        if self.share_cnt:
            if hasattr(self.share_cnt, 'to_alipay_dict'):
                params['share_cnt'] = self.share_cnt.to_alipay_dict()
            else:
                params['share_cnt'] = self.share_cnt
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.topic_tag:
            if hasattr(self.topic_tag, 'to_alipay_dict'):
                params['topic_tag'] = self.topic_tag.to_alipay_dict()
            else:
                params['topic_tag'] = self.topic_tag
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.video_duration:
            if hasattr(self.video_duration, 'to_alipay_dict'):
                params['video_duration'] = self.video_duration.to_alipay_dict()
            else:
                params['video_duration'] = self.video_duration
        if self.video_url:
            if hasattr(self.video_url, 'to_alipay_dict'):
                params['video_url'] = self.video_url.to_alipay_dict()
            else:
                params['video_url'] = self.video_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentItem()
        if 'author_fans' in d:
            o.author_fans = d['author_fans']
        if 'author_id' in d:
            o.author_id = d['author_id']
        if 'author_level' in d:
            o.author_level = d['author_level']
        if 'author_name' in d:
            o.author_name = d['author_name']
        if 'cate' in d:
            o.cate = d['cate']
        if 'cate_cnt' in d:
            o.cate_cnt = d['cate_cnt']
        if 'collect_cnt' in d:
            o.collect_cnt = d['collect_cnt']
        if 'collection' in d:
            o.collection = d['collection']
        if 'comment_cnt' in d:
            o.comment_cnt = d['comment_cnt']
        if 'content' in d:
            o.content = d['content']
        if 'copyright_end' in d:
            o.copyright_end = d['copyright_end']
        if 'copyright_start' in d:
            o.copyright_start = d['copyright_start']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'detail_pic_num' in d:
            o.detail_pic_num = d['detail_pic_num']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'id' in d:
            o.id = d['id']
        if 'key_word' in d:
            o.key_word = d['key_word']
        if 'location_tag' in d:
            o.location_tag = d['location_tag']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'praise_cnt' in d:
            o.praise_cnt = d['praise_cnt']
        if 'pub_time' in d:
            o.pub_time = d['pub_time']
        if 'rating' in d:
            o.rating = d['rating']
        if 'related_goods_ids' in d:
            o.related_goods_ids = d['related_goods_ids']
        if 'share_cnt' in d:
            o.share_cnt = d['share_cnt']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'status' in d:
            o.status = d['status']
        if 'tags' in d:
            o.tags = d['tags']
        if 'title' in d:
            o.title = d['title']
        if 'topic_tag' in d:
            o.topic_tag = d['topic_tag']
        if 'type' in d:
            o.type = d['type']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'video_duration' in d:
            o.video_duration = d['video_duration']
        if 'video_url' in d:
            o.video_url = d['video_url']
        return o


