#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineMarketShopDiscountQueryModel(object):

    def __init__(self):
        self._camp_biz_type_list = None
        self._query_type = None
        self._shop_id = None
        self._user_id = None

    @property
    def camp_biz_type_list(self):
        return self._camp_biz_type_list

    @camp_biz_type_list.setter
    def camp_biz_type_list(self, value):
        if isinstance(value, list):
            self._camp_biz_type_list = list()
            for i in value:
                self._camp_biz_type_list.append(i)
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_biz_type_list:
            if isinstance(self.camp_biz_type_list, list):
                for i in range(0, len(self.camp_biz_type_list)):
                    element = self.camp_biz_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.camp_biz_type_list[i] = element.to_alipay_dict()
            if hasattr(self.camp_biz_type_list, 'to_alipay_dict'):
                params['camp_biz_type_list'] = self.camp_biz_type_list.to_alipay_dict()
            else:
                params['camp_biz_type_list'] = self.camp_biz_type_list
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
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
        o = AlipayOfflineMarketShopDiscountQueryModel()
        if 'camp_biz_type_list' in d:
            o.camp_biz_type_list = d['camp_biz_type_list']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


