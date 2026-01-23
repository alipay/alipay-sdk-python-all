#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AllocSignBizParam(object):

    def __init__(self):
        self._limit_alloc_ratio_disable = None

    @property
    def limit_alloc_ratio_disable(self):
        return self._limit_alloc_ratio_disable

    @limit_alloc_ratio_disable.setter
    def limit_alloc_ratio_disable(self, value):
        self._limit_alloc_ratio_disable = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit_alloc_ratio_disable:
            if hasattr(self.limit_alloc_ratio_disable, 'to_alipay_dict'):
                params['limit_alloc_ratio_disable'] = self.limit_alloc_ratio_disable.to_alipay_dict()
            else:
                params['limit_alloc_ratio_disable'] = self.limit_alloc_ratio_disable
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AllocSignBizParam()
        if 'limit_alloc_ratio_disable' in d:
            o.limit_alloc_ratio_disable = d['limit_alloc_ratio_disable']
        return o


