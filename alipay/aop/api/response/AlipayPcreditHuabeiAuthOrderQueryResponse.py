#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAuthOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAuthOrderQueryResponse, self).__init__()
        self._agreement_no = None
        self._alipay_user_id = None
        self._auth_opt_id = None
        self._gmt_trans = None
        self._order_title = None
        self._out_request_no = None
        self._rest_freeze_amount = None
        self._seller_id = None
        self._trans_amount = None
        self._trans_status = None
        self._trans_type = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def auth_opt_id(self):
        return self._auth_opt_id

    @auth_opt_id.setter
    def auth_opt_id(self, value):
        self._auth_opt_id = value
    @property
    def gmt_trans(self):
        return self._gmt_trans

    @gmt_trans.setter
    def gmt_trans(self, value):
        self._gmt_trans = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def rest_freeze_amount(self):
        return self._rest_freeze_amount

    @rest_freeze_amount.setter
    def rest_freeze_amount(self, value):
        self._rest_freeze_amount = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def trans_status(self):
        return self._trans_status

    @trans_status.setter
    def trans_status(self, value):
        self._trans_status = value
    @property
    def trans_type(self):
        return self._trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._trans_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAuthOrderQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'auth_opt_id' in response:
            self.auth_opt_id = response['auth_opt_id']
        if 'gmt_trans' in response:
            self.gmt_trans = response['gmt_trans']
        if 'order_title' in response:
            self.order_title = response['order_title']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'rest_freeze_amount' in response:
            self.rest_freeze_amount = response['rest_freeze_amount']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'trans_amount' in response:
            self.trans_amount = response['trans_amount']
        if 'trans_status' in response:
            self.trans_status = response['trans_status']
        if 'trans_type' in response:
            self.trans_type = response['trans_type']
