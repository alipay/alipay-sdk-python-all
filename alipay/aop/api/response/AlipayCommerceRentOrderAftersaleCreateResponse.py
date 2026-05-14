#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AftersalePayItemVO import AftersalePayItemVO
from alipay.aop.api.domain.AftersaleRefundItemVO import AftersaleRefundItemVO


class AlipayCommerceRentOrderAftersaleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentOrderAftersaleCreateResponse, self).__init__()
        self._aftersale_id = None
        self._out_aftersale_id = None
        self._pay_items = None
        self._refund_items = None

    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def out_aftersale_id(self):
        return self._out_aftersale_id

    @out_aftersale_id.setter
    def out_aftersale_id(self, value):
        self._out_aftersale_id = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentOrderAftersaleCreateResponse, self).parse_response_content(response_content)
        if 'aftersale_id' in response:
            self.aftersale_id = response['aftersale_id']
        if 'out_aftersale_id' in response:
            self.out_aftersale_id = response['out_aftersale_id']
        if 'pay_items' in response:
            self.pay_items = response['pay_items']
        if 'refund_items' in response:
            self.refund_items = response['refund_items']
