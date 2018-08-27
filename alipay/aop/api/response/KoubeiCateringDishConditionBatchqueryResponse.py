#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaginationDish import PaginationDish


class KoubeiCateringDishConditionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishConditionBatchqueryResponse, self).__init__()
        self._kb_dish_page_info = None

    @property
    def kb_dish_page_info(self):
        return self._kb_dish_page_info

    @kb_dish_page_info.setter
    def kb_dish_page_info(self, value):
        if isinstance(value, PaginationDish):
            self._kb_dish_page_info = value
        else:
            self._kb_dish_page_info = PaginationDish.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishConditionBatchqueryResponse, self).parse_response_content(response_content)
        if 'kb_dish_page_info' in response:
            self.kb_dish_page_info = response['kb_dish_page_info']
