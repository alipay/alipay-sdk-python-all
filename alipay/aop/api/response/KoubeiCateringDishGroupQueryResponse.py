#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishGroupInfo import KbdishGroupInfo


class KoubeiCateringDishGroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishGroupQueryResponse, self).__init__()
        self._kb_dish_group_list = None

    @property
    def kb_dish_group_list(self):
        return self._kb_dish_group_list

    @kb_dish_group_list.setter
    def kb_dish_group_list(self, value):
        if isinstance(value, list):
            self._kb_dish_group_list = list()
            for i in value:
                if isinstance(i, KbdishGroupInfo):
                    self._kb_dish_group_list.append(i)
                else:
                    self._kb_dish_group_list.append(KbdishGroupInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishGroupQueryResponse, self).parse_response_content(response_content)
        if 'kb_dish_group_list' in response:
            self.kb_dish_group_list = response['kb_dish_group_list']
