#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceOrderDTO(object):

    def __init__(self):
        self._article_code = None
        self._article_fee = None
        self._article_id = None
        self._article_name = None
        self._buy_date = None
        self._ext_json = None
        self._fact_total_fee = None
        self._item_code = None
        self._item_id = None
        self._item_name = None
        self._order_id = None
        self._order_type = None

    @property
    def article_code(self):
        return self._article_code

    @article_code.setter
    def article_code(self, value):
        self._article_code = value
    @property
    def article_fee(self):
        return self._article_fee

    @article_fee.setter
    def article_fee(self, value):
        self._article_fee = value
    @property
    def article_id(self):
        return self._article_id

    @article_id.setter
    def article_id(self, value):
        self._article_id = value
    @property
    def article_name(self):
        return self._article_name

    @article_name.setter
    def article_name(self, value):
        self._article_name = value
    @property
    def buy_date(self):
        return self._buy_date

    @buy_date.setter
    def buy_date(self, value):
        self._buy_date = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def fact_total_fee(self):
        return self._fact_total_fee

    @fact_total_fee.setter
    def fact_total_fee(self, value):
        self._fact_total_fee = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.article_code:
            if hasattr(self.article_code, 'to_alipay_dict'):
                params['article_code'] = self.article_code.to_alipay_dict()
            else:
                params['article_code'] = self.article_code
        if self.article_fee:
            if hasattr(self.article_fee, 'to_alipay_dict'):
                params['article_fee'] = self.article_fee.to_alipay_dict()
            else:
                params['article_fee'] = self.article_fee
        if self.article_id:
            if hasattr(self.article_id, 'to_alipay_dict'):
                params['article_id'] = self.article_id.to_alipay_dict()
            else:
                params['article_id'] = self.article_id
        if self.article_name:
            if hasattr(self.article_name, 'to_alipay_dict'):
                params['article_name'] = self.article_name.to_alipay_dict()
            else:
                params['article_name'] = self.article_name
        if self.buy_date:
            if hasattr(self.buy_date, 'to_alipay_dict'):
                params['buy_date'] = self.buy_date.to_alipay_dict()
            else:
                params['buy_date'] = self.buy_date
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
        if self.fact_total_fee:
            if hasattr(self.fact_total_fee, 'to_alipay_dict'):
                params['fact_total_fee'] = self.fact_total_fee.to_alipay_dict()
            else:
                params['fact_total_fee'] = self.fact_total_fee
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceOrderDTO()
        if 'article_code' in d:
            o.article_code = d['article_code']
        if 'article_fee' in d:
            o.article_fee = d['article_fee']
        if 'article_id' in d:
            o.article_id = d['article_id']
        if 'article_name' in d:
            o.article_name = d['article_name']
        if 'buy_date' in d:
            o.buy_date = d['buy_date']
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'fact_total_fee' in d:
            o.fact_total_fee = d['fact_total_fee']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        return o


