#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TouchUvInfo(object):

    def __init__(self):
        self._qr_code_url = None
        self._touch_uv = None

    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
    @property
    def touch_uv(self):
        return self._touch_uv

    @touch_uv.setter
    def touch_uv(self, value):
        self._touch_uv = value


    def to_alipay_dict(self):
        params = dict()
        if self.qr_code_url:
            if hasattr(self.qr_code_url, 'to_alipay_dict'):
                params['qr_code_url'] = self.qr_code_url.to_alipay_dict()
            else:
                params['qr_code_url'] = self.qr_code_url
        if self.touch_uv:
            if hasattr(self.touch_uv, 'to_alipay_dict'):
                params['touch_uv'] = self.touch_uv.to_alipay_dict()
            else:
                params['touch_uv'] = self.touch_uv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TouchUvInfo()
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        if 'touch_uv' in d:
            o.touch_uv = d['touch_uv']
        return o


