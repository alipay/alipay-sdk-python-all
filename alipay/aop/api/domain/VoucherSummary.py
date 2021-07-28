#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherSummary(object):

    def __init__(self):
        self._publish_count = None
        self._used_count = None

    @property
    def publish_count(self):
        return self._publish_count

    @publish_count.setter
    def publish_count(self, value):
        self._publish_count = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.publish_count:
            if hasattr(self.publish_count, 'to_alipay_dict'):
                params['publish_count'] = self.publish_count.to_alipay_dict()
            else:
                params['publish_count'] = self.publish_count
        if self.used_count:
            if hasattr(self.used_count, 'to_alipay_dict'):
                params['used_count'] = self.used_count.to_alipay_dict()
            else:
                params['used_count'] = self.used_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherSummary()
        if 'publish_count' in d:
            o.publish_count = d['publish_count']
        if 'used_count' in d:
            o.used_count = d['used_count']
        return o


