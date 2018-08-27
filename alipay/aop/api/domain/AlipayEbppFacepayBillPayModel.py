#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppFacepayBillPayModel(object):

    def __init__(self):
        self._bill_date = None
        self._bill_key = None
        self._biz_type = None
        self._charge_inst = None
        self._extend_field = None
        self._fine_amount = None
        self._inst_no = None
        self._out_order_no = None
        self._pay_amount = None
        self._pid = None
        self._sub_biz_type = None
        self._user_identity_code = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def fine_amount(self):
        return self._fine_amount

    @fine_amount.setter
    def fine_amount(self, value):
        self._fine_amount = value
    @property
    def inst_no(self):
        return self._inst_no

    @inst_no.setter
    def inst_no(self, value):
        self._inst_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def user_identity_code(self):
        return self._user_identity_code

    @user_identity_code.setter
    def user_identity_code(self, value):
        self._user_identity_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.fine_amount:
            if hasattr(self.fine_amount, 'to_alipay_dict'):
                params['fine_amount'] = self.fine_amount.to_alipay_dict()
            else:
                params['fine_amount'] = self.fine_amount
        if self.inst_no:
            if hasattr(self.inst_no, 'to_alipay_dict'):
                params['inst_no'] = self.inst_no.to_alipay_dict()
            else:
                params['inst_no'] = self.inst_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
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
        o = AlipayEbppFacepayBillPayModel()
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'fine_amount' in d:
            o.fine_amount = d['fine_amount']
        if 'inst_no' in d:
            o.inst_no = d['inst_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pid' in d:
            o.pid = d['pid']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'user_identity_code' in d:
            o.user_identity_code = d['user_identity_code']
        return o


