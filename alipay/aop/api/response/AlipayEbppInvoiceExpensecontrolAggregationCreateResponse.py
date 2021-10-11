#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceExpensecontrolAggregationCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceExpensecontrolAggregationCreateResponse, self).__init__()
        self._aggregation_id = None

    @property
    def aggregation_id(self):
        return self._aggregation_id

    @aggregation_id.setter
    def aggregation_id(self, value):
        self._aggregation_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceExpensecontrolAggregationCreateResponse, self).parse_response_content(response_content)
        if 'aggregation_id' in response:
            self.aggregation_id = response['aggregation_id']
