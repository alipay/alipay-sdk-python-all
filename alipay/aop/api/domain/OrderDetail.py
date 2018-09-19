#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsDetail import GoodsDetail


class OrderDetail(object):

    def __init__(self):
        self._app_id = None
        self._body = None
        self._goods_detail = None
        self._out_trade_no = None
        self._passback_params = None
        self._product_code = None
        self._seller_id = None
        self._seller_logon_id = None
        self._show_url = None
        self._subject = None
        self._total_amount = None

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        self._app_id = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
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
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def passback_params(self):
        return self._passback_params

    @passback_params.setter
    def passback_params(self, value):
        self._passback_params = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_logon_id(self):
        return self._seller_logon_id

    @seller_logon_id.setter
    def seller_logon_id(self, value):
        self._seller_logon_id = value
    @property
    def show_url(self):
        return self._show_url

    @show_url.setter
    def show_url(self, value):
        self._show_url = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_id:
            if hasattr(self.app_id, 'to_alipay_dict'):
                params['app_id'] = self.app_id.to_alipay_dict()
            else:
                params['app_id'] = self.app_id
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
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
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.passback_params:
            if hasattr(self.passback_params, 'to_alipay_dict'):
                params['passback_params'] = self.passback_params.to_alipay_dict()
            else:
                params['passback_params'] = self.passback_params
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_logon_id:
            if hasattr(self.seller_logon_id, 'to_alipay_dict'):
                params['seller_logon_id'] = self.seller_logon_id.to_alipay_dict()
            else:
                params['seller_logon_id'] = self.seller_logon_id
        if self.show_url:
            if hasattr(self.show_url, 'to_alipay_dict'):
                params['show_url'] = self.show_url.to_alipay_dict()
            else:
                params['show_url'] = self.show_url
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
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
        o = OrderDetail()
        if 'app_id' in d:
            o.app_id = d['app_id']
        if 'body' in d:
            o.body = d['body']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'passback_params' in d:
            o.passback_params = d['passback_params']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_logon_id' in d:
            o.seller_logon_id = d['seller_logon_id']
        if 'show_url' in d:
            o.show_url = d['show_url']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


