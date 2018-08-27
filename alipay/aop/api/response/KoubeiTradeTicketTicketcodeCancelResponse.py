#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeTicketTicketcodeCancelResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeTicketTicketcodeCancelResponse, self).__init__()
        self._biz_code = None
        self._request_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeTicketTicketcodeCancelResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'request_id' in response:
            self.request_id = response['request_id']
