#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandChannelpoiCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandChannelpoiCreateResponse, self).__init__()
        self._order_id = None
        self._progress = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandChannelpoiCreateResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'progress' in response:
            self.progress = response['progress']
