#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AllocDetailDTO(object):

    def __init__(self):
        self._account_id = None
        self._alloc_amount = None
        self._alloc_error_code = None
        self._alloc_error_msg = None
        self._alloc_status = None
        self._alloc_time = None
        self._detail_id = None
        self._fund_plan_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def alloc_amount(self):
        return self._alloc_amount

    @alloc_amount.setter
    def alloc_amount(self, value):
        self._alloc_amount = value
    @property
    def alloc_error_code(self):
        return self._alloc_error_code

    @alloc_error_code.setter
    def alloc_error_code(self, value):
        self._alloc_error_code = value
    @property
    def alloc_error_msg(self):
        return self._alloc_error_msg

    @alloc_error_msg.setter
    def alloc_error_msg(self, value):
        self._alloc_error_msg = value
    @property
    def alloc_status(self):
        return self._alloc_status

    @alloc_status.setter
    def alloc_status(self, value):
        self._alloc_status = value
    @property
    def alloc_time(self):
        return self._alloc_time

    @alloc_time.setter
    def alloc_time(self, value):
        self._alloc_time = value
    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value
    @property
    def fund_plan_id(self):
        return self._fund_plan_id

    @fund_plan_id.setter
    def fund_plan_id(self, value):
        self._fund_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.alloc_amount:
            if hasattr(self.alloc_amount, 'to_alipay_dict'):
                params['alloc_amount'] = self.alloc_amount.to_alipay_dict()
            else:
                params['alloc_amount'] = self.alloc_amount
        if self.alloc_error_code:
            if hasattr(self.alloc_error_code, 'to_alipay_dict'):
                params['alloc_error_code'] = self.alloc_error_code.to_alipay_dict()
            else:
                params['alloc_error_code'] = self.alloc_error_code
        if self.alloc_error_msg:
            if hasattr(self.alloc_error_msg, 'to_alipay_dict'):
                params['alloc_error_msg'] = self.alloc_error_msg.to_alipay_dict()
            else:
                params['alloc_error_msg'] = self.alloc_error_msg
        if self.alloc_status:
            if hasattr(self.alloc_status, 'to_alipay_dict'):
                params['alloc_status'] = self.alloc_status.to_alipay_dict()
            else:
                params['alloc_status'] = self.alloc_status
        if self.alloc_time:
            if hasattr(self.alloc_time, 'to_alipay_dict'):
                params['alloc_time'] = self.alloc_time.to_alipay_dict()
            else:
                params['alloc_time'] = self.alloc_time
        if self.detail_id:
            if hasattr(self.detail_id, 'to_alipay_dict'):
                params['detail_id'] = self.detail_id.to_alipay_dict()
            else:
                params['detail_id'] = self.detail_id
        if self.fund_plan_id:
            if hasattr(self.fund_plan_id, 'to_alipay_dict'):
                params['fund_plan_id'] = self.fund_plan_id.to_alipay_dict()
            else:
                params['fund_plan_id'] = self.fund_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AllocDetailDTO()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'alloc_amount' in d:
            o.alloc_amount = d['alloc_amount']
        if 'alloc_error_code' in d:
            o.alloc_error_code = d['alloc_error_code']
        if 'alloc_error_msg' in d:
            o.alloc_error_msg = d['alloc_error_msg']
        if 'alloc_status' in d:
            o.alloc_status = d['alloc_status']
        if 'alloc_time' in d:
            o.alloc_time = d['alloc_time']
        if 'detail_id' in d:
            o.detail_id = d['detail_id']
        if 'fund_plan_id' in d:
            o.fund_plan_id = d['fund_plan_id']
        return o


