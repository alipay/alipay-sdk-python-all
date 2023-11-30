#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplierAppendixUrl(object):

    def __init__(self):
        self._name = None
        self._suffix = None
        self._url = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def suffix(self):
        return self._suffix

    @suffix.setter
    def suffix(self, value):
        self._suffix = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.suffix:
            if hasattr(self.suffix, 'to_alipay_dict'):
                params['suffix'] = self.suffix.to_alipay_dict()
            else:
                params['suffix'] = self.suffix
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
        o = SupplierAppendixUrl()
        if 'name' in d:
            o.name = d['name']
        if 'suffix' in d:
            o.suffix = d['suffix']
        if 'url' in d:
            o.url = d['url']
        return o


