#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantQipanCrowdSpreadModel(object):

    def __init__(self):
        self._apply_channel_list = None
        self._crowd_name = None
        self._is_include_seed = None
        self._seed_crowd_code = None
        self._spread_count = None

    @property
    def apply_channel_list(self):
        return self._apply_channel_list

    @apply_channel_list.setter
    def apply_channel_list(self, value):
        if isinstance(value, list):
            self._apply_channel_list = list()
            for i in value:
                self._apply_channel_list.append(i)
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def is_include_seed(self):
        return self._is_include_seed

    @is_include_seed.setter
    def is_include_seed(self, value):
        self._is_include_seed = value
    @property
    def seed_crowd_code(self):
        return self._seed_crowd_code

    @seed_crowd_code.setter
    def seed_crowd_code(self, value):
        self._seed_crowd_code = value
    @property
    def spread_count(self):
        return self._spread_count

    @spread_count.setter
    def spread_count(self, value):
        self._spread_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_channel_list:
            if isinstance(self.apply_channel_list, list):
                for i in range(0, len(self.apply_channel_list)):
                    element = self.apply_channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_channel_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_channel_list, 'to_alipay_dict'):
                params['apply_channel_list'] = self.apply_channel_list.to_alipay_dict()
            else:
                params['apply_channel_list'] = self.apply_channel_list
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.is_include_seed:
            if hasattr(self.is_include_seed, 'to_alipay_dict'):
                params['is_include_seed'] = self.is_include_seed.to_alipay_dict()
            else:
                params['is_include_seed'] = self.is_include_seed
        if self.seed_crowd_code:
            if hasattr(self.seed_crowd_code, 'to_alipay_dict'):
                params['seed_crowd_code'] = self.seed_crowd_code.to_alipay_dict()
            else:
                params['seed_crowd_code'] = self.seed_crowd_code
        if self.spread_count:
            if hasattr(self.spread_count, 'to_alipay_dict'):
                params['spread_count'] = self.spread_count.to_alipay_dict()
            else:
                params['spread_count'] = self.spread_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanCrowdSpreadModel()
        if 'apply_channel_list' in d:
            o.apply_channel_list = d['apply_channel_list']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'is_include_seed' in d:
            o.is_include_seed = d['is_include_seed']
        if 'seed_crowd_code' in d:
            o.seed_crowd_code = d['seed_crowd_code']
        if 'spread_count' in d:
            o.spread_count = d['spread_count']
        return o


