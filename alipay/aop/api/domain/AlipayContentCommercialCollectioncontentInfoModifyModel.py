#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentCommercialCollectioncontentInfoModifyModel(object):

    def __init__(self):
        self._collection_id = None
        self._content_id = None
        self._jump_url = None

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
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value


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
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentCommercialCollectioncontentInfoModifyModel()
        if 'collection_id' in d:
            o.collection_id = d['collection_id']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        return o


