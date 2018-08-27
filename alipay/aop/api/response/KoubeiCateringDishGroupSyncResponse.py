#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishGroupInfo import KbdishGroupInfo


class KoubeiCateringDishGroupSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishGroupSyncResponse, self).__init__()
        self._kb_dish_group = None

    @property
    def kb_dish_group(self):
        return self._kb_dish_group

    @kb_dish_group.setter
    def kb_dish_group(self, value):
        if isinstance(value, KbdishGroupInfo):
            self._kb_dish_group = value
        else:
            self._kb_dish_group = KbdishGroupInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishGroupSyncResponse, self).parse_response_content(response_content)
        if 'kb_dish_group' in response:
            self.kb_dish_group = response['kb_dish_group']
