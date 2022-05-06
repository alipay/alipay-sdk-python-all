#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnergyGeneratedDTO import EnergyGeneratedDTO


class ReceiptEnergyInfoDTO(object):

    def __init__(self):
        self._code = None
        self._energy_generated = None
        self._full_energy = None
        self._out_biz_no = None
        self._retryable = None
        self._success = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def energy_generated(self):
        return self._energy_generated

    @energy_generated.setter
    def energy_generated(self, value):
        if isinstance(value, list):
            self._energy_generated = list()
            for i in value:
                if isinstance(i, EnergyGeneratedDTO):
                    self._energy_generated.append(i)
                else:
                    self._energy_generated.append(EnergyGeneratedDTO.from_alipay_dict(i))
    @property
    def full_energy(self):
        return self._full_energy

    @full_energy.setter
    def full_energy(self, value):
        self._full_energy = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def retryable(self):
        return self._retryable

    @retryable.setter
    def retryable(self, value):
        self._retryable = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.energy_generated:
            if isinstance(self.energy_generated, list):
                for i in range(0, len(self.energy_generated)):
                    element = self.energy_generated[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.energy_generated[i] = element.to_alipay_dict()
            if hasattr(self.energy_generated, 'to_alipay_dict'):
                params['energy_generated'] = self.energy_generated.to_alipay_dict()
            else:
                params['energy_generated'] = self.energy_generated
        if self.full_energy:
            if hasattr(self.full_energy, 'to_alipay_dict'):
                params['full_energy'] = self.full_energy.to_alipay_dict()
            else:
                params['full_energy'] = self.full_energy
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.retryable:
            if hasattr(self.retryable, 'to_alipay_dict'):
                params['retryable'] = self.retryable.to_alipay_dict()
            else:
                params['retryable'] = self.retryable
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiptEnergyInfoDTO()
        if 'code' in d:
            o.code = d['code']
        if 'energy_generated' in d:
            o.energy_generated = d['energy_generated']
        if 'full_energy' in d:
            o.full_energy = d['full_energy']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'retryable' in d:
            o.retryable = d['retryable']
        if 'success' in d:
            o.success = d['success']
        return o


