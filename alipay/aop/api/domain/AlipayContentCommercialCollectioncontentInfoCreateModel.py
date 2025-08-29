#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentCommercialCollectioncontentInfoCreateModel(object):

    def __init__(self):
        self._banner_url = None
        self._collection_category = None
        self._collection_id = None
        self._collection_name = None
        self._collection_second_category = None
        self._completed_status = None
        self._content_id = None
        self._content_source = None
        self._episodes_count = None
        self._episodes_number = None
        self._jump_url = None
        self._request_type = None
        self._short_title = None

    @property
    def banner_url(self):
        return self._banner_url

    @banner_url.setter
    def banner_url(self, value):
        self._banner_url = value
    @property
    def collection_category(self):
        return self._collection_category

    @collection_category.setter
    def collection_category(self, value):
        self._collection_category = value
    @property
    def collection_id(self):
        return self._collection_id

    @collection_id.setter
    def collection_id(self, value):
        self._collection_id = value
    @property
    def collection_name(self):
        return self._collection_name

    @collection_name.setter
    def collection_name(self, value):
        self._collection_name = value
    @property
    def collection_second_category(self):
        return self._collection_second_category

    @collection_second_category.setter
    def collection_second_category(self, value):
        self._collection_second_category = value
    @property
    def completed_status(self):
        return self._completed_status

    @completed_status.setter
    def completed_status(self, value):
        self._completed_status = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def content_source(self):
        return self._content_source

    @content_source.setter
    def content_source(self, value):
        self._content_source = value
    @property
    def episodes_count(self):
        return self._episodes_count

    @episodes_count.setter
    def episodes_count(self, value):
        self._episodes_count = value
    @property
    def episodes_number(self):
        return self._episodes_number

    @episodes_number.setter
    def episodes_number(self, value):
        self._episodes_number = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value
    @property
    def short_title(self):
        return self._short_title

    @short_title.setter
    def short_title(self, value):
        self._short_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.banner_url:
            if hasattr(self.banner_url, 'to_alipay_dict'):
                params['banner_url'] = self.banner_url.to_alipay_dict()
            else:
                params['banner_url'] = self.banner_url
        if self.collection_category:
            if hasattr(self.collection_category, 'to_alipay_dict'):
                params['collection_category'] = self.collection_category.to_alipay_dict()
            else:
                params['collection_category'] = self.collection_category
        if self.collection_id:
            if hasattr(self.collection_id, 'to_alipay_dict'):
                params['collection_id'] = self.collection_id.to_alipay_dict()
            else:
                params['collection_id'] = self.collection_id
        if self.collection_name:
            if hasattr(self.collection_name, 'to_alipay_dict'):
                params['collection_name'] = self.collection_name.to_alipay_dict()
            else:
                params['collection_name'] = self.collection_name
        if self.collection_second_category:
            if hasattr(self.collection_second_category, 'to_alipay_dict'):
                params['collection_second_category'] = self.collection_second_category.to_alipay_dict()
            else:
                params['collection_second_category'] = self.collection_second_category
        if self.completed_status:
            if hasattr(self.completed_status, 'to_alipay_dict'):
                params['completed_status'] = self.completed_status.to_alipay_dict()
            else:
                params['completed_status'] = self.completed_status
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.content_source:
            if hasattr(self.content_source, 'to_alipay_dict'):
                params['content_source'] = self.content_source.to_alipay_dict()
            else:
                params['content_source'] = self.content_source
        if self.episodes_count:
            if hasattr(self.episodes_count, 'to_alipay_dict'):
                params['episodes_count'] = self.episodes_count.to_alipay_dict()
            else:
                params['episodes_count'] = self.episodes_count
        if self.episodes_number:
            if hasattr(self.episodes_number, 'to_alipay_dict'):
                params['episodes_number'] = self.episodes_number.to_alipay_dict()
            else:
                params['episodes_number'] = self.episodes_number
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.request_type:
            if hasattr(self.request_type, 'to_alipay_dict'):
                params['request_type'] = self.request_type.to_alipay_dict()
            else:
                params['request_type'] = self.request_type
        if self.short_title:
            if hasattr(self.short_title, 'to_alipay_dict'):
                params['short_title'] = self.short_title.to_alipay_dict()
            else:
                params['short_title'] = self.short_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentCommercialCollectioncontentInfoCreateModel()
        if 'banner_url' in d:
            o.banner_url = d['banner_url']
        if 'collection_category' in d:
            o.collection_category = d['collection_category']
        if 'collection_id' in d:
            o.collection_id = d['collection_id']
        if 'collection_name' in d:
            o.collection_name = d['collection_name']
        if 'collection_second_category' in d:
            o.collection_second_category = d['collection_second_category']
        if 'completed_status' in d:
            o.completed_status = d['completed_status']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'content_source' in d:
            o.content_source = d['content_source']
        if 'episodes_count' in d:
            o.episodes_count = d['episodes_count']
        if 'episodes_number' in d:
            o.episodes_number = d['episodes_number']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'request_type' in d:
            o.request_type = d['request_type']
        if 'short_title' in d:
            o.short_title = d['short_title']
        return o


