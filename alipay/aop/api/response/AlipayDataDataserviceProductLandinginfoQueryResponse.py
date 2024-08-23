#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LandingTypeDto import LandingTypeDto


class AlipayDataDataserviceProductLandinginfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceProductLandinginfoQueryResponse, self).__init__()
        self._item_id = None
        self._landing = None
        self._out_item_id = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def landing(self):
        return self._landing

    @landing.setter
    def landing(self, value):
        if isinstance(value, LandingTypeDto):
            self._landing = value
        else:
            self._landing = LandingTypeDto.from_alipay_dict(value)
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceProductLandinginfoQueryResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'landing' in response:
            self.landing = response['landing']
        if 'out_item_id' in response:
            self.out_item_id = response['out_item_id']
