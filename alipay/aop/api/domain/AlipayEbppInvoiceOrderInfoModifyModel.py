#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceOrderInfoModifyModel(object):

    def __init__(self):
        self._actual_amount = None
        self._gmt_check_in = None
        self._gmt_check_out = None
        self._inv_status = None
        self._order_id = None
        self._order_status = None
        self._platform_code = None
        self._platform_user_id = None
        self._user_id = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def gmt_check_in(self):
        return self._gmt_check_in

    @gmt_check_in.setter
    def gmt_check_in(self, value):
        self._gmt_check_in = value
    @property
    def gmt_check_out(self):
        return self._gmt_check_out

    @gmt_check_out.setter
    def gmt_check_out(self, value):
        self._gmt_check_out = value
    @property
    def inv_status(self):
        return self._inv_status

    @inv_status.setter
    def inv_status(self, value):
        self._inv_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def platform_user_id(self):
        return self._platform_user_id

    @platform_user_id.setter
    def platform_user_id(self, value):
        self._platform_user_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.gmt_check_in:
            if hasattr(self.gmt_check_in, 'to_alipay_dict'):
                params['gmt_check_in'] = self.gmt_check_in.to_alipay_dict()
            else:
                params['gmt_check_in'] = self.gmt_check_in
        if self.gmt_check_out:
            if hasattr(self.gmt_check_out, 'to_alipay_dict'):
                params['gmt_check_out'] = self.gmt_check_out.to_alipay_dict()
            else:
                params['gmt_check_out'] = self.gmt_check_out
        if self.inv_status:
            if hasattr(self.inv_status, 'to_alipay_dict'):
                params['inv_status'] = self.inv_status.to_alipay_dict()
            else:
                params['inv_status'] = self.inv_status
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.platform_user_id:
            if hasattr(self.platform_user_id, 'to_alipay_dict'):
                params['platform_user_id'] = self.platform_user_id.to_alipay_dict()
            else:
                params['platform_user_id'] = self.platform_user_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceOrderInfoModifyModel()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'gmt_check_in' in d:
            o.gmt_check_in = d['gmt_check_in']
        if 'gmt_check_out' in d:
            o.gmt_check_out = d['gmt_check_out']
        if 'inv_status' in d:
            o.inv_status = d['inv_status']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'platform_user_id' in d:
            o.platform_user_id = d['platform_user_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


