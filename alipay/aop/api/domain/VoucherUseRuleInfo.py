#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherUseTimeInfo import VoucherUseTimeInfo


class VoucherUseRuleInfo(object):

    def __init__(self):
        self._quantity_limit_per_user = None
        self._quantity_limit_per_user_period_type = None
        self._voucher_max_use_times = None
        self._voucher_use_ext_info = None
        self._voucher_use_time_info = None

    @property
    def quantity_limit_per_user(self):
        return self._quantity_limit_per_user

    @quantity_limit_per_user.setter
    def quantity_limit_per_user(self, value):
        self._quantity_limit_per_user = value
    @property
    def quantity_limit_per_user_period_type(self):
        return self._quantity_limit_per_user_period_type

    @quantity_limit_per_user_period_type.setter
    def quantity_limit_per_user_period_type(self, value):
        self._quantity_limit_per_user_period_type = value
    @property
    def voucher_max_use_times(self):
        return self._voucher_max_use_times

    @voucher_max_use_times.setter
    def voucher_max_use_times(self, value):
        self._voucher_max_use_times = value
    @property
    def voucher_use_ext_info(self):
        return self._voucher_use_ext_info

    @voucher_use_ext_info.setter
    def voucher_use_ext_info(self, value):
        self._voucher_use_ext_info = value
    @property
    def voucher_use_time_info(self):
        return self._voucher_use_time_info

    @voucher_use_time_info.setter
    def voucher_use_time_info(self, value):
        if isinstance(value, VoucherUseTimeInfo):
            self._voucher_use_time_info = value
        else:
            self._voucher_use_time_info = VoucherUseTimeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.quantity_limit_per_user:
            if hasattr(self.quantity_limit_per_user, 'to_alipay_dict'):
                params['quantity_limit_per_user'] = self.quantity_limit_per_user.to_alipay_dict()
            else:
                params['quantity_limit_per_user'] = self.quantity_limit_per_user
        if self.quantity_limit_per_user_period_type:
            if hasattr(self.quantity_limit_per_user_period_type, 'to_alipay_dict'):
                params['quantity_limit_per_user_period_type'] = self.quantity_limit_per_user_period_type.to_alipay_dict()
            else:
                params['quantity_limit_per_user_period_type'] = self.quantity_limit_per_user_period_type
        if self.voucher_max_use_times:
            if hasattr(self.voucher_max_use_times, 'to_alipay_dict'):
                params['voucher_max_use_times'] = self.voucher_max_use_times.to_alipay_dict()
            else:
                params['voucher_max_use_times'] = self.voucher_max_use_times
        if self.voucher_use_ext_info:
            if hasattr(self.voucher_use_ext_info, 'to_alipay_dict'):
                params['voucher_use_ext_info'] = self.voucher_use_ext_info.to_alipay_dict()
            else:
                params['voucher_use_ext_info'] = self.voucher_use_ext_info
        if self.voucher_use_time_info:
            if hasattr(self.voucher_use_time_info, 'to_alipay_dict'):
                params['voucher_use_time_info'] = self.voucher_use_time_info.to_alipay_dict()
            else:
                params['voucher_use_time_info'] = self.voucher_use_time_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUseRuleInfo()
        if 'quantity_limit_per_user' in d:
            o.quantity_limit_per_user = d['quantity_limit_per_user']
        if 'quantity_limit_per_user_period_type' in d:
            o.quantity_limit_per_user_period_type = d['quantity_limit_per_user_period_type']
        if 'voucher_max_use_times' in d:
            o.voucher_max_use_times = d['voucher_max_use_times']
        if 'voucher_use_ext_info' in d:
            o.voucher_use_ext_info = d['voucher_use_ext_info']
        if 'voucher_use_time_info' in d:
            o.voucher_use_time_info = d['voucher_use_time_info']
        return o


