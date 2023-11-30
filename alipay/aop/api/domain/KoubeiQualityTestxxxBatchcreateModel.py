#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiQualityTestxxxBatchcreateModel(object):

    def __init__(self):
        self._s = None
        self._ss_openid = None

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value
    @property
    def ss_openid(self):
        return self._ss_openid

    @ss_openid.setter
    def ss_openid(self, value):
        self._ss_openid = value


    def to_alipay_dict(self):
        params = dict()
        if self.s:
            if hasattr(self.s, 'to_alipay_dict'):
                params['s'] = self.s.to_alipay_dict()
            else:
                params['s'] = self.s
        if self.ss_openid:
            if hasattr(self.ss_openid, 'to_alipay_dict'):
                params['ss_openid'] = self.ss_openid.to_alipay_dict()
            else:
                params['ss_openid'] = self.ss_openid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiQualityTestxxxBatchcreateModel()
        if 's' in d:
            o.s = d['s']
        if 'ss_openid' in d:
            o.ss_openid = d['ss_openid']
        return o


