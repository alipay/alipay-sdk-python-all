#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceCpataskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceCpataskQueryResponse, self).__init__()
        self._alipay_order_no = None
        self._callback_url = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceCpataskQueryResponse, self).parse_response_content(response_content)
        if 'alipay_order_no' in response:
            self.alipay_order_no = response['alipay_order_no']
        if 'callback_url' in response:
            self.callback_url = response['callback_url']
