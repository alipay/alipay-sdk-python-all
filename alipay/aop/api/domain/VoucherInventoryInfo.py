#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherInventoryInfo(object):

    def __init__(self):
        self._send_count = None
        self._use_count = None

    @property
    def send_count(self):
        return self._send_count

    @send_count.setter
    def send_count(self, value):
        self._send_count = value
    @property
    def use_count(self):
        return self._use_count

    @use_count.setter
    def use_count(self, value):
        self._use_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.send_count:
            if hasattr(self.send_count, 'to_alipay_dict'):
                params['send_count'] = self.send_count.to_alipay_dict()
            else:
                params['send_count'] = self.send_count
        if self.use_count:
            if hasattr(self.use_count, 'to_alipay_dict'):
                params['use_count'] = self.use_count.to_alipay_dict()
            else:
                params['use_count'] = self.use_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherInventoryInfo()
        if 'send_count' in d:
            o.send_count = d['send_count']
        if 'use_count' in d:
            o.use_count = d['use_count']
        return o


