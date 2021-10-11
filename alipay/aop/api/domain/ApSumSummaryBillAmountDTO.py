#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ApSumSummaryBillAmountDTO(object):

    def __init__(self):
        self._bill_amount = None
        self._checkout_amount = None
        self._confirmed_amount = None
        self._settled_amount = None
        self._settling_amount = None
        self._un_confirmed_amount = None
        self._un_settle_amount = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._bill_amount = value
        else:
            self._bill_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def checkout_amount(self):
        return self._checkout_amount

    @checkout_amount.setter
    def checkout_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._checkout_amount = value
        else:
            self._checkout_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def confirmed_amount(self):
        return self._confirmed_amount

    @confirmed_amount.setter
    def confirmed_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._confirmed_amount = value
        else:
            self._confirmed_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def settled_amount(self):
        return self._settled_amount

    @settled_amount.setter
    def settled_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._settled_amount = value
        else:
            self._settled_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def settling_amount(self):
        return self._settling_amount

    @settling_amount.setter
    def settling_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._settling_amount = value
        else:
            self._settling_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def un_confirmed_amount(self):
        return self._un_confirmed_amount

    @un_confirmed_amount.setter
    def un_confirmed_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._un_confirmed_amount = value
        else:
            self._un_confirmed_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def un_settle_amount(self):
        return self._un_settle_amount

    @un_settle_amount.setter
    def un_settle_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._un_settle_amount = value
        else:
            self._un_settle_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.checkout_amount:
            if hasattr(self.checkout_amount, 'to_alipay_dict'):
                params['checkout_amount'] = self.checkout_amount.to_alipay_dict()
            else:
                params['checkout_amount'] = self.checkout_amount
        if self.confirmed_amount:
            if hasattr(self.confirmed_amount, 'to_alipay_dict'):
                params['confirmed_amount'] = self.confirmed_amount.to_alipay_dict()
            else:
                params['confirmed_amount'] = self.confirmed_amount
        if self.settled_amount:
            if hasattr(self.settled_amount, 'to_alipay_dict'):
                params['settled_amount'] = self.settled_amount.to_alipay_dict()
            else:
                params['settled_amount'] = self.settled_amount
        if self.settling_amount:
            if hasattr(self.settling_amount, 'to_alipay_dict'):
                params['settling_amount'] = self.settling_amount.to_alipay_dict()
            else:
                params['settling_amount'] = self.settling_amount
        if self.un_confirmed_amount:
            if hasattr(self.un_confirmed_amount, 'to_alipay_dict'):
                params['un_confirmed_amount'] = self.un_confirmed_amount.to_alipay_dict()
            else:
                params['un_confirmed_amount'] = self.un_confirmed_amount
        if self.un_settle_amount:
            if hasattr(self.un_settle_amount, 'to_alipay_dict'):
                params['un_settle_amount'] = self.un_settle_amount.to_alipay_dict()
            else:
                params['un_settle_amount'] = self.un_settle_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApSumSummaryBillAmountDTO()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'checkout_amount' in d:
            o.checkout_amount = d['checkout_amount']
        if 'confirmed_amount' in d:
            o.confirmed_amount = d['confirmed_amount']
        if 'settled_amount' in d:
            o.settled_amount = d['settled_amount']
        if 'settling_amount' in d:
            o.settling_amount = d['settling_amount']
        if 'un_confirmed_amount' in d:
            o.un_confirmed_amount = d['un_confirmed_amount']
        if 'un_settle_amount' in d:
            o.un_settle_amount = d['un_settle_amount']
        return o


