#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbasePersonalIdentityCreateModel(object):

    def __init__(self):
        self._full_name = None
        self._id_number = None
        self._passport_id = None

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.full_name:
            if hasattr(self.full_name, 'to_alipay_dict'):
                params['full_name'] = self.full_name.to_alipay_dict()
            else:
                params['full_name'] = self.full_name
        if self.id_number:
            if hasattr(self.id_number, 'to_alipay_dict'):
                params['id_number'] = self.id_number.to_alipay_dict()
            else:
                params['id_number'] = self.id_number
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbasePersonalIdentityCreateModel()
        if 'full_name' in d:
            o.full_name = d['full_name']
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        return o


