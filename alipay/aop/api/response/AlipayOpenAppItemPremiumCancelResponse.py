#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppItemPremiumCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItemPremiumCancelResponse, self).__init__()
        self._item_id = None
        self._reason = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItemPremiumCancelResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'reason' in response:
            self.reason = response['reason']
