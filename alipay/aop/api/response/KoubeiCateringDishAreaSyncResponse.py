#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishAreaInfo import KbdishAreaInfo


class KoubeiCateringDishAreaSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishAreaSyncResponse, self).__init__()
        self._kb_dish_area = None

    @property
    def kb_dish_area(self):
        return self._kb_dish_area

    @kb_dish_area.setter
    def kb_dish_area(self, value):
        if isinstance(value, KbdishAreaInfo):
            self._kb_dish_area = value
        else:
            self._kb_dish_area = KbdishAreaInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishAreaSyncResponse, self).parse_response_content(response_content)
        if 'kb_dish_area' in response:
            self.kb_dish_area = response['kb_dish_area']
