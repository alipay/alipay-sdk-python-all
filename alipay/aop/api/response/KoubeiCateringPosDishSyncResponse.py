#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringPosDishSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosDishSyncResponse, self).__init__()
        self._dish_id = None

    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosDishSyncResponse, self).parse_response_content(response_content)
        if 'dish_id' in response:
            self.dish_id = response['dish_id']
