#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsPolicyDigest(object):

    def __init__(self):
        self._effect_end_time = None
        self._effect_start_time = None
        self._out_policy_no = None
        self._policy_no = None
        self._policy_status = None
        self._policy_type = None
        self._premium = None
        self._sum_insured = None
        self._surrender_amount = None
        self._surrender_time = None

    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def out_policy_no(self):
        return self._out_policy_no

    @out_policy_no.setter
    def out_policy_no(self, value):
        self._out_policy_no = value
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
    def policy_type(self):
        return self._policy_type

    @policy_type.setter
    def policy_type(self, value):
        self._policy_type = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value
    @property
    def surrender_amount(self):
        return self._surrender_amount

    @surrender_amount.setter
    def surrender_amount(self, value):
        self._surrender_amount = value
    @property
    def surrender_time(self):
        return self._surrender_time

    @surrender_time.setter
    def surrender_time(self, value):
        self._surrender_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.effect_end_time:
            if hasattr(self.effect_end_time, 'to_alipay_dict'):
                params['effect_end_time'] = self.effect_end_time.to_alipay_dict()
            else:
                params['effect_end_time'] = self.effect_end_time
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.out_policy_no:
            if hasattr(self.out_policy_no, 'to_alipay_dict'):
                params['out_policy_no'] = self.out_policy_no.to_alipay_dict()
            else:
                params['out_policy_no'] = self.out_policy_no
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
        if self.policy_type:
            if hasattr(self.policy_type, 'to_alipay_dict'):
                params['policy_type'] = self.policy_type.to_alipay_dict()
            else:
                params['policy_type'] = self.policy_type
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        if self.surrender_amount:
            if hasattr(self.surrender_amount, 'to_alipay_dict'):
                params['surrender_amount'] = self.surrender_amount.to_alipay_dict()
            else:
                params['surrender_amount'] = self.surrender_amount
        if self.surrender_time:
            if hasattr(self.surrender_time, 'to_alipay_dict'):
                params['surrender_time'] = self.surrender_time.to_alipay_dict()
            else:
                params['surrender_time'] = self.surrender_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsPolicyDigest()
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'out_policy_no' in d:
            o.out_policy_no = d['out_policy_no']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'policy_status' in d:
            o.policy_status = d['policy_status']
        if 'policy_type' in d:
            o.policy_type = d['policy_type']
        if 'premium' in d:
            o.premium = d['premium']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        if 'surrender_amount' in d:
            o.surrender_amount = d['surrender_amount']
        if 'surrender_time' in d:
            o.surrender_time = d['surrender_time']
        return o


