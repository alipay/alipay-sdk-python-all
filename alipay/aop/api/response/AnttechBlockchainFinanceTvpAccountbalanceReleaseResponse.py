#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceTvpAccountbalanceReleaseResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTvpAccountbalanceReleaseResponse, self).__init__()
        self._channel_order_id = None
        self._fund_status = None

    @property
    def channel_order_id(self):
        return self._channel_order_id

    @channel_order_id.setter
    def channel_order_id(self, value):
        self._channel_order_id = value
    @property
    def fund_status(self):
        return self._fund_status

    @fund_status.setter
    def fund_status(self, value):
        self._fund_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTvpAccountbalanceReleaseResponse, self).parse_response_content(response_content)
        if 'channel_order_id' in response:
            self.channel_order_id = response['channel_order_id']
        if 'fund_status' in response:
            self.fund_status = response['fund_status']
