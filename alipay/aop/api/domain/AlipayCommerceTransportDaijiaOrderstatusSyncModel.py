#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderBillReq import OrderBillReq
from alipay.aop.api.domain.DesignatedDriverInfo import DesignatedDriverInfo


class AlipayCommerceTransportDaijiaOrderstatusSyncModel(object):

    def __init__(self):
        self._bill = None
        self._driver_info = None
        self._open_id = None
        self._order_category = None
        self._order_id = None
        self._order_status = None
        self._order_supply_name = None
        self._out_order_no = None
        self._user_id = None

    @property
    def bill(self):
        return self._bill

    @bill.setter
    def bill(self, value):
        if isinstance(value, OrderBillReq):
            self._bill = value
        else:
            self._bill = OrderBillReq.from_alipay_dict(value)
    @property
    def driver_info(self):
        return self._driver_info

    @driver_info.setter
    def driver_info(self, value):
        if isinstance(value, DesignatedDriverInfo):
            self._driver_info = value
        else:
            self._driver_info = DesignatedDriverInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_category(self):
        return self._order_category

    @order_category.setter
    def order_category(self, value):
        self._order_category = value
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
    def order_supply_name(self):
        return self._order_supply_name

    @order_supply_name.setter
    def order_supply_name(self, value):
        self._order_supply_name = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill:
            if hasattr(self.bill, 'to_alipay_dict'):
                params['bill'] = self.bill.to_alipay_dict()
            else:
                params['bill'] = self.bill
        if self.driver_info:
            if hasattr(self.driver_info, 'to_alipay_dict'):
                params['driver_info'] = self.driver_info.to_alipay_dict()
            else:
                params['driver_info'] = self.driver_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_category:
            if hasattr(self.order_category, 'to_alipay_dict'):
                params['order_category'] = self.order_category.to_alipay_dict()
            else:
                params['order_category'] = self.order_category
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
        if self.order_supply_name:
            if hasattr(self.order_supply_name, 'to_alipay_dict'):
                params['order_supply_name'] = self.order_supply_name.to_alipay_dict()
            else:
                params['order_supply_name'] = self.order_supply_name
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportDaijiaOrderstatusSyncModel()
        if 'bill' in d:
            o.bill = d['bill']
        if 'driver_info' in d:
            o.driver_info = d['driver_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_category' in d:
            o.order_category = d['order_category']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_supply_name' in d:
            o.order_supply_name = d['order_supply_name']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


