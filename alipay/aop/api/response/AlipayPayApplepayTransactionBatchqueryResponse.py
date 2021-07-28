#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BaseOpenApiResponseHeaderDTO import BaseOpenApiResponseHeaderDTO
from alipay.aop.api.domain.TransactionDetailDTO import TransactionDetailDTO


class AlipayPayApplepayTransactionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayApplepayTransactionBatchqueryResponse, self).__init__()
        self._last_updated_tag = None
        self._response_header = None
        self._transaction_details = None

    @property
    def last_updated_tag(self):
        return self._last_updated_tag

    @last_updated_tag.setter
    def last_updated_tag(self, value):
        self._last_updated_tag = value
    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        if isinstance(value, BaseOpenApiResponseHeaderDTO):
            self._response_header = value
        else:
            self._response_header = BaseOpenApiResponseHeaderDTO.from_alipay_dict(value)
    @property
    def transaction_details(self):
        return self._transaction_details

    @transaction_details.setter
    def transaction_details(self, value):
        if isinstance(value, list):
            self._transaction_details = list()
            for i in value:
                if isinstance(i, TransactionDetailDTO):
                    self._transaction_details.append(i)
                else:
                    self._transaction_details.append(TransactionDetailDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayPayApplepayTransactionBatchqueryResponse, self).parse_response_content(response_content)
        if 'last_updated_tag' in response:
            self.last_updated_tag = response['last_updated_tag']
        if 'response_header' in response:
            self.response_header = response['response_header']
        if 'transaction_details' in response:
            self.transaction_details = response['transaction_details']
