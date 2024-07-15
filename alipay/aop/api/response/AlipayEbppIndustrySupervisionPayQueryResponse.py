#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionPayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionPayQueryResponse, self).__init__()
        self._amount = None
        self._currency = None
        self._out_flow_id = None
        self._out_order_no = None
        self._pay_status = None
        self._pay_title = None
        self._payee_participant_info = None
        self._payer_participant_info = None
        self._remark = None
        self._trade_no = None

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
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_title(self):
        return self._pay_title

    @pay_title.setter
    def pay_title(self, value):
        self._pay_title = value
    @property
    def payee_participant_info(self):
        return self._payee_participant_info

    @payee_participant_info.setter
    def payee_participant_info(self, value):
        self._payee_participant_info = value
    @property
    def payer_participant_info(self):
        return self._payer_participant_info

    @payer_participant_info.setter
    def payer_participant_info(self, value):
        self._payer_participant_info = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionPayQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'currency' in response:
            self.currency = response['currency']
        if 'out_flow_id' in response:
            self.out_flow_id = response['out_flow_id']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'pay_status' in response:
            self.pay_status = response['pay_status']
        if 'pay_title' in response:
            self.pay_title = response['pay_title']
        if 'payee_participant_info' in response:
            self.payee_participant_info = response['payee_participant_info']
        if 'payer_participant_info' in response:
            self.payer_participant_info = response['payer_participant_info']
        if 'remark' in response:
            self.remark = response['remark']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
