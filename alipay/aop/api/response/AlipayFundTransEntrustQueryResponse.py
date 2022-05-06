#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransEntrustQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransEntrustQueryResponse, self).__init__()
        self._entrust_order_id = None
        self._fail_reason = None
        self._out_biz_no = None
        self._rest_tranfer_amount = None
        self._status = None
        self._total_deduct_amount = None
        self._trans_amount = None

    @property
    def entrust_order_id(self):
        return self._entrust_order_id

    @entrust_order_id.setter
    def entrust_order_id(self, value):
        self._entrust_order_id = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def rest_tranfer_amount(self):
        return self._rest_tranfer_amount

    @rest_tranfer_amount.setter
    def rest_tranfer_amount(self, value):
        self._rest_tranfer_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_deduct_amount(self):
        return self._total_deduct_amount

    @total_deduct_amount.setter
    def total_deduct_amount(self, value):
        self._total_deduct_amount = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransEntrustQueryResponse, self).parse_response_content(response_content)
        if 'entrust_order_id' in response:
            self.entrust_order_id = response['entrust_order_id']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'rest_tranfer_amount' in response:
            self.rest_tranfer_amount = response['rest_tranfer_amount']
        if 'status' in response:
            self.status = response['status']
        if 'total_deduct_amount' in response:
            self.total_deduct_amount = response['total_deduct_amount']
        if 'trans_amount' in response:
            self.trans_amount = response['trans_amount']
