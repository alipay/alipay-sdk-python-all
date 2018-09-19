#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemOrderDetail import ItemOrderDetail


class KoubeiTradeItemorderBuyModel(object):

    def __init__(self):
        self._biz_product = None
        self._biz_scene = None
        self._buyer_id = None
        self._item_order_details = None
        self._out_order_no = None
        self._promo_params = None
        self._shop_id = None
        self._subject = None
        self._timeout = None
        self._total_amount = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def item_order_details(self):
        return self._item_order_details

    @item_order_details.setter
    def item_order_details(self, value):
        if isinstance(value, list):
            self._item_order_details = list()
            for i in value:
                if isinstance(i, ItemOrderDetail):
                    self._item_order_details.append(i)
                else:
                    self._item_order_details.append(ItemOrderDetail.from_alipay_dict(i))
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def promo_params(self):
        return self._promo_params

    @promo_params.setter
    def promo_params(self, value):
        self._promo_params = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.item_order_details:
            if isinstance(self.item_order_details, list):
                for i in range(0, len(self.item_order_details)):
                    element = self.item_order_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_order_details[i] = element.to_alipay_dict()
            if hasattr(self.item_order_details, 'to_alipay_dict'):
                params['item_order_details'] = self.item_order_details.to_alipay_dict()
            else:
                params['item_order_details'] = self.item_order_details
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.promo_params:
            if hasattr(self.promo_params, 'to_alipay_dict'):
                params['promo_params'] = self.promo_params.to_alipay_dict()
            else:
                params['promo_params'] = self.promo_params
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.timeout:
            if hasattr(self.timeout, 'to_alipay_dict'):
                params['timeout'] = self.timeout.to_alipay_dict()
            else:
                params['timeout'] = self.timeout
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
        o = KoubeiTradeItemorderBuyModel()
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'item_order_details' in d:
            o.item_order_details = d['item_order_details']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'promo_params' in d:
            o.promo_params = d['promo_params']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'subject' in d:
            o.subject = d['subject']
        if 'timeout' in d:
            o.timeout = d['timeout']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


