#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniTipsDeliveryCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTipsDeliveryCreateResponse, self).__init__()
        self._delivery_id = None

    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTipsDeliveryCreateResponse, self).parse_response_content(response_content)
        if 'delivery_id' in response:
            self.delivery_id = response['delivery_id']
