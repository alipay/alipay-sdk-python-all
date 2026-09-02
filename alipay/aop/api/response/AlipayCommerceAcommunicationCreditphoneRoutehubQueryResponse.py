#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RefundQueryResult import RefundQueryResult
from alipay.aop.api.domain.SignQueryResult import SignQueryResult
from alipay.aop.api.domain.TransferQueryResult import TransferQueryResult
from alipay.aop.api.domain.UnbindQueryResult import UnbindQueryResult


class AlipayCommerceAcommunicationCreditphoneRoutehubQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphoneRoutehubQueryResponse, self).__init__()
        self._alipay_order_no = None
        self._order_no = None
        self._query_type = None
        self._refund_query_result = None
        self._sign_query_result = None
        self._transfer_query_result = None
        self._unbind_query_result = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def refund_query_result(self):
        return self._refund_query_result

    @refund_query_result.setter
    def refund_query_result(self, value):
        if isinstance(value, RefundQueryResult):
            self._refund_query_result = value
        else:
            self._refund_query_result = RefundQueryResult.from_alipay_dict(value)
    @property
    def sign_query_result(self):
        return self._sign_query_result

    @sign_query_result.setter
    def sign_query_result(self, value):
        if isinstance(value, SignQueryResult):
            self._sign_query_result = value
        else:
            self._sign_query_result = SignQueryResult.from_alipay_dict(value)
    @property
    def transfer_query_result(self):
        return self._transfer_query_result

    @transfer_query_result.setter
    def transfer_query_result(self, value):
        if isinstance(value, TransferQueryResult):
            self._transfer_query_result = value
        else:
            self._transfer_query_result = TransferQueryResult.from_alipay_dict(value)
    @property
    def unbind_query_result(self):
        return self._unbind_query_result

    @unbind_query_result.setter
    def unbind_query_result(self, value):
        if isinstance(value, UnbindQueryResult):
            self._unbind_query_result = value
        else:
            self._unbind_query_result = UnbindQueryResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphoneRoutehubQueryResponse, self).parse_response_content(response_content)
        if 'alipay_order_no' in response:
            self.alipay_order_no = response['alipay_order_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'query_type' in response:
            self.query_type = response['query_type']
        if 'refund_query_result' in response:
            self.refund_query_result = response['refund_query_result']
        if 'sign_query_result' in response:
            self.sign_query_result = response['sign_query_result']
        if 'transfer_query_result' in response:
            self.transfer_query_result = response['transfer_query_result']
        if 'unbind_query_result' in response:
            self.unbind_query_result = response['unbind_query_result']
