#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishCookInfo import KbdishCookInfo


class KoubeiCateringDishCookQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishCookQueryResponse, self).__init__()
        self._kb_cook_list = None

    @property
    def kb_cook_list(self):
        return self._kb_cook_list

    @kb_cook_list.setter
    def kb_cook_list(self, value):
        if isinstance(value, list):
            self._kb_cook_list = list()
            for i in value:
                if isinstance(i, KbdishCookInfo):
                    self._kb_cook_list.append(i)
                else:
                    self._kb_cook_list.append(KbdishCookInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishCookQueryResponse, self).parse_response_content(response_content)
        if 'kb_cook_list' in response:
            self.kb_cook_list = response['kb_cook_list']
