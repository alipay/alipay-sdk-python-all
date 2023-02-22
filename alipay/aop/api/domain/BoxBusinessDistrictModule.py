#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BoxBusinessDistrictInfo import BoxBusinessDistrictInfo


class BoxBusinessDistrictModule(object):

    def __init__(self):
        self._business_district_infos = None
        self._module_id = None
        self._module_type = None

    @property
    def business_district_infos(self):
        return self._business_district_infos

    @business_district_infos.setter
    def business_district_infos(self, value):
        if isinstance(value, list):
            self._business_district_infos = list()
            for i in value:
                if isinstance(i, BoxBusinessDistrictInfo):
                    self._business_district_infos.append(i)
                else:
                    self._business_district_infos.append(BoxBusinessDistrictInfo.from_alipay_dict(i))
    @property
    def module_id(self):
        return self._module_id

    @module_id.setter
    def module_id(self, value):
        self._module_id = value
    @property
    def module_type(self):
        return self._module_type

    @module_type.setter
    def module_type(self, value):
        self._module_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_district_infos:
            if isinstance(self.business_district_infos, list):
                for i in range(0, len(self.business_district_infos)):
                    element = self.business_district_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_district_infos[i] = element.to_alipay_dict()
            if hasattr(self.business_district_infos, 'to_alipay_dict'):
                params['business_district_infos'] = self.business_district_infos.to_alipay_dict()
            else:
                params['business_district_infos'] = self.business_district_infos
        if self.module_id:
            if hasattr(self.module_id, 'to_alipay_dict'):
                params['module_id'] = self.module_id.to_alipay_dict()
            else:
                params['module_id'] = self.module_id
        if self.module_type:
            if hasattr(self.module_type, 'to_alipay_dict'):
                params['module_type'] = self.module_type.to_alipay_dict()
            else:
                params['module_type'] = self.module_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoxBusinessDistrictModule()
        if 'business_district_infos' in d:
            o.business_district_infos = d['business_district_infos']
        if 'module_id' in d:
            o.module_id = d['module_id']
        if 'module_type' in d:
            o.module_type = d['module_type']
        return o


