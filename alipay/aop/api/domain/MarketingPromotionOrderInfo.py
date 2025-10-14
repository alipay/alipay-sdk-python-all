#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MarketingProductInfo import MarketingProductInfo


class MarketingPromotionOrderInfo(object):

    def __init__(self):
        self._assess_amount = None
        self._assess_max_amount = None
        self._assess_max_quantity = None
        self._assess_min_amount = None
        self._assess_min_quantity = None
        self._assess_quantity = None
        self._assess_type = None
        self._first_level_emp_id = None
        self._inspect_amount = None
        self._inspect_quantity = None
        self._logistics_bill_no = None
        self._logistics_platform = None
        self._open_id = None
        self._order_create_time = None
        self._order_modify_time = None
        self._order_no = None
        self._order_status = None
        self._order_title = None
        self._product_list = None
        self._promo_id = None
        self._second_level_emp_id = None
        self._service_category_code = None
        self._signup_id = None
        self._unit_type = None
        self._user_id = None

    @property
    def assess_amount(self):
        return self._assess_amount

    @assess_amount.setter
    def assess_amount(self, value):
        self._assess_amount = value
    @property
    def assess_max_amount(self):
        return self._assess_max_amount

    @assess_max_amount.setter
    def assess_max_amount(self, value):
        self._assess_max_amount = value
    @property
    def assess_max_quantity(self):
        return self._assess_max_quantity

    @assess_max_quantity.setter
    def assess_max_quantity(self, value):
        self._assess_max_quantity = value
    @property
    def assess_min_amount(self):
        return self._assess_min_amount

    @assess_min_amount.setter
    def assess_min_amount(self, value):
        self._assess_min_amount = value
    @property
    def assess_min_quantity(self):
        return self._assess_min_quantity

    @assess_min_quantity.setter
    def assess_min_quantity(self, value):
        self._assess_min_quantity = value
    @property
    def assess_quantity(self):
        return self._assess_quantity

    @assess_quantity.setter
    def assess_quantity(self, value):
        self._assess_quantity = value
    @property
    def assess_type(self):
        return self._assess_type

    @assess_type.setter
    def assess_type(self, value):
        self._assess_type = value
    @property
    def first_level_emp_id(self):
        return self._first_level_emp_id

    @first_level_emp_id.setter
    def first_level_emp_id(self, value):
        self._first_level_emp_id = value
    @property
    def inspect_amount(self):
        return self._inspect_amount

    @inspect_amount.setter
    def inspect_amount(self, value):
        self._inspect_amount = value
    @property
    def inspect_quantity(self):
        return self._inspect_quantity

    @inspect_quantity.setter
    def inspect_quantity(self, value):
        self._inspect_quantity = value
    @property
    def logistics_bill_no(self):
        return self._logistics_bill_no

    @logistics_bill_no.setter
    def logistics_bill_no(self, value):
        self._logistics_bill_no = value
    @property
    def logistics_platform(self):
        return self._logistics_platform

    @logistics_platform.setter
    def logistics_platform(self, value):
        self._logistics_platform = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_modify_time(self):
        return self._order_modify_time

    @order_modify_time.setter
    def order_modify_time(self, value):
        self._order_modify_time = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
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
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        if isinstance(value, list):
            self._product_list = list()
            for i in value:
                if isinstance(i, MarketingProductInfo):
                    self._product_list.append(i)
                else:
                    self._product_list.append(MarketingProductInfo.from_alipay_dict(i))
    @property
    def promo_id(self):
        return self._promo_id

    @promo_id.setter
    def promo_id(self, value):
        self._promo_id = value
    @property
    def second_level_emp_id(self):
        return self._second_level_emp_id

    @second_level_emp_id.setter
    def second_level_emp_id(self, value):
        self._second_level_emp_id = value
    @property
    def service_category_code(self):
        return self._service_category_code

    @service_category_code.setter
    def service_category_code(self, value):
        self._service_category_code = value
    @property
    def signup_id(self):
        return self._signup_id

    @signup_id.setter
    def signup_id(self, value):
        self._signup_id = value
    @property
    def unit_type(self):
        return self._unit_type

    @unit_type.setter
    def unit_type(self, value):
        self._unit_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.assess_amount:
            if hasattr(self.assess_amount, 'to_alipay_dict'):
                params['assess_amount'] = self.assess_amount.to_alipay_dict()
            else:
                params['assess_amount'] = self.assess_amount
        if self.assess_max_amount:
            if hasattr(self.assess_max_amount, 'to_alipay_dict'):
                params['assess_max_amount'] = self.assess_max_amount.to_alipay_dict()
            else:
                params['assess_max_amount'] = self.assess_max_amount
        if self.assess_max_quantity:
            if hasattr(self.assess_max_quantity, 'to_alipay_dict'):
                params['assess_max_quantity'] = self.assess_max_quantity.to_alipay_dict()
            else:
                params['assess_max_quantity'] = self.assess_max_quantity
        if self.assess_min_amount:
            if hasattr(self.assess_min_amount, 'to_alipay_dict'):
                params['assess_min_amount'] = self.assess_min_amount.to_alipay_dict()
            else:
                params['assess_min_amount'] = self.assess_min_amount
        if self.assess_min_quantity:
            if hasattr(self.assess_min_quantity, 'to_alipay_dict'):
                params['assess_min_quantity'] = self.assess_min_quantity.to_alipay_dict()
            else:
                params['assess_min_quantity'] = self.assess_min_quantity
        if self.assess_quantity:
            if hasattr(self.assess_quantity, 'to_alipay_dict'):
                params['assess_quantity'] = self.assess_quantity.to_alipay_dict()
            else:
                params['assess_quantity'] = self.assess_quantity
        if self.assess_type:
            if hasattr(self.assess_type, 'to_alipay_dict'):
                params['assess_type'] = self.assess_type.to_alipay_dict()
            else:
                params['assess_type'] = self.assess_type
        if self.first_level_emp_id:
            if hasattr(self.first_level_emp_id, 'to_alipay_dict'):
                params['first_level_emp_id'] = self.first_level_emp_id.to_alipay_dict()
            else:
                params['first_level_emp_id'] = self.first_level_emp_id
        if self.inspect_amount:
            if hasattr(self.inspect_amount, 'to_alipay_dict'):
                params['inspect_amount'] = self.inspect_amount.to_alipay_dict()
            else:
                params['inspect_amount'] = self.inspect_amount
        if self.inspect_quantity:
            if hasattr(self.inspect_quantity, 'to_alipay_dict'):
                params['inspect_quantity'] = self.inspect_quantity.to_alipay_dict()
            else:
                params['inspect_quantity'] = self.inspect_quantity
        if self.logistics_bill_no:
            if hasattr(self.logistics_bill_no, 'to_alipay_dict'):
                params['logistics_bill_no'] = self.logistics_bill_no.to_alipay_dict()
            else:
                params['logistics_bill_no'] = self.logistics_bill_no
        if self.logistics_platform:
            if hasattr(self.logistics_platform, 'to_alipay_dict'):
                params['logistics_platform'] = self.logistics_platform.to_alipay_dict()
            else:
                params['logistics_platform'] = self.logistics_platform
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_modify_time:
            if hasattr(self.order_modify_time, 'to_alipay_dict'):
                params['order_modify_time'] = self.order_modify_time.to_alipay_dict()
            else:
                params['order_modify_time'] = self.order_modify_time
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
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
        if self.product_list:
            if isinstance(self.product_list, list):
                for i in range(0, len(self.product_list)):
                    element = self.product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_list[i] = element.to_alipay_dict()
            if hasattr(self.product_list, 'to_alipay_dict'):
                params['product_list'] = self.product_list.to_alipay_dict()
            else:
                params['product_list'] = self.product_list
        if self.promo_id:
            if hasattr(self.promo_id, 'to_alipay_dict'):
                params['promo_id'] = self.promo_id.to_alipay_dict()
            else:
                params['promo_id'] = self.promo_id
        if self.second_level_emp_id:
            if hasattr(self.second_level_emp_id, 'to_alipay_dict'):
                params['second_level_emp_id'] = self.second_level_emp_id.to_alipay_dict()
            else:
                params['second_level_emp_id'] = self.second_level_emp_id
        if self.service_category_code:
            if hasattr(self.service_category_code, 'to_alipay_dict'):
                params['service_category_code'] = self.service_category_code.to_alipay_dict()
            else:
                params['service_category_code'] = self.service_category_code
        if self.signup_id:
            if hasattr(self.signup_id, 'to_alipay_dict'):
                params['signup_id'] = self.signup_id.to_alipay_dict()
            else:
                params['signup_id'] = self.signup_id
        if self.unit_type:
            if hasattr(self.unit_type, 'to_alipay_dict'):
                params['unit_type'] = self.unit_type.to_alipay_dict()
            else:
                params['unit_type'] = self.unit_type
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
        o = MarketingPromotionOrderInfo()
        if 'assess_amount' in d:
            o.assess_amount = d['assess_amount']
        if 'assess_max_amount' in d:
            o.assess_max_amount = d['assess_max_amount']
        if 'assess_max_quantity' in d:
            o.assess_max_quantity = d['assess_max_quantity']
        if 'assess_min_amount' in d:
            o.assess_min_amount = d['assess_min_amount']
        if 'assess_min_quantity' in d:
            o.assess_min_quantity = d['assess_min_quantity']
        if 'assess_quantity' in d:
            o.assess_quantity = d['assess_quantity']
        if 'assess_type' in d:
            o.assess_type = d['assess_type']
        if 'first_level_emp_id' in d:
            o.first_level_emp_id = d['first_level_emp_id']
        if 'inspect_amount' in d:
            o.inspect_amount = d['inspect_amount']
        if 'inspect_quantity' in d:
            o.inspect_quantity = d['inspect_quantity']
        if 'logistics_bill_no' in d:
            o.logistics_bill_no = d['logistics_bill_no']
        if 'logistics_platform' in d:
            o.logistics_platform = d['logistics_platform']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_modify_time' in d:
            o.order_modify_time = d['order_modify_time']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'product_list' in d:
            o.product_list = d['product_list']
        if 'promo_id' in d:
            o.promo_id = d['promo_id']
        if 'second_level_emp_id' in d:
            o.second_level_emp_id = d['second_level_emp_id']
        if 'service_category_code' in d:
            o.service_category_code = d['service_category_code']
        if 'signup_id' in d:
            o.signup_id = d['signup_id']
        if 'unit_type' in d:
            o.unit_type = d['unit_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


