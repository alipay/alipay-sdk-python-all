#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BoxExclusiveBase import BoxExclusiveBase
from alipay.aop.api.domain.BoxExclusiveService import BoxExclusiveService
from alipay.aop.api.domain.BoxExclusiveService import BoxExclusiveService


class ApplyBoxExclusiveRequest(object):

    def __init__(self):
        self._base_info = None
        self._brand_id = None
        self._default_keywords = None
        self._item_id = None
        self._keywords = None
        self._operator_id = None
        self._related_accounts = None
        self._related_functions = None

    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        if isinstance(value, BoxExclusiveBase):
            self._base_info = value
        else:
            self._base_info = BoxExclusiveBase.from_alipay_dict(value)
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def default_keywords(self):
        return self._default_keywords

    @default_keywords.setter
    def default_keywords(self, value):
        if isinstance(value, list):
            self._default_keywords = list()
            for i in value:
                self._default_keywords.append(i)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, list):
            self._keywords = list()
            for i in value:
                self._keywords.append(i)
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def related_accounts(self):
        return self._related_accounts

    @related_accounts.setter
    def related_accounts(self, value):
        if isinstance(value, list):
            self._related_accounts = list()
            for i in value:
                if isinstance(i, BoxExclusiveService):
                    self._related_accounts.append(i)
                else:
                    self._related_accounts.append(BoxExclusiveService.from_alipay_dict(i))
    @property
    def related_functions(self):
        return self._related_functions

    @related_functions.setter
    def related_functions(self, value):
        if isinstance(value, list):
            self._related_functions = list()
            for i in value:
                if isinstance(i, BoxExclusiveService):
                    self._related_functions.append(i)
                else:
                    self._related_functions.append(BoxExclusiveService.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.default_keywords:
            if isinstance(self.default_keywords, list):
                for i in range(0, len(self.default_keywords)):
                    element = self.default_keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.default_keywords[i] = element.to_alipay_dict()
            if hasattr(self.default_keywords, 'to_alipay_dict'):
                params['default_keywords'] = self.default_keywords.to_alipay_dict()
            else:
                params['default_keywords'] = self.default_keywords
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.keywords:
            if isinstance(self.keywords, list):
                for i in range(0, len(self.keywords)):
                    element = self.keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keywords[i] = element.to_alipay_dict()
            if hasattr(self.keywords, 'to_alipay_dict'):
                params['keywords'] = self.keywords.to_alipay_dict()
            else:
                params['keywords'] = self.keywords
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.related_accounts:
            if isinstance(self.related_accounts, list):
                for i in range(0, len(self.related_accounts)):
                    element = self.related_accounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_accounts[i] = element.to_alipay_dict()
            if hasattr(self.related_accounts, 'to_alipay_dict'):
                params['related_accounts'] = self.related_accounts.to_alipay_dict()
            else:
                params['related_accounts'] = self.related_accounts
        if self.related_functions:
            if isinstance(self.related_functions, list):
                for i in range(0, len(self.related_functions)):
                    element = self.related_functions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_functions[i] = element.to_alipay_dict()
            if hasattr(self.related_functions, 'to_alipay_dict'):
                params['related_functions'] = self.related_functions.to_alipay_dict()
            else:
                params['related_functions'] = self.related_functions
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyBoxExclusiveRequest()
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'default_keywords' in d:
            o.default_keywords = d['default_keywords']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'keywords' in d:
            o.keywords = d['keywords']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'related_accounts' in d:
            o.related_accounts = d['related_accounts']
        if 'related_functions' in d:
            o.related_functions = d['related_functions']
        return o


