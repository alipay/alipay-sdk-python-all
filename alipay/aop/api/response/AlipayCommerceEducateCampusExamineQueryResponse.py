#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCampusExamineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusExamineQueryResponse, self).__init__()
        self._reason = None
        self._status = None

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusExamineQueryResponse, self).parse_response_content(response_content)
        if 'reason' in response:
            self.reason = response['reason']
        if 'status' in response:
            self.status = response['status']
