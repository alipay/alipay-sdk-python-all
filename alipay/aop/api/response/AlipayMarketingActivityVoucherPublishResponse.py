#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingActivityVoucherPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityVoucherPublishResponse, self).__init__()
        self._recharge_url = None

    @property
    def recharge_url(self):
        return self._recharge_url

    @recharge_url.setter
    def recharge_url(self, value):
        self._recharge_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityVoucherPublishResponse, self).parse_response_content(response_content)
        if 'recharge_url' in response:
            self.recharge_url = response['recharge_url']
