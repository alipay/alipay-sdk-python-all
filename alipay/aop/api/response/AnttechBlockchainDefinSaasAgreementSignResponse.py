#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReferenceId import ReferenceId


class AnttechBlockchainDefinSaasAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinSaasAgreementSignResponse, self).__init__()
        self._op_status = None
        self._out_member_id = None
        self._platform_member_id = None

    @property
    def op_status(self):
        return self._op_status

    @op_status.setter
    def op_status(self, value):
        self._op_status = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._out_member_id = value
        else:
            self._out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinSaasAgreementSignResponse, self).parse_response_content(response_content)
        if 'op_status' in response:
            self.op_status = response['op_status']
        if 'out_member_id' in response:
            self.out_member_id = response['out_member_id']
        if 'platform_member_id' in response:
            self.platform_member_id = response['platform_member_id']
