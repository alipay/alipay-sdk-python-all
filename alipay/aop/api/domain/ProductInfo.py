#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductBuyLimitRule import ProductBuyLimitRule
from alipay.aop.api.domain.ProductCategoryInfo import ProductCategoryInfo


class ProductInfo(object):

    def __init__(self):
        self._can_buy_rule = None
        self._can_refund = None
        self._can_refund_minute = None
        self._category_list = None
        self._desc = None
        self._end_time = None
        self._name = None
        self._notice = None
        self._origin_price = None
        self._out_product_id = None
        self._poster = None
        self._product_type = None
        self._refund_desc = None
        self._sale_price = None
        self._start_time = None
        self._stock_count = None
        self._user_name_required = None
        self._voucher_type = None
        self._voucher_verify_type = None

    @property
    def can_buy_rule(self):
        return self._can_buy_rule

    @can_buy_rule.setter
    def can_buy_rule(self, value):
        if isinstance(value, ProductBuyLimitRule):
            self._can_buy_rule = value
        else:
            self._can_buy_rule = ProductBuyLimitRule.from_alipay_dict(value)
    @property
    def can_refund(self):
        return self._can_refund

    @can_refund.setter
    def can_refund(self, value):
        self._can_refund = value
    @property
    def can_refund_minute(self):
        return self._can_refund_minute

    @can_refund_minute.setter
    def can_refund_minute(self, value):
        self._can_refund_minute = value
    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, list):
            self._category_list = list()
            for i in value:
                if isinstance(i, ProductCategoryInfo):
                    self._category_list.append(i)
                else:
                    self._category_list.append(ProductCategoryInfo.from_alipay_dict(i))
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, value):
        self._origin_price = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def poster(self):
        return self._poster

    @poster.setter
    def poster(self, value):
        self._poster = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def refund_desc(self):
        return self._refund_desc

    @refund_desc.setter
    def refund_desc(self, value):
        self._refund_desc = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def stock_count(self):
        return self._stock_count

    @stock_count.setter
    def stock_count(self, value):
        self._stock_count = value
    @property
    def user_name_required(self):
        return self._user_name_required

    @user_name_required.setter
    def user_name_required(self, value):
        self._user_name_required = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def voucher_verify_type(self):
        return self._voucher_verify_type

    @voucher_verify_type.setter
    def voucher_verify_type(self, value):
        self._voucher_verify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_buy_rule:
            if hasattr(self.can_buy_rule, 'to_alipay_dict'):
                params['can_buy_rule'] = self.can_buy_rule.to_alipay_dict()
            else:
                params['can_buy_rule'] = self.can_buy_rule
        if self.can_refund:
            if hasattr(self.can_refund, 'to_alipay_dict'):
                params['can_refund'] = self.can_refund.to_alipay_dict()
            else:
                params['can_refund'] = self.can_refund
        if self.can_refund_minute:
            if hasattr(self.can_refund_minute, 'to_alipay_dict'):
                params['can_refund_minute'] = self.can_refund_minute.to_alipay_dict()
            else:
                params['can_refund_minute'] = self.can_refund_minute
        if self.category_list:
            if isinstance(self.category_list, list):
                for i in range(0, len(self.category_list)):
                    element = self.category_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_list[i] = element.to_alipay_dict()
            if hasattr(self.category_list, 'to_alipay_dict'):
                params['category_list'] = self.category_list.to_alipay_dict()
            else:
                params['category_list'] = self.category_list
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.origin_price:
            if hasattr(self.origin_price, 'to_alipay_dict'):
                params['origin_price'] = self.origin_price.to_alipay_dict()
            else:
                params['origin_price'] = self.origin_price
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        if self.poster:
            if hasattr(self.poster, 'to_alipay_dict'):
                params['poster'] = self.poster.to_alipay_dict()
            else:
                params['poster'] = self.poster
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.refund_desc:
            if hasattr(self.refund_desc, 'to_alipay_dict'):
                params['refund_desc'] = self.refund_desc.to_alipay_dict()
            else:
                params['refund_desc'] = self.refund_desc
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.stock_count:
            if hasattr(self.stock_count, 'to_alipay_dict'):
                params['stock_count'] = self.stock_count.to_alipay_dict()
            else:
                params['stock_count'] = self.stock_count
        if self.user_name_required:
            if hasattr(self.user_name_required, 'to_alipay_dict'):
                params['user_name_required'] = self.user_name_required.to_alipay_dict()
            else:
                params['user_name_required'] = self.user_name_required
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        if self.voucher_verify_type:
            if hasattr(self.voucher_verify_type, 'to_alipay_dict'):
                params['voucher_verify_type'] = self.voucher_verify_type.to_alipay_dict()
            else:
                params['voucher_verify_type'] = self.voucher_verify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductInfo()
        if 'can_buy_rule' in d:
            o.can_buy_rule = d['can_buy_rule']
        if 'can_refund' in d:
            o.can_refund = d['can_refund']
        if 'can_refund_minute' in d:
            o.can_refund_minute = d['can_refund_minute']
        if 'category_list' in d:
            o.category_list = d['category_list']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'name' in d:
            o.name = d['name']
        if 'notice' in d:
            o.notice = d['notice']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        if 'poster' in d:
            o.poster = d['poster']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'refund_desc' in d:
            o.refund_desc = d['refund_desc']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'stock_count' in d:
            o.stock_count = d['stock_count']
        if 'user_name_required' in d:
            o.user_name_required = d['user_name_required']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'voucher_verify_type' in d:
            o.voucher_verify_type = d['voucher_verify_type']
        return o


