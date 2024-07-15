#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompanyRelationInfo import CompanyRelationInfo
from alipay.aop.api.domain.ShopRelationInfo import ShopRelationInfo


class RebusinessEntityRelation(object):

    def __init__(self):
        self._org_list = None
        self._shop_list = None

    @property
    def org_list(self):
        return self._org_list

    @org_list.setter
    def org_list(self, value):
        if isinstance(value, list):
            self._org_list = list()
            for i in value:
                if isinstance(i, CompanyRelationInfo):
                    self._org_list.append(i)
                else:
                    self._org_list.append(CompanyRelationInfo.from_alipay_dict(i))
    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                if isinstance(i, ShopRelationInfo):
                    self._shop_list.append(i)
                else:
                    self._shop_list.append(ShopRelationInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.org_list:
            if isinstance(self.org_list, list):
                for i in range(0, len(self.org_list)):
                    element = self.org_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.org_list[i] = element.to_alipay_dict()
            if hasattr(self.org_list, 'to_alipay_dict'):
                params['org_list'] = self.org_list.to_alipay_dict()
            else:
                params['org_list'] = self.org_list
        if self.shop_list:
            if isinstance(self.shop_list, list):
                for i in range(0, len(self.shop_list)):
                    element = self.shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_list, 'to_alipay_dict'):
                params['shop_list'] = self.shop_list.to_alipay_dict()
            else:
                params['shop_list'] = self.shop_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RebusinessEntityRelation()
        if 'org_list' in d:
            o.org_list = d['org_list']
        if 'shop_list' in d:
            o.shop_list = d['shop_list']
        return o


