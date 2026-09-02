#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseChannelRateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseChannelRateQueryResponse, self).__init__()
        self._commission_rate = None
        self._sell_channel_code = None
        self._split_rate = None

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        self._commission_rate = value
    @property
    def sell_channel_code(self):
        return self._sell_channel_code

    @sell_channel_code.setter
    def sell_channel_code(self, value):
        self._sell_channel_code = value
    @property
    def split_rate(self):
        return self._split_rate

    @split_rate.setter
    def split_rate(self, value):
        self._split_rate = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseChannelRateQueryResponse, self).parse_response_content(response_content)
        if 'commission_rate' in response:
            self.commission_rate = response['commission_rate']
        if 'sell_channel_code' in response:
            self.sell_channel_code = response['sell_channel_code']
        if 'split_rate' in response:
            self.split_rate = response['split_rate']
