#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringOrderInfoVerifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringOrderInfoVerifyResponse, self).__init__()
        self._idempotent = None
        self._order_id = None
        self._retry = None

    @property
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringOrderInfoVerifyResponse, self).parse_response_content(response_content)
        if 'idempotent' in response:
            self.idempotent = response['idempotent']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'retry' in response:
            self.retry = response['retry']
