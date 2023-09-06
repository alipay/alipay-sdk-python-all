#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradeExtendParams import TradeExtendParams
from alipay.aop.api.domain.SubsidyAmountParam import SubsidyAmountParam


class AlipayCommerceMedicalPaymentCreateandpayModel(object):

    def __init__(self):
        self._account_amount = None
        self._alipay_user_id = None
        self._call_url = None
        self._extend_params = None
        self._gmt_out_create = None
        self._gov_amount = None
        self._med_org_ord = None
        self._merchant_name = None
        self._open_id = None
        self._org_no = None
        self._other_amount = None
        self._out_trade_no = None
        self._pay_auth_no = None
        self._pay_order_id = None
        self._payment_city_code = None
        self._real_amount = None
        self._subsidy_amount_params = None
        self._total_amount = None
        self._trade_no = None

    @property
    def account_amount(self):
        return self._account_amount

    @account_amount.setter
    def account_amount(self, value):
        self._account_amount = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def call_url(self):
        return self._call_url

    @call_url.setter
    def call_url(self, value):
        self._call_url = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, TradeExtendParams):
            self._extend_params = value
        else:
            self._extend_params = TradeExtendParams.from_alipay_dict(value)
    @property
    def gmt_out_create(self):
        return self._gmt_out_create

    @gmt_out_create.setter
    def gmt_out_create(self, value):
        self._gmt_out_create = value
    @property
    def gov_amount(self):
        return self._gov_amount

    @gov_amount.setter
    def gov_amount(self, value):
        self._gov_amount = value
    @property
    def med_org_ord(self):
        return self._med_org_ord

    @med_org_ord.setter
    def med_org_ord(self, value):
        self._med_org_ord = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_no(self):
        return self._org_no

    @org_no.setter
    def org_no(self, value):
        self._org_no = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        self._other_amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_auth_no(self):
        return self._pay_auth_no

    @pay_auth_no.setter
    def pay_auth_no(self, value):
        self._pay_auth_no = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def payment_city_code(self):
        return self._payment_city_code

    @payment_city_code.setter
    def payment_city_code(self, value):
        self._payment_city_code = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def subsidy_amount_params(self):
        return self._subsidy_amount_params

    @subsidy_amount_params.setter
    def subsidy_amount_params(self, value):
        if isinstance(value, list):
            self._subsidy_amount_params = list()
            for i in value:
                if isinstance(i, SubsidyAmountParam):
                    self._subsidy_amount_params.append(i)
                else:
                    self._subsidy_amount_params.append(SubsidyAmountParam.from_alipay_dict(i))
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
        if self.account_amount:
            if hasattr(self.account_amount, 'to_alipay_dict'):
                params['account_amount'] = self.account_amount.to_alipay_dict()
            else:
                params['account_amount'] = self.account_amount
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.call_url:
            if hasattr(self.call_url, 'to_alipay_dict'):
                params['call_url'] = self.call_url.to_alipay_dict()
            else:
                params['call_url'] = self.call_url
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.gmt_out_create:
            if hasattr(self.gmt_out_create, 'to_alipay_dict'):
                params['gmt_out_create'] = self.gmt_out_create.to_alipay_dict()
            else:
                params['gmt_out_create'] = self.gmt_out_create
        if self.gov_amount:
            if hasattr(self.gov_amount, 'to_alipay_dict'):
                params['gov_amount'] = self.gov_amount.to_alipay_dict()
            else:
                params['gov_amount'] = self.gov_amount
        if self.med_org_ord:
            if hasattr(self.med_org_ord, 'to_alipay_dict'):
                params['med_org_ord'] = self.med_org_ord.to_alipay_dict()
            else:
                params['med_org_ord'] = self.med_org_ord
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_no:
            if hasattr(self.org_no, 'to_alipay_dict'):
                params['org_no'] = self.org_no.to_alipay_dict()
            else:
                params['org_no'] = self.org_no
        if self.other_amount:
            if hasattr(self.other_amount, 'to_alipay_dict'):
                params['other_amount'] = self.other_amount.to_alipay_dict()
            else:
                params['other_amount'] = self.other_amount
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_auth_no:
            if hasattr(self.pay_auth_no, 'to_alipay_dict'):
                params['pay_auth_no'] = self.pay_auth_no.to_alipay_dict()
            else:
                params['pay_auth_no'] = self.pay_auth_no
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.payment_city_code:
            if hasattr(self.payment_city_code, 'to_alipay_dict'):
                params['payment_city_code'] = self.payment_city_code.to_alipay_dict()
            else:
                params['payment_city_code'] = self.payment_city_code
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.subsidy_amount_params:
            if isinstance(self.subsidy_amount_params, list):
                for i in range(0, len(self.subsidy_amount_params)):
                    element = self.subsidy_amount_params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subsidy_amount_params[i] = element.to_alipay_dict()
            if hasattr(self.subsidy_amount_params, 'to_alipay_dict'):
                params['subsidy_amount_params'] = self.subsidy_amount_params.to_alipay_dict()
            else:
                params['subsidy_amount_params'] = self.subsidy_amount_params
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
        o = AlipayCommerceMedicalPaymentCreateandpayModel()
        if 'account_amount' in d:
            o.account_amount = d['account_amount']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'call_url' in d:
            o.call_url = d['call_url']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'gmt_out_create' in d:
            o.gmt_out_create = d['gmt_out_create']
        if 'gov_amount' in d:
            o.gov_amount = d['gov_amount']
        if 'med_org_ord' in d:
            o.med_org_ord = d['med_org_ord']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_no' in d:
            o.org_no = d['org_no']
        if 'other_amount' in d:
            o.other_amount = d['other_amount']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_auth_no' in d:
            o.pay_auth_no = d['pay_auth_no']
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'payment_city_code' in d:
            o.payment_city_code = d['payment_city_code']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'subsidy_amount_params' in d:
            o.subsidy_amount_params = d['subsidy_amount_params']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


