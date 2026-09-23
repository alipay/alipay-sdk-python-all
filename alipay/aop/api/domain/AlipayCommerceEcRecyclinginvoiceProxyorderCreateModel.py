#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceProxyorderCreateModel(object):

    def __init__(self):
        self._farmer_account_no = None
        self._farmer_account_type = None
        self._farmer_cert_no = None
        self._farmer_name = None
        self._out_request_no = None
        self._pay_order_no = None
        self._proxy_account_no = None
        self._proxy_account_type = None
        self._proxy_cert_no = None
        self._proxy_earnest_amount = None
        self._proxy_name = None

    @property
    def farmer_account_no(self):
        return self._farmer_account_no

    @farmer_account_no.setter
    def farmer_account_no(self, value):
        self._farmer_account_no = value
    @property
    def farmer_account_type(self):
        return self._farmer_account_type

    @farmer_account_type.setter
    def farmer_account_type(self, value):
        self._farmer_account_type = value
    @property
    def farmer_cert_no(self):
        return self._farmer_cert_no

    @farmer_cert_no.setter
    def farmer_cert_no(self, value):
        self._farmer_cert_no = value
    @property
    def farmer_name(self):
        return self._farmer_name

    @farmer_name.setter
    def farmer_name(self, value):
        self._farmer_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_order_no(self):
        return self._pay_order_no

    @pay_order_no.setter
    def pay_order_no(self, value):
        self._pay_order_no = value
    @property
    def proxy_account_no(self):
        return self._proxy_account_no

    @proxy_account_no.setter
    def proxy_account_no(self, value):
        self._proxy_account_no = value
    @property
    def proxy_account_type(self):
        return self._proxy_account_type

    @proxy_account_type.setter
    def proxy_account_type(self, value):
        self._proxy_account_type = value
    @property
    def proxy_cert_no(self):
        return self._proxy_cert_no

    @proxy_cert_no.setter
    def proxy_cert_no(self, value):
        self._proxy_cert_no = value
    @property
    def proxy_earnest_amount(self):
        return self._proxy_earnest_amount

    @proxy_earnest_amount.setter
    def proxy_earnest_amount(self, value):
        self._proxy_earnest_amount = value
    @property
    def proxy_name(self):
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, value):
        self._proxy_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.farmer_account_no:
            if hasattr(self.farmer_account_no, 'to_alipay_dict'):
                params['farmer_account_no'] = self.farmer_account_no.to_alipay_dict()
            else:
                params['farmer_account_no'] = self.farmer_account_no
        if self.farmer_account_type:
            if hasattr(self.farmer_account_type, 'to_alipay_dict'):
                params['farmer_account_type'] = self.farmer_account_type.to_alipay_dict()
            else:
                params['farmer_account_type'] = self.farmer_account_type
        if self.farmer_cert_no:
            if hasattr(self.farmer_cert_no, 'to_alipay_dict'):
                params['farmer_cert_no'] = self.farmer_cert_no.to_alipay_dict()
            else:
                params['farmer_cert_no'] = self.farmer_cert_no
        if self.farmer_name:
            if hasattr(self.farmer_name, 'to_alipay_dict'):
                params['farmer_name'] = self.farmer_name.to_alipay_dict()
            else:
                params['farmer_name'] = self.farmer_name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.pay_order_no:
            if hasattr(self.pay_order_no, 'to_alipay_dict'):
                params['pay_order_no'] = self.pay_order_no.to_alipay_dict()
            else:
                params['pay_order_no'] = self.pay_order_no
        if self.proxy_account_no:
            if hasattr(self.proxy_account_no, 'to_alipay_dict'):
                params['proxy_account_no'] = self.proxy_account_no.to_alipay_dict()
            else:
                params['proxy_account_no'] = self.proxy_account_no
        if self.proxy_account_type:
            if hasattr(self.proxy_account_type, 'to_alipay_dict'):
                params['proxy_account_type'] = self.proxy_account_type.to_alipay_dict()
            else:
                params['proxy_account_type'] = self.proxy_account_type
        if self.proxy_cert_no:
            if hasattr(self.proxy_cert_no, 'to_alipay_dict'):
                params['proxy_cert_no'] = self.proxy_cert_no.to_alipay_dict()
            else:
                params['proxy_cert_no'] = self.proxy_cert_no
        if self.proxy_earnest_amount:
            if hasattr(self.proxy_earnest_amount, 'to_alipay_dict'):
                params['proxy_earnest_amount'] = self.proxy_earnest_amount.to_alipay_dict()
            else:
                params['proxy_earnest_amount'] = self.proxy_earnest_amount
        if self.proxy_name:
            if hasattr(self.proxy_name, 'to_alipay_dict'):
                params['proxy_name'] = self.proxy_name.to_alipay_dict()
            else:
                params['proxy_name'] = self.proxy_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceProxyorderCreateModel()
        if 'farmer_account_no' in d:
            o.farmer_account_no = d['farmer_account_no']
        if 'farmer_account_type' in d:
            o.farmer_account_type = d['farmer_account_type']
        if 'farmer_cert_no' in d:
            o.farmer_cert_no = d['farmer_cert_no']
        if 'farmer_name' in d:
            o.farmer_name = d['farmer_name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'pay_order_no' in d:
            o.pay_order_no = d['pay_order_no']
        if 'proxy_account_no' in d:
            o.proxy_account_no = d['proxy_account_no']
        if 'proxy_account_type' in d:
            o.proxy_account_type = d['proxy_account_type']
        if 'proxy_cert_no' in d:
            o.proxy_cert_no = d['proxy_cert_no']
        if 'proxy_earnest_amount' in d:
            o.proxy_earnest_amount = d['proxy_earnest_amount']
        if 'proxy_name' in d:
            o.proxy_name = d['proxy_name']
        return o


