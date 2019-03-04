#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemOrderOpenData import ItemOrderOpenData


class AntMerchantExpandTradeorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandTradeorderQueryResponse, self).__init__()
        self._amount = None
        self._biz_seq = None
        self._buyer_id = None
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_paid = None
        self._item_orders = None
        self._logistics_status = None
        self._memo = None
        self._merchant_subsidy_amount = None
        self._order_id = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._partner_id = None
        self._partner_subsidy_amount = None
        self._real_amount = None
        self._seller_id = None
        self._shop_id = None
        self._status = None
        self._trade_no = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_seq(self):
        return self._biz_seq

    @biz_seq.setter
    def biz_seq(self, value):
        self._biz_seq = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    def gmt_paid(self):
        return self._gmt_paid

    @gmt_paid.setter
    def gmt_paid(self, value):
        self._gmt_paid = value
    @property
    def item_orders(self):
        return self._item_orders

    @item_orders.setter
    def item_orders(self, value):
        if isinstance(value, list):
            self._item_orders = list()
            for i in value:
                if isinstance(i, ItemOrderOpenData):
                    self._item_orders.append(i)
                else:
                    self._item_orders.append(ItemOrderOpenData.from_alipay_dict(i))
    @property
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_subsidy_amount(self):
        return self._merchant_subsidy_amount

    @merchant_subsidy_amount.setter
    def merchant_subsidy_amount(self, value):
        self._merchant_subsidy_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_subsidy_amount(self):
        return self._partner_subsidy_amount

    @partner_subsidy_amount.setter
    def partner_subsidy_amount(self, value):
        self._partner_subsidy_amount = value
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
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandTradeorderQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_seq' in response:
            self.biz_seq = response['biz_seq']
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'gmt_paid' in response:
            self.gmt_paid = response['gmt_paid']
        if 'item_orders' in response:
            self.item_orders = response['item_orders']
        if 'logistics_status' in response:
            self.logistics_status = response['logistics_status']
        if 'memo' in response:
            self.memo = response['memo']
        if 'merchant_subsidy_amount' in response:
            self.merchant_subsidy_amount = response['merchant_subsidy_amount']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'out_biz_type' in response:
            self.out_biz_type = response['out_biz_type']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'partner_subsidy_amount' in response:
            self.partner_subsidy_amount = response['partner_subsidy_amount']
        if 'real_amount' in response:
            self.real_amount = response['real_amount']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'status' in response:
            self.status = response['status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'type' in response:
            self.type = response['type']
