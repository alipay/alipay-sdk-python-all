#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ToppingsInfo import ToppingsInfo
from alipay.aop.api.domain.GroupRestrictionInfo import GroupRestrictionInfo


class ToppingsGroupInfo(object):

    def __init__(self):
        self._id = None
        self._name = None
        self._optional_toppings = None
        self._restriction_info = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def optional_toppings(self):
        return self._optional_toppings

    @optional_toppings.setter
    def optional_toppings(self, value):
        if isinstance(value, list):
            self._optional_toppings = list()
            for i in value:
                if isinstance(i, ToppingsInfo):
                    self._optional_toppings.append(i)
                else:
                    self._optional_toppings.append(ToppingsInfo.from_alipay_dict(i))
    @property
    def restriction_info(self):
        return self._restriction_info

    @restriction_info.setter
    def restriction_info(self, value):
        if isinstance(value, GroupRestrictionInfo):
            self._restriction_info = value
        else:
            self._restriction_info = GroupRestrictionInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.optional_toppings:
            if isinstance(self.optional_toppings, list):
                for i in range(0, len(self.optional_toppings)):
                    element = self.optional_toppings[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.optional_toppings[i] = element.to_alipay_dict()
            if hasattr(self.optional_toppings, 'to_alipay_dict'):
                params['optional_toppings'] = self.optional_toppings.to_alipay_dict()
            else:
                params['optional_toppings'] = self.optional_toppings
        if self.restriction_info:
            if hasattr(self.restriction_info, 'to_alipay_dict'):
                params['restriction_info'] = self.restriction_info.to_alipay_dict()
            else:
                params['restriction_info'] = self.restriction_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ToppingsGroupInfo()
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'optional_toppings' in d:
            o.optional_toppings = d['optional_toppings']
        if 'restriction_info' in d:
            o.restriction_info = d['restriction_info']
        return o


