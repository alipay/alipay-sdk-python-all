#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniCloudFilelistQueryModel(object):

    def __init__(self):
        self._cloud_id = None
        self._next_token = None
        self._page_size = None
        self._path = None
        self._prefix = None

    @property
    def cloud_id(self):
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, value):
        self._cloud_id = value
    @property
    def next_token(self):
        return self._next_token

    @next_token.setter
    def next_token(self, value):
        self._next_token = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        self._prefix = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_id:
            if hasattr(self.cloud_id, 'to_alipay_dict'):
                params['cloud_id'] = self.cloud_id.to_alipay_dict()
            else:
                params['cloud_id'] = self.cloud_id
        if self.next_token:
            if hasattr(self.next_token, 'to_alipay_dict'):
                params['next_token'] = self.next_token.to_alipay_dict()
            else:
                params['next_token'] = self.next_token
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.prefix:
            if hasattr(self.prefix, 'to_alipay_dict'):
                params['prefix'] = self.prefix.to_alipay_dict()
            else:
                params['prefix'] = self.prefix
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniCloudFilelistQueryModel()
        if 'cloud_id' in d:
            o.cloud_id = d['cloud_id']
        if 'next_token' in d:
            o.next_token = d['next_token']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'path' in d:
            o.path = d['path']
        if 'prefix' in d:
            o.prefix = d['prefix']
        return o


