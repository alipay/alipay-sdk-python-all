#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GiftCardVo import GiftCardVo


class AlipayFundWalletCardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletCardQueryResponse, self).__init__()
        self._gift_card_vos = None
        self._total_nums = None
        self._total_pages = None

    @property
    def gift_card_vos(self):
        return self._gift_card_vos

    @gift_card_vos.setter
    def gift_card_vos(self, value):
        if isinstance(value, list):
            self._gift_card_vos = list()
            for i in value:
                if isinstance(i, GiftCardVo):
                    self._gift_card_vos.append(i)
                else:
                    self._gift_card_vos.append(GiftCardVo.from_alipay_dict(i))
    @property
    def total_nums(self):
        return self._total_nums

    @total_nums.setter
    def total_nums(self, value):
        self._total_nums = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletCardQueryResponse, self).parse_response_content(response_content)
        if 'gift_card_vos' in response:
            self.gift_card_vos = response['gift_card_vos']
        if 'total_nums' in response:
            self.total_nums = response['total_nums']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
