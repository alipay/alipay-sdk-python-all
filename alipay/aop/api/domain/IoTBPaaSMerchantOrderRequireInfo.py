#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IoTBPaaSMerchantOrderRequireInfo(object):

    def __init__(self):
        self._content = None
        self._name = None
        self._valid = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.valid:
            if hasattr(self.valid, 'to_alipay_dict'):
                params['valid'] = self.valid.to_alipay_dict()
            else:
                params['valid'] = self.valid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IoTBPaaSMerchantOrderRequireInfo()
        if 'content' in d:
            o.content = d['content']
        if 'name' in d:
            o.name = d['name']
        if 'valid' in d:
            o.valid = d['valid']
        return o


