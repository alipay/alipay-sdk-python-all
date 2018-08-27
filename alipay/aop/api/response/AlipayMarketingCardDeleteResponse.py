#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCardDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardDeleteResponse, self).__init__()
        self._biz_serial_no = None

    @property
    def biz_serial_no(self):
        return self._biz_serial_no

    @biz_serial_no.setter
    def biz_serial_no(self, value):
        self._biz_serial_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardDeleteResponse, self).parse_response_content(response_content)
        if 'biz_serial_no' in response:
            self.biz_serial_no = response['biz_serial_no']
