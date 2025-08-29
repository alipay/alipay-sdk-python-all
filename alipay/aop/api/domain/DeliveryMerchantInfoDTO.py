#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryMerchantInfoDTO(object):

    def __init__(self):
        self._deduct_out = None
        self._deduct_out_type = None
        self._merchant_pid = None
        self._mrchant_pid = None

    @property
    def deduct_out(self):
        return self._deduct_out

    @deduct_out.setter
    def deduct_out(self, value):
        self._deduct_out = value
    @property
    def deduct_out_type(self):
        return self._deduct_out_type

    @deduct_out_type.setter
    def deduct_out_type(self, value):
        self._deduct_out_type = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def mrchant_pid(self):
        return self._mrchant_pid

    @mrchant_pid.setter
    def mrchant_pid(self, value):
        self._mrchant_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_out:
            if hasattr(self.deduct_out, 'to_alipay_dict'):
                params['deduct_out'] = self.deduct_out.to_alipay_dict()
            else:
                params['deduct_out'] = self.deduct_out
        if self.deduct_out_type:
            if hasattr(self.deduct_out_type, 'to_alipay_dict'):
                params['deduct_out_type'] = self.deduct_out_type.to_alipay_dict()
            else:
                params['deduct_out_type'] = self.deduct_out_type
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.mrchant_pid:
            if hasattr(self.mrchant_pid, 'to_alipay_dict'):
                params['mrchant_pid'] = self.mrchant_pid.to_alipay_dict()
            else:
                params['mrchant_pid'] = self.mrchant_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryMerchantInfoDTO()
        if 'deduct_out' in d:
            o.deduct_out = d['deduct_out']
        if 'deduct_out_type' in d:
            o.deduct_out_type = d['deduct_out_type']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'mrchant_pid' in d:
            o.mrchant_pid = d['mrchant_pid']
        return o


