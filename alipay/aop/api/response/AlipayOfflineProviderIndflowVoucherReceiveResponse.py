#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdVoucherPrizeDetail import AdVoucherPrizeDetail


class AlipayOfflineProviderIndflowVoucherReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderIndflowVoucherReceiveResponse, self).__init__()
        self._prize_details = None

    @property
    def prize_details(self):
        return self._prize_details

    @prize_details.setter
    def prize_details(self, value):
        if isinstance(value, list):
            self._prize_details = list()
            for i in value:
                if isinstance(i, AdVoucherPrizeDetail):
                    self._prize_details.append(i)
                else:
                    self._prize_details.append(AdVoucherPrizeDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderIndflowVoucherReceiveResponse, self).parse_response_content(response_content)
        if 'prize_details' in response:
            self.prize_details = response['prize_details']
