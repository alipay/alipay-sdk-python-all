#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpOrderRatingQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpOrderRatingQueryResponse, self).__init__()
        self._amount = None
        self._credit_level = None
        self._decision = None
        self._ext_info = None
        self._order_no = None
        self._order_status = None
        self._out_order_no = None
        self._reject_reason = None
        self._zm_score = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def credit_level(self):
        return self._credit_level

    @credit_level.setter
    def credit_level(self, value):
        self._credit_level = value
    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        self._decision = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def zm_score(self):
        return self._zm_score

    @zm_score.setter
    def zm_score(self, value):
        self._zm_score = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpOrderRatingQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'credit_level' in response:
            self.credit_level = response['credit_level']
        if 'decision' in response:
            self.decision = response['decision']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'zm_score' in response:
            self.zm_score = response['zm_score']
