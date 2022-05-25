#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSchoolcontentModifyModel(object):

    def __init__(self):
        self._carrier_app_id = None
        self._carrier_source_url = None
        self._content_id = None
        self._detail_url = None
        self._display_style = None
        self._image_data = None
        self._out_content_id = None
        self._school_name = None
        self._source_type = None
        self._text_data = None
        self._video_data = None

    @property
    def carrier_app_id(self):
        return self._carrier_app_id

    @carrier_app_id.setter
    def carrier_app_id(self, value):
        self._carrier_app_id = value
    @property
    def carrier_source_url(self):
        return self._carrier_source_url

    @carrier_source_url.setter
    def carrier_source_url(self, value):
        self._carrier_source_url = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def display_style(self):
        return self._display_style

    @display_style.setter
    def display_style(self, value):
        self._display_style = value
    @property
    def image_data(self):
        return self._image_data

    @image_data.setter
    def image_data(self, value):
        if isinstance(value, list):
            self._image_data = list()
            for i in value:
                self._image_data.append(i)
    @property
    def out_content_id(self):
        return self._out_content_id

    @out_content_id.setter
    def out_content_id(self, value):
        self._out_content_id = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def text_data(self):
        return self._text_data

    @text_data.setter
    def text_data(self, value):
        if isinstance(value, list):
            self._text_data = list()
            for i in value:
                self._text_data.append(i)
    @property
    def video_data(self):
        return self._video_data

    @video_data.setter
    def video_data(self, value):
        if isinstance(value, list):
            self._video_data = list()
            for i in value:
                self._video_data.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.carrier_app_id:
            if hasattr(self.carrier_app_id, 'to_alipay_dict'):
                params['carrier_app_id'] = self.carrier_app_id.to_alipay_dict()
            else:
                params['carrier_app_id'] = self.carrier_app_id
        if self.carrier_source_url:
            if hasattr(self.carrier_source_url, 'to_alipay_dict'):
                params['carrier_source_url'] = self.carrier_source_url.to_alipay_dict()
            else:
                params['carrier_source_url'] = self.carrier_source_url
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.display_style:
            if hasattr(self.display_style, 'to_alipay_dict'):
                params['display_style'] = self.display_style.to_alipay_dict()
            else:
                params['display_style'] = self.display_style
        if self.image_data:
            if isinstance(self.image_data, list):
                for i in range(0, len(self.image_data)):
                    element = self.image_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_data[i] = element.to_alipay_dict()
            if hasattr(self.image_data, 'to_alipay_dict'):
                params['image_data'] = self.image_data.to_alipay_dict()
            else:
                params['image_data'] = self.image_data
        if self.out_content_id:
            if hasattr(self.out_content_id, 'to_alipay_dict'):
                params['out_content_id'] = self.out_content_id.to_alipay_dict()
            else:
                params['out_content_id'] = self.out_content_id
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.text_data:
            if isinstance(self.text_data, list):
                for i in range(0, len(self.text_data)):
                    element = self.text_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.text_data[i] = element.to_alipay_dict()
            if hasattr(self.text_data, 'to_alipay_dict'):
                params['text_data'] = self.text_data.to_alipay_dict()
            else:
                params['text_data'] = self.text_data
        if self.video_data:
            if isinstance(self.video_data, list):
                for i in range(0, len(self.video_data)):
                    element = self.video_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_data[i] = element.to_alipay_dict()
            if hasattr(self.video_data, 'to_alipay_dict'):
                params['video_data'] = self.video_data.to_alipay_dict()
            else:
                params['video_data'] = self.video_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSchoolcontentModifyModel()
        if 'carrier_app_id' in d:
            o.carrier_app_id = d['carrier_app_id']
        if 'carrier_source_url' in d:
            o.carrier_source_url = d['carrier_source_url']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'display_style' in d:
            o.display_style = d['display_style']
        if 'image_data' in d:
            o.image_data = d['image_data']
        if 'out_content_id' in d:
            o.out_content_id = d['out_content_id']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'text_data' in d:
            o.text_data = d['text_data']
        if 'video_data' in d:
            o.video_data = d['video_data']
        return o


