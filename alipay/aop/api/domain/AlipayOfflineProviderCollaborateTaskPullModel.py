#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderCollaborateTaskPullModel(object):

    def __init__(self):
        self._count = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderCollaborateTaskPullModel()
        if 'count' in d:
            o.count = d['count']
        return o


