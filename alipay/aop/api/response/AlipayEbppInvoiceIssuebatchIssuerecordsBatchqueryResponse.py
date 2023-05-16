#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IssueRecordInfo import IssueRecordInfo


class AlipayEbppInvoiceIssuebatchIssuerecordsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceIssuebatchIssuerecordsBatchqueryResponse, self).__init__()
        self._issue_record_info_list = None
        self._page_num = None
        self._page_size = None
        self._total_page_count = None

    @property
    def issue_record_info_list(self):
        return self._issue_record_info_list

    @issue_record_info_list.setter
    def issue_record_info_list(self, value):
        if isinstance(value, list):
            self._issue_record_info_list = list()
            for i in value:
                if isinstance(i, IssueRecordInfo):
                    self._issue_record_info_list.append(i)
                else:
                    self._issue_record_info_list.append(IssueRecordInfo.from_alipay_dict(i))
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceIssuebatchIssuerecordsBatchqueryResponse, self).parse_response_content(response_content)
        if 'issue_record_info_list' in response:
            self.issue_record_info_list = response['issue_record_info_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
