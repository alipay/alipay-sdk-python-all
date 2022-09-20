#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppTestagainCreateModel(object):

    def __init__(self):
        self._buyer_openid = None
        self._xxxxxx = None

    @property
    def buyer_openid(self):
        return self._buyer_openid

    @buyer_openid.setter
    def buyer_openid(self, value):
        self._buyer_openid = value
    @property
    def xxxxxx(self):
        return self._xxxxxx

    @xxxxxx.setter
    def xxxxxx(self, value):
        self._xxxxxx = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_openid:
            if hasattr(self.buyer_openid, 'to_alipay_dict'):
                params['buyer_openid'] = self.buyer_openid.to_alipay_dict()
            else:
                params['buyer_openid'] = self.buyer_openid
        if self.xxxxxx:
            if hasattr(self.xxxxxx, 'to_alipay_dict'):
                params['xxxxxx'] = self.xxxxxx.to_alipay_dict()
            else:
                params['xxxxxx'] = self.xxxxxx
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppTestagainCreateModel()
        if 'buyer_openid' in d:
            o.buyer_openid = d['buyer_openid']
        if 'xxxxxx' in d:
            o.xxxxxx = d['xxxxxx']
        return o


