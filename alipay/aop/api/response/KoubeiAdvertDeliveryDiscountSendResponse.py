#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiAdvertDeliveryDiscountSendResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertDeliveryDiscountSendResponse, self).__init__()
        self._benefit_detail = None
        self._benefit_id = None

    @property
    def benefit_detail(self):
        return self._benefit_detail

    @benefit_detail.setter
    def benefit_detail(self, value):
        self._benefit_detail = value
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertDeliveryDiscountSendResponse, self).parse_response_content(response_content)
        if 'benefit_detail' in response:
            self.benefit_detail = response['benefit_detail']
        if 'benefit_id' in response:
            self.benefit_id = response['benefit_id']
