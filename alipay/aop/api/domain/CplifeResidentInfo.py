#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CplifeResidentInfo(object):

    def __init__(self):
        self._entity_id = None
        self._idcard_no = None
        self._name = None
        self._out_entity_id = None
        self._out_resident_id = None
        self._type = None

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def idcard_no(self):
        return self._idcard_no

    @idcard_no.setter
    def idcard_no(self, value):
        self._idcard_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_entity_id(self):
        return self._out_entity_id

    @out_entity_id.setter
    def out_entity_id(self, value):
        self._out_entity_id = value
    @property
    def out_resident_id(self):
        return self._out_resident_id

    @out_resident_id.setter
    def out_resident_id(self, value):
        self._out_resident_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.idcard_no:
            if hasattr(self.idcard_no, 'to_alipay_dict'):
                params['idcard_no'] = self.idcard_no.to_alipay_dict()
            else:
                params['idcard_no'] = self.idcard_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_entity_id:
            if hasattr(self.out_entity_id, 'to_alipay_dict'):
                params['out_entity_id'] = self.out_entity_id.to_alipay_dict()
            else:
                params['out_entity_id'] = self.out_entity_id
        if self.out_resident_id:
            if hasattr(self.out_resident_id, 'to_alipay_dict'):
                params['out_resident_id'] = self.out_resident_id.to_alipay_dict()
            else:
                params['out_resident_id'] = self.out_resident_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CplifeResidentInfo()
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'idcard_no' in d:
            o.idcard_no = d['idcard_no']
        if 'name' in d:
            o.name = d['name']
        if 'out_entity_id' in d:
            o.out_entity_id = d['out_entity_id']
        if 'out_resident_id' in d:
            o.out_resident_id = d['out_resident_id']
        if 'type' in d:
            o.type = d['type']
        return o


