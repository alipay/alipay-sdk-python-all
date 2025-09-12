#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleSubOrderAfterSaleInfoVO import RecycleSubOrderAfterSaleInfoVO


class AlipayCommerceRecycleOrderAftersaleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleOrderAftersaleCreateResponse, self).__init__()
        self._after_sale_id = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._sub_order_after_sale_info_list = None
        self._user_id = None

    @property
    def after_sale_id(self):
        return self._after_sale_id

    @after_sale_id.setter
    def after_sale_id(self, value):
        self._after_sale_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def sub_order_after_sale_info_list(self):
        return self._sub_order_after_sale_info_list

    @sub_order_after_sale_info_list.setter
    def sub_order_after_sale_info_list(self, value):
        if isinstance(value, list):
            self._sub_order_after_sale_info_list = list()
            for i in value:
                if isinstance(i, RecycleSubOrderAfterSaleInfoVO):
                    self._sub_order_after_sale_info_list.append(i)
                else:
                    self._sub_order_after_sale_info_list.append(RecycleSubOrderAfterSaleInfoVO.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleOrderAftersaleCreateResponse, self).parse_response_content(response_content)
        if 'after_sale_id' in response:
            self.after_sale_id = response['after_sale_id']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'sub_order_after_sale_info_list' in response:
            self.sub_order_after_sale_info_list = response['sub_order_after_sale_info_list']
        if 'user_id' in response:
            self.user_id = response['user_id']
