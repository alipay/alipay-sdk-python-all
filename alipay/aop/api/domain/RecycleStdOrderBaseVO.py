#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleAssessProductVO import RecycleAssessProductVO


class RecycleStdOrderBaseVO(object):

    def __init__(self):
        self._assess_max_amount = None
        self._assess_min_amount = None
        self._assess_price_type = None
        self._assess_products = None
        self._merchant_order_no = None
        self._order_create_time = None
        self._order_id = None
        self._order_memo = None
        self._order_modify_time = None
        self._order_status = None
        self._order_title = None
        self._recycle_category = None
        self._user_total_amount = None

    @property
    def assess_max_amount(self):
        return self._assess_max_amount

    @assess_max_amount.setter
    def assess_max_amount(self, value):
        self._assess_max_amount = value
    @property
    def assess_min_amount(self):
        return self._assess_min_amount

    @assess_min_amount.setter
    def assess_min_amount(self, value):
        self._assess_min_amount = value
    @property
    def assess_price_type(self):
        return self._assess_price_type

    @assess_price_type.setter
    def assess_price_type(self, value):
        self._assess_price_type = value
    @property
    def assess_products(self):
        return self._assess_products

    @assess_products.setter
    def assess_products(self, value):
        if isinstance(value, list):
            self._assess_products = list()
            for i in value:
                if isinstance(i, RecycleAssessProductVO):
                    self._assess_products.append(i)
                else:
                    self._assess_products.append(RecycleAssessProductVO.from_alipay_dict(i))
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_memo(self):
        return self._order_memo

    @order_memo.setter
    def order_memo(self, value):
        self._order_memo = value
    @property
    def order_modify_time(self):
        return self._order_modify_time

    @order_modify_time.setter
    def order_modify_time(self, value):
        self._order_modify_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def recycle_category(self):
        return self._recycle_category

    @recycle_category.setter
    def recycle_category(self, value):
        self._recycle_category = value
    @property
    def user_total_amount(self):
        return self._user_total_amount

    @user_total_amount.setter
    def user_total_amount(self, value):
        self._user_total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.assess_max_amount:
            if hasattr(self.assess_max_amount, 'to_alipay_dict'):
                params['assess_max_amount'] = self.assess_max_amount.to_alipay_dict()
            else:
                params['assess_max_amount'] = self.assess_max_amount
        if self.assess_min_amount:
            if hasattr(self.assess_min_amount, 'to_alipay_dict'):
                params['assess_min_amount'] = self.assess_min_amount.to_alipay_dict()
            else:
                params['assess_min_amount'] = self.assess_min_amount
        if self.assess_price_type:
            if hasattr(self.assess_price_type, 'to_alipay_dict'):
                params['assess_price_type'] = self.assess_price_type.to_alipay_dict()
            else:
                params['assess_price_type'] = self.assess_price_type
        if self.assess_products:
            if isinstance(self.assess_products, list):
                for i in range(0, len(self.assess_products)):
                    element = self.assess_products[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.assess_products[i] = element.to_alipay_dict()
            if hasattr(self.assess_products, 'to_alipay_dict'):
                params['assess_products'] = self.assess_products.to_alipay_dict()
            else:
                params['assess_products'] = self.assess_products
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_memo:
            if hasattr(self.order_memo, 'to_alipay_dict'):
                params['order_memo'] = self.order_memo.to_alipay_dict()
            else:
                params['order_memo'] = self.order_memo
        if self.order_modify_time:
            if hasattr(self.order_modify_time, 'to_alipay_dict'):
                params['order_modify_time'] = self.order_modify_time.to_alipay_dict()
            else:
                params['order_modify_time'] = self.order_modify_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.recycle_category:
            if hasattr(self.recycle_category, 'to_alipay_dict'):
                params['recycle_category'] = self.recycle_category.to_alipay_dict()
            else:
                params['recycle_category'] = self.recycle_category
        if self.user_total_amount:
            if hasattr(self.user_total_amount, 'to_alipay_dict'):
                params['user_total_amount'] = self.user_total_amount.to_alipay_dict()
            else:
                params['user_total_amount'] = self.user_total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleStdOrderBaseVO()
        if 'assess_max_amount' in d:
            o.assess_max_amount = d['assess_max_amount']
        if 'assess_min_amount' in d:
            o.assess_min_amount = d['assess_min_amount']
        if 'assess_price_type' in d:
            o.assess_price_type = d['assess_price_type']
        if 'assess_products' in d:
            o.assess_products = d['assess_products']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_memo' in d:
            o.order_memo = d['order_memo']
        if 'order_modify_time' in d:
            o.order_modify_time = d['order_modify_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'recycle_category' in d:
            o.recycle_category = d['recycle_category']
        if 'user_total_amount' in d:
            o.user_total_amount = d['user_total_amount']
        return o


