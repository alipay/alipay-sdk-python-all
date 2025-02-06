#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PerformBill(object):

    def __init__(self):
        self._alloc_status = None
        self._bill_amount = None
        self._bill_no = None
        self._chargeoff_status = None
        self._gmt_alloc = None
        self._gmt_chargeoff_finish = None
        self._gmt_chargeoff_start = None
        self._gmt_create = None
        self._gmt_pay = None
        self._gmt_refund = None
        self._gmt_settle = None
        self._out_no = None
        self._pay_amount = None
        self._settle_status = None
        self._status = None
        self._trade_no = None

    @property
    def alloc_status(self):
        return self._alloc_status

    @alloc_status.setter
    def alloc_status(self, value):
        self._alloc_status = value
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def chargeoff_status(self):
        return self._chargeoff_status

    @chargeoff_status.setter
    def chargeoff_status(self, value):
        self._chargeoff_status = value
    @property
    def gmt_alloc(self):
        return self._gmt_alloc

    @gmt_alloc.setter
    def gmt_alloc(self, value):
        self._gmt_alloc = value
    @property
    def gmt_chargeoff_finish(self):
        return self._gmt_chargeoff_finish

    @gmt_chargeoff_finish.setter
    def gmt_chargeoff_finish(self, value):
        self._gmt_chargeoff_finish = value
    @property
    def gmt_chargeoff_start(self):
        return self._gmt_chargeoff_start

    @gmt_chargeoff_start.setter
    def gmt_chargeoff_start(self, value):
        self._gmt_chargeoff_start = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def gmt_settle(self):
        return self._gmt_settle

    @gmt_settle.setter
    def gmt_settle(self, value):
        self._gmt_settle = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alloc_status:
            if hasattr(self.alloc_status, 'to_alipay_dict'):
                params['alloc_status'] = self.alloc_status.to_alipay_dict()
            else:
                params['alloc_status'] = self.alloc_status
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.chargeoff_status:
            if hasattr(self.chargeoff_status, 'to_alipay_dict'):
                params['chargeoff_status'] = self.chargeoff_status.to_alipay_dict()
            else:
                params['chargeoff_status'] = self.chargeoff_status
        if self.gmt_alloc:
            if hasattr(self.gmt_alloc, 'to_alipay_dict'):
                params['gmt_alloc'] = self.gmt_alloc.to_alipay_dict()
            else:
                params['gmt_alloc'] = self.gmt_alloc
        if self.gmt_chargeoff_finish:
            if hasattr(self.gmt_chargeoff_finish, 'to_alipay_dict'):
                params['gmt_chargeoff_finish'] = self.gmt_chargeoff_finish.to_alipay_dict()
            else:
                params['gmt_chargeoff_finish'] = self.gmt_chargeoff_finish
        if self.gmt_chargeoff_start:
            if hasattr(self.gmt_chargeoff_start, 'to_alipay_dict'):
                params['gmt_chargeoff_start'] = self.gmt_chargeoff_start.to_alipay_dict()
            else:
                params['gmt_chargeoff_start'] = self.gmt_chargeoff_start
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.gmt_refund:
            if hasattr(self.gmt_refund, 'to_alipay_dict'):
                params['gmt_refund'] = self.gmt_refund.to_alipay_dict()
            else:
                params['gmt_refund'] = self.gmt_refund
        if self.gmt_settle:
            if hasattr(self.gmt_settle, 'to_alipay_dict'):
                params['gmt_settle'] = self.gmt_settle.to_alipay_dict()
            else:
                params['gmt_settle'] = self.gmt_settle
        if self.out_no:
            if hasattr(self.out_no, 'to_alipay_dict'):
                params['out_no'] = self.out_no.to_alipay_dict()
            else:
                params['out_no'] = self.out_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PerformBill()
        if 'alloc_status' in d:
            o.alloc_status = d['alloc_status']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'chargeoff_status' in d:
            o.chargeoff_status = d['chargeoff_status']
        if 'gmt_alloc' in d:
            o.gmt_alloc = d['gmt_alloc']
        if 'gmt_chargeoff_finish' in d:
            o.gmt_chargeoff_finish = d['gmt_chargeoff_finish']
        if 'gmt_chargeoff_start' in d:
            o.gmt_chargeoff_start = d['gmt_chargeoff_start']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'gmt_refund' in d:
            o.gmt_refund = d['gmt_refund']
        if 'gmt_settle' in d:
            o.gmt_settle = d['gmt_settle']
        if 'out_no' in d:
            o.out_no = d['out_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'status' in d:
            o.status = d['status']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


