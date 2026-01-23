#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardBookingSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardBookingSyncResponse, self).__init__()
        self._booking_id = None

    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, value):
        self._booking_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardBookingSyncResponse, self).parse_response_content(response_content)
        if 'booking_id' in response:
            self.booking_id = response['booking_id']
