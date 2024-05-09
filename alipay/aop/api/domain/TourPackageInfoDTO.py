#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TourPackageInfoDTO(object):

    def __init__(self):
        self._departure_time = None
        self._identity_card = None
        self._mobile = None
        self._name = None
        self._population = None
        self._return_time = None

    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value):
        self._departure_time = value
    @property
    def identity_card(self):
        return self._identity_card

    @identity_card.setter
    def identity_card(self, value):
        self._identity_card = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value
    @property
    def return_time(self):
        return self._return_time

    @return_time.setter
    def return_time(self, value):
        self._return_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.departure_time:
            if hasattr(self.departure_time, 'to_alipay_dict'):
                params['departure_time'] = self.departure_time.to_alipay_dict()
            else:
                params['departure_time'] = self.departure_time
        if self.identity_card:
            if hasattr(self.identity_card, 'to_alipay_dict'):
                params['identity_card'] = self.identity_card.to_alipay_dict()
            else:
                params['identity_card'] = self.identity_card
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.population:
            if hasattr(self.population, 'to_alipay_dict'):
                params['population'] = self.population.to_alipay_dict()
            else:
                params['population'] = self.population
        if self.return_time:
            if hasattr(self.return_time, 'to_alipay_dict'):
                params['return_time'] = self.return_time.to_alipay_dict()
            else:
                params['return_time'] = self.return_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TourPackageInfoDTO()
        if 'departure_time' in d:
            o.departure_time = d['departure_time']
        if 'identity_card' in d:
            o.identity_card = d['identity_card']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'population' in d:
            o.population = d['population']
        if 'return_time' in d:
            o.return_time = d['return_time']
        return o


