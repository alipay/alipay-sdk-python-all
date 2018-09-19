#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteligentConstraintInfo(object):

    def __init__(self):
        self._crowd_group_id = None
        self._item_ids = None
        self._min_cost = None
        self._suit_shops = None
        self._user_win_count = None
        self._user_win_frequency = None

    @property
    def crowd_group_id(self):
        return self._crowd_group_id

    @crowd_group_id.setter
    def crowd_group_id(self, value):
        self._crowd_group_id = value
    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        self._item_ids = value
    @property
    def min_cost(self):
        return self._min_cost

    @min_cost.setter
    def min_cost(self, value):
        self._min_cost = value
    @property
    def suit_shops(self):
        return self._suit_shops

    @suit_shops.setter
    def suit_shops(self, value):
        if isinstance(value, list):
            self._suit_shops = list()
            for i in value:
                self._suit_shops.append(i)
    @property
    def user_win_count(self):
        return self._user_win_count

    @user_win_count.setter
    def user_win_count(self, value):
        self._user_win_count = value
    @property
    def user_win_frequency(self):
        return self._user_win_frequency

    @user_win_frequency.setter
    def user_win_frequency(self, value):
        self._user_win_frequency = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_group_id:
            if hasattr(self.crowd_group_id, 'to_alipay_dict'):
                params['crowd_group_id'] = self.crowd_group_id.to_alipay_dict()
            else:
                params['crowd_group_id'] = self.crowd_group_id
        if self.item_ids:
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        if self.min_cost:
            if hasattr(self.min_cost, 'to_alipay_dict'):
                params['min_cost'] = self.min_cost.to_alipay_dict()
            else:
                params['min_cost'] = self.min_cost
        if self.suit_shops:
            if isinstance(self.suit_shops, list):
                for i in range(0, len(self.suit_shops)):
                    element = self.suit_shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.suit_shops[i] = element.to_alipay_dict()
            if hasattr(self.suit_shops, 'to_alipay_dict'):
                params['suit_shops'] = self.suit_shops.to_alipay_dict()
            else:
                params['suit_shops'] = self.suit_shops
        if self.user_win_count:
            if hasattr(self.user_win_count, 'to_alipay_dict'):
                params['user_win_count'] = self.user_win_count.to_alipay_dict()
            else:
                params['user_win_count'] = self.user_win_count
        if self.user_win_frequency:
            if hasattr(self.user_win_frequency, 'to_alipay_dict'):
                params['user_win_frequency'] = self.user_win_frequency.to_alipay_dict()
            else:
                params['user_win_frequency'] = self.user_win_frequency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteligentConstraintInfo()
        if 'crowd_group_id' in d:
            o.crowd_group_id = d['crowd_group_id']
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        if 'min_cost' in d:
            o.min_cost = d['min_cost']
        if 'suit_shops' in d:
            o.suit_shops = d['suit_shops']
        if 'user_win_count' in d:
            o.user_win_count = d['user_win_count']
        if 'user_win_frequency' in d:
            o.user_win_frequency = d['user_win_frequency']
        return o


