#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PreCreateWaybillIstd(object):

    def __init__(self):
        self._coupon_fee = None
        self._deliver_fee = None
        self._dispatch_duration = None
        self._distance = None
        self._fee = None
        self._insurance_fee = None
        self._logistics_code = None
        self._logistics_token = None
        self._pay_amount = None
        self._service_code = None
        self._third_code = None
        self._third_sub_code = None
        self._third_sub_msg = None

    @property
    def coupon_fee(self):
        return self._coupon_fee

    @coupon_fee.setter
    def coupon_fee(self, value):
        self._coupon_fee = value
    @property
    def deliver_fee(self):
        return self._deliver_fee

    @deliver_fee.setter
    def deliver_fee(self, value):
        self._deliver_fee = value
    @property
    def dispatch_duration(self):
        return self._dispatch_duration

    @dispatch_duration.setter
    def dispatch_duration(self, value):
        self._dispatch_duration = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def insurance_fee(self):
        return self._insurance_fee

    @insurance_fee.setter
    def insurance_fee(self, value):
        self._insurance_fee = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_token(self):
        return self._logistics_token

    @logistics_token.setter
    def logistics_token(self, value):
        self._logistics_token = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def third_code(self):
        return self._third_code

    @third_code.setter
    def third_code(self, value):
        self._third_code = value
    @property
    def third_sub_code(self):
        return self._third_sub_code

    @third_sub_code.setter
    def third_sub_code(self, value):
        self._third_sub_code = value
    @property
    def third_sub_msg(self):
        return self._third_sub_msg

    @third_sub_msg.setter
    def third_sub_msg(self, value):
        self._third_sub_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_fee:
            if hasattr(self.coupon_fee, 'to_alipay_dict'):
                params['coupon_fee'] = self.coupon_fee.to_alipay_dict()
            else:
                params['coupon_fee'] = self.coupon_fee
        if self.deliver_fee:
            if hasattr(self.deliver_fee, 'to_alipay_dict'):
                params['deliver_fee'] = self.deliver_fee.to_alipay_dict()
            else:
                params['deliver_fee'] = self.deliver_fee
        if self.dispatch_duration:
            if hasattr(self.dispatch_duration, 'to_alipay_dict'):
                params['dispatch_duration'] = self.dispatch_duration.to_alipay_dict()
            else:
                params['dispatch_duration'] = self.dispatch_duration
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.insurance_fee:
            if hasattr(self.insurance_fee, 'to_alipay_dict'):
                params['insurance_fee'] = self.insurance_fee.to_alipay_dict()
            else:
                params['insurance_fee'] = self.insurance_fee
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_token:
            if hasattr(self.logistics_token, 'to_alipay_dict'):
                params['logistics_token'] = self.logistics_token.to_alipay_dict()
            else:
                params['logistics_token'] = self.logistics_token
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.third_code:
            if hasattr(self.third_code, 'to_alipay_dict'):
                params['third_code'] = self.third_code.to_alipay_dict()
            else:
                params['third_code'] = self.third_code
        if self.third_sub_code:
            if hasattr(self.third_sub_code, 'to_alipay_dict'):
                params['third_sub_code'] = self.third_sub_code.to_alipay_dict()
            else:
                params['third_sub_code'] = self.third_sub_code
        if self.third_sub_msg:
            if hasattr(self.third_sub_msg, 'to_alipay_dict'):
                params['third_sub_msg'] = self.third_sub_msg.to_alipay_dict()
            else:
                params['third_sub_msg'] = self.third_sub_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PreCreateWaybillIstd()
        if 'coupon_fee' in d:
            o.coupon_fee = d['coupon_fee']
        if 'deliver_fee' in d:
            o.deliver_fee = d['deliver_fee']
        if 'dispatch_duration' in d:
            o.dispatch_duration = d['dispatch_duration']
        if 'distance' in d:
            o.distance = d['distance']
        if 'fee' in d:
            o.fee = d['fee']
        if 'insurance_fee' in d:
            o.insurance_fee = d['insurance_fee']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_token' in d:
            o.logistics_token = d['logistics_token']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'third_code' in d:
            o.third_code = d['third_code']
        if 'third_sub_code' in d:
            o.third_sub_code = d['third_sub_code']
        if 'third_sub_msg' in d:
            o.third_sub_msg = d['third_sub_msg']
        return o


