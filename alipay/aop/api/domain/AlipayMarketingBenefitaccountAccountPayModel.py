#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingBenefitaccountAccountPayModel(object):

    def __init__(self):
        self._amount = None
        self._benefit_account_no = None
        self._biz_dt = None
        self._biz_no = None
        self._extend_info = None
        self._fund_principal = None
        self._fund_provider = None
        self._fund_user_id = None
        self._other_pay = None
        self._other_pay_fund_user_id = None
        self._publisher_user_id = None
        self._recharge_type = None
        self._redirect_url = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def benefit_account_no(self):
        return self._benefit_account_no

    @benefit_account_no.setter
    def benefit_account_no(self, value):
        self._benefit_account_no = value
    @property
    def biz_dt(self):
        return self._biz_dt

    @biz_dt.setter
    def biz_dt(self, value):
        self._biz_dt = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def fund_principal(self):
        return self._fund_principal

    @fund_principal.setter
    def fund_principal(self, value):
        self._fund_principal = value
    @property
    def fund_provider(self):
        return self._fund_provider

    @fund_provider.setter
    def fund_provider(self, value):
        self._fund_provider = value
    @property
    def fund_user_id(self):
        return self._fund_user_id

    @fund_user_id.setter
    def fund_user_id(self, value):
        self._fund_user_id = value
    @property
    def other_pay(self):
        return self._other_pay

    @other_pay.setter
    def other_pay(self, value):
        self._other_pay = value
    @property
    def other_pay_fund_user_id(self):
        return self._other_pay_fund_user_id

    @other_pay_fund_user_id.setter
    def other_pay_fund_user_id(self, value):
        self._other_pay_fund_user_id = value
    @property
    def publisher_user_id(self):
        return self._publisher_user_id

    @publisher_user_id.setter
    def publisher_user_id(self, value):
        self._publisher_user_id = value
    @property
    def recharge_type(self):
        return self._recharge_type

    @recharge_type.setter
    def recharge_type(self, value):
        self._recharge_type = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.benefit_account_no:
            if hasattr(self.benefit_account_no, 'to_alipay_dict'):
                params['benefit_account_no'] = self.benefit_account_no.to_alipay_dict()
            else:
                params['benefit_account_no'] = self.benefit_account_no
        if self.biz_dt:
            if hasattr(self.biz_dt, 'to_alipay_dict'):
                params['biz_dt'] = self.biz_dt.to_alipay_dict()
            else:
                params['biz_dt'] = self.biz_dt
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.fund_principal:
            if hasattr(self.fund_principal, 'to_alipay_dict'):
                params['fund_principal'] = self.fund_principal.to_alipay_dict()
            else:
                params['fund_principal'] = self.fund_principal
        if self.fund_provider:
            if hasattr(self.fund_provider, 'to_alipay_dict'):
                params['fund_provider'] = self.fund_provider.to_alipay_dict()
            else:
                params['fund_provider'] = self.fund_provider
        if self.fund_user_id:
            if hasattr(self.fund_user_id, 'to_alipay_dict'):
                params['fund_user_id'] = self.fund_user_id.to_alipay_dict()
            else:
                params['fund_user_id'] = self.fund_user_id
        if self.other_pay:
            if hasattr(self.other_pay, 'to_alipay_dict'):
                params['other_pay'] = self.other_pay.to_alipay_dict()
            else:
                params['other_pay'] = self.other_pay
        if self.other_pay_fund_user_id:
            if hasattr(self.other_pay_fund_user_id, 'to_alipay_dict'):
                params['other_pay_fund_user_id'] = self.other_pay_fund_user_id.to_alipay_dict()
            else:
                params['other_pay_fund_user_id'] = self.other_pay_fund_user_id
        if self.publisher_user_id:
            if hasattr(self.publisher_user_id, 'to_alipay_dict'):
                params['publisher_user_id'] = self.publisher_user_id.to_alipay_dict()
            else:
                params['publisher_user_id'] = self.publisher_user_id
        if self.recharge_type:
            if hasattr(self.recharge_type, 'to_alipay_dict'):
                params['recharge_type'] = self.recharge_type.to_alipay_dict()
            else:
                params['recharge_type'] = self.recharge_type
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingBenefitaccountAccountPayModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'benefit_account_no' in d:
            o.benefit_account_no = d['benefit_account_no']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'fund_principal' in d:
            o.fund_principal = d['fund_principal']
        if 'fund_provider' in d:
            o.fund_provider = d['fund_provider']
        if 'fund_user_id' in d:
            o.fund_user_id = d['fund_user_id']
        if 'other_pay' in d:
            o.other_pay = d['other_pay']
        if 'other_pay_fund_user_id' in d:
            o.other_pay_fund_user_id = d['other_pay_fund_user_id']
        if 'publisher_user_id' in d:
            o.publisher_user_id = d['publisher_user_id']
        if 'recharge_type' in d:
            o.recharge_type = d['recharge_type']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        return o


