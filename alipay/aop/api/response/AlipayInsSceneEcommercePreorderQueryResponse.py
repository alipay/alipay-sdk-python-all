#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsPreOrderDTO import InsPreOrderDTO


class AlipayInsSceneEcommercePreorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommercePreorderQueryResponse, self).__init__()
        self._pre_orders = None

    @property
    def pre_orders(self):
        return self._pre_orders

    @pre_orders.setter
    def pre_orders(self, value):
        if isinstance(value, list):
            self._pre_orders = list()
            for i in value:
                if isinstance(i, InsPreOrderDTO):
                    self._pre_orders.append(i)
                else:
                    self._pre_orders.append(InsPreOrderDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommercePreorderQueryResponse, self).parse_response_content(response_content)
        if 'pre_orders' in response:
            self.pre_orders = response['pre_orders']
