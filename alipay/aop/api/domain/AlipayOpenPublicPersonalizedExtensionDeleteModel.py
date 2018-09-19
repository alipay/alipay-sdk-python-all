#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicPersonalizedExtensionDeleteModel(object):

    def __init__(self):
        self._extension_key = None

    @property
    def extension_key(self):
        return self._extension_key

    @extension_key.setter
    def extension_key(self, value):
        self._extension_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.extension_key:
            if hasattr(self.extension_key, 'to_alipay_dict'):
                params['extension_key'] = self.extension_key.to_alipay_dict()
            else:
                params['extension_key'] = self.extension_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicPersonalizedExtensionDeleteModel()
        if 'extension_key' in d:
            o.extension_key = d['extension_key']
        return o


