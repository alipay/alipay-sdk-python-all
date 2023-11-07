#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundMbpcardCardBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundMbpcardCardBindResponse, self).__init__()
        self._bind_result = None
        self._card_no = None
        self._origin_amount = None
        self._valid_end_date = None
        self._valid_start_date = None

    @property
    def bind_result(self):
        return self._bind_result

    @bind_result.setter
    def bind_result(self, value):
        self._bind_result = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value
    @property
    def valid_end_date(self):
        return self._valid_end_date

    @valid_end_date.setter
    def valid_end_date(self, value):
        self._valid_end_date = value
    @property
    def valid_start_date(self):
        return self._valid_start_date

    @valid_start_date.setter
    def valid_start_date(self, value):
        self._valid_start_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundMbpcardCardBindResponse, self).parse_response_content(response_content)
        if 'bind_result' in response:
            self.bind_result = response['bind_result']
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'origin_amount' in response:
            self.origin_amount = response['origin_amount']
        if 'valid_end_date' in response:
            self.valid_end_date = response['valid_end_date']
        if 'valid_start_date' in response:
            self.valid_start_date = response['valid_start_date']
