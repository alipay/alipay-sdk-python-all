#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserElectronicidUserbarcodeCreateModel(object):

    def __init__(self):
        self._cert_id = None
        self._expire_time = None

    @property
    def cert_id(self):
        return self._cert_id

    @cert_id.setter
    def cert_id(self, value):
        self._cert_id = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_id:
            if hasattr(self.cert_id, 'to_alipay_dict'):
                params['cert_id'] = self.cert_id.to_alipay_dict()
            else:
                params['cert_id'] = self.cert_id
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserElectronicidUserbarcodeCreateModel()
        if 'cert_id' in d:
            o.cert_id = d['cert_id']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        return o


