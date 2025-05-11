#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandLeadsModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandLeadsModifyResponse, self).__init__()
        self._fail_reason = None
        self._need_audit = None
        self._pass = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def need_audit(self):
        return self._need_audit

    @need_audit.setter
    def need_audit(self, value):
        self._need_audit = value
    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandLeadsModifyResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'need_audit' in response:
            self.need_audit = response['need_audit']
        if 'pass' in response:
            self.pass = response['pass']
