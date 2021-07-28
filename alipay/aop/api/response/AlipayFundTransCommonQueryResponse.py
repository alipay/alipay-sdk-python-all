#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransCommonQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransCommonQueryResponse, self).__init__()
        self._arrival_time_end = None
        self._deduct_bill_info = None
        self._error_code = None
        self._fail_reason = None
        self._order_fee = None
        self._order_id = None
        self._out_biz_no = None
        self._passback_params = None
        self._pay_date = None
        self._pay_fund_order_id = None
        self._status = None
        self._trans_amount = None
        self._transfer_bill_info = None

    @property
    def arrival_time_end(self):
        return self._arrival_time_end

    @arrival_time_end.setter
    def arrival_time_end(self, value):
        self._arrival_time_end = value
    @property
    def deduct_bill_info(self):
        return self._deduct_bill_info

    @deduct_bill_info.setter
    def deduct_bill_info(self, value):
        self._deduct_bill_info = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def order_fee(self):
        return self._order_fee

    @order_fee.setter
    def order_fee(self, value):
        self._order_fee = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def passback_params(self):
        return self._passback_params

    @passback_params.setter
    def passback_params(self, value):
        self._passback_params = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def pay_fund_order_id(self):
        return self._pay_fund_order_id

    @pay_fund_order_id.setter
    def pay_fund_order_id(self, value):
        self._pay_fund_order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def transfer_bill_info(self):
        return self._transfer_bill_info

    @transfer_bill_info.setter
    def transfer_bill_info(self, value):
        self._transfer_bill_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransCommonQueryResponse, self).parse_response_content(response_content)
        if 'arrival_time_end' in response:
            self.arrival_time_end = response['arrival_time_end']
        if 'deduct_bill_info' in response:
            self.deduct_bill_info = response['deduct_bill_info']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'order_fee' in response:
            self.order_fee = response['order_fee']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'passback_params' in response:
            self.passback_params = response['passback_params']
        if 'pay_date' in response:
            self.pay_date = response['pay_date']
        if 'pay_fund_order_id' in response:
            self.pay_fund_order_id = response['pay_fund_order_id']
        if 'status' in response:
            self.status = response['status']
        if 'trans_amount' in response:
            self.trans_amount = response['trans_amount']
        if 'transfer_bill_info' in response:
            self.transfer_bill_info = response['transfer_bill_info']
