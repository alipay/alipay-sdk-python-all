#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishCookInfo import KbdishCookInfo


class KoubeiCateringDishCookSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishCookSyncResponse, self).__init__()
        self._kb_dish_cook = None

    @property
    def kb_dish_cook(self):
        return self._kb_dish_cook

    @kb_dish_cook.setter
    def kb_dish_cook(self, value):
        if isinstance(value, KbdishCookInfo):
            self._kb_dish_cook = value
        else:
            self._kb_dish_cook = KbdishCookInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishCookSyncResponse, self).parse_response_content(response_content)
        if 'kb_dish_cook' in response:
            self.kb_dish_cook = response['kb_dish_cook']
