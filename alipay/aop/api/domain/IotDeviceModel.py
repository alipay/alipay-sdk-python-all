#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotDeviceModel(object):

    def __init__(self):
        self._category_id = None
        self._connection_types = None
        self._connection_url = None
        self._decription = None
        self._icon = None
        self._manufacturer = None
        self._model_id = None
        self._model_name = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def connection_types(self):
        return self._connection_types

    @connection_types.setter
    def connection_types(self, value):
        if isinstance(value, list):
            self._connection_types = list()
            for i in value:
                self._connection_types.append(i)
    @property
    def connection_url(self):
        return self._connection_url

    @connection_url.setter
    def connection_url(self, value):
        self._connection_url = value
    @property
    def decription(self):
        return self._decription

    @decription.setter
    def decription(self, value):
        self._decription = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.connection_types:
            if isinstance(self.connection_types, list):
                for i in range(0, len(self.connection_types)):
                    element = self.connection_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.connection_types[i] = element.to_alipay_dict()
            if hasattr(self.connection_types, 'to_alipay_dict'):
                params['connection_types'] = self.connection_types.to_alipay_dict()
            else:
                params['connection_types'] = self.connection_types
        if self.connection_url:
            if hasattr(self.connection_url, 'to_alipay_dict'):
                params['connection_url'] = self.connection_url.to_alipay_dict()
            else:
                params['connection_url'] = self.connection_url
        if self.decription:
            if hasattr(self.decription, 'to_alipay_dict'):
                params['decription'] = self.decription.to_alipay_dict()
            else:
                params['decription'] = self.decription
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.manufacturer:
            if hasattr(self.manufacturer, 'to_alipay_dict'):
                params['manufacturer'] = self.manufacturer.to_alipay_dict()
            else:
                params['manufacturer'] = self.manufacturer
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        if self.model_name:
            if hasattr(self.model_name, 'to_alipay_dict'):
                params['model_name'] = self.model_name.to_alipay_dict()
            else:
                params['model_name'] = self.model_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotDeviceModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'connection_types' in d:
            o.connection_types = d['connection_types']
        if 'connection_url' in d:
            o.connection_url = d['connection_url']
        if 'decription' in d:
            o.decription = d['decription']
        if 'icon' in d:
            o.icon = d['icon']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'model_name' in d:
            o.model_name = d['model_name']
        return o


