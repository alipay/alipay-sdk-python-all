#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MultiChannelJoinGiftVO import MultiChannelJoinGiftVO


class AlipayMerchantGroupGroupgiftQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupgiftQueryResponse, self).__init__()
        self._multi_channel_join_gift = None

    @property
    def multi_channel_join_gift(self):
        return self._multi_channel_join_gift

    @multi_channel_join_gift.setter
    def multi_channel_join_gift(self, value):
        if isinstance(value, MultiChannelJoinGiftVO):
            self._multi_channel_join_gift = value
        else:
            self._multi_channel_join_gift = MultiChannelJoinGiftVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupgiftQueryResponse, self).parse_response_content(response_content)
        if 'multi_channel_join_gift' in response:
            self.multi_channel_join_gift = response['multi_channel_join_gift']
