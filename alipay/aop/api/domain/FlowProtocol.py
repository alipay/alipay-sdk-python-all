#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FlowProtocol(object):

    def __init__(self):
        self._content = None
        self._content_type = None
        self._name = None
        self._protocol_version = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def protocol_version(self):
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, value):
        self._protocol_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.protocol_version:
            if hasattr(self.protocol_version, 'to_alipay_dict'):
                params['protocol_version'] = self.protocol_version.to_alipay_dict()
            else:
                params['protocol_version'] = self.protocol_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FlowProtocol()
        if 'content' in d:
            o.content = d['content']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'name' in d:
            o.name = d['name']
        if 'protocol_version' in d:
            o.protocol_version = d['protocol_version']
        return o


