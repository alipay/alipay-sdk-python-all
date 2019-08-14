#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundExtendParams(object):

    def __init__(self):
        self._credit_category_id = None
        self._credit_service_id = None

    @property
    def credit_category_id(self):
        return self._credit_category_id

    @credit_category_id.setter
    def credit_category_id(self, value):
        self._credit_category_id = value
    @property
    def credit_service_id(self):
        return self._credit_service_id

    @credit_service_id.setter
    def credit_service_id(self, value):
        self._credit_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_category_id:
            if hasattr(self.credit_category_id, 'to_alipay_dict'):
                params['credit_category_id'] = self.credit_category_id.to_alipay_dict()
            else:
                params['credit_category_id'] = self.credit_category_id
        if self.credit_service_id:
            if hasattr(self.credit_service_id, 'to_alipay_dict'):
                params['credit_service_id'] = self.credit_service_id.to_alipay_dict()
            else:
                params['credit_service_id'] = self.credit_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundExtendParams()
        if 'credit_category_id' in d:
            o.credit_category_id = d['credit_category_id']
        if 'credit_service_id' in d:
            o.credit_service_id = d['credit_service_id']
        return o


