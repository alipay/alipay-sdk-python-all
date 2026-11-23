#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AiPayTemplateData(object):

    def __init__(self):
        self._data = None
        self._publish_version = None
        self._tpl_hash = None
        self._tpl_url = None
        self._tpl_version = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def publish_version(self):
        return self._publish_version

    @publish_version.setter
    def publish_version(self, value):
        self._publish_version = value
    @property
    def tpl_hash(self):
        return self._tpl_hash

    @tpl_hash.setter
    def tpl_hash(self, value):
        self._tpl_hash = value
    @property
    def tpl_url(self):
        return self._tpl_url

    @tpl_url.setter
    def tpl_url(self, value):
        self._tpl_url = value
    @property
    def tpl_version(self):
        return self._tpl_version

    @tpl_version.setter
    def tpl_version(self, value):
        self._tpl_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.publish_version:
            if hasattr(self.publish_version, 'to_alipay_dict'):
                params['publish_version'] = self.publish_version.to_alipay_dict()
            else:
                params['publish_version'] = self.publish_version
        if self.tpl_hash:
            if hasattr(self.tpl_hash, 'to_alipay_dict'):
                params['tpl_hash'] = self.tpl_hash.to_alipay_dict()
            else:
                params['tpl_hash'] = self.tpl_hash
        if self.tpl_url:
            if hasattr(self.tpl_url, 'to_alipay_dict'):
                params['tpl_url'] = self.tpl_url.to_alipay_dict()
            else:
                params['tpl_url'] = self.tpl_url
        if self.tpl_version:
            if hasattr(self.tpl_version, 'to_alipay_dict'):
                params['tpl_version'] = self.tpl_version.to_alipay_dict()
            else:
                params['tpl_version'] = self.tpl_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AiPayTemplateData()
        if 'data' in d:
            o.data = d['data']
        if 'publish_version' in d:
            o.publish_version = d['publish_version']
        if 'tpl_hash' in d:
            o.tpl_hash = d['tpl_hash']
        if 'tpl_url' in d:
            o.tpl_url = d['tpl_url']
        if 'tpl_version' in d:
            o.tpl_version = d['tpl_version']
        return o


