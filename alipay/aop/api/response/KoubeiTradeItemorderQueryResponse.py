#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemOrderVO import ItemOrderVO


class KoubeiTradeItemorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeItemorderQueryResponse, self).__init__()
        self._biz_product = None
        self._buyer_id = None
        self._deliver_seller_real_amount = None
        self._discount_amount = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_payment = None
        self._item_order_vo = None
        self._order_no = None
        self._out_order_no = None
        self._partner_id = None
        self._real_pay_amount = None
        self._seller_id = None
        self._status = None
        self._total_amount = None
        self._trade_no = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def deliver_seller_real_amount(self):
        return self._deliver_seller_real_amount

    @deliver_seller_real_amount.setter
    def deliver_seller_real_amount(self, value):
        self._deliver_seller_real_amount = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def item_order_vo(self):
        return self._item_order_vo

    @item_order_vo.setter
    def item_order_vo(self, value):
        if isinstance(value, list):
            self._item_order_vo = list()
            for i in value:
                if isinstance(i, ItemOrderVO):
                    self._item_order_vo.append(i)
                else:
                    self._item_order_vo.append(ItemOrderVO.from_alipay_dict(i))
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def real_pay_amount(self):
        return self._real_pay_amount

    @real_pay_amount.setter
    def real_pay_amount(self, value):
        self._real_pay_amount = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeItemorderQueryResponse, self).parse_response_content(response_content)
        if 'biz_product' in response:
            self.biz_product = response['biz_product']
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'deliver_seller_real_amount' in response:
            self.deliver_seller_real_amount = response['deliver_seller_real_amount']
        if 'discount_amount' in response:
            self.discount_amount = response['discount_amount']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'item_order_vo' in response:
            self.item_order_vo = response['item_order_vo']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'real_pay_amount' in response:
            self.real_pay_amount = response['real_pay_amount']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'status' in response:
            self.status = response['status']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
