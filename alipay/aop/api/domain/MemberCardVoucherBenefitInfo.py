#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberCardVoucherBenefitInfo(object):

    def __init__(self):
        self._modulus = None
        self._voucher_activity_id = None
        self._voucher_type = None
        self._vouvher_type = None

    @property
    def modulus(self):
        return self._modulus

    @modulus.setter
    def modulus(self, value):
        self._modulus = value
    @property
    def voucher_activity_id(self):
        return self._voucher_activity_id

    @voucher_activity_id.setter
    def voucher_activity_id(self, value):
        self._voucher_activity_id = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def vouvher_type(self):
        return self._vouvher_type

    @vouvher_type.setter
    def vouvher_type(self, value):
        self._vouvher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.modulus:
            if hasattr(self.modulus, 'to_alipay_dict'):
                params['modulus'] = self.modulus.to_alipay_dict()
            else:
                params['modulus'] = self.modulus
        if self.voucher_activity_id:
            if hasattr(self.voucher_activity_id, 'to_alipay_dict'):
                params['voucher_activity_id'] = self.voucher_activity_id.to_alipay_dict()
            else:
                params['voucher_activity_id'] = self.voucher_activity_id
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        if self.vouvher_type:
            if hasattr(self.vouvher_type, 'to_alipay_dict'):
                params['vouvher_type'] = self.vouvher_type.to_alipay_dict()
            else:
                params['vouvher_type'] = self.vouvher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCardVoucherBenefitInfo()
        if 'modulus' in d:
            o.modulus = d['modulus']
        if 'voucher_activity_id' in d:
            o.voucher_activity_id = d['voucher_activity_id']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'vouvher_type' in d:
            o.vouvher_type = d['vouvher_type']
        return o


