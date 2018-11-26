#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringPosDishgroupSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosDishgroupSyncResponse, self).__init__()
        self._dish_group_id = None

    @property
    def dish_group_id(self):
        return self._dish_group_id

    @dish_group_id.setter
    def dish_group_id(self, value):
        self._dish_group_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosDishgroupSyncResponse, self).parse_response_content(response_content)
        if 'dish_group_id' in response:
            self.dish_group_id = response['dish_group_id']
