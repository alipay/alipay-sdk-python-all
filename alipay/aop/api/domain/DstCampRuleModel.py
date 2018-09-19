#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DstCampRuleModel(object):

    def __init__(self):
        self._alipay_cashier = None
        self._discount_type = None
        self._id = None
        self._prize_count_per_account = None
        self._product_type = None
        self._rule_uuid = None
        self._voucher_id = None

    @property
    def alipay_cashier(self):
        return self._alipay_cashier

    @alipay_cashier.setter
    def alipay_cashier(self, value):
        self._alipay_cashier = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def prize_count_per_account(self):
        return self._prize_count_per_account

    @prize_count_per_account.setter
    def prize_count_per_account(self, value):
        self._prize_count_per_account = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def rule_uuid(self):
        return self._rule_uuid

    @rule_uuid.setter
    def rule_uuid(self, value):
        self._rule_uuid = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_cashier:
            if hasattr(self.alipay_cashier, 'to_alipay_dict'):
                params['alipay_cashier'] = self.alipay_cashier.to_alipay_dict()
            else:
                params['alipay_cashier'] = self.alipay_cashier
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.prize_count_per_account:
            if hasattr(self.prize_count_per_account, 'to_alipay_dict'):
                params['prize_count_per_account'] = self.prize_count_per_account.to_alipay_dict()
            else:
                params['prize_count_per_account'] = self.prize_count_per_account
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.rule_uuid:
            if hasattr(self.rule_uuid, 'to_alipay_dict'):
                params['rule_uuid'] = self.rule_uuid.to_alipay_dict()
            else:
                params['rule_uuid'] = self.rule_uuid
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DstCampRuleModel()
        if 'alipay_cashier' in d:
            o.alipay_cashier = d['alipay_cashier']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'id' in d:
            o.id = d['id']
        if 'prize_count_per_account' in d:
            o.prize_count_per_account = d['prize_count_per_account']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'rule_uuid' in d:
            o.rule_uuid = d['rule_uuid']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


