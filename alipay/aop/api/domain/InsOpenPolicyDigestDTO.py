#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenPolicyDigestDTO(object):

    def __init__(self):
        self._inst_id = None
        self._policy_effect_time = None
        self._policy_end_time = None
        self._policy_no = None
        self._policy_status = None
        self._pre_order_id = None
        self._premium = None
        self._product_code = None
        self._sum_insured = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def policy_effect_time(self):
        return self._policy_effect_time

    @policy_effect_time.setter
    def policy_effect_time(self, value):
        self._policy_effect_time = value
    @property
    def policy_end_time(self):
        return self._policy_end_time

    @policy_end_time.setter
    def policy_end_time(self, value):
        self._policy_end_time = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def policy_status(self):
        return self._policy_status

    @policy_status.setter
    def policy_status(self, value):
        self._policy_status = value
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.policy_effect_time:
            if hasattr(self.policy_effect_time, 'to_alipay_dict'):
                params['policy_effect_time'] = self.policy_effect_time.to_alipay_dict()
            else:
                params['policy_effect_time'] = self.policy_effect_time
        if self.policy_end_time:
            if hasattr(self.policy_end_time, 'to_alipay_dict'):
                params['policy_end_time'] = self.policy_end_time.to_alipay_dict()
            else:
                params['policy_end_time'] = self.policy_end_time
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.policy_status:
            if hasattr(self.policy_status, 'to_alipay_dict'):
                params['policy_status'] = self.policy_status.to_alipay_dict()
            else:
                params['policy_status'] = self.policy_status
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
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
        o = InsOpenPolicyDigestDTO()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'policy_effect_time' in d:
            o.policy_effect_time = d['policy_effect_time']
        if 'policy_end_time' in d:
            o.policy_end_time = d['policy_end_time']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'policy_status' in d:
            o.policy_status = d['policy_status']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'premium' in d:
            o.premium = d['premium']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


