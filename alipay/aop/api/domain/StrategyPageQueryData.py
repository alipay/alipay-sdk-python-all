#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StrategyPageStructure import StrategyPageStructure


class StrategyPageQueryData(object):

    def __init__(self):
        self._correct_words = None
        self._current_page = None
        self._filter_words = None
        self._items = None
        self._items_per_page = None
        self._page_structure = None
        self._total_page = None
        self._value = None

    @property
    def correct_words(self):
        return self._correct_words

    @correct_words.setter
    def correct_words(self, value):
        self._correct_words = value
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def filter_words(self):
        return self._filter_words

    @filter_words.setter
    def filter_words(self, value):
        self._filter_words = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
    @property
    def items_per_page(self):
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, value):
        self._items_per_page = value
    @property
    def page_structure(self):
        return self._page_structure

    @page_structure.setter
    def page_structure(self, value):
        if isinstance(value, StrategyPageStructure):
            self._page_structure = value
        else:
            self._page_structure = StrategyPageStructure.from_alipay_dict(value)
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, list):
            self._value = list()
            for i in value:
                self._value.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.correct_words:
            if hasattr(self.correct_words, 'to_alipay_dict'):
                params['correct_words'] = self.correct_words.to_alipay_dict()
            else:
                params['correct_words'] = self.correct_words
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.filter_words:
            if hasattr(self.filter_words, 'to_alipay_dict'):
                params['filter_words'] = self.filter_words.to_alipay_dict()
            else:
                params['filter_words'] = self.filter_words
        if self.items:
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.items_per_page:
            if hasattr(self.items_per_page, 'to_alipay_dict'):
                params['items_per_page'] = self.items_per_page.to_alipay_dict()
            else:
                params['items_per_page'] = self.items_per_page
        if self.page_structure:
            if hasattr(self.page_structure, 'to_alipay_dict'):
                params['page_structure'] = self.page_structure.to_alipay_dict()
            else:
                params['page_structure'] = self.page_structure
        if self.total_page:
            if hasattr(self.total_page, 'to_alipay_dict'):
                params['total_page'] = self.total_page.to_alipay_dict()
            else:
                params['total_page'] = self.total_page
        if self.value:
            if isinstance(self.value, list):
                for i in range(0, len(self.value)):
                    element = self.value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.value[i] = element.to_alipay_dict()
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StrategyPageQueryData()
        if 'correct_words' in d:
            o.correct_words = d['correct_words']
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'filter_words' in d:
            o.filter_words = d['filter_words']
        if 'items' in d:
            o.items = d['items']
        if 'items_per_page' in d:
            o.items_per_page = d['items_per_page']
        if 'page_structure' in d:
            o.page_structure = d['page_structure']
        if 'total_page' in d:
            o.total_page = d['total_page']
        if 'value' in d:
            o.value = d['value']
        return o


