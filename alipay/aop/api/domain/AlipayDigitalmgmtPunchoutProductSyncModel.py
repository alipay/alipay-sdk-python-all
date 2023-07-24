#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PunchoutAccessProductDTO import PunchoutAccessProductDTO


class AlipayDigitalmgmtPunchoutProductSyncModel(object):

    def __init__(self):
        self._access_product_dtos = None

    @property
    def access_product_dtos(self):
        return self._access_product_dtos

    @access_product_dtos.setter
    def access_product_dtos(self, value):
        if isinstance(value, list):
            self._access_product_dtos = list()
            for i in value:
                if isinstance(i, PunchoutAccessProductDTO):
                    self._access_product_dtos.append(i)
                else:
                    self._access_product_dtos.append(PunchoutAccessProductDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.access_product_dtos:
            if isinstance(self.access_product_dtos, list):
                for i in range(0, len(self.access_product_dtos)):
                    element = self.access_product_dtos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.access_product_dtos[i] = element.to_alipay_dict()
            if hasattr(self.access_product_dtos, 'to_alipay_dict'):
                params['access_product_dtos'] = self.access_product_dtos.to_alipay_dict()
            else:
                params['access_product_dtos'] = self.access_product_dtos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtPunchoutProductSyncModel()
        if 'access_product_dtos' in d:
            o.access_product_dtos = d['access_product_dtos']
        return o


