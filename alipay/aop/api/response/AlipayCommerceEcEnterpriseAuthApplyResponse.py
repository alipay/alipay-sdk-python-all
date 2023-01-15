#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEnterpriseAuthApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseAuthApplyResponse, self).__init__()
        self._auth_apply_id = None

    @property
    def auth_apply_id(self):
        return self._auth_apply_id

    @auth_apply_id.setter
    def auth_apply_id(self, value):
        self._auth_apply_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseAuthApplyResponse, self).parse_response_content(response_content)
        if 'auth_apply_id' in response:
            self.auth_apply_id = response['auth_apply_id']
