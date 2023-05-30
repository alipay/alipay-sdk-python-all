#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtBankCouponAvailableTime import DtBankCouponAvailableTime


class DtBankVoucherInfo(object):

    def __init__(self):
        self._coupon_available_time = None
        self._coupon_instruction_list = None

    @property
    def coupon_available_time(self):
        return self._coupon_available_time

    @coupon_available_time.setter
    def coupon_available_time(self, value):
        if isinstance(value, DtBankCouponAvailableTime):
            self._coupon_available_time = value
        else:
            self._coupon_available_time = DtBankCouponAvailableTime.from_alipay_dict(value)
    @property
    def coupon_instruction_list(self):
        return self._coupon_instruction_list

    @coupon_instruction_list.setter
    def coupon_instruction_list(self, value):
        if isinstance(value, list):
            self._coupon_instruction_list = list()
            for i in value:
                self._coupon_instruction_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_available_time:
            if hasattr(self.coupon_available_time, 'to_alipay_dict'):
                params['coupon_available_time'] = self.coupon_available_time.to_alipay_dict()
            else:
                params['coupon_available_time'] = self.coupon_available_time
        if self.coupon_instruction_list:
            if isinstance(self.coupon_instruction_list, list):
                for i in range(0, len(self.coupon_instruction_list)):
                    element = self.coupon_instruction_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coupon_instruction_list[i] = element.to_alipay_dict()
            if hasattr(self.coupon_instruction_list, 'to_alipay_dict'):
                params['coupon_instruction_list'] = self.coupon_instruction_list.to_alipay_dict()
            else:
                params['coupon_instruction_list'] = self.coupon_instruction_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankVoucherInfo()
        if 'coupon_available_time' in d:
            o.coupon_available_time = d['coupon_available_time']
        if 'coupon_instruction_list' in d:
            o.coupon_instruction_list = d['coupon_instruction_list']
        return o


