#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoSettleApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoSettleApplyResponse, self).__init__()
        self._agreement_id = None
        self._fail_reason = None
        self._out_request_no = None
        self._settle_status = None
        self._withhold_plan_no = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def withhold_plan_no(self):
        return self._withhold_plan_no

    @withhold_plan_no.setter
    def withhold_plan_no(self, value):
        self._withhold_plan_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoSettleApplyResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'settle_status' in response:
            self.settle_status = response['settle_status']
        if 'withhold_plan_no' in response:
            self.withhold_plan_no = response['withhold_plan_no']
