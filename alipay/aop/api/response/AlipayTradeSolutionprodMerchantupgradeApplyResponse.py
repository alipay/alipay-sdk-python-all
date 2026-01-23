#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSolutionprodMerchantupgradeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSolutionprodMerchantupgradeApplyResponse, self).__init__()
        self._jump_url = None
        self._order_id = None
        self._status = None

    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSolutionprodMerchantupgradeApplyResponse, self).parse_response_content(response_content)
        if 'jump_url' in response:
            self.jump_url = response['jump_url']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'status' in response:
            self.status = response['status']
