#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrizeCustomMenu import PrizeCustomMenu
from alipay.aop.api.domain.OpenPromoPrizeDimension import OpenPromoPrizeDimension
from alipay.aop.api.domain.OpenPromoPrizeRelativeTime import OpenPromoPrizeRelativeTime


class OpenPromoPrize(object):

    def __init__(self):
        self._prize_base_rule_amount = None
        self._prize_custom_menu = None
        self._prize_desc = None
        self._prize_detail_img = None
        self._prize_dimension_time = None
        self._prize_end_time = None
        self._prize_logo = None
        self._prize_name = None
        self._prize_relative_time = None
        self._prize_start_time = None
        self._prize_subtitle = None
        self._prize_suitable_shops = None
        self._prize_template_end_time = None
        self._prize_template_start_time = None
        self._prize_terms = None
        self._prize_type = None
        self._prize_worth_amount = None

    @property
    def prize_base_rule_amount(self):
        return self._prize_base_rule_amount

    @prize_base_rule_amount.setter
    def prize_base_rule_amount(self, value):
        self._prize_base_rule_amount = value
    @property
    def prize_custom_menu(self):
        return self._prize_custom_menu

    @prize_custom_menu.setter
    def prize_custom_menu(self, value):
        if isinstance(value, list):
            self._prize_custom_menu = list()
            for i in value:
                if isinstance(i, PrizeCustomMenu):
                    self._prize_custom_menu.append(i)
                else:
                    self._prize_custom_menu.append(PrizeCustomMenu.from_alipay_dict(i))
    @property
    def prize_desc(self):
        return self._prize_desc

    @prize_desc.setter
    def prize_desc(self, value):
        self._prize_desc = value
    @property
    def prize_detail_img(self):
        return self._prize_detail_img

    @prize_detail_img.setter
    def prize_detail_img(self, value):
        self._prize_detail_img = value
    @property
    def prize_dimension_time(self):
        return self._prize_dimension_time

    @prize_dimension_time.setter
    def prize_dimension_time(self, value):
        if isinstance(value, list):
            self._prize_dimension_time = list()
            for i in value:
                if isinstance(i, OpenPromoPrizeDimension):
                    self._prize_dimension_time.append(i)
                else:
                    self._prize_dimension_time.append(OpenPromoPrizeDimension.from_alipay_dict(i))
    @property
    def prize_end_time(self):
        return self._prize_end_time

    @prize_end_time.setter
    def prize_end_time(self, value):
        self._prize_end_time = value
    @property
    def prize_logo(self):
        return self._prize_logo

    @prize_logo.setter
    def prize_logo(self, value):
        self._prize_logo = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_relative_time(self):
        return self._prize_relative_time

    @prize_relative_time.setter
    def prize_relative_time(self, value):
        if isinstance(value, OpenPromoPrizeRelativeTime):
            self._prize_relative_time = value
        else:
            self._prize_relative_time = OpenPromoPrizeRelativeTime.from_alipay_dict(value)
    @property
    def prize_start_time(self):
        return self._prize_start_time

    @prize_start_time.setter
    def prize_start_time(self, value):
        self._prize_start_time = value
    @property
    def prize_subtitle(self):
        return self._prize_subtitle

    @prize_subtitle.setter
    def prize_subtitle(self, value):
        self._prize_subtitle = value
    @property
    def prize_suitable_shops(self):
        return self._prize_suitable_shops

    @prize_suitable_shops.setter
    def prize_suitable_shops(self, value):
        if isinstance(value, list):
            self._prize_suitable_shops = list()
            for i in value:
                self._prize_suitable_shops.append(i)
    @property
    def prize_template_end_time(self):
        return self._prize_template_end_time

    @prize_template_end_time.setter
    def prize_template_end_time(self, value):
        self._prize_template_end_time = value
    @property
    def prize_template_start_time(self):
        return self._prize_template_start_time

    @prize_template_start_time.setter
    def prize_template_start_time(self, value):
        self._prize_template_start_time = value
    @property
    def prize_terms(self):
        return self._prize_terms

    @prize_terms.setter
    def prize_terms(self, value):
        if isinstance(value, list):
            self._prize_terms = list()
            for i in value:
                self._prize_terms.append(i)
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def prize_worth_amount(self):
        return self._prize_worth_amount

    @prize_worth_amount.setter
    def prize_worth_amount(self, value):
        self._prize_worth_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_base_rule_amount:
            if hasattr(self.prize_base_rule_amount, 'to_alipay_dict'):
                params['prize_base_rule_amount'] = self.prize_base_rule_amount.to_alipay_dict()
            else:
                params['prize_base_rule_amount'] = self.prize_base_rule_amount
        if self.prize_custom_menu:
            if isinstance(self.prize_custom_menu, list):
                for i in range(0, len(self.prize_custom_menu)):
                    element = self.prize_custom_menu[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_custom_menu[i] = element.to_alipay_dict()
            if hasattr(self.prize_custom_menu, 'to_alipay_dict'):
                params['prize_custom_menu'] = self.prize_custom_menu.to_alipay_dict()
            else:
                params['prize_custom_menu'] = self.prize_custom_menu
        if self.prize_desc:
            if hasattr(self.prize_desc, 'to_alipay_dict'):
                params['prize_desc'] = self.prize_desc.to_alipay_dict()
            else:
                params['prize_desc'] = self.prize_desc
        if self.prize_detail_img:
            if hasattr(self.prize_detail_img, 'to_alipay_dict'):
                params['prize_detail_img'] = self.prize_detail_img.to_alipay_dict()
            else:
                params['prize_detail_img'] = self.prize_detail_img
        if self.prize_dimension_time:
            if isinstance(self.prize_dimension_time, list):
                for i in range(0, len(self.prize_dimension_time)):
                    element = self.prize_dimension_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_dimension_time[i] = element.to_alipay_dict()
            if hasattr(self.prize_dimension_time, 'to_alipay_dict'):
                params['prize_dimension_time'] = self.prize_dimension_time.to_alipay_dict()
            else:
                params['prize_dimension_time'] = self.prize_dimension_time
        if self.prize_end_time:
            if hasattr(self.prize_end_time, 'to_alipay_dict'):
                params['prize_end_time'] = self.prize_end_time.to_alipay_dict()
            else:
                params['prize_end_time'] = self.prize_end_time
        if self.prize_logo:
            if hasattr(self.prize_logo, 'to_alipay_dict'):
                params['prize_logo'] = self.prize_logo.to_alipay_dict()
            else:
                params['prize_logo'] = self.prize_logo
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_relative_time:
            if hasattr(self.prize_relative_time, 'to_alipay_dict'):
                params['prize_relative_time'] = self.prize_relative_time.to_alipay_dict()
            else:
                params['prize_relative_time'] = self.prize_relative_time
        if self.prize_start_time:
            if hasattr(self.prize_start_time, 'to_alipay_dict'):
                params['prize_start_time'] = self.prize_start_time.to_alipay_dict()
            else:
                params['prize_start_time'] = self.prize_start_time
        if self.prize_subtitle:
            if hasattr(self.prize_subtitle, 'to_alipay_dict'):
                params['prize_subtitle'] = self.prize_subtitle.to_alipay_dict()
            else:
                params['prize_subtitle'] = self.prize_subtitle
        if self.prize_suitable_shops:
            if isinstance(self.prize_suitable_shops, list):
                for i in range(0, len(self.prize_suitable_shops)):
                    element = self.prize_suitable_shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_suitable_shops[i] = element.to_alipay_dict()
            if hasattr(self.prize_suitable_shops, 'to_alipay_dict'):
                params['prize_suitable_shops'] = self.prize_suitable_shops.to_alipay_dict()
            else:
                params['prize_suitable_shops'] = self.prize_suitable_shops
        if self.prize_template_end_time:
            if hasattr(self.prize_template_end_time, 'to_alipay_dict'):
                params['prize_template_end_time'] = self.prize_template_end_time.to_alipay_dict()
            else:
                params['prize_template_end_time'] = self.prize_template_end_time
        if self.prize_template_start_time:
            if hasattr(self.prize_template_start_time, 'to_alipay_dict'):
                params['prize_template_start_time'] = self.prize_template_start_time.to_alipay_dict()
            else:
                params['prize_template_start_time'] = self.prize_template_start_time
        if self.prize_terms:
            if isinstance(self.prize_terms, list):
                for i in range(0, len(self.prize_terms)):
                    element = self.prize_terms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_terms[i] = element.to_alipay_dict()
            if hasattr(self.prize_terms, 'to_alipay_dict'):
                params['prize_terms'] = self.prize_terms.to_alipay_dict()
            else:
                params['prize_terms'] = self.prize_terms
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.prize_worth_amount:
            if hasattr(self.prize_worth_amount, 'to_alipay_dict'):
                params['prize_worth_amount'] = self.prize_worth_amount.to_alipay_dict()
            else:
                params['prize_worth_amount'] = self.prize_worth_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenPromoPrize()
        if 'prize_base_rule_amount' in d:
            o.prize_base_rule_amount = d['prize_base_rule_amount']
        if 'prize_custom_menu' in d:
            o.prize_custom_menu = d['prize_custom_menu']
        if 'prize_desc' in d:
            o.prize_desc = d['prize_desc']
        if 'prize_detail_img' in d:
            o.prize_detail_img = d['prize_detail_img']
        if 'prize_dimension_time' in d:
            o.prize_dimension_time = d['prize_dimension_time']
        if 'prize_end_time' in d:
            o.prize_end_time = d['prize_end_time']
        if 'prize_logo' in d:
            o.prize_logo = d['prize_logo']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_relative_time' in d:
            o.prize_relative_time = d['prize_relative_time']
        if 'prize_start_time' in d:
            o.prize_start_time = d['prize_start_time']
        if 'prize_subtitle' in d:
            o.prize_subtitle = d['prize_subtitle']
        if 'prize_suitable_shops' in d:
            o.prize_suitable_shops = d['prize_suitable_shops']
        if 'prize_template_end_time' in d:
            o.prize_template_end_time = d['prize_template_end_time']
        if 'prize_template_start_time' in d:
            o.prize_template_start_time = d['prize_template_start_time']
        if 'prize_terms' in d:
            o.prize_terms = d['prize_terms']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'prize_worth_amount' in d:
            o.prize_worth_amount = d['prize_worth_amount']
        return o


