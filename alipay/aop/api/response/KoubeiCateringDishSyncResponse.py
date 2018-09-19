#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishInfo import KbdishInfo


class KoubeiCateringDishSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishSyncResponse, self).__init__()
        self._kb_dish_info = None

    @property
    def kb_dish_info(self):
        return self._kb_dish_info

    @kb_dish_info.setter
    def kb_dish_info(self, value):
        if isinstance(value, KbdishInfo):
            self._kb_dish_info = value
        else:
            self._kb_dish_info = KbdishInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishSyncResponse, self).parse_response_content(response_content)
        if 'kb_dish_info' in response:
            self.kb_dish_info = response['kb_dish_info']
