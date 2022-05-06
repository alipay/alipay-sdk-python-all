#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnergyGeneratedDTO(object):

    def __init__(self):
        self._energy = None
        self._key = None

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value


    def to_alipay_dict(self):
        params = dict()
        if self.energy:
            if hasattr(self.energy, 'to_alipay_dict'):
                params['energy'] = self.energy.to_alipay_dict()
            else:
                params['energy'] = self.energy
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnergyGeneratedDTO()
        if 'energy' in d:
            o.energy = d['energy']
        if 'key' in d:
            o.key = d['key']
        return o


