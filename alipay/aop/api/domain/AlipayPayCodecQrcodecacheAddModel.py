#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayCodecQrcodecacheAddModel(object):

    def __init__(self):
        self._compress = None
        self._json = None
        self._key = None
        self._time = None
        self._value = None

    @property
    def compress(self):
        return self._compress

    @compress.setter
    def compress(self, value):
        self._compress = value
    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        if isinstance(value, list):
            self._json = list()
            for i in value:
                self._json.append(i)
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.compress:
            if hasattr(self.compress, 'to_alipay_dict'):
                params['compress'] = self.compress.to_alipay_dict()
            else:
                params['compress'] = self.compress
        if self.json:
            if isinstance(self.json, list):
                for i in range(0, len(self.json)):
                    element = self.json[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.json[i] = element.to_alipay_dict()
            if hasattr(self.json, 'to_alipay_dict'):
                params['json'] = self.json.to_alipay_dict()
            else:
                params['json'] = self.json
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayCodecQrcodecacheAddModel()
        if 'compress' in d:
            o.compress = d['compress']
        if 'json' in d:
            o.json = d['json']
        if 'key' in d:
            o.key = d['key']
        if 'time' in d:
            o.time = d['time']
        if 'value' in d:
            o.value = d['value']
        return o


