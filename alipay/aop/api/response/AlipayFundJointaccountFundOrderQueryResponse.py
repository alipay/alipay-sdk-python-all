#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountFundOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountFundOrderQueryResponse, self).__init__()
        self._amount = None
        self._biz_date = None
        self._biz_trans_id = None
        self._error_code = None
        self._error_msg = None
        self._order_title = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_trans_id(self):
        return self._biz_trans_id

    @biz_trans_id.setter
    def biz_trans_id(self, value):
        self._biz_trans_id = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountFundOrderQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_date' in response:
            self.biz_date = response['biz_date']
        if 'biz_trans_id' in response:
            self.biz_trans_id = response['biz_trans_id']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'order_title' in response:
            self.order_title = response['order_title']
        if 'status' in response:
            self.status = response['status']
