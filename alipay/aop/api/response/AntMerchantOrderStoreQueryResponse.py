#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderExt import OrderExt
from alipay.aop.api.domain.StoreOrderGood import StoreOrderGood


class AntMerchantOrderStoreQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantOrderStoreQueryResponse, self).__init__()
        self._buyer_id = None
        self._contact_phone = None
        self._ext = None
        self._goods_info_list = None
        self._memo = None
        self._order_id = None
        self._out_biz_no = None
        self._seller_id = None
        self._user_name = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        if isinstance(value, list):
            self._ext = list()
            for i in value:
                if isinstance(i, OrderExt):
                    self._ext.append(i)
                else:
                    self._ext.append(OrderExt.from_alipay_dict(i))
    @property
    def goods_info_list(self):
        return self._goods_info_list

    @goods_info_list.setter
    def goods_info_list(self, value):
        if isinstance(value, list):
            self._goods_info_list = list()
            for i in value:
                if isinstance(i, StoreOrderGood):
                    self._goods_info_list.append(i)
                else:
                    self._goods_info_list.append(StoreOrderGood.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
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
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantOrderStoreQueryResponse, self).parse_response_content(response_content)
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'contact_phone' in response:
            self.contact_phone = response['contact_phone']
        if 'ext' in response:
            self.ext = response['ext']
        if 'goods_info_list' in response:
            self.goods_info_list = response['goods_info_list']
        if 'memo' in response:
            self.memo = response['memo']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
