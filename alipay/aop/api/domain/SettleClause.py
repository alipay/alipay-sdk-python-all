#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubMerchant import SubMerchant


class SettleClause(object):

    def __init__(self):
        self._amount = None
        self._currency = None
        self._settle_account_entity = None
        self._settle_account_id = None
        self._settle_account_id_type = None
        self._settle_account_type = None
        self._settle_entity_id = None
        self._settle_entity_type = None
        self._sub_merchant = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def settle_account_entity(self):
        return self._settle_account_entity

    @settle_account_entity.setter
    def settle_account_entity(self, value):
        self._settle_account_entity = value
    @property
    def settle_account_id(self):
        return self._settle_account_id

    @settle_account_id.setter
    def settle_account_id(self, value):
        self._settle_account_id = value
    @property
    def settle_account_id_type(self):
        return self._settle_account_id_type

    @settle_account_id_type.setter
    def settle_account_id_type(self, value):
        self._settle_account_id_type = value
    @property
    def settle_account_type(self):
        return self._settle_account_type

    @settle_account_type.setter
    def settle_account_type(self, value):
        self._settle_account_type = value
    @property
    def settle_entity_id(self):
        return self._settle_entity_id

    @settle_entity_id.setter
    def settle_entity_id(self, value):
        self._settle_entity_id = value
    @property
    def settle_entity_type(self):
        return self._settle_entity_type

    @settle_entity_type.setter
    def settle_entity_type(self, value):
        self._settle_entity_type = value
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SubMerchant):
            self._sub_merchant = value
        else:
            self._sub_merchant = SubMerchant.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.settle_account_entity:
            if hasattr(self.settle_account_entity, 'to_alipay_dict'):
                params['settle_account_entity'] = self.settle_account_entity.to_alipay_dict()
            else:
                params['settle_account_entity'] = self.settle_account_entity
        if self.settle_account_id:
            if hasattr(self.settle_account_id, 'to_alipay_dict'):
                params['settle_account_id'] = self.settle_account_id.to_alipay_dict()
            else:
                params['settle_account_id'] = self.settle_account_id
        if self.settle_account_id_type:
            if hasattr(self.settle_account_id_type, 'to_alipay_dict'):
                params['settle_account_id_type'] = self.settle_account_id_type.to_alipay_dict()
            else:
                params['settle_account_id_type'] = self.settle_account_id_type
        if self.settle_account_type:
            if hasattr(self.settle_account_type, 'to_alipay_dict'):
                params['settle_account_type'] = self.settle_account_type.to_alipay_dict()
            else:
                params['settle_account_type'] = self.settle_account_type
        if self.settle_entity_id:
            if hasattr(self.settle_entity_id, 'to_alipay_dict'):
                params['settle_entity_id'] = self.settle_entity_id.to_alipay_dict()
            else:
                params['settle_entity_id'] = self.settle_entity_id
        if self.settle_entity_type:
            if hasattr(self.settle_entity_type, 'to_alipay_dict'):
                params['settle_entity_type'] = self.settle_entity_type.to_alipay_dict()
            else:
                params['settle_entity_type'] = self.settle_entity_type
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleClause()
        if 'amount' in d:
            o.amount = d['amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'settle_account_entity' in d:
            o.settle_account_entity = d['settle_account_entity']
        if 'settle_account_id' in d:
            o.settle_account_id = d['settle_account_id']
        if 'settle_account_id_type' in d:
            o.settle_account_id_type = d['settle_account_id_type']
        if 'settle_account_type' in d:
            o.settle_account_type = d['settle_account_type']
        if 'settle_entity_id' in d:
            o.settle_entity_id = d['settle_entity_id']
        if 'settle_entity_type' in d:
            o.settle_entity_type = d['settle_entity_type']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        return o


