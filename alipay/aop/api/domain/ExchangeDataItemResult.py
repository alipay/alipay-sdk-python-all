#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FieldInfoResult import FieldInfoResult
from alipay.aop.api.domain.ExchangeRecordResult import ExchangeRecordResult


class ExchangeDataItemResult(object):

    def __init__(self):
        self._attribute_key = None
        self._attribute_name = None
        self._cert_source = None
        self._cert_status = None
        self._fields = None
        self._records = None
        self._schema_type = None

    @property
    def attribute_key(self):
        return self._attribute_key

    @attribute_key.setter
    def attribute_key(self, value):
        self._attribute_key = value
    @property
    def attribute_name(self):
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, value):
        self._attribute_name = value
    @property
    def cert_source(self):
        return self._cert_source

    @cert_source.setter
    def cert_source(self, value):
        self._cert_source = value
    @property
    def cert_status(self):
        return self._cert_status

    @cert_status.setter
    def cert_status(self, value):
        self._cert_status = value
    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        if isinstance(value, list):
            self._fields = list()
            for i in value:
                if isinstance(i, FieldInfoResult):
                    self._fields.append(i)
                else:
                    self._fields.append(FieldInfoResult.from_alipay_dict(i))
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, ExchangeRecordResult):
                    self._records.append(i)
                else:
                    self._records.append(ExchangeRecordResult.from_alipay_dict(i))
    @property
    def schema_type(self):
        return self._schema_type

    @schema_type.setter
    def schema_type(self, value):
        self._schema_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.attribute_key:
            if hasattr(self.attribute_key, 'to_alipay_dict'):
                params['attribute_key'] = self.attribute_key.to_alipay_dict()
            else:
                params['attribute_key'] = self.attribute_key
        if self.attribute_name:
            if hasattr(self.attribute_name, 'to_alipay_dict'):
                params['attribute_name'] = self.attribute_name.to_alipay_dict()
            else:
                params['attribute_name'] = self.attribute_name
        if self.cert_source:
            if hasattr(self.cert_source, 'to_alipay_dict'):
                params['cert_source'] = self.cert_source.to_alipay_dict()
            else:
                params['cert_source'] = self.cert_source
        if self.cert_status:
            if hasattr(self.cert_status, 'to_alipay_dict'):
                params['cert_status'] = self.cert_status.to_alipay_dict()
            else:
                params['cert_status'] = self.cert_status
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
        if self.schema_type:
            if hasattr(self.schema_type, 'to_alipay_dict'):
                params['schema_type'] = self.schema_type.to_alipay_dict()
            else:
                params['schema_type'] = self.schema_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExchangeDataItemResult()
        if 'attribute_key' in d:
            o.attribute_key = d['attribute_key']
        if 'attribute_name' in d:
            o.attribute_name = d['attribute_name']
        if 'cert_source' in d:
            o.cert_source = d['cert_source']
        if 'cert_status' in d:
            o.cert_status = d['cert_status']
        if 'fields' in d:
            o.fields = d['fields']
        if 'records' in d:
            o.records = d['records']
        if 'schema_type' in d:
            o.schema_type = d['schema_type']
        return o


