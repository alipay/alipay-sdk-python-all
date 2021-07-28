#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HelloBikePriceCondition import HelloBikePriceCondition
from alipay.aop.api.domain.HelloBikePriceConstraint import HelloBikePriceConstraint


class AlipayDataAiserviceSmartpriceGetModel(object):

    def __init__(self):
        self._ad_source = None
        self._base_price_cent = None
        self._card_type_version = None
        self._channel = None
        self._city_code = None
        self._conditions = None
        self._constraints = None
        self._default_promo_price_cent = None
        self._from = None
        self._high_price_cent = None
        self._lower_price_cent = None
        self._plat_form = None
        self._rank = None
        self._scene_code = None
        self._system_code = None
        self._trace_id = None
        self._user_id = None

    @property
    def ad_source(self):
        return self._ad_source

    @ad_source.setter
    def ad_source(self, value):
        self._ad_source = value
    @property
    def base_price_cent(self):
        return self._base_price_cent

    @base_price_cent.setter
    def base_price_cent(self, value):
        self._base_price_cent = value
    @property
    def card_type_version(self):
        return self._card_type_version

    @card_type_version.setter
    def card_type_version(self, value):
        self._card_type_version = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        if isinstance(value, list):
            self._conditions = list()
            for i in value:
                if isinstance(i, HelloBikePriceCondition):
                    self._conditions.append(i)
                else:
                    self._conditions.append(HelloBikePriceCondition.from_alipay_dict(i))
    @property
    def constraints(self):
        return self._constraints

    @constraints.setter
    def constraints(self, value):
        if isinstance(value, list):
            self._constraints = list()
            for i in value:
                if isinstance(i, HelloBikePriceConstraint):
                    self._constraints.append(i)
                else:
                    self._constraints.append(HelloBikePriceConstraint.from_alipay_dict(i))
    @property
    def default_promo_price_cent(self):
        return self._default_promo_price_cent

    @default_promo_price_cent.setter
    def default_promo_price_cent(self, value):
        self._default_promo_price_cent = value
    @property
    def from(self):
        return self._from

    @from.setter
    def from(self, value):
        self._from = value
    @property
    def high_price_cent(self):
        return self._high_price_cent

    @high_price_cent.setter
    def high_price_cent(self, value):
        self._high_price_cent = value
    @property
    def lower_price_cent(self):
        return self._lower_price_cent

    @lower_price_cent.setter
    def lower_price_cent(self, value):
        self._lower_price_cent = value
    @property
    def plat_form(self):
        return self._plat_form

    @plat_form.setter
    def plat_form(self, value):
        self._plat_form = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def system_code(self):
        return self._system_code

    @system_code.setter
    def system_code(self, value):
        self._system_code = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_source:
            if hasattr(self.ad_source, 'to_alipay_dict'):
                params['ad_source'] = self.ad_source.to_alipay_dict()
            else:
                params['ad_source'] = self.ad_source
        if self.base_price_cent:
            if hasattr(self.base_price_cent, 'to_alipay_dict'):
                params['base_price_cent'] = self.base_price_cent.to_alipay_dict()
            else:
                params['base_price_cent'] = self.base_price_cent
        if self.card_type_version:
            if hasattr(self.card_type_version, 'to_alipay_dict'):
                params['card_type_version'] = self.card_type_version.to_alipay_dict()
            else:
                params['card_type_version'] = self.card_type_version
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.conditions:
            if isinstance(self.conditions, list):
                for i in range(0, len(self.conditions)):
                    element = self.conditions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conditions[i] = element.to_alipay_dict()
            if hasattr(self.conditions, 'to_alipay_dict'):
                params['conditions'] = self.conditions.to_alipay_dict()
            else:
                params['conditions'] = self.conditions
        if self.constraints:
            if isinstance(self.constraints, list):
                for i in range(0, len(self.constraints)):
                    element = self.constraints[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.constraints[i] = element.to_alipay_dict()
            if hasattr(self.constraints, 'to_alipay_dict'):
                params['constraints'] = self.constraints.to_alipay_dict()
            else:
                params['constraints'] = self.constraints
        if self.default_promo_price_cent:
            if hasattr(self.default_promo_price_cent, 'to_alipay_dict'):
                params['default_promo_price_cent'] = self.default_promo_price_cent.to_alipay_dict()
            else:
                params['default_promo_price_cent'] = self.default_promo_price_cent
        if self.from:
            if hasattr(self.from, 'to_alipay_dict'):
                params['from'] = self.from.to_alipay_dict()
            else:
                params['from'] = self.from
        if self.high_price_cent:
            if hasattr(self.high_price_cent, 'to_alipay_dict'):
                params['high_price_cent'] = self.high_price_cent.to_alipay_dict()
            else:
                params['high_price_cent'] = self.high_price_cent
        if self.lower_price_cent:
            if hasattr(self.lower_price_cent, 'to_alipay_dict'):
                params['lower_price_cent'] = self.lower_price_cent.to_alipay_dict()
            else:
                params['lower_price_cent'] = self.lower_price_cent
        if self.plat_form:
            if hasattr(self.plat_form, 'to_alipay_dict'):
                params['plat_form'] = self.plat_form.to_alipay_dict()
            else:
                params['plat_form'] = self.plat_form
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.system_code:
            if hasattr(self.system_code, 'to_alipay_dict'):
                params['system_code'] = self.system_code.to_alipay_dict()
            else:
                params['system_code'] = self.system_code
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
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
        o = AlipayDataAiserviceSmartpriceGetModel()
        if 'ad_source' in d:
            o.ad_source = d['ad_source']
        if 'base_price_cent' in d:
            o.base_price_cent = d['base_price_cent']
        if 'card_type_version' in d:
            o.card_type_version = d['card_type_version']
        if 'channel' in d:
            o.channel = d['channel']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'conditions' in d:
            o.conditions = d['conditions']
        if 'constraints' in d:
            o.constraints = d['constraints']
        if 'default_promo_price_cent' in d:
            o.default_promo_price_cent = d['default_promo_price_cent']
        if 'from' in d:
            o.from = d['from']
        if 'high_price_cent' in d:
            o.high_price_cent = d['high_price_cent']
        if 'lower_price_cent' in d:
            o.lower_price_cent = d['lower_price_cent']
        if 'plat_form' in d:
            o.plat_form = d['plat_form']
        if 'rank' in d:
            o.rank = d['rank']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'system_code' in d:
            o.system_code = d['system_code']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


