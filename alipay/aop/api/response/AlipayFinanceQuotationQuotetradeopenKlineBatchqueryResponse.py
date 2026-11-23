#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuotationKLineDTO import QuotationKLineDTO
from alipay.aop.api.domain.KLineFailureOpenApiDTO import KLineFailureOpenApiDTO


class AlipayFinanceQuotationQuotetradeopenKlineBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceQuotationQuotetradeopenKlineBatchqueryResponse, self).__init__()
        self._data = None
        self._failures = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, QuotationKLineDTO):
                    self._data.append(i)
                else:
                    self._data.append(QuotationKLineDTO.from_alipay_dict(i))
    @property
    def failures(self):
        return self._failures

    @failures.setter
    def failures(self, value):
        if isinstance(value, list):
            self._failures = list()
            for i in value:
                if isinstance(i, KLineFailureOpenApiDTO):
                    self._failures.append(i)
                else:
                    self._failures.append(KLineFailureOpenApiDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceQuotationQuotetradeopenKlineBatchqueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'failures' in response:
            self.failures = response['failures']
