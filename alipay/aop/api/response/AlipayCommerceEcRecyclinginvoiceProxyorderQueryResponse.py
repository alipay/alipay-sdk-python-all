#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceProxyorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceProxyorderQueryResponse, self).__init__()
        self._auth_url = None
        self._confirm_time = None
        self._farmer_account_no = None
        self._farmer_account_type = None
        self._farmer_name = None
        self._out_request_no = None
        self._pay_order_no = None
        self._proxy_account_no = None
        self._proxy_account_type = None
        self._proxy_earnest_amount = None
        self._proxy_name = None
        self._proxy_order_id = None
        self._proxy_order_status = None

    @property
    def auth_url(self):
        return self._auth_url

    @auth_url.setter
    def auth_url(self, value):
        self._auth_url = value
    @property
    def confirm_time(self):
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, value):
        self._confirm_time = value
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
    @property
    def proxy_order_id(self):
        return self._proxy_order_id

    @proxy_order_id.setter
    def proxy_order_id(self, value):
        self._proxy_order_id = value
    @property
    def proxy_order_status(self):
        return self._proxy_order_status

    @proxy_order_status.setter
    def proxy_order_status(self, value):
        self._proxy_order_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceProxyorderQueryResponse, self).parse_response_content(response_content)
        if 'auth_url' in response:
            self.auth_url = response['auth_url']
        if 'confirm_time' in response:
            self.confirm_time = response['confirm_time']
        if 'farmer_account_no' in response:
            self.farmer_account_no = response['farmer_account_no']
        if 'farmer_account_type' in response:
            self.farmer_account_type = response['farmer_account_type']
        if 'farmer_name' in response:
            self.farmer_name = response['farmer_name']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'pay_order_no' in response:
            self.pay_order_no = response['pay_order_no']
        if 'proxy_account_no' in response:
            self.proxy_account_no = response['proxy_account_no']
        if 'proxy_account_type' in response:
            self.proxy_account_type = response['proxy_account_type']
        if 'proxy_earnest_amount' in response:
            self.proxy_earnest_amount = response['proxy_earnest_amount']
        if 'proxy_name' in response:
            self.proxy_name = response['proxy_name']
        if 'proxy_order_id' in response:
            self.proxy_order_id = response['proxy_order_id']
        if 'proxy_order_status' in response:
            self.proxy_order_status = response['proxy_order_status']
