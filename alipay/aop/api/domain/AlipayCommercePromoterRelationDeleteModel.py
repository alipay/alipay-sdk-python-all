#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePromoterRelationDeleteModel(object):

    def __init__(self):
        self._delete_role = None
        self._merchant_pid = None
        self._promoter_id = None
        self._promoter_open_id = None
        self._related_shop_list = None
        self._shop_id = None

    @property
    def delete_role(self):
        return self._delete_role

    @delete_role.setter
    def delete_role(self, value):
        self._delete_role = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def promoter_id(self):
        return self._promoter_id

    @promoter_id.setter
    def promoter_id(self, value):
        self._promoter_id = value
    @property
    def promoter_open_id(self):
        return self._promoter_open_id

    @promoter_open_id.setter
    def promoter_open_id(self, value):
        self._promoter_open_id = value
    @property
    def related_shop_list(self):
        return self._related_shop_list

    @related_shop_list.setter
    def related_shop_list(self, value):
        if isinstance(value, list):
            self._related_shop_list = list()
            for i in value:
                self._related_shop_list.append(i)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delete_role:
            if hasattr(self.delete_role, 'to_alipay_dict'):
                params['delete_role'] = self.delete_role.to_alipay_dict()
            else:
                params['delete_role'] = self.delete_role
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.promoter_id:
            if hasattr(self.promoter_id, 'to_alipay_dict'):
                params['promoter_id'] = self.promoter_id.to_alipay_dict()
            else:
                params['promoter_id'] = self.promoter_id
        if self.promoter_open_id:
            if hasattr(self.promoter_open_id, 'to_alipay_dict'):
                params['promoter_open_id'] = self.promoter_open_id.to_alipay_dict()
            else:
                params['promoter_open_id'] = self.promoter_open_id
        if self.related_shop_list:
            if isinstance(self.related_shop_list, list):
                for i in range(0, len(self.related_shop_list)):
                    element = self.related_shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_shop_list[i] = element.to_alipay_dict()
            if hasattr(self.related_shop_list, 'to_alipay_dict'):
                params['related_shop_list'] = self.related_shop_list.to_alipay_dict()
            else:
                params['related_shop_list'] = self.related_shop_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePromoterRelationDeleteModel()
        if 'delete_role' in d:
            o.delete_role = d['delete_role']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'promoter_id' in d:
            o.promoter_id = d['promoter_id']
        if 'promoter_open_id' in d:
            o.promoter_open_id = d['promoter_open_id']
        if 'related_shop_list' in d:
            o.related_shop_list = d['related_shop_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


