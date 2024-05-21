#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KongsuTest(object):

    def __init__(self):
        self._json = None
        self._s_open_id = None
        self._sss = None

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        self._json = value
    @property
    def s_open_id(self):
        return self._s_open_id

    @s_open_id.setter
    def s_open_id(self, value):
        self._s_open_id = value
    @property
    def sss(self):
        return self._sss

    @sss.setter
    def sss(self, value):
        self._sss = value


    def to_alipay_dict(self):
        params = dict()
        if self.json:
            if hasattr(self.json, 'to_alipay_dict'):
                params['json'] = self.json.to_alipay_dict()
            else:
                params['json'] = self.json
        if self.s_open_id:
            if hasattr(self.s_open_id, 'to_alipay_dict'):
                params['s_open_id'] = self.s_open_id.to_alipay_dict()
            else:
                params['s_open_id'] = self.s_open_id
        if self.sss:
            if hasattr(self.sss, 'to_alipay_dict'):
                params['sss'] = self.sss.to_alipay_dict()
            else:
                params['sss'] = self.sss
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KongsuTest()
        if 'json' in d:
            o.json = d['json']
        if 's_open_id' in d:
            o.s_open_id = d['s_open_id']
        if 'sss' in d:
            o.sss = d['sss']
        return o


