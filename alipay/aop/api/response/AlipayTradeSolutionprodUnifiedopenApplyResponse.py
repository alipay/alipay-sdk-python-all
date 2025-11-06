#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSolutionprodUnifiedopenApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSolutionprodUnifiedopenApplyResponse, self).__init__()
        self._jump_url = None
        self._uniopen_order_id = None
        self._uniopen_status = None

    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def uniopen_order_id(self):
        return self._uniopen_order_id

    @uniopen_order_id.setter
    def uniopen_order_id(self, value):
        self._uniopen_order_id = value
    @property
    def uniopen_status(self):
        return self._uniopen_status

    @uniopen_status.setter
    def uniopen_status(self, value):
        self._uniopen_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSolutionprodUnifiedopenApplyResponse, self).parse_response_content(response_content)
        if 'jump_url' in response:
            self.jump_url = response['jump_url']
        if 'uniopen_order_id' in response:
            self.uniopen_order_id = response['uniopen_order_id']
        if 'uniopen_status' in response:
            self.uniopen_status = response['uniopen_status']
