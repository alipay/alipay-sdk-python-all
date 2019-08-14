#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotWifiSetModel(object):

    def __init__(self):
        self._biz_tid = None
        self._pwd = None
        self._ssid = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def pwd(self):
        return self._pwd

    @pwd.setter
    def pwd(self, value):
        self._pwd = value
    @property
    def ssid(self):
        return self._ssid

    @ssid.setter
    def ssid(self, value):
        self._ssid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.pwd:
            if hasattr(self.pwd, 'to_alipay_dict'):
                params['pwd'] = self.pwd.to_alipay_dict()
            else:
                params['pwd'] = self.pwd
        if self.ssid:
            if hasattr(self.ssid, 'to_alipay_dict'):
                params['ssid'] = self.ssid.to_alipay_dict()
            else:
                params['ssid'] = self.ssid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotWifiSetModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'pwd' in d:
            o.pwd = d['pwd']
        if 'ssid' in d:
            o.ssid = d['ssid']
        return o


