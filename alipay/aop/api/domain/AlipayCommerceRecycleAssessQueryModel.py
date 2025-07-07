#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleAddressInfo import RecycleAddressInfo


class AlipayCommerceRecycleAssessQueryModel(object):

    def __init__(self):
        self._address_info = None
        self._open_id = None
        self._product_code = None
        self._recycle_approach = None
        self._relation_id_list = None
        self._user_id = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RecycleAddressInfo):
            self._address_info = value
        else:
            self._address_info = RecycleAddressInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def recycle_approach(self):
        return self._recycle_approach

    @recycle_approach.setter
    def recycle_approach(self, value):
        self._recycle_approach = value
    @property
    def relation_id_list(self):
        return self._relation_id_list

    @relation_id_list.setter
    def relation_id_list(self, value):
        if isinstance(value, list):
            self._relation_id_list = list()
            for i in value:
                self._relation_id_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.recycle_approach:
            if hasattr(self.recycle_approach, 'to_alipay_dict'):
                params['recycle_approach'] = self.recycle_approach.to_alipay_dict()
            else:
                params['recycle_approach'] = self.recycle_approach
        if self.relation_id_list:
            if isinstance(self.relation_id_list, list):
                for i in range(0, len(self.relation_id_list)):
                    element = self.relation_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.relation_id_list[i] = element.to_alipay_dict()
            if hasattr(self.relation_id_list, 'to_alipay_dict'):
                params['relation_id_list'] = self.relation_id_list.to_alipay_dict()
            else:
                params['relation_id_list'] = self.relation_id_list
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
        o = AlipayCommerceRecycleAssessQueryModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'recycle_approach' in d:
            o.recycle_approach = d['recycle_approach']
        if 'relation_id_list' in d:
            o.relation_id_list = d['relation_id_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


