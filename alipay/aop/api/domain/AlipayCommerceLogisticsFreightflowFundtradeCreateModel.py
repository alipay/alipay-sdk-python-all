#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsFreightflowFundtradeCreateModel(object):

    def __init__(self):
        self._biz_no = None
        self._body = None
        self._currency = None
        self._logistics_code = None
        self._memo = None
        self._mode = None
        self._mybank_app_id = None
        self._partner_id = None
        self._pay_expire_time = None
        self._payee_card_name = None
        self._payee_id = None
        self._total_amount = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def mybank_app_id(self):
        return self._mybank_app_id

    @mybank_app_id.setter
    def mybank_app_id(self, value):
        self._mybank_app_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_expire_time(self):
        return self._pay_expire_time

    @pay_expire_time.setter
    def pay_expire_time(self, value):
        self._pay_expire_time = value
    @property
    def payee_card_name(self):
        return self._payee_card_name

    @payee_card_name.setter
    def payee_card_name(self, value):
        self._payee_card_name = value
    @property
    def payee_id(self):
        return self._payee_id

    @payee_id.setter
    def payee_id(self, value):
        self._payee_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.mybank_app_id:
            if hasattr(self.mybank_app_id, 'to_alipay_dict'):
                params['mybank_app_id'] = self.mybank_app_id.to_alipay_dict()
            else:
                params['mybank_app_id'] = self.mybank_app_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_expire_time:
            if hasattr(self.pay_expire_time, 'to_alipay_dict'):
                params['pay_expire_time'] = self.pay_expire_time.to_alipay_dict()
            else:
                params['pay_expire_time'] = self.pay_expire_time
        if self.payee_card_name:
            if hasattr(self.payee_card_name, 'to_alipay_dict'):
                params['payee_card_name'] = self.payee_card_name.to_alipay_dict()
            else:
                params['payee_card_name'] = self.payee_card_name
        if self.payee_id:
            if hasattr(self.payee_id, 'to_alipay_dict'):
                params['payee_id'] = self.payee_id.to_alipay_dict()
            else:
                params['payee_id'] = self.payee_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowFundtradeCreateModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'body' in d:
            o.body = d['body']
        if 'currency' in d:
            o.currency = d['currency']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'memo' in d:
            o.memo = d['memo']
        if 'mode' in d:
            o.mode = d['mode']
        if 'mybank_app_id' in d:
            o.mybank_app_id = d['mybank_app_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_expire_time' in d:
            o.pay_expire_time = d['pay_expire_time']
        if 'payee_card_name' in d:
            o.payee_card_name = d['payee_card_name']
        if 'payee_id' in d:
            o.payee_id = d['payee_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


