#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheThirteen import RainyComplexTypesTheThirteen


class AlipayDataDataserviceTreeapithirdteenRainystestQueryModel(object):

    def __init__(self):
        self._req_ref_strong = None

    @property
    def req_ref_strong(self):
        return self._req_ref_strong

    @req_ref_strong.setter
    def req_ref_strong(self, value):
        if isinstance(value, RainyComplexTypesTheThirteen):
            self._req_ref_strong = value
        else:
            self._req_ref_strong = RainyComplexTypesTheThirteen.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.req_ref_strong:
            if hasattr(self.req_ref_strong, 'to_alipay_dict'):
                params['req_ref_strong'] = self.req_ref_strong.to_alipay_dict()
            else:
                params['req_ref_strong'] = self.req_ref_strong
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceTreeapithirdteenRainystestQueryModel()
        if 'req_ref_strong' in d:
            o.req_ref_strong = d['req_ref_strong']
        return o


