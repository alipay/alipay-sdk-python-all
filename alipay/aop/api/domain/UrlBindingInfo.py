#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UrlBindingInfo(object):

    def __init__(self):
        self._applied = None
        self._qr_code_url = None

    @property
    def applied(self):
        return self._applied

    @applied.setter
    def applied(self, value):
        self._applied = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.applied:
            if hasattr(self.applied, 'to_alipay_dict'):
                params['applied'] = self.applied.to_alipay_dict()
            else:
                params['applied'] = self.applied
        if self.qr_code_url:
            if hasattr(self.qr_code_url, 'to_alipay_dict'):
                params['qr_code_url'] = self.qr_code_url.to_alipay_dict()
            else:
                params['qr_code_url'] = self.qr_code_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UrlBindingInfo()
        if 'applied' in d:
            o.applied = d['applied']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        return o


