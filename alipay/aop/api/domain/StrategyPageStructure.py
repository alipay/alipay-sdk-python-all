#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StrategySearchField import StrategySearchField
from alipay.aop.api.domain.StrategyShowField import StrategyShowField
from alipay.aop.api.domain.StrategySortField import StrategySortField


class StrategyPageStructure(object):

    def __init__(self):
        self._batch_switch = None
        self._ext_info = None
        self._form_code = None
        self._page_code = None
        self._page_name = None
        self._search_fields = None
        self._show_fields = None
        self._sort_fields = None
        self._title_field = None

    @property
    def batch_switch(self):
        return self._batch_switch

    @batch_switch.setter
    def batch_switch(self, value):
        self._batch_switch = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def form_code(self):
        return self._form_code

    @form_code.setter
    def form_code(self, value):
        self._form_code = value
    @property
    def page_code(self):
        return self._page_code

    @page_code.setter
    def page_code(self, value):
        self._page_code = value
    @property
    def page_name(self):
        return self._page_name

    @page_name.setter
    def page_name(self, value):
        self._page_name = value
    @property
    def search_fields(self):
        return self._search_fields

    @search_fields.setter
    def search_fields(self, value):
        if isinstance(value, list):
            self._search_fields = list()
            for i in value:
                if isinstance(i, StrategySearchField):
                    self._search_fields.append(i)
                else:
                    self._search_fields.append(StrategySearchField.from_alipay_dict(i))
    @property
    def show_fields(self):
        return self._show_fields

    @show_fields.setter
    def show_fields(self, value):
        if isinstance(value, list):
            self._show_fields = list()
            for i in value:
                if isinstance(i, StrategyShowField):
                    self._show_fields.append(i)
                else:
                    self._show_fields.append(StrategyShowField.from_alipay_dict(i))
    @property
    def sort_fields(self):
        return self._sort_fields

    @sort_fields.setter
    def sort_fields(self, value):
        if isinstance(value, list):
            self._sort_fields = list()
            for i in value:
                if isinstance(i, StrategySortField):
                    self._sort_fields.append(i)
                else:
                    self._sort_fields.append(StrategySortField.from_alipay_dict(i))
    @property
    def title_field(self):
        return self._title_field

    @title_field.setter
    def title_field(self, value):
        self._title_field = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_switch:
            if hasattr(self.batch_switch, 'to_alipay_dict'):
                params['batch_switch'] = self.batch_switch.to_alipay_dict()
            else:
                params['batch_switch'] = self.batch_switch
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.form_code:
            if hasattr(self.form_code, 'to_alipay_dict'):
                params['form_code'] = self.form_code.to_alipay_dict()
            else:
                params['form_code'] = self.form_code
        if self.page_code:
            if hasattr(self.page_code, 'to_alipay_dict'):
                params['page_code'] = self.page_code.to_alipay_dict()
            else:
                params['page_code'] = self.page_code
        if self.page_name:
            if hasattr(self.page_name, 'to_alipay_dict'):
                params['page_name'] = self.page_name.to_alipay_dict()
            else:
                params['page_name'] = self.page_name
        if self.search_fields:
            if isinstance(self.search_fields, list):
                for i in range(0, len(self.search_fields)):
                    element = self.search_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.search_fields[i] = element.to_alipay_dict()
            if hasattr(self.search_fields, 'to_alipay_dict'):
                params['search_fields'] = self.search_fields.to_alipay_dict()
            else:
                params['search_fields'] = self.search_fields
        if self.show_fields:
            if isinstance(self.show_fields, list):
                for i in range(0, len(self.show_fields)):
                    element = self.show_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.show_fields[i] = element.to_alipay_dict()
            if hasattr(self.show_fields, 'to_alipay_dict'):
                params['show_fields'] = self.show_fields.to_alipay_dict()
            else:
                params['show_fields'] = self.show_fields
        if self.sort_fields:
            if isinstance(self.sort_fields, list):
                for i in range(0, len(self.sort_fields)):
                    element = self.sort_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sort_fields[i] = element.to_alipay_dict()
            if hasattr(self.sort_fields, 'to_alipay_dict'):
                params['sort_fields'] = self.sort_fields.to_alipay_dict()
            else:
                params['sort_fields'] = self.sort_fields
        if self.title_field:
            if hasattr(self.title_field, 'to_alipay_dict'):
                params['title_field'] = self.title_field.to_alipay_dict()
            else:
                params['title_field'] = self.title_field
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StrategyPageStructure()
        if 'batch_switch' in d:
            o.batch_switch = d['batch_switch']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'form_code' in d:
            o.form_code = d['form_code']
        if 'page_code' in d:
            o.page_code = d['page_code']
        if 'page_name' in d:
            o.page_name = d['page_name']
        if 'search_fields' in d:
            o.search_fields = d['search_fields']
        if 'show_fields' in d:
            o.show_fields = d['show_fields']
        if 'sort_fields' in d:
            o.sort_fields = d['sort_fields']
        if 'title_field' in d:
            o.title_field = d['title_field']
        return o


