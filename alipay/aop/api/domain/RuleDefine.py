#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RuleDefine(object):

    def __init__(self):
        self._biz_tids = None

    @property
    def biz_tids(self):
        return self._biz_tids

    @biz_tids.setter
    def biz_tids(self, value):
        if isinstance(value, list):
            self._biz_tids = list()
            for i in value:
                self._biz_tids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tids:
            if isinstance(self.biz_tids, list):
                for i in range(0, len(self.biz_tids)):
                    element = self.biz_tids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_tids[i] = element.to_alipay_dict()
            if hasattr(self.biz_tids, 'to_alipay_dict'):
                params['biz_tids'] = self.biz_tids.to_alipay_dict()
            else:
                params['biz_tids'] = self.biz_tids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleDefine()
        if 'biz_tids' in d:
            o.biz_tids = d['biz_tids']
        return o


