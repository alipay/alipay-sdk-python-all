#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseContentlibNewsflashSendModel(object):

    def __init__(self):
        self._author = None
        self._content = None
        self._ext_info = None
        self._images = None
        self._opr_tags = None
        self._publish_date = None
        self._recommend = None
        self._source_channel_key = None
        self._source_id = None
        self._summary = None
        self._title = None

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        self._images = value
    @property
    def opr_tags(self):
        return self._opr_tags

    @opr_tags.setter
    def opr_tags(self, value):
        self._opr_tags = value
    @property
    def publish_date(self):
        return self._publish_date

    @publish_date.setter
    def publish_date(self, value):
        self._publish_date = value
    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def source_channel_key(self):
        return self._source_channel_key

    @source_channel_key.setter
    def source_channel_key(self, value):
        self._source_channel_key = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.author:
            if hasattr(self.author, 'to_alipay_dict'):
                params['author'] = self.author.to_alipay_dict()
            else:
                params['author'] = self.author
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.images:
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        if self.opr_tags:
            if hasattr(self.opr_tags, 'to_alipay_dict'):
                params['opr_tags'] = self.opr_tags.to_alipay_dict()
            else:
                params['opr_tags'] = self.opr_tags
        if self.publish_date:
            if hasattr(self.publish_date, 'to_alipay_dict'):
                params['publish_date'] = self.publish_date.to_alipay_dict()
            else:
                params['publish_date'] = self.publish_date
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.source_channel_key:
            if hasattr(self.source_channel_key, 'to_alipay_dict'):
                params['source_channel_key'] = self.source_channel_key.to_alipay_dict()
            else:
                params['source_channel_key'] = self.source_channel_key
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseContentlibNewsflashSendModel()
        if 'author' in d:
            o.author = d['author']
        if 'content' in d:
            o.content = d['content']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'images' in d:
            o.images = d['images']
        if 'opr_tags' in d:
            o.opr_tags = d['opr_tags']
        if 'publish_date' in d:
            o.publish_date = d['publish_date']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'source_channel_key' in d:
            o.source_channel_key = d['source_channel_key']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        return o


