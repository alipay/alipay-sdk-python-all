#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Recurring import Recurring


class NexusSimplePrice(object):

    def __init__(self):
        self._active = None
        self._id = None
        self._metadata = None
        self._recurring = None
        self._type = None
        self._unit_amount = None

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
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
    def recurring(self):
        return self._recurring

    @recurring.setter
    def recurring(self, value):
        if isinstance(value, Recurring):
            self._recurring = value
        else:
            self._recurring = Recurring.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self._unit_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.active:
            if hasattr(self.active, 'to_alipay_dict'):
                params['active'] = self.active.to_alipay_dict()
            else:
                params['active'] = self.active
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
        if self.recurring:
            if hasattr(self.recurring, 'to_alipay_dict'):
                params['recurring'] = self.recurring.to_alipay_dict()
            else:
                params['recurring'] = self.recurring
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.unit_amount:
            if hasattr(self.unit_amount, 'to_alipay_dict'):
                params['unit_amount'] = self.unit_amount.to_alipay_dict()
            else:
                params['unit_amount'] = self.unit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NexusSimplePrice()
        if 'active' in d:
            o.active = d['active']
        if 'id' in d:
            o.id = d['id']
        if 'metadata' in d:
            o.metadata = d['metadata']
        if 'recurring' in d:
            o.recurring = d['recurring']
        if 'type' in d:
            o.type = d['type']
        if 'unit_amount' in d:
            o.unit_amount = d['unit_amount']
        return o


