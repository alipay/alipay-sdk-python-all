#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionFundtransferQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionFundtransferQueryResponse, self).__init__()
        self._account_no = None
        self._amount = None
        self._biz_scene = None
        self._currency = None
        self._operate_no = None
        self._opposite_account_no = None
        self._out_flow_id = None
        self._transfer_scene = None
        self._transfer_status = None
        self._transfer_time = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def operate_no(self):
        return self._operate_no

    @operate_no.setter
    def operate_no(self, value):
        self._operate_no = value
    @property
    def opposite_account_no(self):
        return self._opposite_account_no

    @opposite_account_no.setter
    def opposite_account_no(self, value):
        self._opposite_account_no = value
    @property
    def out_flow_id(self):
        return self._out_flow_id

    @out_flow_id.setter
    def out_flow_id(self, value):
        self._out_flow_id = value
    @property
    def transfer_scene(self):
        return self._transfer_scene

    @transfer_scene.setter
    def transfer_scene(self, value):
        self._transfer_scene = value
    @property
    def transfer_status(self):
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, value):
        self._transfer_status = value
    @property
    def transfer_time(self):
        return self._transfer_time

    @transfer_time.setter
    def transfer_time(self, value):
        self._transfer_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionFundtransferQueryResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'currency' in response:
            self.currency = response['currency']
        if 'operate_no' in response:
            self.operate_no = response['operate_no']
        if 'opposite_account_no' in response:
            self.opposite_account_no = response['opposite_account_no']
        if 'out_flow_id' in response:
            self.out_flow_id = response['out_flow_id']
        if 'transfer_scene' in response:
            self.transfer_scene = response['transfer_scene']
        if 'transfer_status' in response:
            self.transfer_status = response['transfer_status']
        if 'transfer_time' in response:
            self.transfer_time = response['transfer_time']
