#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizCard import BizCard


class AlipayCommerceTransportIndustryCardlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIndustryCardlistQueryResponse, self).__init__()
        self._card_list = None
        self._total = None

    @property
    def card_list(self):
        return self._card_list

    @card_list.setter
    def card_list(self, value):
        if isinstance(value, list):
            self._card_list = list()
            for i in value:
                if isinstance(i, BizCard):
                    self._card_list.append(i)
                else:
                    self._card_list.append(BizCard.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIndustryCardlistQueryResponse, self).parse_response_content(response_content)
        if 'card_list' in response:
            self.card_list = response['card_list']
        if 'total' in response:
            self.total = response['total']
