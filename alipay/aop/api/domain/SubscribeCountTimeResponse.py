#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubscribeCountTimeResponse(object):

    def __init__(self):
        self._count_success = None

    @property
    def count_success(self):
        return self._count_success

    @count_success.setter
    def count_success(self, value):
        self._count_success = value


    def to_alipay_dict(self):
        params = dict()
        if self.count_success:
            if hasattr(self.count_success, 'to_alipay_dict'):
                params['count_success'] = self.count_success.to_alipay_dict()
            else:
                params['count_success'] = self.count_success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscribeCountTimeResponse()
        if 'count_success' in d:
            o.count_success = d['count_success']
        return o


