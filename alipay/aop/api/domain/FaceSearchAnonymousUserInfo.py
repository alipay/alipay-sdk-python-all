#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaceSearchAnonymousUserInfo(object):

    def __init__(self):
        self._merchantid = None
        self._merchantuid = None

    @property
    def merchantid(self):
        return self._merchantid

    @merchantid.setter
    def merchantid(self, value):
        self._merchantid = value
    @property
    def merchantuid(self):
        return self._merchantuid

    @merchantuid.setter
    def merchantuid(self, value):
        self._merchantuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchantid:
            if hasattr(self.merchantid, 'to_alipay_dict'):
                params['merchantid'] = self.merchantid.to_alipay_dict()
            else:
                params['merchantid'] = self.merchantid
        if self.merchantuid:
            if hasattr(self.merchantuid, 'to_alipay_dict'):
                params['merchantuid'] = self.merchantuid.to_alipay_dict()
            else:
                params['merchantuid'] = self.merchantuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaceSearchAnonymousUserInfo()
        if 'merchantid' in d:
            o.merchantid = d['merchantid']
        if 'merchantuid' in d:
            o.merchantuid = d['merchantuid']
        return o


