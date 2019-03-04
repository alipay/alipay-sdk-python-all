#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataNamelistSendModel(object):

    def __init__(self):
        self._bizname = None
        self._payload = None
        self._sysname = None

    @property
    def bizname(self):
        return self._bizname

    @bizname.setter
    def bizname(self, value):
        self._bizname = value
    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = value
    @property
    def sysname(self):
        return self._sysname

    @sysname.setter
    def sysname(self, value):
        self._sysname = value


    def to_alipay_dict(self):
        params = dict()
        if self.bizname:
            if hasattr(self.bizname, 'to_alipay_dict'):
                params['bizname'] = self.bizname.to_alipay_dict()
            else:
                params['bizname'] = self.bizname
        if self.payload:
            if hasattr(self.payload, 'to_alipay_dict'):
                params['payload'] = self.payload.to_alipay_dict()
            else:
                params['payload'] = self.payload
        if self.sysname:
            if hasattr(self.sysname, 'to_alipay_dict'):
                params['sysname'] = self.sysname.to_alipay_dict()
            else:
                params['sysname'] = self.sysname
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataNamelistSendModel()
        if 'bizname' in d:
            o.bizname = d['bizname']
        if 'payload' in d:
            o.payload = d['payload']
        if 'sysname' in d:
            o.sysname = d['sysname']
        return o


