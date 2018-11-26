#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataMallShopitemsQueryModel(object):

    def __init__(self):
        self._collect_type = None
        self._mall_id = None
        self._max_coupons_num = None
        self._max_items_num = None
        self._page_no = None
        self._page_size = None
        self._product_id = None
        self._product_version = None
        self._user_id = None

    @property
    def collect_type(self):
        return self._collect_type

    @collect_type.setter
    def collect_type(self, value):
        self._collect_type = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def max_coupons_num(self):
        return self._max_coupons_num

    @max_coupons_num.setter
    def max_coupons_num(self, value):
        self._max_coupons_num = value
    @property
    def max_items_num(self):
        return self._max_items_num

    @max_items_num.setter
    def max_items_num(self, value):
        self._max_items_num = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_version(self):
        return self._product_version

    @product_version.setter
    def product_version(self, value):
        self._product_version = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.collect_type:
            if hasattr(self.collect_type, 'to_alipay_dict'):
                params['collect_type'] = self.collect_type.to_alipay_dict()
            else:
                params['collect_type'] = self.collect_type
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.max_coupons_num:
            if hasattr(self.max_coupons_num, 'to_alipay_dict'):
                params['max_coupons_num'] = self.max_coupons_num.to_alipay_dict()
            else:
                params['max_coupons_num'] = self.max_coupons_num
        if self.max_items_num:
            if hasattr(self.max_items_num, 'to_alipay_dict'):
                params['max_items_num'] = self.max_items_num.to_alipay_dict()
            else:
                params['max_items_num'] = self.max_items_num
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_version:
            if hasattr(self.product_version, 'to_alipay_dict'):
                params['product_version'] = self.product_version.to_alipay_dict()
            else:
                params['product_version'] = self.product_version
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
        o = KoubeiMarketingDataMallShopitemsQueryModel()
        if 'collect_type' in d:
            o.collect_type = d['collect_type']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'max_coupons_num' in d:
            o.max_coupons_num = d['max_coupons_num']
        if 'max_items_num' in d:
            o.max_items_num = d['max_items_num']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_version' in d:
            o.product_version = d['product_version']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


