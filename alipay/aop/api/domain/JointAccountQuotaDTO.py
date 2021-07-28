#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JointAccountQuotaDTO(object):

    def __init__(self):
        self._quota_dimension = None
        self._quota_total = None

    @property
    def quota_dimension(self):
        return self._quota_dimension

    @quota_dimension.setter
    def quota_dimension(self, value):
        self._quota_dimension = value
    @property
    def quota_total(self):
        return self._quota_total

    @quota_total.setter
    def quota_total(self, value):
        self._quota_total = value


    def to_alipay_dict(self):
        params = dict()
        if self.quota_dimension:
            if hasattr(self.quota_dimension, 'to_alipay_dict'):
                params['quota_dimension'] = self.quota_dimension.to_alipay_dict()
            else:
                params['quota_dimension'] = self.quota_dimension
        if self.quota_total:
            if hasattr(self.quota_total, 'to_alipay_dict'):
                params['quota_total'] = self.quota_total.to_alipay_dict()
            else:
                params['quota_total'] = self.quota_total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JointAccountQuotaDTO()
        if 'quota_dimension' in d:
            o.quota_dimension = d['quota_dimension']
        if 'quota_total' in d:
            o.quota_total = d['quota_total']
        return o


