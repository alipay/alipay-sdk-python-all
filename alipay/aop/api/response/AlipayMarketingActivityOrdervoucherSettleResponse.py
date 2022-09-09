#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingActivityOrdervoucherSettleResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherSettleResponse, self).__init__()
        self._settle_no = None

    @property
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherSettleResponse, self).parse_response_content(response_content)
        if 'settle_no' in response:
            self.settle_no = response['settle_no']
