#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsSubOrderEmploymentDigest(object):

    def __init__(self):
        self._close_reason = None
        self._out_employee_id = None
        self._policy_no = None
        self._premium = None
        self._sub_order_no = None
        self._sub_order_status = None
        self._sum_insured = None

    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def out_employee_id(self):
        return self._out_employee_id

    @out_employee_id.setter
    def out_employee_id(self, value):
        self._out_employee_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def sub_order_no(self):
        return self._sub_order_no

    @sub_order_no.setter
    def sub_order_no(self, value):
        self._sub_order_no = value
    @property
    def sub_order_status(self):
        return self._sub_order_status

    @sub_order_status.setter
    def sub_order_status(self, value):
        self._sub_order_status = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
        if self.out_employee_id:
            if hasattr(self.out_employee_id, 'to_alipay_dict'):
                params['out_employee_id'] = self.out_employee_id.to_alipay_dict()
            else:
                params['out_employee_id'] = self.out_employee_id
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.sub_order_no:
            if hasattr(self.sub_order_no, 'to_alipay_dict'):
                params['sub_order_no'] = self.sub_order_no.to_alipay_dict()
            else:
                params['sub_order_no'] = self.sub_order_no
        if self.sub_order_status:
            if hasattr(self.sub_order_status, 'to_alipay_dict'):
                params['sub_order_status'] = self.sub_order_status.to_alipay_dict()
            else:
                params['sub_order_status'] = self.sub_order_status
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsSubOrderEmploymentDigest()
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'out_employee_id' in d:
            o.out_employee_id = d['out_employee_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'premium' in d:
            o.premium = d['premium']
        if 'sub_order_no' in d:
            o.sub_order_no = d['sub_order_no']
        if 'sub_order_status' in d:
            o.sub_order_status = d['sub_order_status']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


