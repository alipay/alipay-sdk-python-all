#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayQueryBillDetailListResponse(object):

    def __init__(self):
        self._acc_amount = None
        self._acc_pay_status = None
        self._account_no = None
        self._batch_no = None
        self._description = None
        self._draw_date = None
        self._org_biz_no = None
        self._out_biz_no = None
        self._pay_cert_name = None
        self._pay_cert_num = None
        self._pay_cert_type = None
        self._payment_date = None
        self._rent_bank_name = None
        self._rent_card_num = None
        self._self_amount = None
        self._settle_serial_no = None
        self._total_amount = None
        self._trade_no = None

    @property
    def acc_amount(self):
        return self._acc_amount

    @acc_amount.setter
    def acc_amount(self, value):
        self._acc_amount = value
    @property
    def acc_pay_status(self):
        return self._acc_pay_status

    @acc_pay_status.setter
    def acc_pay_status(self, value):
        self._acc_pay_status = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def draw_date(self):
        return self._draw_date

    @draw_date.setter
    def draw_date(self, value):
        self._draw_date = value
    @property
    def org_biz_no(self):
        return self._org_biz_no

    @org_biz_no.setter
    def org_biz_no(self, value):
        self._org_biz_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_cert_name(self):
        return self._pay_cert_name

    @pay_cert_name.setter
    def pay_cert_name(self, value):
        self._pay_cert_name = value
    @property
    def pay_cert_num(self):
        return self._pay_cert_num

    @pay_cert_num.setter
    def pay_cert_num(self, value):
        self._pay_cert_num = value
    @property
    def pay_cert_type(self):
        return self._pay_cert_type

    @pay_cert_type.setter
    def pay_cert_type(self, value):
        self._pay_cert_type = value
    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value
    @property
    def rent_bank_name(self):
        return self._rent_bank_name

    @rent_bank_name.setter
    def rent_bank_name(self, value):
        self._rent_bank_name = value
    @property
    def rent_card_num(self):
        return self._rent_card_num

    @rent_card_num.setter
    def rent_card_num(self, value):
        self._rent_card_num = value
    @property
    def self_amount(self):
        return self._self_amount

    @self_amount.setter
    def self_amount(self, value):
        self._self_amount = value
    @property
    def settle_serial_no(self):
        return self._settle_serial_no

    @settle_serial_no.setter
    def settle_serial_no(self, value):
        self._settle_serial_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.acc_amount:
            if hasattr(self.acc_amount, 'to_alipay_dict'):
                params['acc_amount'] = self.acc_amount.to_alipay_dict()
            else:
                params['acc_amount'] = self.acc_amount
        if self.acc_pay_status:
            if hasattr(self.acc_pay_status, 'to_alipay_dict'):
                params['acc_pay_status'] = self.acc_pay_status.to_alipay_dict()
            else:
                params['acc_pay_status'] = self.acc_pay_status
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.draw_date:
            if hasattr(self.draw_date, 'to_alipay_dict'):
                params['draw_date'] = self.draw_date.to_alipay_dict()
            else:
                params['draw_date'] = self.draw_date
        if self.org_biz_no:
            if hasattr(self.org_biz_no, 'to_alipay_dict'):
                params['org_biz_no'] = self.org_biz_no.to_alipay_dict()
            else:
                params['org_biz_no'] = self.org_biz_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_cert_name:
            if hasattr(self.pay_cert_name, 'to_alipay_dict'):
                params['pay_cert_name'] = self.pay_cert_name.to_alipay_dict()
            else:
                params['pay_cert_name'] = self.pay_cert_name
        if self.pay_cert_num:
            if hasattr(self.pay_cert_num, 'to_alipay_dict'):
                params['pay_cert_num'] = self.pay_cert_num.to_alipay_dict()
            else:
                params['pay_cert_num'] = self.pay_cert_num
        if self.pay_cert_type:
            if hasattr(self.pay_cert_type, 'to_alipay_dict'):
                params['pay_cert_type'] = self.pay_cert_type.to_alipay_dict()
            else:
                params['pay_cert_type'] = self.pay_cert_type
        if self.payment_date:
            if hasattr(self.payment_date, 'to_alipay_dict'):
                params['payment_date'] = self.payment_date.to_alipay_dict()
            else:
                params['payment_date'] = self.payment_date
        if self.rent_bank_name:
            if hasattr(self.rent_bank_name, 'to_alipay_dict'):
                params['rent_bank_name'] = self.rent_bank_name.to_alipay_dict()
            else:
                params['rent_bank_name'] = self.rent_bank_name
        if self.rent_card_num:
            if hasattr(self.rent_card_num, 'to_alipay_dict'):
                params['rent_card_num'] = self.rent_card_num.to_alipay_dict()
            else:
                params['rent_card_num'] = self.rent_card_num
        if self.self_amount:
            if hasattr(self.self_amount, 'to_alipay_dict'):
                params['self_amount'] = self.self_amount.to_alipay_dict()
            else:
                params['self_amount'] = self.self_amount
        if self.settle_serial_no:
            if hasattr(self.settle_serial_no, 'to_alipay_dict'):
                params['settle_serial_no'] = self.settle_serial_no.to_alipay_dict()
            else:
                params['settle_serial_no'] = self.settle_serial_no
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
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
        o = RentPayQueryBillDetailListResponse()
        if 'acc_amount' in d:
            o.acc_amount = d['acc_amount']
        if 'acc_pay_status' in d:
            o.acc_pay_status = d['acc_pay_status']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'description' in d:
            o.description = d['description']
        if 'draw_date' in d:
            o.draw_date = d['draw_date']
        if 'org_biz_no' in d:
            o.org_biz_no = d['org_biz_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_cert_name' in d:
            o.pay_cert_name = d['pay_cert_name']
        if 'pay_cert_num' in d:
            o.pay_cert_num = d['pay_cert_num']
        if 'pay_cert_type' in d:
            o.pay_cert_type = d['pay_cert_type']
        if 'payment_date' in d:
            o.payment_date = d['payment_date']
        if 'rent_bank_name' in d:
            o.rent_bank_name = d['rent_bank_name']
        if 'rent_card_num' in d:
            o.rent_card_num = d['rent_card_num']
        if 'self_amount' in d:
            o.self_amount = d['self_amount']
        if 'settle_serial_no' in d:
            o.settle_serial_no = d['settle_serial_no']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


