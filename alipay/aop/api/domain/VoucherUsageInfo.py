#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherUsageInfo(object):

    def __init__(self):
        self._goto_use_url = None
        self._use_record_url = None

    @property
    def goto_use_url(self):
        return self._goto_use_url

    @goto_use_url.setter
    def goto_use_url(self, value):
        self._goto_use_url = value
    @property
    def use_record_url(self):
        return self._use_record_url

    @use_record_url.setter
    def use_record_url(self, value):
        self._use_record_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.goto_use_url:
            if hasattr(self.goto_use_url, 'to_alipay_dict'):
                params['goto_use_url'] = self.goto_use_url.to_alipay_dict()
            else:
                params['goto_use_url'] = self.goto_use_url
        if self.use_record_url:
            if hasattr(self.use_record_url, 'to_alipay_dict'):
                params['use_record_url'] = self.use_record_url.to_alipay_dict()
            else:
                params['use_record_url'] = self.use_record_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUsageInfo()
        if 'goto_use_url' in d:
            o.goto_use_url = d['goto_use_url']
        if 'use_record_url' in d:
            o.use_record_url = d['use_record_url']
        return o


