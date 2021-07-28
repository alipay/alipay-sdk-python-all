#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProtocolPreviewVO(object):

    def __init__(self):
        self._protocol_content = None
        self._protocol_file_path = None
        self._protocol_name = None

    @property
    def protocol_content(self):
        return self._protocol_content

    @protocol_content.setter
    def protocol_content(self, value):
        self._protocol_content = value
    @property
    def protocol_file_path(self):
        return self._protocol_file_path

    @protocol_file_path.setter
    def protocol_file_path(self, value):
        self._protocol_file_path = value
    @property
    def protocol_name(self):
        return self._protocol_name

    @protocol_name.setter
    def protocol_name(self, value):
        self._protocol_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.protocol_content:
            if hasattr(self.protocol_content, 'to_alipay_dict'):
                params['protocol_content'] = self.protocol_content.to_alipay_dict()
            else:
                params['protocol_content'] = self.protocol_content
        if self.protocol_file_path:
            if hasattr(self.protocol_file_path, 'to_alipay_dict'):
                params['protocol_file_path'] = self.protocol_file_path.to_alipay_dict()
            else:
                params['protocol_file_path'] = self.protocol_file_path
        if self.protocol_name:
            if hasattr(self.protocol_name, 'to_alipay_dict'):
                params['protocol_name'] = self.protocol_name.to_alipay_dict()
            else:
                params['protocol_name'] = self.protocol_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProtocolPreviewVO()
        if 'protocol_content' in d:
            o.protocol_content = d['protocol_content']
        if 'protocol_file_path' in d:
            o.protocol_file_path = d['protocol_file_path']
        if 'protocol_name' in d:
            o.protocol_name = d['protocol_name']
        return o


