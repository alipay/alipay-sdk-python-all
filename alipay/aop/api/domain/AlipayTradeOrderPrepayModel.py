#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessParams import BusinessParams
from alipay.aop.api.domain.ExtendParams import ExtendParams
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.RoyaltyInfo import RoyaltyInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo


class AlipayTradeOrderPrepayModel(object):

    def __init__(self):
        self._body = None
        self._business_params = None
        self._extend_params = None
        self._goods_detail = None
        self._order_scene = None
        self._out_trade_no = None
        self._product_code = None
        self._royalty_info = None
        self._seller_id = None
        self._settle_info = None
        self._subject = None
        self._time_expire = None
        self._timeout_express = None
        self._total_amount = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        if isinstance(value, BusinessParams):
            self._business_params = value
        else:
            self._business_params = BusinessParams.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, ExtendParams):
            self._extend_params = value
        else:
            self._extend_params = ExtendParams.from_alipay_dict(value)
    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        if isinstance(value, list):
            self._goods_detail = list()
            for i in value:
                if isinstance(i, GoodsDetail):
                    self._goods_detail.append(i)
                else:
                    self._goods_detail.append(GoodsDetail.from_alipay_dict(i))
    @property
    def order_scene(self):
        return self._order_scene

    @order_scene.setter
    def order_scene(self, value):
        self._order_scene = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def royalty_info(self):
        return self._royalty_info

    @royalty_info.setter
    def royalty_info(self, value):
        if isinstance(value, RoyaltyInfo):
            self._royalty_info = value
        else:
            self._royalty_info = RoyaltyInfo.from_alipay_dict(value)
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def settle_info(self):
        return self._settle_info

    @settle_info.setter
    def settle_info(self, value):
        if isinstance(value, SettleInfo):
            self._settle_info = value
        else:
            self._settle_info = SettleInfo.from_alipay_dict(value)
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.goods_detail:
            if isinstance(self.goods_detail, list):
                for i in range(0, len(self.goods_detail)):
                    element = self.goods_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_detail[i] = element.to_alipay_dict()
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        if self.order_scene:
            if hasattr(self.order_scene, 'to_alipay_dict'):
                params['order_scene'] = self.order_scene.to_alipay_dict()
            else:
                params['order_scene'] = self.order_scene
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.royalty_info:
            if hasattr(self.royalty_info, 'to_alipay_dict'):
                params['royalty_info'] = self.royalty_info.to_alipay_dict()
            else:
                params['royalty_info'] = self.royalty_info
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.settle_info:
            if hasattr(self.settle_info, 'to_alipay_dict'):
                params['settle_info'] = self.settle_info.to_alipay_dict()
            else:
                params['settle_info'] = self.settle_info
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeOrderPrepayModel()
        if 'body' in d:
            o.body = d['body']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'order_scene' in d:
            o.order_scene = d['order_scene']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'royalty_info' in d:
            o.royalty_info = d['royalty_info']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'settle_info' in d:
            o.settle_info = d['settle_info']
        if 'subject' in d:
            o.subject = d['subject']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


