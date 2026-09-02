#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AutohomeContactStatusModel(object):

    def __init__(self):
        self._has_contacted = None
        self._has_intent = None

    @property
    def has_contacted(self):
        return self._has_contacted

    @has_contacted.setter
    def has_contacted(self, value):
        self._has_contacted = value
    @property
    def has_intent(self):
        return self._has_intent

    @has_intent.setter
    def has_intent(self, value):
        self._has_intent = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_contacted:
            if hasattr(self.has_contacted, 'to_alipay_dict'):
                params['has_contacted'] = self.has_contacted.to_alipay_dict()
            else:
                params['has_contacted'] = self.has_contacted
        if self.has_intent:
            if hasattr(self.has_intent, 'to_alipay_dict'):
                params['has_intent'] = self.has_intent.to_alipay_dict()
            else:
                params['has_intent'] = self.has_intent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AutohomeContactStatusModel()
        if 'has_contacted' in d:
            o.has_contacted = d['has_contacted']
        if 'has_intent' in d:
            o.has_intent = d['has_intent']
        return o


