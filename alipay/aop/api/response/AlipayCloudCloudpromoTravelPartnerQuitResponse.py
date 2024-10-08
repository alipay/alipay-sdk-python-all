#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoTravelPartnerQuitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoTravelPartnerQuitResponse, self).__init__()
        self._assist_status = None
        self._item_id = None

    @property
    def assist_status(self):
        return self._assist_status

    @assist_status.setter
    def assist_status(self, value):
        self._assist_status = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoTravelPartnerQuitResponse, self).parse_response_content(response_content)
        if 'assist_status' in response:
            self.assist_status = response['assist_status']
        if 'item_id' in response:
            self.item_id = response['item_id']
