#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KoubeiItemDescription import KoubeiItemDescription
from alipay.aop.api.domain.KoubeiOperationContext import KoubeiOperationContext
from alipay.aop.api.domain.KoubeiTradeVoucherItemTemplete import KoubeiTradeVoucherItemTemplete


class KoubeiItemModifyModel(object):

    def __init__(self):
        self._auth_code = None
        self._category_id = None
        self._cover = None
        self._descriptions = None
        self._gmt_end = None
        self._gmt_start = None
        self._inventory = None
        self._item_detail_url = None
        self._item_id = None
        self._memo = None
        self._operation_context = None
        self._original_price = None
        self._picture_details = None
        self._price = None
        self._request_id = None
        self._shop_ids = None
        self._subject = None
        self._tb_cover = None
        self._trade_voucher_item_template = None
        self._weight = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def descriptions(self):
        return self._descriptions

    @descriptions.setter
    def descriptions(self, value):
        if isinstance(value, list):
            self._descriptions = list()
            for i in value:
                if isinstance(i, KoubeiItemDescription):
                    self._descriptions.append(i)
                else:
                    self._descriptions.append(KoubeiItemDescription.from_alipay_dict(i))
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def item_detail_url(self):
        return self._item_detail_url

    @item_detail_url.setter
    def item_detail_url(self, value):
        self._item_detail_url = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operation_context(self):
        return self._operation_context

    @operation_context.setter
    def operation_context(self, value):
        if isinstance(value, KoubeiOperationContext):
            self._operation_context = value
        else:
            self._operation_context = KoubeiOperationContext.from_alipay_dict(value)
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def picture_details(self):
        return self._picture_details

    @picture_details.setter
    def picture_details(self, value):
        self._picture_details = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        self._shop_ids = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def tb_cover(self):
        return self._tb_cover

    @tb_cover.setter
    def tb_cover(self, value):
        self._tb_cover = value
    @property
    def trade_voucher_item_template(self):
        return self._trade_voucher_item_template

    @trade_voucher_item_template.setter
    def trade_voucher_item_template(self, value):
        if isinstance(value, KoubeiTradeVoucherItemTemplete):
            self._trade_voucher_item_template = value
        else:
            self._trade_voucher_item_template = KoubeiTradeVoucherItemTemplete.from_alipay_dict(value)
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.descriptions:
            if isinstance(self.descriptions, list):
                for i in range(0, len(self.descriptions)):
                    element = self.descriptions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.descriptions[i] = element.to_alipay_dict()
            if hasattr(self.descriptions, 'to_alipay_dict'):
                params['descriptions'] = self.descriptions.to_alipay_dict()
            else:
                params['descriptions'] = self.descriptions
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.item_detail_url:
            if hasattr(self.item_detail_url, 'to_alipay_dict'):
                params['item_detail_url'] = self.item_detail_url.to_alipay_dict()
            else:
                params['item_detail_url'] = self.item_detail_url
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operation_context:
            if hasattr(self.operation_context, 'to_alipay_dict'):
                params['operation_context'] = self.operation_context.to_alipay_dict()
            else:
                params['operation_context'] = self.operation_context
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.picture_details:
            if hasattr(self.picture_details, 'to_alipay_dict'):
                params['picture_details'] = self.picture_details.to_alipay_dict()
            else:
                params['picture_details'] = self.picture_details
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.shop_ids:
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.tb_cover:
            if hasattr(self.tb_cover, 'to_alipay_dict'):
                params['tb_cover'] = self.tb_cover.to_alipay_dict()
            else:
                params['tb_cover'] = self.tb_cover
        if self.trade_voucher_item_template:
            if hasattr(self.trade_voucher_item_template, 'to_alipay_dict'):
                params['trade_voucher_item_template'] = self.trade_voucher_item_template.to_alipay_dict()
            else:
                params['trade_voucher_item_template'] = self.trade_voucher_item_template
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiItemModifyModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'cover' in d:
            o.cover = d['cover']
        if 'descriptions' in d:
            o.descriptions = d['descriptions']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'item_detail_url' in d:
            o.item_detail_url = d['item_detail_url']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operation_context' in d:
            o.operation_context = d['operation_context']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'picture_details' in d:
            o.picture_details = d['picture_details']
        if 'price' in d:
            o.price = d['price']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        if 'subject' in d:
            o.subject = d['subject']
        if 'tb_cover' in d:
            o.tb_cover = d['tb_cover']
        if 'trade_voucher_item_template' in d:
            o.trade_voucher_item_template = d['trade_voucher_item_template']
        if 'weight' in d:
            o.weight = d['weight']
        return o


