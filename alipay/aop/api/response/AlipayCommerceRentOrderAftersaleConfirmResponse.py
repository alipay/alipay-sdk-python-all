#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AftersalePayItemVO import AftersalePayItemVO
from alipay.aop.api.domain.AftersaleRefundItemVO import AftersaleRefundItemVO


class AlipayCommerceRentOrderAftersaleConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentOrderAftersaleConfirmResponse, self).__init__()
        self._pay_items = None
        self._refund_items = None
        self._trade_no = None

    @property
    def pay_items(self):
        return self._pay_items

    @pay_items.setter
    def pay_items(self, value):
        if isinstance(value, list):
            self._pay_items = list()
            for i in value:
                if isinstance(i, AftersalePayItemVO):
                    self._pay_items.append(i)
                else:
                    self._pay_items.append(AftersalePayItemVO.from_alipay_dict(i))
    @property
    def refund_items(self):
        return self._refund_items

    @refund_items.setter
    def refund_items(self, value):
        if isinstance(value, list):
            self._refund_items = list()
            for i in value:
                if isinstance(i, AftersaleRefundItemVO):
                    self._refund_items.append(i)
                else:
                    self._refund_items.append(AftersaleRefundItemVO.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentOrderAftersaleConfirmResponse, self).parse_response_content(response_content)
        if 'pay_items' in response:
            self.pay_items = response['pay_items']
        if 'refund_items' in response:
            self.refund_items = response['refund_items']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
