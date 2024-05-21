#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OnlineRideSuperWalletData import OnlineRideSuperWalletData


class AlipayCommerceTransportOnlinerideSuperwalletQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOnlinerideSuperwalletQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, OnlineRideSuperWalletData):
            self._data = value
        else:
            self._data = OnlineRideSuperWalletData.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOnlinerideSuperwalletQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
