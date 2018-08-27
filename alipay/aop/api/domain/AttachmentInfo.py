#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AttachmentInfo(object):

    def __init__(self):
        self._atta_url = None
        self._name = None
        self._type = None

    @property
    def atta_url(self):
        return self._atta_url

    @atta_url.setter
    def atta_url(self, value):
        self._atta_url = value
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
        if self.atta_url:
            if hasattr(self.atta_url, 'to_alipay_dict'):
                params['atta_url'] = self.atta_url.to_alipay_dict()
            else:
                params['atta_url'] = self.atta_url
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
        o = AttachmentInfo()
        if 'atta_url' in d:
            o.atta_url = d['atta_url']
        if 'name' in d:
            o.name = d['name']
        if 'type' in d:
            o.type = d['type']
        return o


