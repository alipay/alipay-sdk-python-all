#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneOrderChangeConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneOrderChangeConsultResponse, self).__init__()
        self._charge_type = None
        self._consult_order_id = None
        self._endorse_price = None

    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def consult_order_id(self):
        return self._consult_order_id

    @consult_order_id.setter
    def consult_order_id(self, value):
        self._consult_order_id = value
    @property
    def endorse_price(self):
        return self._endorse_price

    @endorse_price.setter
    def endorse_price(self, value):
        self._endorse_price = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneOrderChangeConsultResponse, self).parse_response_content(response_content)
        if 'charge_type' in response:
            self.charge_type = response['charge_type']
        if 'consult_order_id' in response:
            self.consult_order_id = response['consult_order_id']
        if 'endorse_price' in response:
            self.endorse_price = response['endorse_price']
