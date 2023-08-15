#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantQipanLbscrowdCreateModel(object):

    def __init__(self):
        self._apply_channel_list = None
        self._crowd_name = None
        self._shop_distance = None
        self._shop_id_list = None

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
    def shop_distance(self):
        return self._shop_distance

    @shop_distance.setter
    def shop_distance(self, value):
        self._shop_distance = value
    @property
    def shop_id_list(self):
        return self._shop_id_list

    @shop_id_list.setter
    def shop_id_list(self, value):
        if isinstance(value, list):
            self._shop_id_list = list()
            for i in value:
                self._shop_id_list.append(i)


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
        if self.shop_distance:
            if hasattr(self.shop_distance, 'to_alipay_dict'):
                params['shop_distance'] = self.shop_distance.to_alipay_dict()
            else:
                params['shop_distance'] = self.shop_distance
        if self.shop_id_list:
            if isinstance(self.shop_id_list, list):
                for i in range(0, len(self.shop_id_list)):
                    element = self.shop_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_id_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_id_list, 'to_alipay_dict'):
                params['shop_id_list'] = self.shop_id_list.to_alipay_dict()
            else:
                params['shop_id_list'] = self.shop_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanLbscrowdCreateModel()
        if 'apply_channel_list' in d:
            o.apply_channel_list = d['apply_channel_list']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'shop_distance' in d:
            o.shop_distance = d['shop_distance']
        if 'shop_id_list' in d:
            o.shop_id_list = d['shop_id_list']
        return o


