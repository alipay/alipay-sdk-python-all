#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsPreOrderDTO import InsPreOrderDTO


class AlipayInsSceneEcommercePreorderquoteConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommercePreorderquoteConsultResponse, self).__init__()
        self._pre_order = None

    @property
    def pre_order(self):
        return self._pre_order

    @pre_order.setter
    def pre_order(self, value):
        if isinstance(value, InsPreOrderDTO):
            self._pre_order = value
        else:
            self._pre_order = InsPreOrderDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommercePreorderquoteConsultResponse, self).parse_response_content(response_content)
        if 'pre_order' in response:
            self.pre_order = response['pre_order']
