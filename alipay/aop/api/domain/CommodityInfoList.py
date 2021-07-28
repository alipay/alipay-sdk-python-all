#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommodityInfoList(object):

    def __init__(self):
        self._area_code = None
        self._basic_amount = None
        self._benefit_amout = None
        self._category = None
        self._commodity_name = None
        self._commodity_type = None
        self._customer_amount = None
        self._directing_url = None
        self._display_img_url = None
        self._display_name = None
        self._end_date = None
        self._inventory = None
        self._monthly_sale = None
        self._out_commodity_id = None
        self._start_date = None
        self._status = None
        self._sub_category = None
        self._tags = None
        self._total_sale = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def basic_amount(self):
        return self._basic_amount

    @basic_amount.setter
    def basic_amount(self, value):
        self._basic_amount = value
    @property
    def benefit_amout(self):
        return self._benefit_amout

    @benefit_amout.setter
    def benefit_amout(self, value):
        self._benefit_amout = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def commodity_name(self):
        return self._commodity_name

    @commodity_name.setter
    def commodity_name(self, value):
        self._commodity_name = value
    @property
    def commodity_type(self):
        return self._commodity_type

    @commodity_type.setter
    def commodity_type(self, value):
        self._commodity_type = value
    @property
    def customer_amount(self):
        return self._customer_amount

    @customer_amount.setter
    def customer_amount(self, value):
        self._customer_amount = value
    @property
    def directing_url(self):
        return self._directing_url

    @directing_url.setter
    def directing_url(self, value):
        self._directing_url = value
    @property
    def display_img_url(self):
        return self._display_img_url

    @display_img_url.setter
    def display_img_url(self, value):
        self._display_img_url = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def monthly_sale(self):
        return self._monthly_sale

    @monthly_sale.setter
    def monthly_sale(self, value):
        self._monthly_sale = value
    @property
    def out_commodity_id(self):
        return self._out_commodity_id

    @out_commodity_id.setter
    def out_commodity_id(self, value):
        self._out_commodity_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_category(self):
        return self._sub_category

    @sub_category.setter
    def sub_category(self, value):
        self._sub_category = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)
    @property
    def total_sale(self):
        return self._total_sale

    @total_sale.setter
    def total_sale(self, value):
        self._total_sale = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.basic_amount:
            if hasattr(self.basic_amount, 'to_alipay_dict'):
                params['basic_amount'] = self.basic_amount.to_alipay_dict()
            else:
                params['basic_amount'] = self.basic_amount
        if self.benefit_amout:
            if hasattr(self.benefit_amout, 'to_alipay_dict'):
                params['benefit_amout'] = self.benefit_amout.to_alipay_dict()
            else:
                params['benefit_amout'] = self.benefit_amout
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.commodity_name:
            if hasattr(self.commodity_name, 'to_alipay_dict'):
                params['commodity_name'] = self.commodity_name.to_alipay_dict()
            else:
                params['commodity_name'] = self.commodity_name
        if self.commodity_type:
            if hasattr(self.commodity_type, 'to_alipay_dict'):
                params['commodity_type'] = self.commodity_type.to_alipay_dict()
            else:
                params['commodity_type'] = self.commodity_type
        if self.customer_amount:
            if hasattr(self.customer_amount, 'to_alipay_dict'):
                params['customer_amount'] = self.customer_amount.to_alipay_dict()
            else:
                params['customer_amount'] = self.customer_amount
        if self.directing_url:
            if hasattr(self.directing_url, 'to_alipay_dict'):
                params['directing_url'] = self.directing_url.to_alipay_dict()
            else:
                params['directing_url'] = self.directing_url
        if self.display_img_url:
            if hasattr(self.display_img_url, 'to_alipay_dict'):
                params['display_img_url'] = self.display_img_url.to_alipay_dict()
            else:
                params['display_img_url'] = self.display_img_url
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.monthly_sale:
            if hasattr(self.monthly_sale, 'to_alipay_dict'):
                params['monthly_sale'] = self.monthly_sale.to_alipay_dict()
            else:
                params['monthly_sale'] = self.monthly_sale
        if self.out_commodity_id:
            if hasattr(self.out_commodity_id, 'to_alipay_dict'):
                params['out_commodity_id'] = self.out_commodity_id.to_alipay_dict()
            else:
                params['out_commodity_id'] = self.out_commodity_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_category:
            if hasattr(self.sub_category, 'to_alipay_dict'):
                params['sub_category'] = self.sub_category.to_alipay_dict()
            else:
                params['sub_category'] = self.sub_category
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.total_sale:
            if hasattr(self.total_sale, 'to_alipay_dict'):
                params['total_sale'] = self.total_sale.to_alipay_dict()
            else:
                params['total_sale'] = self.total_sale
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommodityInfoList()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'basic_amount' in d:
            o.basic_amount = d['basic_amount']
        if 'benefit_amout' in d:
            o.benefit_amout = d['benefit_amout']
        if 'category' in d:
            o.category = d['category']
        if 'commodity_name' in d:
            o.commodity_name = d['commodity_name']
        if 'commodity_type' in d:
            o.commodity_type = d['commodity_type']
        if 'customer_amount' in d:
            o.customer_amount = d['customer_amount']
        if 'directing_url' in d:
            o.directing_url = d['directing_url']
        if 'display_img_url' in d:
            o.display_img_url = d['display_img_url']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'monthly_sale' in d:
            o.monthly_sale = d['monthly_sale']
        if 'out_commodity_id' in d:
            o.out_commodity_id = d['out_commodity_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        if 'sub_category' in d:
            o.sub_category = d['sub_category']
        if 'tags' in d:
            o.tags = d['tags']
        if 'total_sale' in d:
            o.total_sale = d['total_sale']
        return o


