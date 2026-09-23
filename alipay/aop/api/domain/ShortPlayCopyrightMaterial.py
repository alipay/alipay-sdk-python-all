#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShortPlayCopyrightMaterial(object):

    def __init__(self):
        self._commitment_material_ids = None
        self._license_material_ids = None
        self._ownership_material_ids = None
        self._title_modification_material_id = None

    @property
    def commitment_material_ids(self):
        return self._commitment_material_ids

    @commitment_material_ids.setter
    def commitment_material_ids(self, value):
        if isinstance(value, list):
            self._commitment_material_ids = list()
            for i in value:
                self._commitment_material_ids.append(i)
    @property
    def license_material_ids(self):
        return self._license_material_ids

    @license_material_ids.setter
    def license_material_ids(self, value):
        if isinstance(value, list):
            self._license_material_ids = list()
            for i in value:
                self._license_material_ids.append(i)
    @property
    def ownership_material_ids(self):
        return self._ownership_material_ids

    @ownership_material_ids.setter
    def ownership_material_ids(self, value):
        if isinstance(value, list):
            self._ownership_material_ids = list()
            for i in value:
                self._ownership_material_ids.append(i)
    @property
    def title_modification_material_id(self):
        return self._title_modification_material_id

    @title_modification_material_id.setter
    def title_modification_material_id(self, value):
        self._title_modification_material_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commitment_material_ids:
            if isinstance(self.commitment_material_ids, list):
                for i in range(0, len(self.commitment_material_ids)):
                    element = self.commitment_material_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commitment_material_ids[i] = element.to_alipay_dict()
            if hasattr(self.commitment_material_ids, 'to_alipay_dict'):
                params['commitment_material_ids'] = self.commitment_material_ids.to_alipay_dict()
            else:
                params['commitment_material_ids'] = self.commitment_material_ids
        if self.license_material_ids:
            if isinstance(self.license_material_ids, list):
                for i in range(0, len(self.license_material_ids)):
                    element = self.license_material_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.license_material_ids[i] = element.to_alipay_dict()
            if hasattr(self.license_material_ids, 'to_alipay_dict'):
                params['license_material_ids'] = self.license_material_ids.to_alipay_dict()
            else:
                params['license_material_ids'] = self.license_material_ids
        if self.ownership_material_ids:
            if isinstance(self.ownership_material_ids, list):
                for i in range(0, len(self.ownership_material_ids)):
                    element = self.ownership_material_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ownership_material_ids[i] = element.to_alipay_dict()
            if hasattr(self.ownership_material_ids, 'to_alipay_dict'):
                params['ownership_material_ids'] = self.ownership_material_ids.to_alipay_dict()
            else:
                params['ownership_material_ids'] = self.ownership_material_ids
        if self.title_modification_material_id:
            if hasattr(self.title_modification_material_id, 'to_alipay_dict'):
                params['title_modification_material_id'] = self.title_modification_material_id.to_alipay_dict()
            else:
                params['title_modification_material_id'] = self.title_modification_material_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShortPlayCopyrightMaterial()
        if 'commitment_material_ids' in d:
            o.commitment_material_ids = d['commitment_material_ids']
        if 'license_material_ids' in d:
            o.license_material_ids = d['license_material_ids']
        if 'ownership_material_ids' in d:
            o.ownership_material_ids = d['ownership_material_ids']
        if 'title_modification_material_id' in d:
            o.title_modification_material_id = d['title_modification_material_id']
        return o


