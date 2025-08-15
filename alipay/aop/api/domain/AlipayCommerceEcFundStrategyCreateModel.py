#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcPayRestriction import EcPayRestriction


class AlipayCommerceEcFundStrategyCreateModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._fund_account_id = None
        self._name = None
        self._restrictions = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def fund_account_id(self):
        return self._fund_account_id

    @fund_account_id.setter
    def fund_account_id(self, value):
        self._fund_account_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def restrictions(self):
        return self._restrictions

    @restrictions.setter
    def restrictions(self, value):
        if isinstance(value, list):
            self._restrictions = list()
            for i in value:
                if isinstance(i, EcPayRestriction):
                    self._restrictions.append(i)
                else:
                    self._restrictions.append(EcPayRestriction.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.fund_account_id:
            if hasattr(self.fund_account_id, 'to_alipay_dict'):
                params['fund_account_id'] = self.fund_account_id.to_alipay_dict()
            else:
                params['fund_account_id'] = self.fund_account_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.restrictions:
            if isinstance(self.restrictions, list):
                for i in range(0, len(self.restrictions)):
                    element = self.restrictions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.restrictions[i] = element.to_alipay_dict()
            if hasattr(self.restrictions, 'to_alipay_dict'):
                params['restrictions'] = self.restrictions.to_alipay_dict()
            else:
                params['restrictions'] = self.restrictions
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcFundStrategyCreateModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'fund_account_id' in d:
            o.fund_account_id = d['fund_account_id']
        if 'name' in d:
            o.name = d['name']
        if 'restrictions' in d:
            o.restrictions = d['restrictions']
        return o


