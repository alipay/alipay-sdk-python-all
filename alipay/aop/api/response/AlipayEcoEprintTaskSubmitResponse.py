#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEprintTaskSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEprintTaskSubmitResponse, self).__init__()
        self._out_order_id = None

    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEprintTaskSubmitResponse, self).parse_response_content(response_content)
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
