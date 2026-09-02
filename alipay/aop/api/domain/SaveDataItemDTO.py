#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FieldInfoDTO import FieldInfoDTO
from alipay.aop.api.domain.SaveRecordDTO import SaveRecordDTO


class SaveDataItemDTO(object):

    def __init__(self):
        self._attribute_key = None
        self._cert_source = None
        self._fields = None
        self._records = None

    @property
    def attribute_key(self):
        return self._attribute_key

    @attribute_key.setter
    def attribute_key(self, value):
        self._attribute_key = value
    @property
    def cert_source(self):
        return self._cert_source

    @cert_source.setter
    def cert_source(self, value):
        self._cert_source = value
    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        if isinstance(value, list):
            self._fields = list()
            for i in value:
                if isinstance(i, FieldInfoDTO):
                    self._fields.append(i)
                else:
                    self._fields.append(FieldInfoDTO.from_alipay_dict(i))
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, SaveRecordDTO):
                    self._records.append(i)
                else:
                    self._records.append(SaveRecordDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.attribute_key:
            if hasattr(self.attribute_key, 'to_alipay_dict'):
                params['attribute_key'] = self.attribute_key.to_alipay_dict()
            else:
                params['attribute_key'] = self.attribute_key
        if self.cert_source:
            if hasattr(self.cert_source, 'to_alipay_dict'):
                params['cert_source'] = self.cert_source.to_alipay_dict()
            else:
                params['cert_source'] = self.cert_source
        if self.fields:
            if isinstance(self.fields, list):
                for i in range(0, len(self.fields)):
                    element = self.fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fields[i] = element.to_alipay_dict()
            if hasattr(self.fields, 'to_alipay_dict'):
                params['fields'] = self.fields.to_alipay_dict()
            else:
                params['fields'] = self.fields
        if self.records:
            if isinstance(self.records, list):
                for i in range(0, len(self.records)):
                    element = self.records[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.records[i] = element.to_alipay_dict()
            if hasattr(self.records, 'to_alipay_dict'):
                params['records'] = self.records.to_alipay_dict()
            else:
                params['records'] = self.records
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaveDataItemDTO()
        if 'attribute_key' in d:
            o.attribute_key = d['attribute_key']
        if 'cert_source' in d:
            o.cert_source = d['cert_source']
        if 'fields' in d:
            o.fields = d['fields']
        if 'records' in d:
            o.records = d['records']
        return o


