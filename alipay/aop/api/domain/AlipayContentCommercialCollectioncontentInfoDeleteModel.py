#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentCommercialCollectioncontentInfoDeleteModel(object):

    def __init__(self):
        self._collection_id = None
        self._content_id = None
        self._request_type = None

    @property
    def collection_id(self):
        return self._collection_id

    @collection_id.setter
    def collection_id(self, value):
        self._collection_id = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.collection_id:
            if hasattr(self.collection_id, 'to_alipay_dict'):
                params['collection_id'] = self.collection_id.to_alipay_dict()
            else:
                params['collection_id'] = self.collection_id
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.request_type:
            if hasattr(self.request_type, 'to_alipay_dict'):
                params['request_type'] = self.request_type.to_alipay_dict()
            else:
                params['request_type'] = self.request_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentCommercialCollectioncontentInfoDeleteModel()
        if 'collection_id' in d:
            o.collection_id = d['collection_id']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'request_type' in d:
            o.request_type = d['request_type']
        return o


