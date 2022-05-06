#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceSignStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceSignStatusQueryResponse, self).__init__()
        self._business_id = None
        self._comment = None
        self._status = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceSignStatusQueryResponse, self).parse_response_content(response_content)
        if 'business_id' in response:
            self.business_id = response['business_id']
        if 'comment' in response:
            self.comment = response['comment']
        if 'status' in response:
            self.status = response['status']
