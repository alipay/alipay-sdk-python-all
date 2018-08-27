#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MenuAnalysisData(object):

    def __init__(self):
        self._avg_click_user_cnt = None
        self._click_cnt = None
        self._click_user_cnt = None
        self._date = None
        self._menu_type = None
        self._name = None
        self._sub_name = None

    @property
    def avg_click_user_cnt(self):
        return self._avg_click_user_cnt

    @avg_click_user_cnt.setter
    def avg_click_user_cnt(self, value):
        self._avg_click_user_cnt = value
    @property
    def click_cnt(self):
        return self._click_cnt

    @click_cnt.setter
    def click_cnt(self, value):
        self._click_cnt = value
    @property
    def click_user_cnt(self):
        return self._click_user_cnt

    @click_user_cnt.setter
    def click_user_cnt(self, value):
        self._click_user_cnt = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def menu_type(self):
        return self._menu_type

    @menu_type.setter
    def menu_type(self, value):
        self._menu_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def sub_name(self):
        return self._sub_name

    @sub_name.setter
    def sub_name(self, value):
        self._sub_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_click_user_cnt:
            if hasattr(self.avg_click_user_cnt, 'to_alipay_dict'):
                params['avg_click_user_cnt'] = self.avg_click_user_cnt.to_alipay_dict()
            else:
                params['avg_click_user_cnt'] = self.avg_click_user_cnt
        if self.click_cnt:
            if hasattr(self.click_cnt, 'to_alipay_dict'):
                params['click_cnt'] = self.click_cnt.to_alipay_dict()
            else:
                params['click_cnt'] = self.click_cnt
        if self.click_user_cnt:
            if hasattr(self.click_user_cnt, 'to_alipay_dict'):
                params['click_user_cnt'] = self.click_user_cnt.to_alipay_dict()
            else:
                params['click_user_cnt'] = self.click_user_cnt
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.menu_type:
            if hasattr(self.menu_type, 'to_alipay_dict'):
                params['menu_type'] = self.menu_type.to_alipay_dict()
            else:
                params['menu_type'] = self.menu_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.sub_name:
            if hasattr(self.sub_name, 'to_alipay_dict'):
                params['sub_name'] = self.sub_name.to_alipay_dict()
            else:
                params['sub_name'] = self.sub_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MenuAnalysisData()
        if 'avg_click_user_cnt' in d:
            o.avg_click_user_cnt = d['avg_click_user_cnt']
        if 'click_cnt' in d:
            o.click_cnt = d['click_cnt']
        if 'click_user_cnt' in d:
            o.click_user_cnt = d['click_user_cnt']
        if 'date' in d:
            o.date = d['date']
        if 'menu_type' in d:
            o.menu_type = d['menu_type']
        if 'name' in d:
            o.name = d['name']
        if 'sub_name' in d:
            o.sub_name = d['sub_name']
        return o


