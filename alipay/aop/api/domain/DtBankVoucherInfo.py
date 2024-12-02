#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtbankActivitySendControlConfigInfo import DtbankActivitySendControlConfigInfo
from alipay.aop.api.domain.DtBankCouponAvailableTime import DtBankCouponAvailableTime


class DtBankVoucherInfo(object):

    def __init__(self):
        self._activity_send_control_config_info = None
        self._allow_voucher_split = None
        self._coupon_available_time = None
        self._coupon_instruction_list = None
        self._threshold_text = None

    @property
    def activity_send_control_config_info(self):
        return self._activity_send_control_config_info

    @activity_send_control_config_info.setter
    def activity_send_control_config_info(self, value):
        if isinstance(value, DtbankActivitySendControlConfigInfo):
            self._activity_send_control_config_info = value
        else:
            self._activity_send_control_config_info = DtbankActivitySendControlConfigInfo.from_alipay_dict(value)
    @property
    def allow_voucher_split(self):
        return self._allow_voucher_split

    @allow_voucher_split.setter
    def allow_voucher_split(self, value):
        self._allow_voucher_split = value
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
    @property
    def threshold_text(self):
        return self._threshold_text

    @threshold_text.setter
    def threshold_text(self, value):
        self._threshold_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_send_control_config_info:
            if hasattr(self.activity_send_control_config_info, 'to_alipay_dict'):
                params['activity_send_control_config_info'] = self.activity_send_control_config_info.to_alipay_dict()
            else:
                params['activity_send_control_config_info'] = self.activity_send_control_config_info
        if self.allow_voucher_split:
            if hasattr(self.allow_voucher_split, 'to_alipay_dict'):
                params['allow_voucher_split'] = self.allow_voucher_split.to_alipay_dict()
            else:
                params['allow_voucher_split'] = self.allow_voucher_split
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
        if self.threshold_text:
            if hasattr(self.threshold_text, 'to_alipay_dict'):
                params['threshold_text'] = self.threshold_text.to_alipay_dict()
            else:
                params['threshold_text'] = self.threshold_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankVoucherInfo()
        if 'activity_send_control_config_info' in d:
            o.activity_send_control_config_info = d['activity_send_control_config_info']
        if 'allow_voucher_split' in d:
            o.allow_voucher_split = d['allow_voucher_split']
        if 'coupon_available_time' in d:
            o.coupon_available_time = d['coupon_available_time']
        if 'coupon_instruction_list' in d:
            o.coupon_instruction_list = d['coupon_instruction_list']
        if 'threshold_text' in d:
            o.threshold_text = d['threshold_text']
        return o


