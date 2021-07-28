#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinCustomerMemberQueryModel(object):

    def __init__(self):
        self._biz_product = None
        self._map_id_type = None
        self._map_id_value = None
        self._member_id = None
        self._member_role_type = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def map_id_type(self):
        return self._map_id_type

    @map_id_type.setter
    def map_id_type(self, value):
        self._map_id_type = value
    @property
    def map_id_value(self):
        return self._map_id_value

    @map_id_value.setter
    def map_id_value(self, value):
        self._map_id_value = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def member_role_type(self):
        return self._member_role_type

    @member_role_type.setter
    def member_role_type(self, value):
        self._member_role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.map_id_type:
            if hasattr(self.map_id_type, 'to_alipay_dict'):
                params['map_id_type'] = self.map_id_type.to_alipay_dict()
            else:
                params['map_id_type'] = self.map_id_type
        if self.map_id_value:
            if hasattr(self.map_id_value, 'to_alipay_dict'):
                params['map_id_value'] = self.map_id_value.to_alipay_dict()
            else:
                params['map_id_value'] = self.map_id_value
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.member_role_type:
            if hasattr(self.member_role_type, 'to_alipay_dict'):
                params['member_role_type'] = self.member_role_type.to_alipay_dict()
            else:
                params['member_role_type'] = self.member_role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinCustomerMemberQueryModel()
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'map_id_type' in d:
            o.map_id_type = d['map_id_type']
        if 'map_id_value' in d:
            o.map_id_value = d['map_id_value']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'member_role_type' in d:
            o.member_role_type = d['member_role_type']
        return o


