#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChannelShop import ChannelShop


class AntMerchantExpandChanneldigitalpoiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandChanneldigitalpoiQueryResponse, self).__init__()
        self._shop_info = None

    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, list):
            self._shop_info = list()
            for i in value:
                if isinstance(i, ChannelShop):
                    self._shop_info.append(i)
                else:
                    self._shop_info.append(ChannelShop.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandChanneldigitalpoiQueryResponse, self).parse_response_content(response_content)
        if 'shop_info' in response:
            self.shop_info = response['shop_info']
