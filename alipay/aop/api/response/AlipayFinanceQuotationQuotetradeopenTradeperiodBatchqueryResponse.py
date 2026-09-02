#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ObjTradingPeriodDTO import ObjTradingPeriodDTO


class AlipayFinanceQuotationQuotetradeopenTradeperiodBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceQuotationQuotetradeopenTradeperiodBatchqueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, ObjTradingPeriodDTO):
                    self._data.append(i)
                else:
                    self._data.append(ObjTradingPeriodDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceQuotationQuotetradeopenTradeperiodBatchqueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
