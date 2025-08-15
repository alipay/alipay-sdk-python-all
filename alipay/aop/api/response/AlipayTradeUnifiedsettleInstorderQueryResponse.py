#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UnifiedSettleTradeInstOrderInfo import UnifiedSettleTradeInstOrderInfo


class AlipayTradeUnifiedsettleInstorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeUnifiedsettleInstorderQueryResponse, self).__init__()
        self._has_more = None
        self._order_info_list = None

    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def order_info_list(self):
        return self._order_info_list

    @order_info_list.setter
    def order_info_list(self, value):
        if isinstance(value, list):
            self._order_info_list = list()
            for i in value:
                if isinstance(i, UnifiedSettleTradeInstOrderInfo):
                    self._order_info_list.append(i)
                else:
                    self._order_info_list.append(UnifiedSettleTradeInstOrderInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeUnifiedsettleInstorderQueryResponse, self).parse_response_content(response_content)
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'order_info_list' in response:
            self.order_info_list = response['order_info_list']
