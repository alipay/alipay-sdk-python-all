#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAuthOrderFreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAuthOrderFreezeResponse, self).__init__()
        self._amount = None
        self._auth_no = None
        self._credit_amount = None
        self._fund_amount = None
        self._gmt_trans = None
        self._operation_id = None
        self._out_order_no = None
        self._out_request_no = None
        self._payer_logon_id = None
        self._payer_user_id = None
        self._pre_auth_type = None
        self._status = None
        self._trans_currency = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def credit_amount(self):
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, value):
        self._credit_amount = value
    @property
    def fund_amount(self):
        return self._fund_amount

    @fund_amount.setter
    def fund_amount(self, value):
        self._fund_amount = value
    @property
    def gmt_trans(self):
        return self._gmt_trans

    @gmt_trans.setter
    def gmt_trans(self, value):
        self._gmt_trans = value
    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def payer_logon_id(self):
        return self._payer_logon_id

    @payer_logon_id.setter
    def payer_logon_id(self, value):
        self._payer_logon_id = value
    @property
    def payer_user_id(self):
        return self._payer_user_id

    @payer_user_id.setter
    def payer_user_id(self, value):
        self._payer_user_id = value
    @property
    def pre_auth_type(self):
        return self._pre_auth_type

    @pre_auth_type.setter
    def pre_auth_type(self, value):
        self._pre_auth_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAuthOrderFreezeResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'auth_no' in response:
            self.auth_no = response['auth_no']
        if 'credit_amount' in response:
            self.credit_amount = response['credit_amount']
        if 'fund_amount' in response:
            self.fund_amount = response['fund_amount']
        if 'gmt_trans' in response:
            self.gmt_trans = response['gmt_trans']
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'payer_logon_id' in response:
            self.payer_logon_id = response['payer_logon_id']
        if 'payer_user_id' in response:
            self.payer_user_id = response['payer_user_id']
        if 'pre_auth_type' in response:
            self.pre_auth_type = response['pre_auth_type']
        if 'status' in response:
            self.status = response['status']
        if 'trans_currency' in response:
            self.trans_currency = response['trans_currency']
