#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleExtParam import SettleExtParam
from alipay.aop.api.domain.RoyaltyDetailInfoPojo import RoyaltyDetailInfoPojo


class AlipayCommerceRentZatSellerSettleModel(object):

    def __init__(self):
        self._biz_order_id = None
        self._extend_param = None
        self._operator_id = None
        self._out_request_no = None
        self._royalty_mode = None
        self._royalty_param = None
        self._trade_no = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def extend_param(self):
        return self._extend_param

    @extend_param.setter
    def extend_param(self, value):
        if isinstance(value, SettleExtParam):
            self._extend_param = value
        else:
            self._extend_param = SettleExtParam.from_alipay_dict(value)
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def royalty_mode(self):
        return self._royalty_mode

    @royalty_mode.setter
    def royalty_mode(self, value):
        self._royalty_mode = value
    @property
    def royalty_param(self):
        return self._royalty_param

    @royalty_param.setter
    def royalty_param(self, value):
        if isinstance(value, RoyaltyDetailInfoPojo):
            self._royalty_param = value
        else:
            self._royalty_param = RoyaltyDetailInfoPojo.from_alipay_dict(value)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.extend_param:
            if hasattr(self.extend_param, 'to_alipay_dict'):
                params['extend_param'] = self.extend_param.to_alipay_dict()
            else:
                params['extend_param'] = self.extend_param
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.royalty_mode:
            if hasattr(self.royalty_mode, 'to_alipay_dict'):
                params['royalty_mode'] = self.royalty_mode.to_alipay_dict()
            else:
                params['royalty_mode'] = self.royalty_mode
        if self.royalty_param:
            if hasattr(self.royalty_param, 'to_alipay_dict'):
                params['royalty_param'] = self.royalty_param.to_alipay_dict()
            else:
                params['royalty_param'] = self.royalty_param
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
        o = AlipayCommerceRentZatSellerSettleModel()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'extend_param' in d:
            o.extend_param = d['extend_param']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'royalty_mode' in d:
            o.royalty_mode = d['royalty_mode']
        if 'royalty_param' in d:
            o.royalty_param = d['royalty_param']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


