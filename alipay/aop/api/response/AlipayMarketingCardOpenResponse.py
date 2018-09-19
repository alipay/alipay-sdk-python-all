#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantCard import MerchantCard


class AlipayMarketingCardOpenResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardOpenResponse, self).__init__()
        self._card_info = None
        self._open_card_channel = None
        self._open_card_channel_id = None

    @property
    def card_info(self):
        return self._card_info

    @card_info.setter
    def card_info(self, value):
        if isinstance(value, MerchantCard):
            self._card_info = value
        else:
            self._card_info = MerchantCard.from_alipay_dict(value)
    @property
    def open_card_channel(self):
        return self._open_card_channel

    @open_card_channel.setter
    def open_card_channel(self, value):
        self._open_card_channel = value
    @property
    def open_card_channel_id(self):
        return self._open_card_channel_id

    @open_card_channel_id.setter
    def open_card_channel_id(self, value):
        self._open_card_channel_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardOpenResponse, self).parse_response_content(response_content)
        if 'card_info' in response:
            self.card_info = response['card_info']
        if 'open_card_channel' in response:
            self.open_card_channel = response['open_card_channel']
        if 'open_card_channel_id' in response:
            self.open_card_channel_id = response['open_card_channel_id']
