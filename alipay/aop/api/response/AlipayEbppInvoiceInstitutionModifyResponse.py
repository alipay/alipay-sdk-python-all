#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IssueRuleIdInfo import IssueRuleIdInfo
from alipay.aop.api.domain.StandardIdInfo import StandardIdInfo


class AlipayEbppInvoiceInstitutionModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceInstitutionModifyResponse, self).__init__()
        self._issue_rule_id_info_list = None
        self._result = None
        self._standard_id_info_list = None

    @property
    def issue_rule_id_info_list(self):
        return self._issue_rule_id_info_list

    @issue_rule_id_info_list.setter
    def issue_rule_id_info_list(self, value):
        if isinstance(value, list):
            self._issue_rule_id_info_list = list()
            for i in value:
                if isinstance(i, IssueRuleIdInfo):
                    self._issue_rule_id_info_list.append(i)
                else:
                    self._issue_rule_id_info_list.append(IssueRuleIdInfo.from_alipay_dict(i))
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def standard_id_info_list(self):
        return self._standard_id_info_list

    @standard_id_info_list.setter
    def standard_id_info_list(self, value):
        if isinstance(value, list):
            self._standard_id_info_list = list()
            for i in value:
                if isinstance(i, StandardIdInfo):
                    self._standard_id_info_list.append(i)
                else:
                    self._standard_id_info_list.append(StandardIdInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceInstitutionModifyResponse, self).parse_response_content(response_content)
        if 'issue_rule_id_info_list' in response:
            self.issue_rule_id_info_list = response['issue_rule_id_info_list']
        if 'result' in response:
            self.result = response['result']
        if 'standard_id_info_list' in response:
            self.standard_id_info_list = response['standard_id_info_list']
