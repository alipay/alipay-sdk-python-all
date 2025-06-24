#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePropertyPointSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyPointSaveResponse, self).__init__()
        self._location_point_id = None
        self._nfc_card_id = None

    @property
    def location_point_id(self):
        return self._location_point_id

    @location_point_id.setter
    def location_point_id(self, value):
        self._location_point_id = value
    @property
    def nfc_card_id(self):
        return self._nfc_card_id

    @nfc_card_id.setter
    def nfc_card_id(self, value):
        self._nfc_card_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyPointSaveResponse, self).parse_response_content(response_content)
        if 'location_point_id' in response:
            self.location_point_id = response['location_point_id']
        if 'nfc_card_id' in response:
            self.nfc_card_id = response['nfc_card_id']
