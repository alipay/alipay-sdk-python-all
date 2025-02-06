#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayVoyagerFlightSupplierNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerFlightSupplierNotifyResponse, self).__init__()
        self._consume_status = None

    @property
    def consume_status(self):
        return self._consume_status

    @consume_status.setter
    def consume_status(self, value):
        self._consume_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerFlightSupplierNotifyResponse, self).parse_response_content(response_content)
        if 'consume_status' in response:
            self.consume_status = response['consume_status']
