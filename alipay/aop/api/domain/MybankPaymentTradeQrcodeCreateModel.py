#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeQrcodeCreateModel(object):

    def __init__(self):
        self._account_category = None
        self._account_type = None
        self._amount = None
        self._bank_name = None
        self._biz_no = None
        self._biz_scene = None
        self._branch_inst_code = None
        self._branch_name = None
        self._channel = None
        self._currency = None
        self._enterprise_scheme_ar_no = None
        self._inst_code = None
        self._invalid_date = None
        self._order_ext = None
        self._personal_scheme_ar_no = None
        self._qr_code_type = None
        self._receipt_account_name = None
        self._receipt_account_no = None

    @property
    def account_category(self):
        return self._account_category

    @account_category.setter
    def account_category(self, value):
        self._account_category = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def branch_inst_code(self):
        return self._branch_inst_code

    @branch_inst_code.setter
    def branch_inst_code(self, value):
        self._branch_inst_code = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def enterprise_scheme_ar_no(self):
        return self._enterprise_scheme_ar_no

    @enterprise_scheme_ar_no.setter
    def enterprise_scheme_ar_no(self, value):
        self._enterprise_scheme_ar_no = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def invalid_date(self):
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = value
    @property
    def order_ext(self):
        return self._order_ext

    @order_ext.setter
    def order_ext(self, value):
        self._order_ext = value
    @property
    def personal_scheme_ar_no(self):
        return self._personal_scheme_ar_no

    @personal_scheme_ar_no.setter
    def personal_scheme_ar_no(self, value):
        self._personal_scheme_ar_no = value
    @property
    def qr_code_type(self):
        return self._qr_code_type

    @qr_code_type.setter
    def qr_code_type(self, value):
        self._qr_code_type = value
    @property
    def receipt_account_name(self):
        return self._receipt_account_name

    @receipt_account_name.setter
    def receipt_account_name(self, value):
        self._receipt_account_name = value
    @property
    def receipt_account_no(self):
        return self._receipt_account_no

    @receipt_account_no.setter
    def receipt_account_no(self, value):
        self._receipt_account_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_category:
            if hasattr(self.account_category, 'to_alipay_dict'):
                params['account_category'] = self.account_category.to_alipay_dict()
            else:
                params['account_category'] = self.account_category
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.branch_inst_code:
            if hasattr(self.branch_inst_code, 'to_alipay_dict'):
                params['branch_inst_code'] = self.branch_inst_code.to_alipay_dict()
            else:
                params['branch_inst_code'] = self.branch_inst_code
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.enterprise_scheme_ar_no:
            if hasattr(self.enterprise_scheme_ar_no, 'to_alipay_dict'):
                params['enterprise_scheme_ar_no'] = self.enterprise_scheme_ar_no.to_alipay_dict()
            else:
                params['enterprise_scheme_ar_no'] = self.enterprise_scheme_ar_no
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.invalid_date:
            if hasattr(self.invalid_date, 'to_alipay_dict'):
                params['invalid_date'] = self.invalid_date.to_alipay_dict()
            else:
                params['invalid_date'] = self.invalid_date
        if self.order_ext:
            if hasattr(self.order_ext, 'to_alipay_dict'):
                params['order_ext'] = self.order_ext.to_alipay_dict()
            else:
                params['order_ext'] = self.order_ext
        if self.personal_scheme_ar_no:
            if hasattr(self.personal_scheme_ar_no, 'to_alipay_dict'):
                params['personal_scheme_ar_no'] = self.personal_scheme_ar_no.to_alipay_dict()
            else:
                params['personal_scheme_ar_no'] = self.personal_scheme_ar_no
        if self.qr_code_type:
            if hasattr(self.qr_code_type, 'to_alipay_dict'):
                params['qr_code_type'] = self.qr_code_type.to_alipay_dict()
            else:
                params['qr_code_type'] = self.qr_code_type
        if self.receipt_account_name:
            if hasattr(self.receipt_account_name, 'to_alipay_dict'):
                params['receipt_account_name'] = self.receipt_account_name.to_alipay_dict()
            else:
                params['receipt_account_name'] = self.receipt_account_name
        if self.receipt_account_no:
            if hasattr(self.receipt_account_no, 'to_alipay_dict'):
                params['receipt_account_no'] = self.receipt_account_no.to_alipay_dict()
            else:
                params['receipt_account_no'] = self.receipt_account_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeQrcodeCreateModel()
        if 'account_category' in d:
            o.account_category = d['account_category']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'amount' in d:
            o.amount = d['amount']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'branch_inst_code' in d:
            o.branch_inst_code = d['branch_inst_code']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'channel' in d:
            o.channel = d['channel']
        if 'currency' in d:
            o.currency = d['currency']
        if 'enterprise_scheme_ar_no' in d:
            o.enterprise_scheme_ar_no = d['enterprise_scheme_ar_no']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'invalid_date' in d:
            o.invalid_date = d['invalid_date']
        if 'order_ext' in d:
            o.order_ext = d['order_ext']
        if 'personal_scheme_ar_no' in d:
            o.personal_scheme_ar_no = d['personal_scheme_ar_no']
        if 'qr_code_type' in d:
            o.qr_code_type = d['qr_code_type']
        if 'receipt_account_name' in d:
            o.receipt_account_name = d['receipt_account_name']
        if 'receipt_account_no' in d:
            o.receipt_account_no = d['receipt_account_no']
        return o


