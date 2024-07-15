#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoItemConsultDetailInfo(object):

    def __init__(self):
        self._buy_restrict = None
        self._item_id = None
        self._out_item_id = None
        self._out_sku_id = None
        self._promo_amount = None
        self._promo_type = None
        self._restrict_code = None
        self._restrict_reason = None
        self._sale_promo_type = None
        self._single_consume = None
        self._sku_id = None

    @property
    def buy_restrict(self):
        return self._buy_restrict

    @buy_restrict.setter
    def buy_restrict(self, value):
        self._buy_restrict = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def promo_amount(self):
        return self._promo_amount

    @promo_amount.setter
    def promo_amount(self, value):
        self._promo_amount = value
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def restrict_code(self):
        return self._restrict_code

    @restrict_code.setter
    def restrict_code(self, value):
        self._restrict_code = value
    @property
    def restrict_reason(self):
        return self._restrict_reason

    @restrict_reason.setter
    def restrict_reason(self, value):
        self._restrict_reason = value
    @property
    def sale_promo_type(self):
        return self._sale_promo_type

    @sale_promo_type.setter
    def sale_promo_type(self, value):
        self._sale_promo_type = value
    @property
    def single_consume(self):
        return self._single_consume

    @single_consume.setter
    def single_consume(self, value):
        self._single_consume = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buy_restrict:
            if hasattr(self.buy_restrict, 'to_alipay_dict'):
                params['buy_restrict'] = self.buy_restrict.to_alipay_dict()
            else:
                params['buy_restrict'] = self.buy_restrict
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.promo_amount:
            if hasattr(self.promo_amount, 'to_alipay_dict'):
                params['promo_amount'] = self.promo_amount.to_alipay_dict()
            else:
                params['promo_amount'] = self.promo_amount
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.restrict_code:
            if hasattr(self.restrict_code, 'to_alipay_dict'):
                params['restrict_code'] = self.restrict_code.to_alipay_dict()
            else:
                params['restrict_code'] = self.restrict_code
        if self.restrict_reason:
            if hasattr(self.restrict_reason, 'to_alipay_dict'):
                params['restrict_reason'] = self.restrict_reason.to_alipay_dict()
            else:
                params['restrict_reason'] = self.restrict_reason
        if self.sale_promo_type:
            if hasattr(self.sale_promo_type, 'to_alipay_dict'):
                params['sale_promo_type'] = self.sale_promo_type.to_alipay_dict()
            else:
                params['sale_promo_type'] = self.sale_promo_type
        if self.single_consume:
            if hasattr(self.single_consume, 'to_alipay_dict'):
                params['single_consume'] = self.single_consume.to_alipay_dict()
            else:
                params['single_consume'] = self.single_consume
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoItemConsultDetailInfo()
        if 'buy_restrict' in d:
            o.buy_restrict = d['buy_restrict']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'promo_amount' in d:
            o.promo_amount = d['promo_amount']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'restrict_code' in d:
            o.restrict_code = d['restrict_code']
        if 'restrict_reason' in d:
            o.restrict_reason = d['restrict_reason']
        if 'sale_promo_type' in d:
            o.sale_promo_type = d['sale_promo_type']
        if 'single_consume' in d:
            o.single_consume = d['single_consume']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


