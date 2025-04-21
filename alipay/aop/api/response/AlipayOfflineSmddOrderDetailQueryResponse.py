#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemOrderBean import ItemOrderBean
from alipay.aop.api.domain.RequireBean import RequireBean


class AlipayOfflineSmddOrderDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddOrderDetailQueryResponse, self).__init__()
        self._claim_code = None
        self._create_time = None
        self._item_order_list = None
        self._memo = None
        self._order_id = None
        self._order_status = None
        self._order_status_desc = None
        self._order_timeout = None
        self._out_biz_type = None
        self._real_price = None
        self._require_info_list = None
        self._shop_id = None
        self._table_no = None
        self._timeout_stamp = None
        self._total_price = None
        self._trade_no = None

    @property
    def claim_code(self):
        return self._claim_code

    @claim_code.setter
    def claim_code(self, value):
        self._claim_code = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def item_order_list(self):
        return self._item_order_list

    @item_order_list.setter
    def item_order_list(self, value):
        if isinstance(value, list):
            self._item_order_list = list()
            for i in value:
                if isinstance(i, ItemOrderBean):
                    self._item_order_list.append(i)
                else:
                    self._item_order_list.append(ItemOrderBean.from_alipay_dict(i))
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
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_status_desc(self):
        return self._order_status_desc

    @order_status_desc.setter
    def order_status_desc(self, value):
        self._order_status_desc = value
    @property
    def order_timeout(self):
        return self._order_timeout

    @order_timeout.setter
    def order_timeout(self, value):
        self._order_timeout = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def real_price(self):
        return self._real_price

    @real_price.setter
    def real_price(self, value):
        self._real_price = value
    @property
    def require_info_list(self):
        return self._require_info_list

    @require_info_list.setter
    def require_info_list(self, value):
        if isinstance(value, list):
            self._require_info_list = list()
            for i in value:
                if isinstance(i, RequireBean):
                    self._require_info_list.append(i)
                else:
                    self._require_info_list.append(RequireBean.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def table_no(self):
        return self._table_no

    @table_no.setter
    def table_no(self, value):
        self._table_no = value
    @property
    def timeout_stamp(self):
        return self._timeout_stamp

    @timeout_stamp.setter
    def timeout_stamp(self, value):
        self._timeout_stamp = value
    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddOrderDetailQueryResponse, self).parse_response_content(response_content)
        if 'claim_code' in response:
            self.claim_code = response['claim_code']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'item_order_list' in response:
            self.item_order_list = response['item_order_list']
        if 'memo' in response:
            self.memo = response['memo']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_status_desc' in response:
            self.order_status_desc = response['order_status_desc']
        if 'order_timeout' in response:
            self.order_timeout = response['order_timeout']
        if 'out_biz_type' in response:
            self.out_biz_type = response['out_biz_type']
        if 'real_price' in response:
            self.real_price = response['real_price']
        if 'require_info_list' in response:
            self.require_info_list = response['require_info_list']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'table_no' in response:
            self.table_no = response['table_no']
        if 'timeout_stamp' in response:
            self.timeout_stamp = response['timeout_stamp']
        if 'total_price' in response:
            self.total_price = response['total_price']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
