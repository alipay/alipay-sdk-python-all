#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionOrderfundUnfreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionOrderfundUnfreezeResponse, self).__init__()
        self._amount = None
        self._currency = None
        self._out_flow_id = None
        self._relation_out_order_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def out_flow_id(self):
        return self._out_flow_id

    @out_flow_id.setter
    def out_flow_id(self, value):
        self._out_flow_id = value
    @property
    def relation_out_order_no(self):
        return self._relation_out_order_no

    @relation_out_order_no.setter
    def relation_out_order_no(self, value):
        self._relation_out_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionOrderfundUnfreezeResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'currency' in response:
            self.currency = response['currency']
        if 'out_flow_id' in response:
            self.out_flow_id = response['out_flow_id']
        if 'relation_out_order_no' in response:
            self.relation_out_order_no = response['relation_out_order_no']
