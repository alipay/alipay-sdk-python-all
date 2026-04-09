#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NexusSimplePrice import NexusSimplePrice


class NexusPayProduct(object):

    def __init__(self):
        self._active = None
        self._default_price = None
        self._default_price_id = None
        self._description = None
        self._gmt_create = None
        self._id = None
        self._metadata = None
        self._name = None

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
    @property
    def default_price(self):
        return self._default_price

    @default_price.setter
    def default_price(self, value):
        if isinstance(value, NexusSimplePrice):
            self._default_price = value
        else:
            self._default_price = NexusSimplePrice.from_alipay_dict(value)
    @property
    def default_price_id(self):
        return self._default_price_id

    @default_price_id.setter
    def default_price_id(self, value):
        self._default_price_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.active:
            if hasattr(self.active, 'to_alipay_dict'):
                params['active'] = self.active.to_alipay_dict()
            else:
                params['active'] = self.active
        if self.default_price:
            if hasattr(self.default_price, 'to_alipay_dict'):
                params['default_price'] = self.default_price.to_alipay_dict()
            else:
                params['default_price'] = self.default_price
        if self.default_price_id:
            if hasattr(self.default_price_id, 'to_alipay_dict'):
                params['default_price_id'] = self.default_price_id.to_alipay_dict()
            else:
                params['default_price_id'] = self.default_price_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.metadata:
            if hasattr(self.metadata, 'to_alipay_dict'):
                params['metadata'] = self.metadata.to_alipay_dict()
            else:
                params['metadata'] = self.metadata
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NexusPayProduct()
        if 'active' in d:
            o.active = d['active']
        if 'default_price' in d:
            o.default_price = d['default_price']
        if 'default_price_id' in d:
            o.default_price_id = d['default_price_id']
        if 'description' in d:
            o.description = d['description']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'id' in d:
            o.id = d['id']
        if 'metadata' in d:
            o.metadata = d['metadata']
        if 'name' in d:
            o.name = d['name']
        return o


