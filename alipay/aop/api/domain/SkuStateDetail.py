#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttachGood import AttachGood
from alipay.aop.api.domain.AIChatAttribute import AIChatAttribute
from alipay.aop.api.domain.TasteMethod import TasteMethod


class SkuStateDetail(object):

    def __init__(self):
        self._account = None
        self._attach_list = None
        self._attach_multiple = None
        self._attributes = None
        self._item_id = None
        self._item_name = None
        self._price = None
        self._recommend = None
        self._taste_methods = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def attach_list(self):
        return self._attach_list

    @attach_list.setter
    def attach_list(self, value):
        if isinstance(value, list):
            self._attach_list = list()
            for i in value:
                if isinstance(i, AttachGood):
                    self._attach_list.append(i)
                else:
                    self._attach_list.append(AttachGood.from_alipay_dict(i))
    @property
    def attach_multiple(self):
        return self._attach_multiple

    @attach_multiple.setter
    def attach_multiple(self, value):
        self._attach_multiple = value
    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        if isinstance(value, list):
            self._attributes = list()
            for i in value:
                if isinstance(i, AIChatAttribute):
                    self._attributes.append(i)
                else:
                    self._attributes.append(AIChatAttribute.from_alipay_dict(i))
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def taste_methods(self):
        return self._taste_methods

    @taste_methods.setter
    def taste_methods(self, value):
        if isinstance(value, list):
            self._taste_methods = list()
            for i in value:
                if isinstance(i, TasteMethod):
                    self._taste_methods.append(i)
                else:
                    self._taste_methods.append(TasteMethod.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.attach_list:
            if isinstance(self.attach_list, list):
                for i in range(0, len(self.attach_list)):
                    element = self.attach_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attach_list[i] = element.to_alipay_dict()
            if hasattr(self.attach_list, 'to_alipay_dict'):
                params['attach_list'] = self.attach_list.to_alipay_dict()
            else:
                params['attach_list'] = self.attach_list
        if self.attach_multiple:
            if hasattr(self.attach_multiple, 'to_alipay_dict'):
                params['attach_multiple'] = self.attach_multiple.to_alipay_dict()
            else:
                params['attach_multiple'] = self.attach_multiple
        if self.attributes:
            if isinstance(self.attributes, list):
                for i in range(0, len(self.attributes)):
                    element = self.attributes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attributes[i] = element.to_alipay_dict()
            if hasattr(self.attributes, 'to_alipay_dict'):
                params['attributes'] = self.attributes.to_alipay_dict()
            else:
                params['attributes'] = self.attributes
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.taste_methods:
            if isinstance(self.taste_methods, list):
                for i in range(0, len(self.taste_methods)):
                    element = self.taste_methods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.taste_methods[i] = element.to_alipay_dict()
            if hasattr(self.taste_methods, 'to_alipay_dict'):
                params['taste_methods'] = self.taste_methods.to_alipay_dict()
            else:
                params['taste_methods'] = self.taste_methods
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuStateDetail()
        if 'account' in d:
            o.account = d['account']
        if 'attach_list' in d:
            o.attach_list = d['attach_list']
        if 'attach_multiple' in d:
            o.attach_multiple = d['attach_multiple']
        if 'attributes' in d:
            o.attributes = d['attributes']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'price' in d:
            o.price = d['price']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'taste_methods' in d:
            o.taste_methods = d['taste_methods']
        return o


