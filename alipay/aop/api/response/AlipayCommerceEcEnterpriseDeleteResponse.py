#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEnterpriseDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseDeleteResponse, self).__init__()
        self._enterprise_id = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseDeleteResponse, self).parse_response_content(response_content)
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
