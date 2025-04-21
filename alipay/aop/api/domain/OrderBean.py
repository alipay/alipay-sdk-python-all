#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityBean import ActivityBean
from alipay.aop.api.domain.CodeExtBean import CodeExtBean
from alipay.aop.api.domain.ItemOrderBean import ItemOrderBean
from alipay.aop.api.domain.RequireBean import RequireBean


class OrderBean(object):

    def __init__(self):
        self._activity_list = None
        self._claim_code = None
        self._code_ext = None
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
    def activity_list(self):
        return self._activity_list

    @activity_list.setter
    def activity_list(self, value):
        if isinstance(value, list):
            self._activity_list = list()
            for i in value:
                if isinstance(i, ActivityBean):
                    self._activity_list.append(i)
                else:
                    self._activity_list.append(ActivityBean.from_alipay_dict(i))
    @property
    def claim_code(self):
        return self._claim_code

    @claim_code.setter
    def claim_code(self, value):
        self._claim_code = value
    @property
    def code_ext(self):
        return self._code_ext

    @code_ext.setter
    def code_ext(self, value):
        if isinstance(value, CodeExtBean):
            self._code_ext = value
        else:
            self._code_ext = CodeExtBean.from_alipay_dict(value)
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


    def to_alipay_dict(self):
        params = dict()
        if self.activity_list:
            if isinstance(self.activity_list, list):
                for i in range(0, len(self.activity_list)):
                    element = self.activity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_list, 'to_alipay_dict'):
                params['activity_list'] = self.activity_list.to_alipay_dict()
            else:
                params['activity_list'] = self.activity_list
        if self.claim_code:
            if hasattr(self.claim_code, 'to_alipay_dict'):
                params['claim_code'] = self.claim_code.to_alipay_dict()
            else:
                params['claim_code'] = self.claim_code
        if self.code_ext:
            if hasattr(self.code_ext, 'to_alipay_dict'):
                params['code_ext'] = self.code_ext.to_alipay_dict()
            else:
                params['code_ext'] = self.code_ext
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.item_order_list:
            if isinstance(self.item_order_list, list):
                for i in range(0, len(self.item_order_list)):
                    element = self.item_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_order_list[i] = element.to_alipay_dict()
            if hasattr(self.item_order_list, 'to_alipay_dict'):
                params['item_order_list'] = self.item_order_list.to_alipay_dict()
            else:
                params['item_order_list'] = self.item_order_list
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_status_desc:
            if hasattr(self.order_status_desc, 'to_alipay_dict'):
                params['order_status_desc'] = self.order_status_desc.to_alipay_dict()
            else:
                params['order_status_desc'] = self.order_status_desc
        if self.order_timeout:
            if hasattr(self.order_timeout, 'to_alipay_dict'):
                params['order_timeout'] = self.order_timeout.to_alipay_dict()
            else:
                params['order_timeout'] = self.order_timeout
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.real_price:
            if hasattr(self.real_price, 'to_alipay_dict'):
                params['real_price'] = self.real_price.to_alipay_dict()
            else:
                params['real_price'] = self.real_price
        if self.require_info_list:
            if isinstance(self.require_info_list, list):
                for i in range(0, len(self.require_info_list)):
                    element = self.require_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.require_info_list[i] = element.to_alipay_dict()
            if hasattr(self.require_info_list, 'to_alipay_dict'):
                params['require_info_list'] = self.require_info_list.to_alipay_dict()
            else:
                params['require_info_list'] = self.require_info_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.table_no:
            if hasattr(self.table_no, 'to_alipay_dict'):
                params['table_no'] = self.table_no.to_alipay_dict()
            else:
                params['table_no'] = self.table_no
        if self.timeout_stamp:
            if hasattr(self.timeout_stamp, 'to_alipay_dict'):
                params['timeout_stamp'] = self.timeout_stamp.to_alipay_dict()
            else:
                params['timeout_stamp'] = self.timeout_stamp
        if self.total_price:
            if hasattr(self.total_price, 'to_alipay_dict'):
                params['total_price'] = self.total_price.to_alipay_dict()
            else:
                params['total_price'] = self.total_price
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderBean()
        if 'activity_list' in d:
            o.activity_list = d['activity_list']
        if 'claim_code' in d:
            o.claim_code = d['claim_code']
        if 'code_ext' in d:
            o.code_ext = d['code_ext']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'item_order_list' in d:
            o.item_order_list = d['item_order_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_status_desc' in d:
            o.order_status_desc = d['order_status_desc']
        if 'order_timeout' in d:
            o.order_timeout = d['order_timeout']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'real_price' in d:
            o.real_price = d['real_price']
        if 'require_info_list' in d:
            o.require_info_list = d['require_info_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'table_no' in d:
            o.table_no = d['table_no']
        if 'timeout_stamp' in d:
            o.timeout_stamp = d['timeout_stamp']
        if 'total_price' in d:
            o.total_price = d['total_price']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


