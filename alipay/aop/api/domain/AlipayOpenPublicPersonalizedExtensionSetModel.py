#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicPersonalizedExtensionSetModel(object):

    def __init__(self):
        self._extension_key = None
        self._status = None

    @property
    def extension_key(self):
        return self._extension_key

    @extension_key.setter
    def extension_key(self, value):
        self._extension_key = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.extension_key:
            if hasattr(self.extension_key, 'to_alipay_dict'):
                params['extension_key'] = self.extension_key.to_alipay_dict()
            else:
                params['extension_key'] = self.extension_key
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicPersonalizedExtensionSetModel()
        if 'extension_key' in d:
            o.extension_key = d['extension_key']
        if 'status' in d:
            o.status = d['status']
        return o


