#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationServiceApplyQueryModel(object):

    def __init__(self):
        self._apply_record_id = None
        self._service_code = None

    @property
    def apply_record_id(self):
        return self._apply_record_id

    @apply_record_id.setter
    def apply_record_id(self, value):
        self._apply_record_id = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_record_id:
            if hasattr(self.apply_record_id, 'to_alipay_dict'):
                params['apply_record_id'] = self.apply_record_id.to_alipay_dict()
            else:
                params['apply_record_id'] = self.apply_record_id
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationServiceApplyQueryModel()
        if 'apply_record_id' in d:
            o.apply_record_id = d['apply_record_id']
        if 'service_code' in d:
            o.service_code = d['service_code']
        return o


