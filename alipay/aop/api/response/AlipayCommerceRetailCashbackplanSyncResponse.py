#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailCashbackplanSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailCashbackplanSyncResponse, self).__init__()
        self._delivery_plan_id = None

    @property
    def delivery_plan_id(self):
        return self._delivery_plan_id

    @delivery_plan_id.setter
    def delivery_plan_id(self, value):
        self._delivery_plan_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailCashbackplanSyncResponse, self).parse_response_content(response_content)
        if 'delivery_plan_id' in response:
            self.delivery_plan_id = response['delivery_plan_id']
