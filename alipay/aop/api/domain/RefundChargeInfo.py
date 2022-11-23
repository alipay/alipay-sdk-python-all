#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundSubFee import RefundSubFee


class RefundChargeInfo(object):

    def __init__(self):
        self._charge_type = None
        self._refund_charge_fee = None
        self._refund_sub_fee_detail_list = None
        self._switch_fee_rate = None

    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def refund_charge_fee(self):
        return self._refund_charge_fee

    @refund_charge_fee.setter
    def refund_charge_fee(self, value):
        self._refund_charge_fee = value
    @property
    def refund_sub_fee_detail_list(self):
        return self._refund_sub_fee_detail_list

    @refund_sub_fee_detail_list.setter
    def refund_sub_fee_detail_list(self, value):
        if isinstance(value, list):
            self._refund_sub_fee_detail_list = list()
            for i in value:
                if isinstance(i, RefundSubFee):
                    self._refund_sub_fee_detail_list.append(i)
                else:
                    self._refund_sub_fee_detail_list.append(RefundSubFee.from_alipay_dict(i))
    @property
    def switch_fee_rate(self):
        return self._switch_fee_rate

    @switch_fee_rate.setter
    def switch_fee_rate(self, value):
        self._switch_fee_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.refund_charge_fee:
            if hasattr(self.refund_charge_fee, 'to_alipay_dict'):
                params['refund_charge_fee'] = self.refund_charge_fee.to_alipay_dict()
            else:
                params['refund_charge_fee'] = self.refund_charge_fee
        if self.refund_sub_fee_detail_list:
            if isinstance(self.refund_sub_fee_detail_list, list):
                for i in range(0, len(self.refund_sub_fee_detail_list)):
                    element = self.refund_sub_fee_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_sub_fee_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_sub_fee_detail_list, 'to_alipay_dict'):
                params['refund_sub_fee_detail_list'] = self.refund_sub_fee_detail_list.to_alipay_dict()
            else:
                params['refund_sub_fee_detail_list'] = self.refund_sub_fee_detail_list
        if self.switch_fee_rate:
            if hasattr(self.switch_fee_rate, 'to_alipay_dict'):
                params['switch_fee_rate'] = self.switch_fee_rate.to_alipay_dict()
            else:
                params['switch_fee_rate'] = self.switch_fee_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundChargeInfo()
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'refund_charge_fee' in d:
            o.refund_charge_fee = d['refund_charge_fee']
        if 'refund_sub_fee_detail_list' in d:
            o.refund_sub_fee_detail_list = d['refund_sub_fee_detail_list']
        if 'switch_fee_rate' in d:
            o.switch_fee_rate = d['switch_fee_rate']
        return o


