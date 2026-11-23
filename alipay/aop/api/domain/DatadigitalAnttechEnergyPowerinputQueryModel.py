#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechEnergyPowerinputQueryModel(object):

    def __init__(self):
        self._agreement_code = None
        self._end_date = None
        self._object_code = None
        self._request_id = None
        self._start_date = None
        self._target_customer_code = None

    @property
    def agreement_code(self):
        return self._agreement_code

    @agreement_code.setter
    def agreement_code(self, value):
        self._agreement_code = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def object_code(self):
        return self._object_code

    @object_code.setter
    def object_code(self, value):
        self._object_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def target_customer_code(self):
        return self._target_customer_code

    @target_customer_code.setter
    def target_customer_code(self, value):
        self._target_customer_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_code:
            if hasattr(self.agreement_code, 'to_alipay_dict'):
                params['agreement_code'] = self.agreement_code.to_alipay_dict()
            else:
                params['agreement_code'] = self.agreement_code
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.object_code:
            if hasattr(self.object_code, 'to_alipay_dict'):
                params['object_code'] = self.object_code.to_alipay_dict()
            else:
                params['object_code'] = self.object_code
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.target_customer_code:
            if hasattr(self.target_customer_code, 'to_alipay_dict'):
                params['target_customer_code'] = self.target_customer_code.to_alipay_dict()
            else:
                params['target_customer_code'] = self.target_customer_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechEnergyPowerinputQueryModel()
        if 'agreement_code' in d:
            o.agreement_code = d['agreement_code']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'object_code' in d:
            o.object_code = d['object_code']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'target_customer_code' in d:
            o.target_customer_code = d['target_customer_code']
        return o


