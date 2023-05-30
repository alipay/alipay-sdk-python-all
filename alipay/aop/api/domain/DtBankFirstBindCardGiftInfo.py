#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtBankCouponAvailableTime import DtBankCouponAvailableTime


class DtBankFirstBindCardGiftInfo(object):

    def __init__(self):
        self._assigned_pid_list = None
        self._bank_code_config_account_limit = None
        self._bind_source_list = None
        self._coupon_available_time = None
        self._coupon_instruction_list = None

    @property
    def assigned_pid_list(self):
        return self._assigned_pid_list

    @assigned_pid_list.setter
    def assigned_pid_list(self, value):
        if isinstance(value, list):
            self._assigned_pid_list = list()
            for i in value:
                self._assigned_pid_list.append(i)
    @property
    def bank_code_config_account_limit(self):
        return self._bank_code_config_account_limit

    @bank_code_config_account_limit.setter
    def bank_code_config_account_limit(self, value):
        self._bank_code_config_account_limit = value
    @property
    def bind_source_list(self):
        return self._bind_source_list

    @bind_source_list.setter
    def bind_source_list(self, value):
        if isinstance(value, list):
            self._bind_source_list = list()
            for i in value:
                self._bind_source_list.append(i)
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
        if self.assigned_pid_list:
            if isinstance(self.assigned_pid_list, list):
                for i in range(0, len(self.assigned_pid_list)):
                    element = self.assigned_pid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.assigned_pid_list[i] = element.to_alipay_dict()
            if hasattr(self.assigned_pid_list, 'to_alipay_dict'):
                params['assigned_pid_list'] = self.assigned_pid_list.to_alipay_dict()
            else:
                params['assigned_pid_list'] = self.assigned_pid_list
        if self.bank_code_config_account_limit:
            if hasattr(self.bank_code_config_account_limit, 'to_alipay_dict'):
                params['bank_code_config_account_limit'] = self.bank_code_config_account_limit.to_alipay_dict()
            else:
                params['bank_code_config_account_limit'] = self.bank_code_config_account_limit
        if self.bind_source_list:
            if isinstance(self.bind_source_list, list):
                for i in range(0, len(self.bind_source_list)):
                    element = self.bind_source_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bind_source_list[i] = element.to_alipay_dict()
            if hasattr(self.bind_source_list, 'to_alipay_dict'):
                params['bind_source_list'] = self.bind_source_list.to_alipay_dict()
            else:
                params['bind_source_list'] = self.bind_source_list
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
        o = DtBankFirstBindCardGiftInfo()
        if 'assigned_pid_list' in d:
            o.assigned_pid_list = d['assigned_pid_list']
        if 'bank_code_config_account_limit' in d:
            o.bank_code_config_account_limit = d['bank_code_config_account_limit']
        if 'bind_source_list' in d:
            o.bind_source_list = d['bind_source_list']
        if 'coupon_available_time' in d:
            o.coupon_available_time = d['coupon_available_time']
        if 'coupon_instruction_list' in d:
            o.coupon_instruction_list = d['coupon_instruction_list']
        return o


