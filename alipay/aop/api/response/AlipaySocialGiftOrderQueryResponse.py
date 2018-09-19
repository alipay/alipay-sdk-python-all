#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialGiftOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialGiftOrderQueryResponse, self).__init__()
        self._gift_order_status = None
        self._order_status = None
        self._quantity = None
        self._receiver_id = None
        self._sender_id = None
        self._sku_id = None
        self._total_price = None
        self._voucher_id = None

    @property
    def gift_order_status(self):
        return self._gift_order_status

    @gift_order_status.setter
    def gift_order_status(self, value):
        self._gift_order_status = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def receiver_id(self):
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, value):
        self._receiver_id = value
    @property
    def sender_id(self):
        return self._sender_id

    @sender_id.setter
    def sender_id(self, value):
        self._sender_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialGiftOrderQueryResponse, self).parse_response_content(response_content)
        if 'gift_order_status' in response:
            self.gift_order_status = response['gift_order_status']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'quantity' in response:
            self.quantity = response['quantity']
        if 'receiver_id' in response:
            self.receiver_id = response['receiver_id']
        if 'sender_id' in response:
            self.sender_id = response['sender_id']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']
        if 'total_price' in response:
            self.total_price = response['total_price']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
