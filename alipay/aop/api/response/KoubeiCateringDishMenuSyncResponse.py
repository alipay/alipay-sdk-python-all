#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringDishMenuSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishMenuSyncResponse, self).__init__()
        self._cook_id = None

    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishMenuSyncResponse, self).parse_response_content(response_content)
        if 'cook_id' in response:
            self.cook_id = response['cook_id']
