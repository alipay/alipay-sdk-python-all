#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHdfServicerightConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHdfServicerightConfirmResponse, self).__init__()
        self._biz_identity = None
        self._occupy_result = None
        self._open_partner_user_id = None

    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def occupy_result(self):
        return self._occupy_result

    @occupy_result.setter
    def occupy_result(self, value):
        self._occupy_result = value
    @property
    def open_partner_user_id(self):
        return self._open_partner_user_id

    @open_partner_user_id.setter
    def open_partner_user_id(self, value):
        self._open_partner_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHdfServicerightConfirmResponse, self).parse_response_content(response_content)
        if 'biz_identity' in response:
            self.biz_identity = response['biz_identity']
        if 'occupy_result' in response:
            self.occupy_result = response['occupy_result']
        if 'open_partner_user_id' in response:
            self.open_partner_user_id = response['open_partner_user_id']
