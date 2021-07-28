#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthCardbinPrivateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthCardbinPrivateQueryResponse, self).__init__()
        self._card_type = None
        self._inst_id = None
        self._inst_name = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthCardbinPrivateQueryResponse, self).parse_response_content(response_content)
        if 'card_type' in response:
            self.card_type = response['card_type']
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
        if 'inst_name' in response:
            self.inst_name = response['inst_name']
