#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringPosDishbatchDeleteResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosDishbatchDeleteResponse, self).__init__()
        self._dish_ids = None

    @property
    def dish_ids(self):
        return self._dish_ids

    @dish_ids.setter
    def dish_ids(self, value):
        if isinstance(value, list):
            self._dish_ids = list()
            for i in value:
                self._dish_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosDishbatchDeleteResponse, self).parse_response_content(response_content)
        if 'dish_ids' in response:
            self.dish_ids = response['dish_ids']
