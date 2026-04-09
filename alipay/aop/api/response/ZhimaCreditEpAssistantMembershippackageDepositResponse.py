#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAssistantMembershippackageDepositResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAssistantMembershippackageDepositResponse, self).__init__()
        self._package_id = None
        self._record_id = None

    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAssistantMembershippackageDepositResponse, self).parse_response_content(response_content)
        if 'package_id' in response:
            self.package_id = response['package_id']
        if 'record_id' in response:
            self.record_id = response['record_id']
