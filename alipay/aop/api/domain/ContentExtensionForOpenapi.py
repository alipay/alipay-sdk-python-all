#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContentExtensionForOpenapi(object):

    def __init__(self):
        self._extension = None
        self._extension_type = None

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
    @property
    def extension_type(self):
        return self._extension_type

    @extension_type.setter
    def extension_type(self, value):
        self._extension_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.extension:
            if hasattr(self.extension, 'to_alipay_dict'):
                params['extension'] = self.extension.to_alipay_dict()
            else:
                params['extension'] = self.extension
        if self.extension_type:
            if hasattr(self.extension_type, 'to_alipay_dict'):
                params['extension_type'] = self.extension_type.to_alipay_dict()
            else:
                params['extension_type'] = self.extension_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentExtensionForOpenapi()
        if 'extension' in d:
            o.extension = d['extension']
        if 'extension_type' in d:
            o.extension_type = d['extension_type']
        return o


