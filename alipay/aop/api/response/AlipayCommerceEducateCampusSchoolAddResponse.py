#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCampusSchoolAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusSchoolAddResponse, self).__init__()
        self._inst_id = None
        self._reason = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusSchoolAddResponse, self).parse_response_content(response_content)
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
        if 'reason' in response:
            self.reason = response['reason']
