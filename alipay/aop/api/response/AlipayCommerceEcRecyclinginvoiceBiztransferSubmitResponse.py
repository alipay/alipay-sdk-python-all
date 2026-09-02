#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceBiztransferSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceBiztransferSubmitResponse, self).__init__()
        self._alipay_pay_no = None
        self._biz_transfer_id = None
        self._company_account_id = None
        self._fail_code = None
        self._fail_reason = None
        self._gmt_pay = None
        self._out_biz_transfer_id = None
        self._payee_account = None
        self._payee_account_type = None
        self._payee_name = None
        self._receipt_file_id = None
        self._recycling_order_id = None
        self._transfer_biz_amount = None
        self._transfer_biz_status = None
        self._transfer_biz_type = None

    @property
    def alipay_pay_no(self):
        return self._alipay_pay_no

    @alipay_pay_no.setter
    def alipay_pay_no(self, value):
        self._alipay_pay_no = value
    @property
    def biz_transfer_id(self):
        return self._biz_transfer_id

    @biz_transfer_id.setter
    def biz_transfer_id(self, value):
        self._biz_transfer_id = value
    @property
    def company_account_id(self):
        return self._company_account_id

    @company_account_id.setter
    def company_account_id(self, value):
        self._company_account_id = value
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def out_biz_transfer_id(self):
        return self._out_biz_transfer_id

    @out_biz_transfer_id.setter
    def out_biz_transfer_id(self, value):
        self._out_biz_transfer_id = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def receipt_file_id(self):
        return self._receipt_file_id

    @receipt_file_id.setter
    def receipt_file_id(self, value):
        self._receipt_file_id = value
    @property
    def recycling_order_id(self):
        return self._recycling_order_id

    @recycling_order_id.setter
    def recycling_order_id(self, value):
        self._recycling_order_id = value
    @property
    def transfer_biz_amount(self):
        return self._transfer_biz_amount

    @transfer_biz_amount.setter
    def transfer_biz_amount(self, value):
        self._transfer_biz_amount = value
    @property
    def transfer_biz_status(self):
        return self._transfer_biz_status

    @transfer_biz_status.setter
    def transfer_biz_status(self, value):
        self._transfer_biz_status = value
    @property
    def transfer_biz_type(self):
        return self._transfer_biz_type

    @transfer_biz_type.setter
    def transfer_biz_type(self, value):
        self._transfer_biz_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceBiztransferSubmitResponse, self).parse_response_content(response_content)
        if 'alipay_pay_no' in response:
            self.alipay_pay_no = response['alipay_pay_no']
        if 'biz_transfer_id' in response:
            self.biz_transfer_id = response['biz_transfer_id']
        if 'company_account_id' in response:
            self.company_account_id = response['company_account_id']
        if 'fail_code' in response:
            self.fail_code = response['fail_code']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'gmt_pay' in response:
            self.gmt_pay = response['gmt_pay']
        if 'out_biz_transfer_id' in response:
            self.out_biz_transfer_id = response['out_biz_transfer_id']
        if 'payee_account' in response:
            self.payee_account = response['payee_account']
        if 'payee_account_type' in response:
            self.payee_account_type = response['payee_account_type']
        if 'payee_name' in response:
            self.payee_name = response['payee_name']
        if 'receipt_file_id' in response:
            self.receipt_file_id = response['receipt_file_id']
        if 'recycling_order_id' in response:
            self.recycling_order_id = response['recycling_order_id']
        if 'transfer_biz_amount' in response:
            self.transfer_biz_amount = response['transfer_biz_amount']
        if 'transfer_biz_status' in response:
            self.transfer_biz_status = response['transfer_biz_status']
        if 'transfer_biz_type' in response:
            self.transfer_biz_type = response['transfer_biz_type']
