#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceProxyorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceProxyorderCreateResponse, self).__init__()
        self._auth_url = None
        self._out_request_no = None
        self._proxy_order_id = None
        self._proxy_order_status = None

    @property
    def auth_url(self):
        return self._auth_url

    @auth_url.setter
    def auth_url(self, value):
        self._auth_url = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
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
        response = super(AlipayCommerceEcRecyclinginvoiceProxyorderCreateResponse, self).parse_response_content(response_content)
        if 'auth_url' in response:
            self.auth_url = response['auth_url']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'proxy_order_id' in response:
            self.proxy_order_id = response['proxy_order_id']
        if 'proxy_order_status' in response:
            self.proxy_order_status = response['proxy_order_status']
