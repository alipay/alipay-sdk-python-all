#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UnifiedSettleOrderDetail import UnifiedSettleOrderDetail


class AlipayTradeUnifiedsettleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeUnifiedsettleQueryResponse, self).__init__()
        self._order_detail_list = None

    @property
    def order_detail_list(self):
        return self._order_detail_list

    @order_detail_list.setter
    def order_detail_list(self, value):
        if isinstance(value, list):
            self._order_detail_list = list()
            for i in value:
                if isinstance(i, UnifiedSettleOrderDetail):
                    self._order_detail_list.append(i)
                else:
                    self._order_detail_list.append(UnifiedSettleOrderDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeUnifiedsettleQueryResponse, self).parse_response_content(response_content)
        if 'order_detail_list' in response:
            self.order_detail_list = response['order_detail_list']
