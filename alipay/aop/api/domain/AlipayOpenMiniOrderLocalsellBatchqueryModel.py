#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderLocalsellBatchqueryModel(object):

    def __init__(self):
        self._create_end_time = None
        self._create_start_time = None
        self._item_type = None
        self._merchant_order_no = None
        self._mini_app_id = None
        self._order_id = None
        self._order_status = None
        self._page_num = None
        self._page_size = None
        self._trade_no = None

    @property
    def create_end_time(self):
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, value):
        self._create_end_time = value
    @property
    def create_start_time(self):
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, value):
        self._create_start_time = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
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
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_end_time:
            if hasattr(self.create_end_time, 'to_alipay_dict'):
                params['create_end_time'] = self.create_end_time.to_alipay_dict()
            else:
                params['create_end_time'] = self.create_end_time
        if self.create_start_time:
            if hasattr(self.create_start_time, 'to_alipay_dict'):
                params['create_start_time'] = self.create_start_time.to_alipay_dict()
            else:
                params['create_start_time'] = self.create_start_time
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
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
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
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
        o = AlipayOpenMiniOrderLocalsellBatchqueryModel()
        if 'create_end_time' in d:
            o.create_end_time = d['create_end_time']
        if 'create_start_time' in d:
            o.create_start_time = d['create_start_time']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


