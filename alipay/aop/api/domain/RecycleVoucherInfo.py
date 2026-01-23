#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleVoucherInfo(object):

    def __init__(self):
        self._voucher_amount = None
        self._voucher_expire_time = None
        self._voucher_id = None
        self._voucher_receive_time = None
        self._voucher_status = None

    @property
    def voucher_amount(self):
        return self._voucher_amount

    @voucher_amount.setter
    def voucher_amount(self, value):
        self._voucher_amount = value
    @property
    def voucher_expire_time(self):
        return self._voucher_expire_time

    @voucher_expire_time.setter
    def voucher_expire_time(self, value):
        self._voucher_expire_time = value
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
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_amount:
            if hasattr(self.voucher_amount, 'to_alipay_dict'):
                params['voucher_amount'] = self.voucher_amount.to_alipay_dict()
            else:
                params['voucher_amount'] = self.voucher_amount
        if self.voucher_expire_time:
            if hasattr(self.voucher_expire_time, 'to_alipay_dict'):
                params['voucher_expire_time'] = self.voucher_expire_time.to_alipay_dict()
            else:
                params['voucher_expire_time'] = self.voucher_expire_time
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
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleVoucherInfo()
        if 'voucher_amount' in d:
            o.voucher_amount = d['voucher_amount']
        if 'voucher_expire_time' in d:
            o.voucher_expire_time = d['voucher_expire_time']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_receive_time' in d:
            o.voucher_receive_time = d['voucher_receive_time']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        return o


