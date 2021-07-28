#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExchangeVoucher(object):

    def __init__(self):
        self._amount = None
        self._customer_service_mobile = None
        self._customer_service_url = None
        self._floor_amount = None
        self._refundable = None
        self._sale_amount = None
        self._voucher_detail_url = None
        self._voucher_name = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def customer_service_mobile(self):
        return self._customer_service_mobile

    @customer_service_mobile.setter
    def customer_service_mobile(self, value):
        self._customer_service_mobile = value
    @property
    def customer_service_url(self):
        return self._customer_service_url

    @customer_service_url.setter
    def customer_service_url(self, value):
        self._customer_service_url = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def refundable(self):
        return self._refundable

    @refundable.setter
    def refundable(self, value):
        self._refundable = value
    @property
    def sale_amount(self):
        return self._sale_amount

    @sale_amount.setter
    def sale_amount(self, value):
        self._sale_amount = value
    @property
    def voucher_detail_url(self):
        return self._voucher_detail_url

    @voucher_detail_url.setter
    def voucher_detail_url(self, value):
        self._voucher_detail_url = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.customer_service_mobile:
            if hasattr(self.customer_service_mobile, 'to_alipay_dict'):
                params['customer_service_mobile'] = self.customer_service_mobile.to_alipay_dict()
            else:
                params['customer_service_mobile'] = self.customer_service_mobile
        if self.customer_service_url:
            if hasattr(self.customer_service_url, 'to_alipay_dict'):
                params['customer_service_url'] = self.customer_service_url.to_alipay_dict()
            else:
                params['customer_service_url'] = self.customer_service_url
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.refundable:
            if hasattr(self.refundable, 'to_alipay_dict'):
                params['refundable'] = self.refundable.to_alipay_dict()
            else:
                params['refundable'] = self.refundable
        if self.sale_amount:
            if hasattr(self.sale_amount, 'to_alipay_dict'):
                params['sale_amount'] = self.sale_amount.to_alipay_dict()
            else:
                params['sale_amount'] = self.sale_amount
        if self.voucher_detail_url:
            if hasattr(self.voucher_detail_url, 'to_alipay_dict'):
                params['voucher_detail_url'] = self.voucher_detail_url.to_alipay_dict()
            else:
                params['voucher_detail_url'] = self.voucher_detail_url
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExchangeVoucher()
        if 'amount' in d:
            o.amount = d['amount']
        if 'customer_service_mobile' in d:
            o.customer_service_mobile = d['customer_service_mobile']
        if 'customer_service_url' in d:
            o.customer_service_url = d['customer_service_url']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'refundable' in d:
            o.refundable = d['refundable']
        if 'sale_amount' in d:
            o.sale_amount = d['sale_amount']
        if 'voucher_detail_url' in d:
            o.voucher_detail_url = d['voucher_detail_url']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        return o


