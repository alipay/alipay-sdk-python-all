#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PosCookDishQryModel import PosCookDishQryModel


class KoubeiCateringPosDishBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosDishBatchqueryResponse, self).__init__()
        self._cook_dish = None

    @property
    def cook_dish(self):
        return self._cook_dish

    @cook_dish.setter
    def cook_dish(self, value):
        if isinstance(value, PosCookDishQryModel):
            self._cook_dish = value
        else:
            self._cook_dish = PosCookDishQryModel.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosDishBatchqueryResponse, self).parse_response_content(response_content)
        if 'cook_dish' in response:
            self.cook_dish = response['cook_dish']
