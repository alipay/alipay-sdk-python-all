#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityIsvpayrecordModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityIsvpayrecordModifyResponse, self).__init__()
        self._out_order_id = None
        self._status = None

    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityIsvpayrecordModifyResponse, self).parse_response_content(response_content)
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'status' in response:
            self.status = response['status']
