#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardNumberVO import CardNumberVO


class AlipayFundCouponWufuCostassetsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponWufuCostassetsQueryResponse, self).__init__()
        self._can_cost = None
        self._card_numbers = None
        self._have_enough_cards = None
        self._result_code = None
        self._result_desc = None
        self._result_view = None
        self._success = None

    @property
    def can_cost(self):
        return self._can_cost

    @can_cost.setter
    def can_cost(self, value):
        self._can_cost = value
    @property
    def card_numbers(self):
        return self._card_numbers

    @card_numbers.setter
    def card_numbers(self, value):
        if isinstance(value, list):
            self._card_numbers = list()
            for i in value:
                if isinstance(i, CardNumberVO):
                    self._card_numbers.append(i)
                else:
                    self._card_numbers.append(CardNumberVO.from_alipay_dict(i))
    @property
    def have_enough_cards(self):
        return self._have_enough_cards

    @have_enough_cards.setter
    def have_enough_cards(self, value):
        self._have_enough_cards = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def result_view(self):
        return self._result_view

    @result_view.setter
    def result_view(self, value):
        self._result_view = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponWufuCostassetsQueryResponse, self).parse_response_content(response_content)
        if 'can_cost' in response:
            self.can_cost = response['can_cost']
        if 'card_numbers' in response:
            self.card_numbers = response['card_numbers']
        if 'have_enough_cards' in response:
            self.have_enough_cards = response['have_enough_cards']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'result_view' in response:
            self.result_view = response['result_view']
        if 'success' in response:
            self.success = response['success']
