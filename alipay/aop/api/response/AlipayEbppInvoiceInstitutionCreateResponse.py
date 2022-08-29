#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IssueRuleIdInfo import IssueRuleIdInfo
from alipay.aop.api.domain.StandardIdInfo import StandardIdInfo


class AlipayEbppInvoiceInstitutionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceInstitutionCreateResponse, self).__init__()
        self._institution_id = None
        self._issue_rule_id_info_list = None
        self._standard_id_info_list = None

    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
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
        response = super(AlipayEbppInvoiceInstitutionCreateResponse, self).parse_response_content(response_content)
        if 'institution_id' in response:
            self.institution_id = response['institution_id']
        if 'issue_rule_id_info_list' in response:
            self.issue_rule_id_info_list = response['issue_rule_id_info_list']
        if 'standard_id_info_list' in response:
            self.standard_id_info_list = response['standard_id_info_list']
