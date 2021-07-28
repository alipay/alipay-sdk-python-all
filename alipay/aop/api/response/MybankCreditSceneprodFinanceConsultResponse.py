#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodFinanceConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodFinanceConsultResponse, self).__init__()
        self._finance_branch_ip_role_id = None
        self._finance_branch_name = None
        self._finance_inst_code = None
        self._finance_inst_name = None
        self._info = None
        self._retry = None
        self._route_no = None
        self._status = None
        self._trace_id = None

    @property
    def finance_branch_ip_role_id(self):
        return self._finance_branch_ip_role_id

    @finance_branch_ip_role_id.setter
    def finance_branch_ip_role_id(self, value):
        self._finance_branch_ip_role_id = value
    @property
    def finance_branch_name(self):
        return self._finance_branch_name

    @finance_branch_name.setter
    def finance_branch_name(self, value):
        self._finance_branch_name = value
    @property
    def finance_inst_code(self):
        return self._finance_inst_code

    @finance_inst_code.setter
    def finance_inst_code(self, value):
        self._finance_inst_code = value
    @property
    def finance_inst_name(self):
        return self._finance_inst_name

    @finance_inst_name.setter
    def finance_inst_name(self, value):
        self._finance_inst_name = value
    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def route_no(self):
        return self._route_no

    @route_no.setter
    def route_no(self, value):
        self._route_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodFinanceConsultResponse, self).parse_response_content(response_content)
        if 'finance_branch_ip_role_id' in response:
            self.finance_branch_ip_role_id = response['finance_branch_ip_role_id']
        if 'finance_branch_name' in response:
            self.finance_branch_name = response['finance_branch_name']
        if 'finance_inst_code' in response:
            self.finance_inst_code = response['finance_inst_code']
        if 'finance_inst_name' in response:
            self.finance_inst_name = response['finance_inst_name']
        if 'info' in response:
            self.info = response['info']
        if 'retry' in response:
            self.retry = response['retry']
        if 'route_no' in response:
            self.route_no = response['route_no']
        if 'status' in response:
            self.status = response['status']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
