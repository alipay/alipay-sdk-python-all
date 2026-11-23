#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasEnterprisecertifyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasEnterprisecertifyCreateResponse, self).__init__()
        self._certify_order_no = None
        self._expire_time = None
        self._page_url = None

    @property
    def certify_order_no(self):
        return self._certify_order_no

    @certify_order_no.setter
    def certify_order_no(self, value):
        self._certify_order_no = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasEnterprisecertifyCreateResponse, self).parse_response_content(response_content)
        if 'certify_order_no' in response:
            self.certify_order_no = response['certify_order_no']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'page_url' in response:
            self.page_url = response['page_url']
