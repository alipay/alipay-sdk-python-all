#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RelationInfo(object):

    def __init__(self):
        self._recency = None

    @property
    def recency(self):
        return self._recency

    @recency.setter
    def recency(self, value):
        self._recency = value


    def to_alipay_dict(self):
        params = dict()
        if self.recency:
            if hasattr(self.recency, 'to_alipay_dict'):
                params['recency'] = self.recency.to_alipay_dict()
            else:
                params['recency'] = self.recency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RelationInfo()
        if 'recency' in d:
            o.recency = d['recency']
        return o


