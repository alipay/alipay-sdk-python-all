#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseContentlibStandardvideoSendModel(object):

    def __init__(self):
        self._action_type = None
        self._ext_info = None
        self._public_id = None
        self._source_author = None
        self._source_category = None
        self._source_cover = None
        self._source_id = None
        self._source_publish_date = None
        self._source_summary = None
        self._source_title = None
        self._video_id = None
        self._video_length = None
        self._video_publish_type = None
        self._video_size = None
        self._video_tags = None
        self._video_url = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def source_author(self):
        return self._source_author

    @source_author.setter
    def source_author(self, value):
        self._source_author = value
    @property
    def source_category(self):
        return self._source_category

    @source_category.setter
    def source_category(self, value):
        self._source_category = value
    @property
    def source_cover(self):
        return self._source_cover

    @source_cover.setter
    def source_cover(self, value):
        self._source_cover = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_publish_date(self):
        return self._source_publish_date

    @source_publish_date.setter
    def source_publish_date(self, value):
        self._source_publish_date = value
    @property
    def source_summary(self):
        return self._source_summary

    @source_summary.setter
    def source_summary(self, value):
        self._source_summary = value
    @property
    def source_title(self):
        return self._source_title

    @source_title.setter
    def source_title(self, value):
        self._source_title = value
    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, value):
        self._video_id = value
    @property
    def video_length(self):
        return self._video_length

    @video_length.setter
    def video_length(self, value):
        self._video_length = value
    @property
    def video_publish_type(self):
        return self._video_publish_type

    @video_publish_type.setter
    def video_publish_type(self, value):
        self._video_publish_type = value
    @property
    def video_size(self):
        return self._video_size

    @video_size.setter
    def video_size(self, value):
        self._video_size = value
    @property
    def video_tags(self):
        return self._video_tags

    @video_tags.setter
    def video_tags(self, value):
        self._video_tags = value
    @property
    def video_url(self):
        return self._video_url

    @video_url.setter
    def video_url(self, value):
        self._video_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.source_author:
            if hasattr(self.source_author, 'to_alipay_dict'):
                params['source_author'] = self.source_author.to_alipay_dict()
            else:
                params['source_author'] = self.source_author
        if self.source_category:
            if hasattr(self.source_category, 'to_alipay_dict'):
                params['source_category'] = self.source_category.to_alipay_dict()
            else:
                params['source_category'] = self.source_category
        if self.source_cover:
            if hasattr(self.source_cover, 'to_alipay_dict'):
                params['source_cover'] = self.source_cover.to_alipay_dict()
            else:
                params['source_cover'] = self.source_cover
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_publish_date:
            if hasattr(self.source_publish_date, 'to_alipay_dict'):
                params['source_publish_date'] = self.source_publish_date.to_alipay_dict()
            else:
                params['source_publish_date'] = self.source_publish_date
        if self.source_summary:
            if hasattr(self.source_summary, 'to_alipay_dict'):
                params['source_summary'] = self.source_summary.to_alipay_dict()
            else:
                params['source_summary'] = self.source_summary
        if self.source_title:
            if hasattr(self.source_title, 'to_alipay_dict'):
                params['source_title'] = self.source_title.to_alipay_dict()
            else:
                params['source_title'] = self.source_title
        if self.video_id:
            if hasattr(self.video_id, 'to_alipay_dict'):
                params['video_id'] = self.video_id.to_alipay_dict()
            else:
                params['video_id'] = self.video_id
        if self.video_length:
            if hasattr(self.video_length, 'to_alipay_dict'):
                params['video_length'] = self.video_length.to_alipay_dict()
            else:
                params['video_length'] = self.video_length
        if self.video_publish_type:
            if hasattr(self.video_publish_type, 'to_alipay_dict'):
                params['video_publish_type'] = self.video_publish_type.to_alipay_dict()
            else:
                params['video_publish_type'] = self.video_publish_type
        if self.video_size:
            if hasattr(self.video_size, 'to_alipay_dict'):
                params['video_size'] = self.video_size.to_alipay_dict()
            else:
                params['video_size'] = self.video_size
        if self.video_tags:
            if hasattr(self.video_tags, 'to_alipay_dict'):
                params['video_tags'] = self.video_tags.to_alipay_dict()
            else:
                params['video_tags'] = self.video_tags
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
        o = AlipaySocialBaseContentlibStandardvideoSendModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'source_author' in d:
            o.source_author = d['source_author']
        if 'source_category' in d:
            o.source_category = d['source_category']
        if 'source_cover' in d:
            o.source_cover = d['source_cover']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_publish_date' in d:
            o.source_publish_date = d['source_publish_date']
        if 'source_summary' in d:
            o.source_summary = d['source_summary']
        if 'source_title' in d:
            o.source_title = d['source_title']
        if 'video_id' in d:
            o.video_id = d['video_id']
        if 'video_length' in d:
            o.video_length = d['video_length']
        if 'video_publish_type' in d:
            o.video_publish_type = d['video_publish_type']
        if 'video_size' in d:
            o.video_size = d['video_size']
        if 'video_tags' in d:
            o.video_tags = d['video_tags']
        if 'video_url' in d:
            o.video_url = d['video_url']
        return o


