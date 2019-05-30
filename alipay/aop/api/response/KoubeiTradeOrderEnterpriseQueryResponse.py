#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeOrderEnterpriseQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeOrderEnterpriseQueryResponse, self).__init__()
        self._buyer_user_id = None
        self._ext_info = None
        self._merchant_subsidy_amount = None
        self._order_no = None
        self._order_product = None
        self._out_order_no = None
        self._partner_id = None
        self._real_amount = None
        self._seller_id = None
        self._shop_id = None
        self._status = None
        self._subject = None
        self._subsidy_amount = None
        self._total_amount = None

    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_subsidy_amount(self):
        return self._merchant_subsidy_amount

    @merchant_subsidy_amount.setter
    def merchant_subsidy_amount(self, value):
        self._merchant_subsidy_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_product(self):
        return self._order_product

    @order_product.setter
    def order_product(self, value):
        self._order_product = value
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
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def subsidy_amount(self):
        return self._subsidy_amount

    @subsidy_amount.setter
    def subsidy_amount(self, value):
        self._subsidy_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeOrderEnterpriseQueryResponse, self).parse_response_content(response_content)
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'merchant_subsidy_amount' in response:
            self.merchant_subsidy_amount = response['merchant_subsidy_amount']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_product' in response:
            self.order_product = response['order_product']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'real_amount' in response:
            self.real_amount = response['real_amount']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'status' in response:
            self.status = response['status']
        if 'subject' in response:
            self.subject = response['subject']
        if 'subsidy_amount' in response:
            self.subsidy_amount = response['subsidy_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
