#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotContentModuleInfo(object):

    def __init__(self):
        self._content_sign = None
        self._data = None
        self._id = None
        self._type = None
        self._url = None

    @property
    def content_sign(self):
        return self._content_sign

    @content_sign.setter
    def content_sign(self, value):
        self._content_sign = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_sign:
            if hasattr(self.content_sign, 'to_alipay_dict'):
                params['content_sign'] = self.content_sign.to_alipay_dict()
            else:
                params['content_sign'] = self.content_sign
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotContentModuleInfo()
        if 'content_sign' in d:
            o.content_sign = d['content_sign']
        if 'data' in d:
            o.data = d['data']
        if 'id' in d:
            o.id = d['id']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        return o


