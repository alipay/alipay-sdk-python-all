#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Dishes import Dishes


class KoubeiCateringDishRecommendQueryModel(object):

    def __init__(self):
        self._dish_id = None
        self._dish_list = None
        self._merchent_pid = None
        self._people = None
        self._per_price = None
        self._shop_id = None
        self._type = None
        self._user_id = None

    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        if isinstance(value, list):
            self._dish_list = list()
            for i in value:
                if isinstance(i, Dishes):
                    self._dish_list.append(i)
                else:
                    self._dish_list.append(Dishes.from_alipay_dict(i))
    @property
    def merchent_pid(self):
        return self._merchent_pid

    @merchent_pid.setter
    def merchent_pid(self, value):
        self._merchent_pid = value
    @property
    def people(self):
        return self._people

    @people.setter
    def people(self, value):
        self._people = value
    @property
    def per_price(self):
        return self._per_price

    @per_price.setter
    def per_price(self, value):
        self._per_price = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_list:
            if isinstance(self.dish_list, list):
                for i in range(0, len(self.dish_list)):
                    element = self.dish_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_list, 'to_alipay_dict'):
                params['dish_list'] = self.dish_list.to_alipay_dict()
            else:
                params['dish_list'] = self.dish_list
        if self.merchent_pid:
            if hasattr(self.merchent_pid, 'to_alipay_dict'):
                params['merchent_pid'] = self.merchent_pid.to_alipay_dict()
            else:
                params['merchent_pid'] = self.merchent_pid
        if self.people:
            if hasattr(self.people, 'to_alipay_dict'):
                params['people'] = self.people.to_alipay_dict()
            else:
                params['people'] = self.people
        if self.per_price:
            if hasattr(self.per_price, 'to_alipay_dict'):
                params['per_price'] = self.per_price.to_alipay_dict()
            else:
                params['per_price'] = self.per_price
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = KoubeiCateringDishRecommendQueryModel()
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_list' in d:
            o.dish_list = d['dish_list']
        if 'merchent_pid' in d:
            o.merchent_pid = d['merchent_pid']
        if 'people' in d:
            o.people = d['people']
        if 'per_price' in d:
            o.per_price = d['per_price']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


