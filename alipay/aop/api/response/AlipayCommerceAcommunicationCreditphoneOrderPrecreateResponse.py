#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationCreditphoneOrderPrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphoneOrderPrecreateResponse, self).__init__()
        self._alipay_order_no = None
        self._biz_params = None
        self._out_order_no = None
        self._page_order_no = None
        self._sign_page_url = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def biz_params(self):
        return self._biz_params

    @biz_params.setter
    def biz_params(self, value):
        self._biz_params = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def page_order_no(self):
        return self._page_order_no

    @page_order_no.setter
    def page_order_no(self, value):
        self._page_order_no = value
    @property
    def sign_page_url(self):
        return self._sign_page_url

    @sign_page_url.setter
    def sign_page_url(self, value):
        self._sign_page_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphoneOrderPrecreateResponse, self).parse_response_content(response_content)
        if 'alipay_order_no' in response:
            self.alipay_order_no = response['alipay_order_no']
        if 'biz_params' in response:
            self.biz_params = response['biz_params']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'page_order_no' in response:
            self.page_order_no = response['page_order_no']
        if 'sign_page_url' in response:
            self.sign_page_url = response['sign_page_url']
