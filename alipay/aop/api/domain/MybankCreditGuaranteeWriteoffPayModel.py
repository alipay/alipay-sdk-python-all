#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WriteoffOrderParam import WriteoffOrderParam


class MybankCreditGuaranteeWriteoffPayModel(object):

    def __init__(self):
        self._actual_amount = None
        self._actual_amount_currency = None
        self._apply_amount = None
        self._apply_amount_currency = None
        self._channel = None
        self._seller_login_id = None
        self._site = None
        self._writeoff_apply_no = None
        self._writeoff_order_param_list = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def actual_amount_currency(self):
        return self._actual_amount_currency

    @actual_amount_currency.setter
    def actual_amount_currency(self, value):
        self._actual_amount_currency = value
    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def apply_amount_currency(self):
        return self._apply_amount_currency

    @apply_amount_currency.setter
    def apply_amount_currency(self, value):
        self._apply_amount_currency = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def writeoff_apply_no(self):
        return self._writeoff_apply_no

    @writeoff_apply_no.setter
    def writeoff_apply_no(self, value):
        self._writeoff_apply_no = value
    @property
    def writeoff_order_param_list(self):
        return self._writeoff_order_param_list

    @writeoff_order_param_list.setter
    def writeoff_order_param_list(self, value):
        if isinstance(value, list):
            self._writeoff_order_param_list = list()
            for i in value:
                if isinstance(i, WriteoffOrderParam):
                    self._writeoff_order_param_list.append(i)
                else:
                    self._writeoff_order_param_list.append(WriteoffOrderParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.actual_amount_currency:
            if hasattr(self.actual_amount_currency, 'to_alipay_dict'):
                params['actual_amount_currency'] = self.actual_amount_currency.to_alipay_dict()
            else:
                params['actual_amount_currency'] = self.actual_amount_currency
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.apply_amount_currency:
            if hasattr(self.apply_amount_currency, 'to_alipay_dict'):
                params['apply_amount_currency'] = self.apply_amount_currency.to_alipay_dict()
            else:
                params['apply_amount_currency'] = self.apply_amount_currency
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.writeoff_apply_no:
            if hasattr(self.writeoff_apply_no, 'to_alipay_dict'):
                params['writeoff_apply_no'] = self.writeoff_apply_no.to_alipay_dict()
            else:
                params['writeoff_apply_no'] = self.writeoff_apply_no
        if self.writeoff_order_param_list:
            if isinstance(self.writeoff_order_param_list, list):
                for i in range(0, len(self.writeoff_order_param_list)):
                    element = self.writeoff_order_param_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.writeoff_order_param_list[i] = element.to_alipay_dict()
            if hasattr(self.writeoff_order_param_list, 'to_alipay_dict'):
                params['writeoff_order_param_list'] = self.writeoff_order_param_list.to_alipay_dict()
            else:
                params['writeoff_order_param_list'] = self.writeoff_order_param_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditGuaranteeWriteoffPayModel()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'actual_amount_currency' in d:
            o.actual_amount_currency = d['actual_amount_currency']
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'apply_amount_currency' in d:
            o.apply_amount_currency = d['apply_amount_currency']
        if 'channel' in d:
            o.channel = d['channel']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        if 'site' in d:
            o.site = d['site']
        if 'writeoff_apply_no' in d:
            o.writeoff_apply_no = d['writeoff_apply_no']
        if 'writeoff_order_param_list' in d:
            o.writeoff_order_param_list = d['writeoff_order_param_list']
        return o


