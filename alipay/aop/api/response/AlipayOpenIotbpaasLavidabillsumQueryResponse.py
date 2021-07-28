#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotbpaasLavidabillsumQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotbpaasLavidabillsumQueryResponse, self).__init__()
        self._mercht_disc_amt = None
        self._order_amt = None
        self._recv_amt = None
        self._recv_cnt = None
        self._refund_amt = None
        self._refund_cnt = None

    @property
    def mercht_disc_amt(self):
        return self._mercht_disc_amt

    @mercht_disc_amt.setter
    def mercht_disc_amt(self, value):
        self._mercht_disc_amt = value
    @property
    def order_amt(self):
        return self._order_amt

    @order_amt.setter
    def order_amt(self, value):
        self._order_amt = value
    @property
    def recv_amt(self):
        return self._recv_amt

    @recv_amt.setter
    def recv_amt(self, value):
        self._recv_amt = value
    @property
    def recv_cnt(self):
        return self._recv_cnt

    @recv_cnt.setter
    def recv_cnt(self, value):
        self._recv_cnt = value
    @property
    def refund_amt(self):
        return self._refund_amt

    @refund_amt.setter
    def refund_amt(self, value):
        self._refund_amt = value
    @property
    def refund_cnt(self):
        return self._refund_cnt

    @refund_cnt.setter
    def refund_cnt(self, value):
        self._refund_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotbpaasLavidabillsumQueryResponse, self).parse_response_content(response_content)
        if 'mercht_disc_amt' in response:
            self.mercht_disc_amt = response['mercht_disc_amt']
        if 'order_amt' in response:
            self.order_amt = response['order_amt']
        if 'recv_amt' in response:
            self.recv_amt = response['recv_amt']
        if 'recv_cnt' in response:
            self.recv_cnt = response['recv_cnt']
        if 'refund_amt' in response:
            self.refund_amt = response['refund_amt']
        if 'refund_cnt' in response:
            self.refund_cnt = response['refund_cnt']
