#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentCommercialDemoInitSendModel(object):

    def __init__(self):
        self._appid = None
        self._biztoken = None
        self._msgid = None
        self._timestamp_ms = None

    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def biztoken(self):
        return self._biztoken

    @biztoken.setter
    def biztoken(self, value):
        self._biztoken = value
    @property
    def msgid(self):
        return self._msgid

    @msgid.setter
    def msgid(self, value):
        self._msgid = value
    @property
    def timestamp_ms(self):
        return self._timestamp_ms

    @timestamp_ms.setter
    def timestamp_ms(self, value):
        self._timestamp_ms = value


    def to_alipay_dict(self):
        params = dict()
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.biztoken:
            if hasattr(self.biztoken, 'to_alipay_dict'):
                params['biztoken'] = self.biztoken.to_alipay_dict()
            else:
                params['biztoken'] = self.biztoken
        if self.msgid:
            if hasattr(self.msgid, 'to_alipay_dict'):
                params['msgid'] = self.msgid.to_alipay_dict()
            else:
                params['msgid'] = self.msgid
        if self.timestamp_ms:
            if hasattr(self.timestamp_ms, 'to_alipay_dict'):
                params['timestamp_ms'] = self.timestamp_ms.to_alipay_dict()
            else:
                params['timestamp_ms'] = self.timestamp_ms
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentCommercialDemoInitSendModel()
        if 'appid' in d:
            o.appid = d['appid']
        if 'biztoken' in d:
            o.biztoken = d['biztoken']
        if 'msgid' in d:
            o.msgid = d['msgid']
        if 'timestamp_ms' in d:
            o.timestamp_ms = d['timestamp_ms']
        return o


