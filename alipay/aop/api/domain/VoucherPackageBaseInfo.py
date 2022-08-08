#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherPackageBaseInfo(object):

    def __init__(self):
        self._purchase_end_time = None
        self._purchase_start_time = None
        self._voucher_package_id = None
        self._voucher_package_name = None
        self._voucher_package_status = None
        self._voucher_total_amount = None

    @property
    def purchase_end_time(self):
        return self._purchase_end_time

    @purchase_end_time.setter
    def purchase_end_time(self, value):
        self._purchase_end_time = value
    @property
    def purchase_start_time(self):
        return self._purchase_start_time

    @purchase_start_time.setter
    def purchase_start_time(self, value):
        self._purchase_start_time = value
    @property
    def voucher_package_id(self):
        return self._voucher_package_id

    @voucher_package_id.setter
    def voucher_package_id(self, value):
        self._voucher_package_id = value
    @property
    def voucher_package_name(self):
        return self._voucher_package_name

    @voucher_package_name.setter
    def voucher_package_name(self, value):
        self._voucher_package_name = value
    @property
    def voucher_package_status(self):
        return self._voucher_package_status

    @voucher_package_status.setter
    def voucher_package_status(self, value):
        self._voucher_package_status = value
    @property
    def voucher_total_amount(self):
        return self._voucher_total_amount

    @voucher_total_amount.setter
    def voucher_total_amount(self, value):
        self._voucher_total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.purchase_end_time:
            if hasattr(self.purchase_end_time, 'to_alipay_dict'):
                params['purchase_end_time'] = self.purchase_end_time.to_alipay_dict()
            else:
                params['purchase_end_time'] = self.purchase_end_time
        if self.purchase_start_time:
            if hasattr(self.purchase_start_time, 'to_alipay_dict'):
                params['purchase_start_time'] = self.purchase_start_time.to_alipay_dict()
            else:
                params['purchase_start_time'] = self.purchase_start_time
        if self.voucher_package_id:
            if hasattr(self.voucher_package_id, 'to_alipay_dict'):
                params['voucher_package_id'] = self.voucher_package_id.to_alipay_dict()
            else:
                params['voucher_package_id'] = self.voucher_package_id
        if self.voucher_package_name:
            if hasattr(self.voucher_package_name, 'to_alipay_dict'):
                params['voucher_package_name'] = self.voucher_package_name.to_alipay_dict()
            else:
                params['voucher_package_name'] = self.voucher_package_name
        if self.voucher_package_status:
            if hasattr(self.voucher_package_status, 'to_alipay_dict'):
                params['voucher_package_status'] = self.voucher_package_status.to_alipay_dict()
            else:
                params['voucher_package_status'] = self.voucher_package_status
        if self.voucher_total_amount:
            if hasattr(self.voucher_total_amount, 'to_alipay_dict'):
                params['voucher_total_amount'] = self.voucher_total_amount.to_alipay_dict()
            else:
                params['voucher_total_amount'] = self.voucher_total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherPackageBaseInfo()
        if 'purchase_end_time' in d:
            o.purchase_end_time = d['purchase_end_time']
        if 'purchase_start_time' in d:
            o.purchase_start_time = d['purchase_start_time']
        if 'voucher_package_id' in d:
            o.voucher_package_id = d['voucher_package_id']
        if 'voucher_package_name' in d:
            o.voucher_package_name = d['voucher_package_name']
        if 'voucher_package_status' in d:
            o.voucher_package_status = d['voucher_package_status']
        if 'voucher_total_amount' in d:
            o.voucher_total_amount = d['voucher_total_amount']
        return o


