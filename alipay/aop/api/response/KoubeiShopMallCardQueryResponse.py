#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MallCardBo import MallCardBo


class KoubeiShopMallCardQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiShopMallCardQueryResponse, self).__init__()
        self._cards = None
        self._open = None
        self._open_card_url = None

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        if isinstance(value, list):
            self._cards = list()
            for i in value:
                if isinstance(i, MallCardBo):
                    self._cards.append(i)
                else:
                    self._cards.append(MallCardBo.from_alipay_dict(i))
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value
    @property
    def open_card_url(self):
        return self._open_card_url

    @open_card_url.setter
    def open_card_url(self, value):
        self._open_card_url = value

    def parse_response_content(self, response_content):
        response = super(KoubeiShopMallCardQueryResponse, self).parse_response_content(response_content)
        if 'cards' in response:
            self.cards = response['cards']
        if 'open' in response:
            self.open = response['open']
        if 'open_card_url' in response:
            self.open_card_url = response['open_card_url']
