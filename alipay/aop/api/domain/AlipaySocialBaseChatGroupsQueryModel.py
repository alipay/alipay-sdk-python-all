#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseChatGroupsQueryModel(object):

    def __init__(self):
        self._last_key = None

    @property
    def last_key(self):
        return self._last_key

    @last_key.setter
    def last_key(self, value):
        self._last_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.last_key:
            if hasattr(self.last_key, 'to_alipay_dict'):
                params['last_key'] = self.last_key.to_alipay_dict()
            else:
                params['last_key'] = self.last_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseChatGroupsQueryModel()
        if 'last_key' in d:
            o.last_key = d['last_key']
        return o


