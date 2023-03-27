#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitMaterialInfo import RecruitMaterialInfo


class RecruitEnrollMaterial(object):

    def __init__(self):
        self._materials = None

    @property
    def materials(self):
        return self._materials

    @materials.setter
    def materials(self, value):
        if isinstance(value, list):
            self._materials = list()
            for i in value:
                if isinstance(i, RecruitMaterialInfo):
                    self._materials.append(i)
                else:
                    self._materials.append(RecruitMaterialInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.materials:
            if isinstance(self.materials, list):
                for i in range(0, len(self.materials)):
                    element = self.materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.materials[i] = element.to_alipay_dict()
            if hasattr(self.materials, 'to_alipay_dict'):
                params['materials'] = self.materials.to_alipay_dict()
            else:
                params['materials'] = self.materials
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitEnrollMaterial()
        if 'materials' in d:
            o.materials = d['materials']
        return o


