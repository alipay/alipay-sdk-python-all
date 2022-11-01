#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundZcardprodUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundZcardprodUserQueryResponse, self).__init__()
        self._asset_id = None
        self._bind_status = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundZcardprodUserQueryResponse, self).parse_response_content(response_content)
        if 'asset_id' in response:
            self.asset_id = response['asset_id']
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
