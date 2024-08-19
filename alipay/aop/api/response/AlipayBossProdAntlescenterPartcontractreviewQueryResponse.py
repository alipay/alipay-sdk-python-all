#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlescenterPartcontractreviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlescenterPartcontractreviewQueryResponse, self).__init__()
        self._audit_res = None
        self._audit_time = None
        self._audit_work_no = None
        self._contract_no = None
        self._reason = None
        self._sign_flow_id = None
        self._suggest_info = None

    @property
    def audit_res(self):
        return self._audit_res

    @audit_res.setter
    def audit_res(self, value):
        self._audit_res = value
    @property
    def audit_time(self):
        return self._audit_time

    @audit_time.setter
    def audit_time(self, value):
        self._audit_time = value
    @property
    def audit_work_no(self):
        return self._audit_work_no

    @audit_work_no.setter
    def audit_work_no(self, value):
        self._audit_work_no = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value
    @property
    def suggest_info(self):
        return self._suggest_info

    @suggest_info.setter
    def suggest_info(self, value):
        self._suggest_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlescenterPartcontractreviewQueryResponse, self).parse_response_content(response_content)
        if 'audit_res' in response:
            self.audit_res = response['audit_res']
        if 'audit_time' in response:
            self.audit_time = response['audit_time']
        if 'audit_work_no' in response:
            self.audit_work_no = response['audit_work_no']
        if 'contract_no' in response:
            self.contract_no = response['contract_no']
        if 'reason' in response:
            self.reason = response['reason']
        if 'sign_flow_id' in response:
            self.sign_flow_id = response['sign_flow_id']
        if 'suggest_info' in response:
            self.suggest_info = response['suggest_info']
