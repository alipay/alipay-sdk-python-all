#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLifeserviceRedemptionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceRedemptionQueryResponse, self).__init__()
        self._card_id = None
        self._item_id = None
        self._open_id = None
        self._user_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceRedemptionQueryResponse, self).parse_response_content(response_content)
        if 'card_id' in response:
            self.card_id = response['card_id']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
