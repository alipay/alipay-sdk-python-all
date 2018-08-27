#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishAreaInfo import KbdishAreaInfo


class KoubeiCateringDishAreaQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishAreaQueryResponse, self).__init__()
        self._kb_dish_area_list = None

    @property
    def kb_dish_area_list(self):
        return self._kb_dish_area_list

    @kb_dish_area_list.setter
    def kb_dish_area_list(self, value):
        if isinstance(value, list):
            self._kb_dish_area_list = list()
            for i in value:
                if isinstance(i, KbdishAreaInfo):
                    self._kb_dish_area_list.append(i)
                else:
                    self._kb_dish_area_list.append(KbdishAreaInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishAreaQueryResponse, self).parse_response_content(response_content)
        if 'kb_dish_area_list' in response:
            self.kb_dish_area_list = response['kb_dish_area_list']
