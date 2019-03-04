#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MMemberLevel import MMemberLevel


class MPromoConstraint(object):

    def __init__(self):
        self._crowd_type = None
        self._member_levels = None
        self._need_crowd_flag = None
        self._sub_dimension = None
        self._sub_win_count = None
        self._suit_shop_ids = None
        self._total_win_count = None

    @property
    def crowd_type(self):
        return self._crowd_type

    @crowd_type.setter
    def crowd_type(self, value):
        self._crowd_type = value
    @property
    def member_levels(self):
        return self._member_levels

    @member_levels.setter
    def member_levels(self, value):
        if isinstance(value, list):
            self._member_levels = list()
            for i in value:
                if isinstance(i, MMemberLevel):
                    self._member_levels.append(i)
                else:
                    self._member_levels.append(MMemberLevel.from_alipay_dict(i))
    @property
    def need_crowd_flag(self):
        return self._need_crowd_flag

    @need_crowd_flag.setter
    def need_crowd_flag(self, value):
        self._need_crowd_flag = value
    @property
    def sub_dimension(self):
        return self._sub_dimension

    @sub_dimension.setter
    def sub_dimension(self, value):
        self._sub_dimension = value
    @property
    def sub_win_count(self):
        return self._sub_win_count

    @sub_win_count.setter
    def sub_win_count(self, value):
        self._sub_win_count = value
    @property
    def suit_shop_ids(self):
        return self._suit_shop_ids

    @suit_shop_ids.setter
    def suit_shop_ids(self, value):
        if isinstance(value, list):
            self._suit_shop_ids = list()
            for i in value:
                self._suit_shop_ids.append(i)
    @property
    def total_win_count(self):
        return self._total_win_count

    @total_win_count.setter
    def total_win_count(self, value):
        self._total_win_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_type:
            if hasattr(self.crowd_type, 'to_alipay_dict'):
                params['crowd_type'] = self.crowd_type.to_alipay_dict()
            else:
                params['crowd_type'] = self.crowd_type
        if self.member_levels:
            if isinstance(self.member_levels, list):
                for i in range(0, len(self.member_levels)):
                    element = self.member_levels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.member_levels[i] = element.to_alipay_dict()
            if hasattr(self.member_levels, 'to_alipay_dict'):
                params['member_levels'] = self.member_levels.to_alipay_dict()
            else:
                params['member_levels'] = self.member_levels
        if self.need_crowd_flag:
            if hasattr(self.need_crowd_flag, 'to_alipay_dict'):
                params['need_crowd_flag'] = self.need_crowd_flag.to_alipay_dict()
            else:
                params['need_crowd_flag'] = self.need_crowd_flag
        if self.sub_dimension:
            if hasattr(self.sub_dimension, 'to_alipay_dict'):
                params['sub_dimension'] = self.sub_dimension.to_alipay_dict()
            else:
                params['sub_dimension'] = self.sub_dimension
        if self.sub_win_count:
            if hasattr(self.sub_win_count, 'to_alipay_dict'):
                params['sub_win_count'] = self.sub_win_count.to_alipay_dict()
            else:
                params['sub_win_count'] = self.sub_win_count
        if self.suit_shop_ids:
            if isinstance(self.suit_shop_ids, list):
                for i in range(0, len(self.suit_shop_ids)):
                    element = self.suit_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.suit_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.suit_shop_ids, 'to_alipay_dict'):
                params['suit_shop_ids'] = self.suit_shop_ids.to_alipay_dict()
            else:
                params['suit_shop_ids'] = self.suit_shop_ids
        if self.total_win_count:
            if hasattr(self.total_win_count, 'to_alipay_dict'):
                params['total_win_count'] = self.total_win_count.to_alipay_dict()
            else:
                params['total_win_count'] = self.total_win_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MPromoConstraint()
        if 'crowd_type' in d:
            o.crowd_type = d['crowd_type']
        if 'member_levels' in d:
            o.member_levels = d['member_levels']
        if 'need_crowd_flag' in d:
            o.need_crowd_flag = d['need_crowd_flag']
        if 'sub_dimension' in d:
            o.sub_dimension = d['sub_dimension']
        if 'sub_win_count' in d:
            o.sub_win_count = d['sub_win_count']
        if 'suit_shop_ids' in d:
            o.suit_shop_ids = d['suit_shop_ids']
        if 'total_win_count' in d:
            o.total_win_count = d['total_win_count']
        return o


