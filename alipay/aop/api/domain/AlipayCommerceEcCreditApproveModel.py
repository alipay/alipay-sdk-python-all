#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcCreditApproveModel(object):

    def __init__(self):
        self._apply_serial_no = None
        self._apply_time = None
        self._available_limit = None
        self._capital_limit = None
        self._enterprise_id = None
        self._expiration_date = None
        self._out_request_no = None
        self._rejected_reason = None
        self._result = None

    @property
    def apply_serial_no(self):
        return self._apply_serial_no

    @apply_serial_no.setter
    def apply_serial_no(self, value):
        self._apply_serial_no = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def available_limit(self):
        return self._available_limit

    @available_limit.setter
    def available_limit(self, value):
        self._available_limit = value
    @property
    def capital_limit(self):
        return self._capital_limit

    @capital_limit.setter
    def capital_limit(self, value):
        self._capital_limit = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def rejected_reason(self):
        return self._rejected_reason

    @rejected_reason.setter
    def rejected_reason(self, value):
        self._rejected_reason = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_serial_no:
            if hasattr(self.apply_serial_no, 'to_alipay_dict'):
                params['apply_serial_no'] = self.apply_serial_no.to_alipay_dict()
            else:
                params['apply_serial_no'] = self.apply_serial_no
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.available_limit:
            if hasattr(self.available_limit, 'to_alipay_dict'):
                params['available_limit'] = self.available_limit.to_alipay_dict()
            else:
                params['available_limit'] = self.available_limit
        if self.capital_limit:
            if hasattr(self.capital_limit, 'to_alipay_dict'):
                params['capital_limit'] = self.capital_limit.to_alipay_dict()
            else:
                params['capital_limit'] = self.capital_limit
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.expiration_date:
            if hasattr(self.expiration_date, 'to_alipay_dict'):
                params['expiration_date'] = self.expiration_date.to_alipay_dict()
            else:
                params['expiration_date'] = self.expiration_date
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.rejected_reason:
            if hasattr(self.rejected_reason, 'to_alipay_dict'):
                params['rejected_reason'] = self.rejected_reason.to_alipay_dict()
            else:
                params['rejected_reason'] = self.rejected_reason
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditApproveModel()
        if 'apply_serial_no' in d:
            o.apply_serial_no = d['apply_serial_no']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'available_limit' in d:
            o.available_limit = d['available_limit']
        if 'capital_limit' in d:
            o.capital_limit = d['capital_limit']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'expiration_date' in d:
            o.expiration_date = d['expiration_date']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'rejected_reason' in d:
            o.rejected_reason = d['rejected_reason']
        if 'result' in d:
            o.result = d['result']
        return o


