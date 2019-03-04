#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiServindustryReservationPayshopIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryReservationPayshopIdentifyResponse, self).__init__()
        self._pay_shop = None

    @property
    def pay_shop(self):
        return self._pay_shop

    @pay_shop.setter
    def pay_shop(self, value):
        self._pay_shop = value

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryReservationPayshopIdentifyResponse, self).parse_response_content(response_content)
        if 'pay_shop' in response:
            self.pay_shop = response['pay_shop']
