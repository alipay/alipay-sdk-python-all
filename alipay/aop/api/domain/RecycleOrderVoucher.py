#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleOrderVoucher(object):

    def __init__(self):
        self._percentage = None
        self._voucher_ceiling_amount = None
        self._voucher_expire_time = None
        self._voucher_floor_amount = None
        self._voucher_id = None
        self._voucher_receive_time = None
        self._voucher_type = None

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        self._percentage = value
    @property
    def voucher_ceiling_amount(self):
        return self._voucher_ceiling_amount

    @voucher_ceiling_amount.setter
    def voucher_ceiling_amount(self, value):
        self._voucher_ceiling_amount = value
    @property
    def voucher_expire_time(self):
        return self._voucher_expire_time

    @voucher_expire_time.setter
    def voucher_expire_time(self, value):
        self._voucher_expire_time = value
    @property
    def voucher_floor_amount(self):
        return self._voucher_floor_amount

    @voucher_floor_amount.setter
    def voucher_floor_amount(self, value):
        self._voucher_floor_amount = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_receive_time(self):
        return self._voucher_receive_time

    @voucher_receive_time.setter
    def voucher_receive_time(self, value):
        self._voucher_receive_time = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.percentage:
            if hasattr(self.percentage, 'to_alipay_dict'):
                params['percentage'] = self.percentage.to_alipay_dict()
            else:
                params['percentage'] = self.percentage
        if self.voucher_ceiling_amount:
            if hasattr(self.voucher_ceiling_amount, 'to_alipay_dict'):
                params['voucher_ceiling_amount'] = self.voucher_ceiling_amount.to_alipay_dict()
            else:
                params['voucher_ceiling_amount'] = self.voucher_ceiling_amount
        if self.voucher_expire_time:
            if hasattr(self.voucher_expire_time, 'to_alipay_dict'):
                params['voucher_expire_time'] = self.voucher_expire_time.to_alipay_dict()
            else:
                params['voucher_expire_time'] = self.voucher_expire_time
        if self.voucher_floor_amount:
            if hasattr(self.voucher_floor_amount, 'to_alipay_dict'):
                params['voucher_floor_amount'] = self.voucher_floor_amount.to_alipay_dict()
            else:
                params['voucher_floor_amount'] = self.voucher_floor_amount
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_receive_time:
            if hasattr(self.voucher_receive_time, 'to_alipay_dict'):
                params['voucher_receive_time'] = self.voucher_receive_time.to_alipay_dict()
            else:
                params['voucher_receive_time'] = self.voucher_receive_time
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleOrderVoucher()
        if 'percentage' in d:
            o.percentage = d['percentage']
        if 'voucher_ceiling_amount' in d:
            o.voucher_ceiling_amount = d['voucher_ceiling_amount']
        if 'voucher_expire_time' in d:
            o.voucher_expire_time = d['voucher_expire_time']
        if 'voucher_floor_amount' in d:
            o.voucher_floor_amount = d['voucher_floor_amount']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_receive_time' in d:
            o.voucher_receive_time = d['voucher_receive_time']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


