#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContentVo(object):

    def __init__(self):
        self._card_content = None
        self._card_title = None
        self._card_type = None
        self._cover_image_file_id = None
        self._cover_image_url = None
        self._custom_data_content = None
        self._custom_data_type = None
        self._duration = None
        self._file_id = None
        self._text = None
        self._url = None
        self._url_title = None

    @property
    def card_content(self):
        return self._card_content

    @card_content.setter
    def card_content(self, value):
        self._card_content = value
    @property
    def card_title(self):
        return self._card_title

    @card_title.setter
    def card_title(self, value):
        self._card_title = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def cover_image_file_id(self):
        return self._cover_image_file_id

    @cover_image_file_id.setter
    def cover_image_file_id(self, value):
        self._cover_image_file_id = value
    @property
    def cover_image_url(self):
        return self._cover_image_url

    @cover_image_url.setter
    def cover_image_url(self, value):
        self._cover_image_url = value
    @property
    def custom_data_content(self):
        return self._custom_data_content

    @custom_data_content.setter
    def custom_data_content(self, value):
        self._custom_data_content = value
    @property
    def custom_data_type(self):
        return self._custom_data_type

    @custom_data_type.setter
    def custom_data_type(self, value):
        self._custom_data_type = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def url_title(self):
        return self._url_title

    @url_title.setter
    def url_title(self, value):
        self._url_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_content:
            if hasattr(self.card_content, 'to_alipay_dict'):
                params['card_content'] = self.card_content.to_alipay_dict()
            else:
                params['card_content'] = self.card_content
        if self.card_title:
            if hasattr(self.card_title, 'to_alipay_dict'):
                params['card_title'] = self.card_title.to_alipay_dict()
            else:
                params['card_title'] = self.card_title
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.cover_image_file_id:
            if hasattr(self.cover_image_file_id, 'to_alipay_dict'):
                params['cover_image_file_id'] = self.cover_image_file_id.to_alipay_dict()
            else:
                params['cover_image_file_id'] = self.cover_image_file_id
        if self.cover_image_url:
            if hasattr(self.cover_image_url, 'to_alipay_dict'):
                params['cover_image_url'] = self.cover_image_url.to_alipay_dict()
            else:
                params['cover_image_url'] = self.cover_image_url
        if self.custom_data_content:
            if hasattr(self.custom_data_content, 'to_alipay_dict'):
                params['custom_data_content'] = self.custom_data_content.to_alipay_dict()
            else:
                params['custom_data_content'] = self.custom_data_content
        if self.custom_data_type:
            if hasattr(self.custom_data_type, 'to_alipay_dict'):
                params['custom_data_type'] = self.custom_data_type.to_alipay_dict()
            else:
                params['custom_data_type'] = self.custom_data_type
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.url_title:
            if hasattr(self.url_title, 'to_alipay_dict'):
                params['url_title'] = self.url_title.to_alipay_dict()
            else:
                params['url_title'] = self.url_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentVo()
        if 'card_content' in d:
            o.card_content = d['card_content']
        if 'card_title' in d:
            o.card_title = d['card_title']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'cover_image_file_id' in d:
            o.cover_image_file_id = d['cover_image_file_id']
        if 'cover_image_url' in d:
            o.cover_image_url = d['cover_image_url']
        if 'custom_data_content' in d:
            o.custom_data_content = d['custom_data_content']
        if 'custom_data_type' in d:
            o.custom_data_type = d['custom_data_type']
        if 'duration' in d:
            o.duration = d['duration']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'text' in d:
            o.text = d['text']
        if 'url' in d:
            o.url = d['url']
        if 'url_title' in d:
            o.url_title = d['url_title']
        return o


