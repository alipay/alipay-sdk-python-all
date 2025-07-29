#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFourteen import RainyComplexTypesTheFourteen
from alipay.aop.api.domain.RainyComplexTypesTheFourteen import RainyComplexTypesTheFourteen


class AlipayDataDataserviceTreeapifourteenRainystestQueryModel(object):

    def __init__(self):
        self._req_copy_weak_ref = None
        self._req_field_weak_ref = None

    @property
    def req_copy_weak_ref(self):
        return self._req_copy_weak_ref

    @req_copy_weak_ref.setter
    def req_copy_weak_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourteen):
            self._req_copy_weak_ref = value
        else:
            self._req_copy_weak_ref = RainyComplexTypesTheFourteen.from_alipay_dict(value)
    @property
    def req_field_weak_ref(self):
        return self._req_field_weak_ref

    @req_field_weak_ref.setter
    def req_field_weak_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourteen):
            self._req_field_weak_ref = value
        else:
            self._req_field_weak_ref = RainyComplexTypesTheFourteen.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.req_copy_weak_ref:
            if hasattr(self.req_copy_weak_ref, 'to_alipay_dict'):
                params['req_copy_weak_ref'] = self.req_copy_weak_ref.to_alipay_dict()
            else:
                params['req_copy_weak_ref'] = self.req_copy_weak_ref
        if self.req_field_weak_ref:
            if hasattr(self.req_field_weak_ref, 'to_alipay_dict'):
                params['req_field_weak_ref'] = self.req_field_weak_ref.to_alipay_dict()
            else:
                params['req_field_weak_ref'] = self.req_field_weak_ref
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceTreeapifourteenRainystestQueryModel()
        if 'req_copy_weak_ref' in d:
            o.req_copy_weak_ref = d['req_copy_weak_ref']
        if 'req_field_weak_ref' in d:
            o.req_field_weak_ref = d['req_field_weak_ref']
        return o


