#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtInfoMap import ExtInfoMap
from alipay.aop.api.domain.GoodsDetail import GoodsDetail


class AlipayTradePayinfoSyncModel(object):

    def __init__(self):
        self._buyer_open_id = None
        self._buyer_user_id = None
        self._ext_infos = None
        self._merchant_promo_status = None
        self._order_amount = None
        self._out_trade_no = None
        self._sub_goods_order_list = None

    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        if isinstance(value, ExtInfoMap):
            self._ext_infos = value
        else:
            self._ext_infos = ExtInfoMap.from_alipay_dict(value)
    @property
    def merchant_promo_status(self):
        return self._merchant_promo_status

    @merchant_promo_status.setter
    def merchant_promo_status(self, value):
        self._merchant_promo_status = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def sub_goods_order_list(self):
        return self._sub_goods_order_list

    @sub_goods_order_list.setter
    def sub_goods_order_list(self, value):
        if isinstance(value, list):
            self._sub_goods_order_list = list()
            for i in value:
                if isinstance(i, GoodsDetail):
                    self._sub_goods_order_list.append(i)
                else:
                    self._sub_goods_order_list.append(GoodsDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.buyer_user_id:
            if hasattr(self.buyer_user_id, 'to_alipay_dict'):
                params['buyer_user_id'] = self.buyer_user_id.to_alipay_dict()
            else:
                params['buyer_user_id'] = self.buyer_user_id
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.merchant_promo_status:
            if hasattr(self.merchant_promo_status, 'to_alipay_dict'):
                params['merchant_promo_status'] = self.merchant_promo_status.to_alipay_dict()
            else:
                params['merchant_promo_status'] = self.merchant_promo_status
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.sub_goods_order_list:
            if isinstance(self.sub_goods_order_list, list):
                for i in range(0, len(self.sub_goods_order_list)):
                    element = self.sub_goods_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_goods_order_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_goods_order_list, 'to_alipay_dict'):
                params['sub_goods_order_list'] = self.sub_goods_order_list.to_alipay_dict()
            else:
                params['sub_goods_order_list'] = self.sub_goods_order_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradePayinfoSyncModel()
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'merchant_promo_status' in d:
            o.merchant_promo_status = d['merchant_promo_status']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'sub_goods_order_list' in d:
            o.sub_goods_order_list = d['sub_goods_order_list']
        return o


