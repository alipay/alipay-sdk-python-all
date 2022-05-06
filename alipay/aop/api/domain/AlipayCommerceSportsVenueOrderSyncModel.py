#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductSimpleInfo import ProductSimpleInfo
from alipay.aop.api.domain.VenueOrderTradeInfo import VenueOrderTradeInfo


class AlipayCommerceSportsVenueOrderSyncModel(object):

    def __init__(self):
        self._create_time = None
        self._order_status = None
        self._order_type = None
        self._out_order_id = None
        self._out_sub_venue_id = None
        self._out_venue_id = None
        self._product_group_list = None
        self._sub_venue_id = None
        self._total_amount = None
        self._trade_info_list = None
        self._user_id = None
        self._venue_id = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_sub_venue_id(self):
        return self._out_sub_venue_id

    @out_sub_venue_id.setter
    def out_sub_venue_id(self, value):
        self._out_sub_venue_id = value
    @property
    def out_venue_id(self):
        return self._out_venue_id

    @out_venue_id.setter
    def out_venue_id(self, value):
        self._out_venue_id = value
    @property
    def product_group_list(self):
        return self._product_group_list

    @product_group_list.setter
    def product_group_list(self, value):
        if isinstance(value, list):
            self._product_group_list = list()
            for i in value:
                if isinstance(i, ProductSimpleInfo):
                    self._product_group_list.append(i)
                else:
                    self._product_group_list.append(ProductSimpleInfo.from_alipay_dict(i))
    @property
    def sub_venue_id(self):
        return self._sub_venue_id

    @sub_venue_id.setter
    def sub_venue_id(self, value):
        self._sub_venue_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_info_list(self):
        return self._trade_info_list

    @trade_info_list.setter
    def trade_info_list(self, value):
        if isinstance(value, list):
            self._trade_info_list = list()
            for i in value:
                if isinstance(i, VenueOrderTradeInfo):
                    self._trade_info_list.append(i)
                else:
                    self._trade_info_list.append(VenueOrderTradeInfo.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def venue_id(self):
        return self._venue_id

    @venue_id.setter
    def venue_id(self, value):
        self._venue_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_sub_venue_id:
            if hasattr(self.out_sub_venue_id, 'to_alipay_dict'):
                params['out_sub_venue_id'] = self.out_sub_venue_id.to_alipay_dict()
            else:
                params['out_sub_venue_id'] = self.out_sub_venue_id
        if self.out_venue_id:
            if hasattr(self.out_venue_id, 'to_alipay_dict'):
                params['out_venue_id'] = self.out_venue_id.to_alipay_dict()
            else:
                params['out_venue_id'] = self.out_venue_id
        if self.product_group_list:
            if isinstance(self.product_group_list, list):
                for i in range(0, len(self.product_group_list)):
                    element = self.product_group_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_group_list[i] = element.to_alipay_dict()
            if hasattr(self.product_group_list, 'to_alipay_dict'):
                params['product_group_list'] = self.product_group_list.to_alipay_dict()
            else:
                params['product_group_list'] = self.product_group_list
        if self.sub_venue_id:
            if hasattr(self.sub_venue_id, 'to_alipay_dict'):
                params['sub_venue_id'] = self.sub_venue_id.to_alipay_dict()
            else:
                params['sub_venue_id'] = self.sub_venue_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_info_list:
            if isinstance(self.trade_info_list, list):
                for i in range(0, len(self.trade_info_list)):
                    element = self.trade_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_info_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_info_list, 'to_alipay_dict'):
                params['trade_info_list'] = self.trade_info_list.to_alipay_dict()
            else:
                params['trade_info_list'] = self.trade_info_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.venue_id:
            if hasattr(self.venue_id, 'to_alipay_dict'):
                params['venue_id'] = self.venue_id.to_alipay_dict()
            else:
                params['venue_id'] = self.venue_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsVenueOrderSyncModel()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_sub_venue_id' in d:
            o.out_sub_venue_id = d['out_sub_venue_id']
        if 'out_venue_id' in d:
            o.out_venue_id = d['out_venue_id']
        if 'product_group_list' in d:
            o.product_group_list = d['product_group_list']
        if 'sub_venue_id' in d:
            o.sub_venue_id = d['sub_venue_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_info_list' in d:
            o.trade_info_list = d['trade_info_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'venue_id' in d:
            o.venue_id = d['venue_id']
        return o


