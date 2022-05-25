#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstAccountElementsDTO import InstAccountElementsDTO


class AlipayFincoreFunddsAccountWitnessCreateModel(object):

    def __init__(self):
        self._account_principal_type = None
        self._account_type = None
        self._external_entity_id = None
        self._inst_account_elements = None
        self._memo = None
        self._operator = None
        self._product_code = None
        self._user_id = None

    @property
    def account_principal_type(self):
        return self._account_principal_type

    @account_principal_type.setter
    def account_principal_type(self, value):
        self._account_principal_type = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def external_entity_id(self):
        return self._external_entity_id

    @external_entity_id.setter
    def external_entity_id(self, value):
        self._external_entity_id = value
    @property
    def inst_account_elements(self):
        return self._inst_account_elements

    @inst_account_elements.setter
    def inst_account_elements(self, value):
        if isinstance(value, InstAccountElementsDTO):
            self._inst_account_elements = value
        else:
            self._inst_account_elements = InstAccountElementsDTO.from_alipay_dict(value)
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_principal_type:
            if hasattr(self.account_principal_type, 'to_alipay_dict'):
                params['account_principal_type'] = self.account_principal_type.to_alipay_dict()
            else:
                params['account_principal_type'] = self.account_principal_type
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.external_entity_id:
            if hasattr(self.external_entity_id, 'to_alipay_dict'):
                params['external_entity_id'] = self.external_entity_id.to_alipay_dict()
            else:
                params['external_entity_id'] = self.external_entity_id
        if self.inst_account_elements:
            if hasattr(self.inst_account_elements, 'to_alipay_dict'):
                params['inst_account_elements'] = self.inst_account_elements.to_alipay_dict()
            else:
                params['inst_account_elements'] = self.inst_account_elements
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
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
        o = AlipayFincoreFunddsAccountWitnessCreateModel()
        if 'account_principal_type' in d:
            o.account_principal_type = d['account_principal_type']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'external_entity_id' in d:
            o.external_entity_id = d['external_entity_id']
        if 'inst_account_elements' in d:
            o.inst_account_elements = d['inst_account_elements']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


