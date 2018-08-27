#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMerchantOperatorRoleCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantOperatorRoleCreateResponse, self).__init__()
        self._role_id = None

    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantOperatorRoleCreateResponse, self).parse_response_content(response_content)
        if 'role_id' in response:
            self.role_id = response['role_id']
