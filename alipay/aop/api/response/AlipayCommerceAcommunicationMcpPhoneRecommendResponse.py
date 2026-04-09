#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PhoneItemInfo import PhoneItemInfo
from alipay.aop.api.domain.MobilePhoneInfo import MobilePhoneInfo


class AlipayCommerceAcommunicationMcpPhoneRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationMcpPhoneRecommendResponse, self).__init__()
        self._items = None
        self._mobile_info = None
        self._query_balance_link = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, PhoneItemInfo):
                    self._items.append(i)
                else:
                    self._items.append(PhoneItemInfo.from_alipay_dict(i))
    @property
    def mobile_info(self):
        return self._mobile_info

    @mobile_info.setter
    def mobile_info(self, value):
        if isinstance(value, MobilePhoneInfo):
            self._mobile_info = value
        else:
            self._mobile_info = MobilePhoneInfo.from_alipay_dict(value)
    @property
    def query_balance_link(self):
        return self._query_balance_link

    @query_balance_link.setter
    def query_balance_link(self, value):
        self._query_balance_link = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationMcpPhoneRecommendResponse, self).parse_response_content(response_content)
        if 'items' in response:
            self.items = response['items']
        if 'mobile_info' in response:
            self.mobile_info = response['mobile_info']
        if 'query_balance_link' in response:
            self.query_balance_link = response['query_balance_link']
