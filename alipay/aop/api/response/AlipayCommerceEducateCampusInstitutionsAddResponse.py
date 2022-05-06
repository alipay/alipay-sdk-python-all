#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCampusInstitutionsAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusInstitutionsAddResponse, self).__init__()
        self._inst_id = None
        self._inst_std_code = None
        self._reason = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_std_code(self):
        return self._inst_std_code

    @inst_std_code.setter
    def inst_std_code(self, value):
        self._inst_std_code = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusInstitutionsAddResponse, self).parse_response_content(response_content)
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
        if 'inst_std_code' in response:
            self.inst_std_code = response['inst_std_code']
        if 'reason' in response:
            self.reason = response['reason']
