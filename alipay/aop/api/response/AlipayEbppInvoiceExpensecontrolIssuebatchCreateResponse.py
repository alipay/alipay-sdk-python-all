#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IssueQuotaCheckInfo import IssueQuotaCheckInfo


class AlipayEbppInvoiceExpensecontrolIssuebatchCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceExpensecontrolIssuebatchCreateResponse, self).__init__()
        self._issue_batch_id = None
        self._issue_quota_check_failed_list = None

    @property
    def issue_batch_id(self):
        return self._issue_batch_id

    @issue_batch_id.setter
    def issue_batch_id(self, value):
        self._issue_batch_id = value
    @property
    def issue_quota_check_failed_list(self):
        return self._issue_quota_check_failed_list

    @issue_quota_check_failed_list.setter
    def issue_quota_check_failed_list(self, value):
        if isinstance(value, list):
            self._issue_quota_check_failed_list = list()
            for i in value:
                if isinstance(i, IssueQuotaCheckInfo):
                    self._issue_quota_check_failed_list.append(i)
                else:
                    self._issue_quota_check_failed_list.append(IssueQuotaCheckInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceExpensecontrolIssuebatchCreateResponse, self).parse_response_content(response_content)
        if 'issue_batch_id' in response:
            self.issue_batch_id = response['issue_batch_id']
        if 'issue_quota_check_failed_list' in response:
            self.issue_quota_check_failed_list = response['issue_quota_check_failed_list']
