#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicineSpu import MedicineSpu


class AlipayCommerceMedicalMedicineSpuModifyModel(object):

    def __init__(self):
        self._spu = None

    @property
    def spu(self):
        return self._spu

    @spu.setter
    def spu(self, value):
        if isinstance(value, MedicineSpu):
            self._spu = value
        else:
            self._spu = MedicineSpu.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.spu:
            if hasattr(self.spu, 'to_alipay_dict'):
                params['spu'] = self.spu.to_alipay_dict()
            else:
                params['spu'] = self.spu
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedicineSpuModifyModel()
        if 'spu' in d:
            o.spu = d['spu']
        return o


