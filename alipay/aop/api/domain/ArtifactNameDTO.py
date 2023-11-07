#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryProjectArtifactDTO import DeliveryProjectArtifactDTO
from alipay.aop.api.domain.DeliveryProjectArtifactDTO import DeliveryProjectArtifactDTO


class ArtifactNameDTO(object):

    def __init__(self):
        self._other = None
        self._standard = None

    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, value):
        if isinstance(value, list):
            self._other = list()
            for i in value:
                if isinstance(i, DeliveryProjectArtifactDTO):
                    self._other.append(i)
                else:
                    self._other.append(DeliveryProjectArtifactDTO.from_alipay_dict(i))
    @property
    def standard(self):
        return self._standard

    @standard.setter
    def standard(self, value):
        if isinstance(value, list):
            self._standard = list()
            for i in value:
                if isinstance(i, DeliveryProjectArtifactDTO):
                    self._standard.append(i)
                else:
                    self._standard.append(DeliveryProjectArtifactDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.other:
            if isinstance(self.other, list):
                for i in range(0, len(self.other)):
                    element = self.other[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other[i] = element.to_alipay_dict()
            if hasattr(self.other, 'to_alipay_dict'):
                params['other'] = self.other.to_alipay_dict()
            else:
                params['other'] = self.other
        if self.standard:
            if isinstance(self.standard, list):
                for i in range(0, len(self.standard)):
                    element = self.standard[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.standard[i] = element.to_alipay_dict()
            if hasattr(self.standard, 'to_alipay_dict'):
                params['standard'] = self.standard.to_alipay_dict()
            else:
                params['standard'] = self.standard
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArtifactNameDTO()
        if 'other' in d:
            o.other = d['other']
        if 'standard' in d:
            o.standard = d['standard']
        return o


