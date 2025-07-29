#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RateInfo import RateInfo
from alipay.aop.api.domain.RateInfo import RateInfo


class TaxCategoryInfo(object):

    def __init__(self):
        self._collection_rate = None
        self._description = None
        self._item_category_name = None
        self._item_name = None
        self._parent_code = None
        self._specific_element_tag = None
        self._tax_code = None
        self._vat_rate = None

    @property
    def collection_rate(self):
        return self._collection_rate

    @collection_rate.setter
    def collection_rate(self, value):
        if isinstance(value, list):
            self._collection_rate = list()
            for i in value:
                if isinstance(i, RateInfo):
                    self._collection_rate.append(i)
                else:
                    self._collection_rate.append(RateInfo.from_alipay_dict(i))
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def item_category_name(self):
        return self._item_category_name

    @item_category_name.setter
    def item_category_name(self, value):
        self._item_category_name = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def parent_code(self):
        return self._parent_code

    @parent_code.setter
    def parent_code(self, value):
        self._parent_code = value
    @property
    def specific_element_tag(self):
        return self._specific_element_tag

    @specific_element_tag.setter
    def specific_element_tag(self, value):
        self._specific_element_tag = value
    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, value):
        self._tax_code = value
    @property
    def vat_rate(self):
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, value):
        if isinstance(value, list):
            self._vat_rate = list()
            for i in value:
                if isinstance(i, RateInfo):
                    self._vat_rate.append(i)
                else:
                    self._vat_rate.append(RateInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.collection_rate:
            if isinstance(self.collection_rate, list):
                for i in range(0, len(self.collection_rate)):
                    element = self.collection_rate[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.collection_rate[i] = element.to_alipay_dict()
            if hasattr(self.collection_rate, 'to_alipay_dict'):
                params['collection_rate'] = self.collection_rate.to_alipay_dict()
            else:
                params['collection_rate'] = self.collection_rate
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.item_category_name:
            if hasattr(self.item_category_name, 'to_alipay_dict'):
                params['item_category_name'] = self.item_category_name.to_alipay_dict()
            else:
                params['item_category_name'] = self.item_category_name
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.parent_code:
            if hasattr(self.parent_code, 'to_alipay_dict'):
                params['parent_code'] = self.parent_code.to_alipay_dict()
            else:
                params['parent_code'] = self.parent_code
        if self.specific_element_tag:
            if hasattr(self.specific_element_tag, 'to_alipay_dict'):
                params['specific_element_tag'] = self.specific_element_tag.to_alipay_dict()
            else:
                params['specific_element_tag'] = self.specific_element_tag
        if self.tax_code:
            if hasattr(self.tax_code, 'to_alipay_dict'):
                params['tax_code'] = self.tax_code.to_alipay_dict()
            else:
                params['tax_code'] = self.tax_code
        if self.vat_rate:
            if isinstance(self.vat_rate, list):
                for i in range(0, len(self.vat_rate)):
                    element = self.vat_rate[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vat_rate[i] = element.to_alipay_dict()
            if hasattr(self.vat_rate, 'to_alipay_dict'):
                params['vat_rate'] = self.vat_rate.to_alipay_dict()
            else:
                params['vat_rate'] = self.vat_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaxCategoryInfo()
        if 'collection_rate' in d:
            o.collection_rate = d['collection_rate']
        if 'description' in d:
            o.description = d['description']
        if 'item_category_name' in d:
            o.item_category_name = d['item_category_name']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'parent_code' in d:
            o.parent_code = d['parent_code']
        if 'specific_element_tag' in d:
            o.specific_element_tag = d['specific_element_tag']
        if 'tax_code' in d:
            o.tax_code = d['tax_code']
        if 'vat_rate' in d:
            o.vat_rate = d['vat_rate']
        return o


