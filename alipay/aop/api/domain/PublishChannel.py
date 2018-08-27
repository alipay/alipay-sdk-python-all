#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PublishChannel(object):

    def __init__(self):
        self._config = None
        self._ext_info = None
        self._name = None
        self._type = None

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.config:
            if hasattr(self.config, 'to_alipay_dict'):
                params['config'] = self.config.to_alipay_dict()
            else:
                params['config'] = self.config
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PublishChannel()
        if 'config' in d:
            o.config = d['config']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'name' in d:
            o.name = d['name']
        if 'type' in d:
            o.type = d['type']
        return o


