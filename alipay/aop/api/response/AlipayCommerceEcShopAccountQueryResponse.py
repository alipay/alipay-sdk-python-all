#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcTradeIdentityAccountInfo import EcTradeIdentityAccountInfo


class AlipayCommerceEcShopAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcShopAccountQueryResponse, self).__init__()
        self._trade_identity_list = None

    @property
    def trade_identity_list(self):
        return self._trade_identity_list

    @trade_identity_list.setter
    def trade_identity_list(self, value):
        if isinstance(value, list):
            self._trade_identity_list = list()
            for i in value:
                if isinstance(i, EcTradeIdentityAccountInfo):
                    self._trade_identity_list.append(i)
                else:
                    self._trade_identity_list.append(EcTradeIdentityAccountInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcShopAccountQueryResponse, self).parse_response_content(response_content)
        if 'trade_identity_list' in response:
            self.trade_identity_list = response['trade_identity_list']
