#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseContentlibStandardcontentSendModel(object):

    def __init__(self):
        self._action_type = None
        self._ext_info = None
        self._public_id = None
        self._source_author = None
        self._source_category = None
        self._source_content = None
        self._source_cover = None
        self._source_id = None
        self._source_keywords = None
        self._source_link = None
        self._source_publish_date = None
        self._source_summary = None
        self._source_thumbnail_type = None
        self._source_thumbnails = None
        self._source_title = None

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
    def source_content(self):
        return self._source_content

    @source_content.setter
    def source_content(self, value):
        self._source_content = value
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
    def source_keywords(self):
        return self._source_keywords

    @source_keywords.setter
    def source_keywords(self, value):
        self._source_keywords = value
    @property
    def source_link(self):
        return self._source_link

    @source_link.setter
    def source_link(self, value):
        self._source_link = value
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
    def source_thumbnail_type(self):
        return self._source_thumbnail_type

    @source_thumbnail_type.setter
    def source_thumbnail_type(self, value):
        self._source_thumbnail_type = value
    @property
    def source_thumbnails(self):
        return self._source_thumbnails

    @source_thumbnails.setter
    def source_thumbnails(self, value):
        self._source_thumbnails = value
    @property
    def source_title(self):
        return self._source_title

    @source_title.setter
    def source_title(self, value):
        self._source_title = value


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
        if self.source_content:
            if hasattr(self.source_content, 'to_alipay_dict'):
                params['source_content'] = self.source_content.to_alipay_dict()
            else:
                params['source_content'] = self.source_content
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
        if self.source_keywords:
            if hasattr(self.source_keywords, 'to_alipay_dict'):
                params['source_keywords'] = self.source_keywords.to_alipay_dict()
            else:
                params['source_keywords'] = self.source_keywords
        if self.source_link:
            if hasattr(self.source_link, 'to_alipay_dict'):
                params['source_link'] = self.source_link.to_alipay_dict()
            else:
                params['source_link'] = self.source_link
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
        if self.source_thumbnail_type:
            if hasattr(self.source_thumbnail_type, 'to_alipay_dict'):
                params['source_thumbnail_type'] = self.source_thumbnail_type.to_alipay_dict()
            else:
                params['source_thumbnail_type'] = self.source_thumbnail_type
        if self.source_thumbnails:
            if hasattr(self.source_thumbnails, 'to_alipay_dict'):
                params['source_thumbnails'] = self.source_thumbnails.to_alipay_dict()
            else:
                params['source_thumbnails'] = self.source_thumbnails
        if self.source_title:
            if hasattr(self.source_title, 'to_alipay_dict'):
                params['source_title'] = self.source_title.to_alipay_dict()
            else:
                params['source_title'] = self.source_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseContentlibStandardcontentSendModel()
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
        if 'source_content' in d:
            o.source_content = d['source_content']
        if 'source_cover' in d:
            o.source_cover = d['source_cover']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_keywords' in d:
            o.source_keywords = d['source_keywords']
        if 'source_link' in d:
            o.source_link = d['source_link']
        if 'source_publish_date' in d:
            o.source_publish_date = d['source_publish_date']
        if 'source_summary' in d:
            o.source_summary = d['source_summary']
        if 'source_thumbnail_type' in d:
            o.source_thumbnail_type = d['source_thumbnail_type']
        if 'source_thumbnails' in d:
            o.source_thumbnails = d['source_thumbnails']
        if 'source_title' in d:
            o.source_title = d['source_title']
        return o


