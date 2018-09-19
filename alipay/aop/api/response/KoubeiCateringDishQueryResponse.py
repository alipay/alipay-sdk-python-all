#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishInfo import KbdishInfo


class KoubeiCateringDishQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishQueryResponse, self).__init__()
        self._kb_dish_info_list = None

    @property
    def kb_dish_info_list(self):
        return self._kb_dish_info_list

    @kb_dish_info_list.setter
    def kb_dish_info_list(self, value):
        if isinstance(value, list):
            self._kb_dish_info_list = list()
            for i in value:
                if isinstance(i, KbdishInfo):
                    self._kb_dish_info_list.append(i)
                else:
                    self._kb_dish_info_list.append(KbdishInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishQueryResponse, self).parse_response_content(response_content)
        if 'kb_dish_info_list' in response:
            self.kb_dish_info_list = response['kb_dish_info_list']
