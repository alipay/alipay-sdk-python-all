#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FinanceReceivableResultInfo import FinanceReceivableResultInfo


class AnttechBlockchainFinanceAssetIssueQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceAssetIssueQueryResponse, self).__init__()
        self._failed_code = None
        self._failed_desc = None
        self._receivable_result_info = None
        self._status = None

    @property
    def failed_code(self):
        return self._failed_code

    @failed_code.setter
    def failed_code(self, value):
        self._failed_code = value
    @property
    def failed_desc(self):
        return self._failed_desc

    @failed_desc.setter
    def failed_desc(self, value):
        self._failed_desc = value
    @property
    def receivable_result_info(self):
        return self._receivable_result_info

    @receivable_result_info.setter
    def receivable_result_info(self, value):
        if isinstance(value, FinanceReceivableResultInfo):
            self._receivable_result_info = value
        else:
            self._receivable_result_info = FinanceReceivableResultInfo.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceAssetIssueQueryResponse, self).parse_response_content(response_content)
        if 'failed_code' in response:
            self.failed_code = response['failed_code']
        if 'failed_desc' in response:
            self.failed_desc = response['failed_desc']
        if 'receivable_result_info' in response:
            self.receivable_result_info = response['receivable_result_info']
        if 'status' in response:
            self.status = response['status']
