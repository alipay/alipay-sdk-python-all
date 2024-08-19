#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneSettleWorkersaasSyncModel(object):

    def __init__(self):
        self._emp_name = None
        self._emp_phone = None
        self._front_log_no = None
        self._license_id = None
        self._license_type = None
        self._outer_trade_no = None
        self._pay_account = None
        self._pay_amount = None
        self._settle_type = None
        self._trade_fail_code = None
        self._trade_status = None
        self._trade_time = None

    @property
    def emp_name(self):
        return self._emp_name

    @emp_name.setter
    def emp_name(self, value):
        self._emp_name = value
    @property
    def emp_phone(self):
        return self._emp_phone

    @emp_phone.setter
    def emp_phone(self, value):
        self._emp_phone = value
    @property
    def front_log_no(self):
        return self._front_log_no

    @front_log_no.setter
    def front_log_no(self, value):
        self._front_log_no = value
    @property
    def license_id(self):
        return self._license_id

    @license_id.setter
    def license_id(self, value):
        self._license_id = value
    @property
    def license_type(self):
        return self._license_type

    @license_type.setter
    def license_type(self, value):
        self._license_type = value
    @property
    def outer_trade_no(self):
        return self._outer_trade_no

    @outer_trade_no.setter
    def outer_trade_no(self, value):
        self._outer_trade_no = value
    @property
    def pay_account(self):
        return self._pay_account

    @pay_account.setter
    def pay_account(self, value):
        self._pay_account = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def trade_fail_code(self):
        return self._trade_fail_code

    @trade_fail_code.setter
    def trade_fail_code(self, value):
        self._trade_fail_code = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.emp_name:
            if hasattr(self.emp_name, 'to_alipay_dict'):
                params['emp_name'] = self.emp_name.to_alipay_dict()
            else:
                params['emp_name'] = self.emp_name
        if self.emp_phone:
            if hasattr(self.emp_phone, 'to_alipay_dict'):
                params['emp_phone'] = self.emp_phone.to_alipay_dict()
            else:
                params['emp_phone'] = self.emp_phone
        if self.front_log_no:
            if hasattr(self.front_log_no, 'to_alipay_dict'):
                params['front_log_no'] = self.front_log_no.to_alipay_dict()
            else:
                params['front_log_no'] = self.front_log_no
        if self.license_id:
            if hasattr(self.license_id, 'to_alipay_dict'):
                params['license_id'] = self.license_id.to_alipay_dict()
            else:
                params['license_id'] = self.license_id
        if self.license_type:
            if hasattr(self.license_type, 'to_alipay_dict'):
                params['license_type'] = self.license_type.to_alipay_dict()
            else:
                params['license_type'] = self.license_type
        if self.outer_trade_no:
            if hasattr(self.outer_trade_no, 'to_alipay_dict'):
                params['outer_trade_no'] = self.outer_trade_no.to_alipay_dict()
            else:
                params['outer_trade_no'] = self.outer_trade_no
        if self.pay_account:
            if hasattr(self.pay_account, 'to_alipay_dict'):
                params['pay_account'] = self.pay_account.to_alipay_dict()
            else:
                params['pay_account'] = self.pay_account
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        if self.trade_fail_code:
            if hasattr(self.trade_fail_code, 'to_alipay_dict'):
                params['trade_fail_code'] = self.trade_fail_code.to_alipay_dict()
            else:
                params['trade_fail_code'] = self.trade_fail_code
        if self.trade_status:
            if hasattr(self.trade_status, 'to_alipay_dict'):
                params['trade_status'] = self.trade_status.to_alipay_dict()
            else:
                params['trade_status'] = self.trade_status
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneSettleWorkersaasSyncModel()
        if 'emp_name' in d:
            o.emp_name = d['emp_name']
        if 'emp_phone' in d:
            o.emp_phone = d['emp_phone']
        if 'front_log_no' in d:
            o.front_log_no = d['front_log_no']
        if 'license_id' in d:
            o.license_id = d['license_id']
        if 'license_type' in d:
            o.license_type = d['license_type']
        if 'outer_trade_no' in d:
            o.outer_trade_no = d['outer_trade_no']
        if 'pay_account' in d:
            o.pay_account = d['pay_account']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'trade_fail_code' in d:
            o.trade_fail_code = d['trade_fail_code']
        if 'trade_status' in d:
            o.trade_status = d['trade_status']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


