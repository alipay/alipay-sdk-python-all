#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopServiceItem(object):

    def __init__(self):
        self._description = None
        self._name = None
        self._pictures = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pictures(self):
        return self._pictures

    @pictures.setter
    def pictures(self, value):
        if isinstance(value, list):
            self._pictures = list()
            for i in value:
                self._pictures.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pictures:
            if isinstance(self.pictures, list):
                for i in range(0, len(self.pictures)):
                    element = self.pictures[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pictures[i] = element.to_alipay_dict()
            if hasattr(self.pictures, 'to_alipay_dict'):
                params['pictures'] = self.pictures.to_alipay_dict()
            else:
                params['pictures'] = self.pictures
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopServiceItem()
        if 'description' in d:
            o.description = d['description']
        if 'name' in d:
            o.name = d['name']
        if 'pictures' in d:
            o.pictures = d['pictures']
        return o


