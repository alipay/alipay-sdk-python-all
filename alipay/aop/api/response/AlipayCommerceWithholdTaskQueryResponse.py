#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WithholdTradeDTO import WithholdTradeDTO


class AlipayCommerceWithholdTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWithholdTaskQueryResponse, self).__init__()
        self._open_id = None
        self._user_id = None
        self._withhold_no = None
        self._withhold_trades = None

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
    @property
    def withhold_no(self):
        return self._withhold_no

    @withhold_no.setter
    def withhold_no(self, value):
        self._withhold_no = value
    @property
    def withhold_trades(self):
        return self._withhold_trades

    @withhold_trades.setter
    def withhold_trades(self, value):
        if isinstance(value, list):
            self._withhold_trades = list()
            for i in value:
                if isinstance(i, WithholdTradeDTO):
                    self._withhold_trades.append(i)
                else:
                    self._withhold_trades.append(WithholdTradeDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWithholdTaskQueryResponse, self).parse_response_content(response_content)
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'withhold_no' in response:
            self.withhold_no = response['withhold_no']
        if 'withhold_trades' in response:
            self.withhold_trades = response['withhold_trades']
