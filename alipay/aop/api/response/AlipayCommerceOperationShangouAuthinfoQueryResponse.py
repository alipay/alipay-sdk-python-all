#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationShangouAuthinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationShangouAuthinfoQueryResponse, self).__init__()
        self._mobile_binding_status = None

    @property
    def mobile_binding_status(self):
        return self._mobile_binding_status

    @mobile_binding_status.setter
    def mobile_binding_status(self, value):
        self._mobile_binding_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationShangouAuthinfoQueryResponse, self).parse_response_content(response_content)
        if 'mobile_binding_status' in response:
            self.mobile_binding_status = response['mobile_binding_status']
