#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCouponOperationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCouponOperationQueryResponse, self).__init__()
        self._amount = None
        self._auth_no = None
        self._extra_param = None
        self._gmt_create = None
        self._gmt_trans = None
        self._operation_id = None
        self._operation_type = None
        self._order_title = None
        self._out_order_no = None
        self._out_request_no = None
        self._payee_logon_id = None
        self._payee_user_id = None
        self._payer_logon_id = None
        self._payer_user_id = None
        self._remark = None
        self._status = None
        self._total_pay_refund_amount = None

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
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
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
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
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
    def payee_logon_id(self):
        return self._payee_logon_id

    @payee_logon_id.setter
    def payee_logon_id(self, value):
        self._payee_logon_id = value
    @property
    def payee_user_id(self):
        return self._payee_user_id

    @payee_user_id.setter
    def payee_user_id(self, value):
        self._payee_user_id = value
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
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_pay_refund_amount(self):
        return self._total_pay_refund_amount

    @total_pay_refund_amount.setter
    def total_pay_refund_amount(self, value):
        self._total_pay_refund_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCouponOperationQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'auth_no' in response:
            self.auth_no = response['auth_no']
        if 'extra_param' in response:
            self.extra_param = response['extra_param']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_trans' in response:
            self.gmt_trans = response['gmt_trans']
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'operation_type' in response:
            self.operation_type = response['operation_type']
        if 'order_title' in response:
            self.order_title = response['order_title']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'payee_logon_id' in response:
            self.payee_logon_id = response['payee_logon_id']
        if 'payee_user_id' in response:
            self.payee_user_id = response['payee_user_id']
        if 'payer_logon_id' in response:
            self.payer_logon_id = response['payer_logon_id']
        if 'payer_user_id' in response:
            self.payer_user_id = response['payer_user_id']
        if 'remark' in response:
            self.remark = response['remark']
        if 'status' in response:
            self.status = response['status']
        if 'total_pay_refund_amount' in response:
            self.total_pay_refund_amount = response['total_pay_refund_amount']
