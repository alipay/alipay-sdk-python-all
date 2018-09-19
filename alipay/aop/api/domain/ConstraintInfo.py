#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConstraintInfo(object):

    def __init__(self):
        self._cash_pool_id = None
        self._crowd_group_id = None
        self._crowd_restriction = None
        self._crowd_restriction_value = None
        self._item_ids = None
        self._min_cost = None
        self._subsidy_percent = None
        self._suit_shops = None
        self._user_win_count = None
        self._user_win_frequency = None

    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value
    @property
    def crowd_group_id(self):
        return self._crowd_group_id

    @crowd_group_id.setter
    def crowd_group_id(self, value):
        self._crowd_group_id = value
    @property
    def crowd_restriction(self):
        return self._crowd_restriction

    @crowd_restriction.setter
    def crowd_restriction(self, value):
        self._crowd_restriction = value
    @property
    def crowd_restriction_value(self):
        return self._crowd_restriction_value

    @crowd_restriction_value.setter
    def crowd_restriction_value(self, value):
        self._crowd_restriction_value = value
    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)
    @property
    def min_cost(self):
        return self._min_cost

    @min_cost.setter
    def min_cost(self, value):
        self._min_cost = value
    @property
    def subsidy_percent(self):
        return self._subsidy_percent

    @subsidy_percent.setter
    def subsidy_percent(self, value):
        self._subsidy_percent = value
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
        if self.cash_pool_id:
            if hasattr(self.cash_pool_id, 'to_alipay_dict'):
                params['cash_pool_id'] = self.cash_pool_id.to_alipay_dict()
            else:
                params['cash_pool_id'] = self.cash_pool_id
        if self.crowd_group_id:
            if hasattr(self.crowd_group_id, 'to_alipay_dict'):
                params['crowd_group_id'] = self.crowd_group_id.to_alipay_dict()
            else:
                params['crowd_group_id'] = self.crowd_group_id
        if self.crowd_restriction:
            if hasattr(self.crowd_restriction, 'to_alipay_dict'):
                params['crowd_restriction'] = self.crowd_restriction.to_alipay_dict()
            else:
                params['crowd_restriction'] = self.crowd_restriction
        if self.crowd_restriction_value:
            if hasattr(self.crowd_restriction_value, 'to_alipay_dict'):
                params['crowd_restriction_value'] = self.crowd_restriction_value.to_alipay_dict()
            else:
                params['crowd_restriction_value'] = self.crowd_restriction_value
        if self.item_ids:
            if isinstance(self.item_ids, list):
                for i in range(0, len(self.item_ids)):
                    element = self.item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        if self.min_cost:
            if hasattr(self.min_cost, 'to_alipay_dict'):
                params['min_cost'] = self.min_cost.to_alipay_dict()
            else:
                params['min_cost'] = self.min_cost
        if self.subsidy_percent:
            if hasattr(self.subsidy_percent, 'to_alipay_dict'):
                params['subsidy_percent'] = self.subsidy_percent.to_alipay_dict()
            else:
                params['subsidy_percent'] = self.subsidy_percent
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
        o = ConstraintInfo()
        if 'cash_pool_id' in d:
            o.cash_pool_id = d['cash_pool_id']
        if 'crowd_group_id' in d:
            o.crowd_group_id = d['crowd_group_id']
        if 'crowd_restriction' in d:
            o.crowd_restriction = d['crowd_restriction']
        if 'crowd_restriction_value' in d:
            o.crowd_restriction_value = d['crowd_restriction_value']
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        if 'min_cost' in d:
            o.min_cost = d['min_cost']
        if 'subsidy_percent' in d:
            o.subsidy_percent = d['subsidy_percent']
        if 'suit_shops' in d:
            o.suit_shops = d['suit_shops']
        if 'user_win_count' in d:
            o.user_win_count = d['user_win_count']
        if 'user_win_frequency' in d:
            o.user_win_frequency = d['user_win_frequency']
        return o


