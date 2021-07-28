#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportRailwayTradeSyncModel(object):

    def __init__(self):
        self._biz_date = None
        self._data_version = None
        self._ext_param = None
        self._order_amount = None
        self._order_total_amount = None
        self._order_total_num = None
        self._out_trade_no = None
        self._request_id = None
        self._seller_id = None
        self._trade_no = None
        self._user_id = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_total_amount(self):
        return self._order_total_amount

    @order_total_amount.setter
    def order_total_amount(self, value):
        self._order_total_amount = value
    @property
    def order_total_num(self):
        return self._order_total_num

    @order_total_num.setter
    def order_total_num(self, value):
        self._order_total_num = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_total_amount:
            if hasattr(self.order_total_amount, 'to_alipay_dict'):
                params['order_total_amount'] = self.order_total_amount.to_alipay_dict()
            else:
                params['order_total_amount'] = self.order_total_amount
        if self.order_total_num:
            if hasattr(self.order_total_num, 'to_alipay_dict'):
                params['order_total_num'] = self.order_total_num.to_alipay_dict()
            else:
                params['order_total_num'] = self.order_total_num
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AlipayCommerceTransportRailwayTradeSyncModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_total_amount' in d:
            o.order_total_amount = d['order_total_amount']
        if 'order_total_num' in d:
            o.order_total_num = d['order_total_num']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


