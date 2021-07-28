#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinInsuranceUnifiedApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinInsuranceUnifiedApplyResponse, self).__init__()
        self._biz_message = None
        self._inst_apply_no = None
        self._inst_policy_no = None
        self._policy_status = None
        self._premium = None
        self._request_no = None

    @property
    def biz_message(self):
        return self._biz_message

    @biz_message.setter
    def biz_message(self, value):
        self._biz_message = value
    @property
    def inst_apply_no(self):
        return self._inst_apply_no

    @inst_apply_no.setter
    def inst_apply_no(self, value):
        self._inst_apply_no = value
    @property
    def inst_policy_no(self):
        return self._inst_policy_no

    @inst_policy_no.setter
    def inst_policy_no(self, value):
        self._inst_policy_no = value
    @property
    def policy_status(self):
        return self._policy_status

    @policy_status.setter
    def policy_status(self, value):
        self._policy_status = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinInsuranceUnifiedApplyResponse, self).parse_response_content(response_content)
        if 'biz_message' in response:
            self.biz_message = response['biz_message']
        if 'inst_apply_no' in response:
            self.inst_apply_no = response['inst_apply_no']
        if 'inst_policy_no' in response:
            self.inst_policy_no = response['inst_policy_no']
        if 'policy_status' in response:
            self.policy_status = response['policy_status']
        if 'premium' in response:
            self.premium = response['premium']
        if 'request_no' in response:
            self.request_no = response['request_no']
