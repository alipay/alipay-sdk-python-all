#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExchangeOrderInfo import ExchangeOrderInfo


class AlipayCommerceOperationPromoterExchangeSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoterExchangeSubmitResponse, self).__init__()
        self._exchange_order_result = None

    @property
    def exchange_order_result(self):
        return self._exchange_order_result

    @exchange_order_result.setter
    def exchange_order_result(self, value):
        if isinstance(value, ExchangeOrderInfo):
            self._exchange_order_result = value
        else:
            self._exchange_order_result = ExchangeOrderInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoterExchangeSubmitResponse, self).parse_response_content(response_content)
        if 'exchange_order_result' in response:
            self.exchange_order_result = response['exchange_order_result']
