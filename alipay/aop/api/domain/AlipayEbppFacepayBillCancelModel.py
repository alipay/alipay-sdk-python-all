#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppFacepayBillCancelModel(object):

    def __init__(self):
        self._bill_no = None
        self._out_order_no = None
        self._user_id = None
        self._user_identity_code = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_identity_code(self):
        return self._user_identity_code

    @user_identity_code.setter
    def user_identity_code(self, value):
        self._user_identity_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_identity_code:
            if hasattr(self.user_identity_code, 'to_alipay_dict'):
                params['user_identity_code'] = self.user_identity_code.to_alipay_dict()
            else:
                params['user_identity_code'] = self.user_identity_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppFacepayBillCancelModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_identity_code' in d:
            o.user_identity_code = d['user_identity_code']
        return o


