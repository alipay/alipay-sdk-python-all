#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJfSignprocessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfSignprocessQueryResponse, self).__init__()
        self._agreement_id = None
        self._org_code = None
        self._org_msg = None
        self._status = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def org_msg(self):
        return self._org_msg

    @org_msg.setter
    def org_msg(self, value):
        self._org_msg = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfSignprocessQueryResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'org_code' in response:
            self.org_code = response['org_code']
        if 'org_msg' in response:
            self.org_msg = response['org_msg']
        if 'status' in response:
            self.status = response['status']
