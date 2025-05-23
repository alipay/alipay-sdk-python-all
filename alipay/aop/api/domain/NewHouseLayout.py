#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewHouseLayout(object):

    def __init__(self):
        self._buildings = None
        self._constructed_area = None
        self._estate_project_id = None
        self._external_id = None
        self._introduction = None
        self._layout_id = None
        self._name = None
        self._orientation = None
        self._price = None

    @property
    def buildings(self):
        return self._buildings

    @buildings.setter
    def buildings(self, value):
        self._buildings = value
    @property
    def constructed_area(self):
        return self._constructed_area

    @constructed_area.setter
    def constructed_area(self, value):
        self._constructed_area = value
    @property
    def estate_project_id(self):
        return self._estate_project_id

    @estate_project_id.setter
    def estate_project_id(self, value):
        self._estate_project_id = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
    @property
    def layout_id(self):
        return self._layout_id

    @layout_id.setter
    def layout_id(self, value):
        self._layout_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        self._orientation = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.buildings:
            if hasattr(self.buildings, 'to_alipay_dict'):
                params['buildings'] = self.buildings.to_alipay_dict()
            else:
                params['buildings'] = self.buildings
        if self.constructed_area:
            if hasattr(self.constructed_area, 'to_alipay_dict'):
                params['constructed_area'] = self.constructed_area.to_alipay_dict()
            else:
                params['constructed_area'] = self.constructed_area
        if self.estate_project_id:
            if hasattr(self.estate_project_id, 'to_alipay_dict'):
                params['estate_project_id'] = self.estate_project_id.to_alipay_dict()
            else:
                params['estate_project_id'] = self.estate_project_id
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.introduction:
            if hasattr(self.introduction, 'to_alipay_dict'):
                params['introduction'] = self.introduction.to_alipay_dict()
            else:
                params['introduction'] = self.introduction
        if self.layout_id:
            if hasattr(self.layout_id, 'to_alipay_dict'):
                params['layout_id'] = self.layout_id.to_alipay_dict()
            else:
                params['layout_id'] = self.layout_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.orientation:
            if hasattr(self.orientation, 'to_alipay_dict'):
                params['orientation'] = self.orientation.to_alipay_dict()
            else:
                params['orientation'] = self.orientation
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NewHouseLayout()
        if 'buildings' in d:
            o.buildings = d['buildings']
        if 'constructed_area' in d:
            o.constructed_area = d['constructed_area']
        if 'estate_project_id' in d:
            o.estate_project_id = d['estate_project_id']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'introduction' in d:
            o.introduction = d['introduction']
        if 'layout_id' in d:
            o.layout_id = d['layout_id']
        if 'name' in d:
            o.name = d['name']
        if 'orientation' in d:
            o.orientation = d['orientation']
        if 'price' in d:
            o.price = d['price']
        return o


