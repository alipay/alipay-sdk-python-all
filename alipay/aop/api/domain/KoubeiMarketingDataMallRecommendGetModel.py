#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataMallRecommendGetModel(object):

    def __init__(self):
        self._count = None
        self._data_type = None
        self._device_id = None
        self._mall_id = None
        self._shop_category_ids = None
        self._start = None
        self._user_id = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def shop_category_ids(self):
        return self._shop_category_ids

    @shop_category_ids.setter
    def shop_category_ids(self, value):
        if isinstance(value, list):
            self._shop_category_ids = list()
            for i in value:
                self._shop_category_ids.append(i)
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.shop_category_ids:
            if isinstance(self.shop_category_ids, list):
                for i in range(0, len(self.shop_category_ids)):
                    element = self.shop_category_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_category_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_category_ids, 'to_alipay_dict'):
                params['shop_category_ids'] = self.shop_category_ids.to_alipay_dict()
            else:
                params['shop_category_ids'] = self.shop_category_ids
        if self.start:
            if hasattr(self.start, 'to_alipay_dict'):
                params['start'] = self.start.to_alipay_dict()
            else:
                params['start'] = self.start
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
        o = KoubeiMarketingDataMallRecommendGetModel()
        if 'count' in d:
            o.count = d['count']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'shop_category_ids' in d:
            o.shop_category_ids = d['shop_category_ids']
        if 'start' in d:
            o.start = d['start']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


