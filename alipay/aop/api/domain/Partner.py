#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Partner(object):

    def __init__(self):
        self._need_seal_entity = None
        self._ou = None
        self._part_b_addr = None
        self._part_b_city = None
        self._part_b_country = None
        self._part_b_province = None
        self._partner_name = None

    @property
    def need_seal_entity(self):
        return self._need_seal_entity

    @need_seal_entity.setter
    def need_seal_entity(self, value):
        self._need_seal_entity = value
    @property
    def ou(self):
        return self._ou

    @ou.setter
    def ou(self, value):
        self._ou = value
    @property
    def part_b_addr(self):
        return self._part_b_addr

    @part_b_addr.setter
    def part_b_addr(self, value):
        self._part_b_addr = value
    @property
    def part_b_city(self):
        return self._part_b_city

    @part_b_city.setter
    def part_b_city(self, value):
        self._part_b_city = value
    @property
    def part_b_country(self):
        return self._part_b_country

    @part_b_country.setter
    def part_b_country(self, value):
        self._part_b_country = value
    @property
    def part_b_province(self):
        return self._part_b_province

    @part_b_province.setter
    def part_b_province(self, value):
        self._part_b_province = value
    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_seal_entity:
            if hasattr(self.need_seal_entity, 'to_alipay_dict'):
                params['need_seal_entity'] = self.need_seal_entity.to_alipay_dict()
            else:
                params['need_seal_entity'] = self.need_seal_entity
        if self.ou:
            if hasattr(self.ou, 'to_alipay_dict'):
                params['ou'] = self.ou.to_alipay_dict()
            else:
                params['ou'] = self.ou
        if self.part_b_addr:
            if hasattr(self.part_b_addr, 'to_alipay_dict'):
                params['part_b_addr'] = self.part_b_addr.to_alipay_dict()
            else:
                params['part_b_addr'] = self.part_b_addr
        if self.part_b_city:
            if hasattr(self.part_b_city, 'to_alipay_dict'):
                params['part_b_city'] = self.part_b_city.to_alipay_dict()
            else:
                params['part_b_city'] = self.part_b_city
        if self.part_b_country:
            if hasattr(self.part_b_country, 'to_alipay_dict'):
                params['part_b_country'] = self.part_b_country.to_alipay_dict()
            else:
                params['part_b_country'] = self.part_b_country
        if self.part_b_province:
            if hasattr(self.part_b_province, 'to_alipay_dict'):
                params['part_b_province'] = self.part_b_province.to_alipay_dict()
            else:
                params['part_b_province'] = self.part_b_province
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Partner()
        if 'need_seal_entity' in d:
            o.need_seal_entity = d['need_seal_entity']
        if 'ou' in d:
            o.ou = d['ou']
        if 'part_b_addr' in d:
            o.part_b_addr = d['part_b_addr']
        if 'part_b_city' in d:
            o.part_b_city = d['part_b_city']
        if 'part_b_country' in d:
            o.part_b_country = d['part_b_country']
        if 'part_b_province' in d:
            o.part_b_province = d['part_b_province']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        return o


