#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InstFundFlowRecordDTO import InstFundFlowRecordDTO


class AlipayAccountInstfundAllocationBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountInstfundAllocationBatchqueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._result_object = None
        self._total_count = None

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
    def result_object(self):
        return self._result_object

    @result_object.setter
    def result_object(self, value):
        if isinstance(value, list):
            self._result_object = list()
            for i in value:
                if isinstance(i, InstFundFlowRecordDTO):
                    self._result_object.append(i)
                else:
                    self._result_object.append(InstFundFlowRecordDTO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountInstfundAllocationBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'result_object' in response:
            self.result_object = response['result_object']
        if 'total_count' in response:
            self.total_count = response['total_count']
