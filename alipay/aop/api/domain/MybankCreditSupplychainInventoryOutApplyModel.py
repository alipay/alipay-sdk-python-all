#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InventoryInfo import InventoryInfo
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainInventoryOutApplyModel(object):

    def __init__(self):
        self._ar_no = None
        self._asset_info_list = None
        self._customer = None
        self._out_order_no = None
        self._request_id = None
        self._sale_pd_code = None
        self._trade_type = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def asset_info_list(self):
        return self._asset_info_list

    @asset_info_list.setter
    def asset_info_list(self, value):
        if isinstance(value, list):
            self._asset_info_list = list()
            for i in value:
                if isinstance(i, InventoryInfo):
                    self._asset_info_list.append(i)
                else:
                    self._asset_info_list.append(InventoryInfo.from_alipay_dict(i))
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Member):
            self._customer = value
        else:
            self._customer = Member.from_alipay_dict(value)
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.asset_info_list:
            if isinstance(self.asset_info_list, list):
                for i in range(0, len(self.asset_info_list)):
                    element = self.asset_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_info_list[i] = element.to_alipay_dict()
            if hasattr(self.asset_info_list, 'to_alipay_dict'):
                params['asset_info_list'] = self.asset_info_list.to_alipay_dict()
            else:
                params['asset_info_list'] = self.asset_info_list
        if self.customer:
            if hasattr(self.customer, 'to_alipay_dict'):
                params['customer'] = self.customer.to_alipay_dict()
            else:
                params['customer'] = self.customer
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sale_pd_code:
            if hasattr(self.sale_pd_code, 'to_alipay_dict'):
                params['sale_pd_code'] = self.sale_pd_code.to_alipay_dict()
            else:
                params['sale_pd_code'] = self.sale_pd_code
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainInventoryOutApplyModel()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'asset_info_list' in d:
            o.asset_info_list = d['asset_info_list']
        if 'customer' in d:
            o.customer = d['customer']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


