#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardBinActivityInfo import CardBinActivityInfo


class AlipayMerchantPayforprivilegeCardbinactivityCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPayforprivilegeCardbinactivityCreateormodifyResponse, self).__init__()
        self._card_bin_info = None

    @property
    def card_bin_info(self):
        return self._card_bin_info

    @card_bin_info.setter
    def card_bin_info(self, value):
        if isinstance(value, CardBinActivityInfo):
            self._card_bin_info = value
        else:
            self._card_bin_info = CardBinActivityInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPayforprivilegeCardbinactivityCreateormodifyResponse, self).parse_response_content(response_content)
        if 'card_bin_info' in response:
            self.card_bin_info = response['card_bin_info']
