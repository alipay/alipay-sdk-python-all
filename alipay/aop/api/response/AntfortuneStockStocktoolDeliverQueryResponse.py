#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StockPositionVO import StockPositionVO


class AntfortuneStockStocktoolDeliverQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockStocktoolDeliverQueryResponse, self).__init__()
        self._position_list = None
        self._user_id = None

    @property
    def position_list(self):
        return self._position_list

    @position_list.setter
    def position_list(self, value):
        if isinstance(value, list):
            self._position_list = list()
            for i in value:
                if isinstance(i, StockPositionVO):
                    self._position_list.append(i)
                else:
                    self._position_list.append(StockPositionVO.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockStocktoolDeliverQueryResponse, self).parse_response_content(response_content)
        if 'position_list' in response:
            self.position_list = response['position_list']
        if 'user_id' in response:
            self.user_id = response['user_id']
