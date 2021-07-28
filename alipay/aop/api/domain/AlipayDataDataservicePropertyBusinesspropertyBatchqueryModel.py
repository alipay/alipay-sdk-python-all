#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataservicePropertyBusinesspropertyBatchqueryModel(object):

    def __init__(self):
        self._business_profile_id = None
        self._business_property_ids = None
        self._column_guid = None
        self._property_name = None
        self._status = None
        self._table_guid = None

    @property
    def business_profile_id(self):
        return self._business_profile_id

    @business_profile_id.setter
    def business_profile_id(self, value):
        self._business_profile_id = value
    @property
    def business_property_ids(self):
        return self._business_property_ids

    @business_property_ids.setter
    def business_property_ids(self, value):
        if isinstance(value, list):
            self._business_property_ids = list()
            for i in value:
                self._business_property_ids.append(i)
    @property
    def column_guid(self):
        return self._column_guid

    @column_guid.setter
    def column_guid(self, value):
        self._column_guid = value
    @property
    def property_name(self):
        return self._property_name

    @property_name.setter
    def property_name(self, value):
        self._property_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, list):
            self._status = list()
            for i in value:
                self._status.append(i)
    @property
    def table_guid(self):
        return self._table_guid

    @table_guid.setter
    def table_guid(self, value):
        self._table_guid = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_profile_id:
            if hasattr(self.business_profile_id, 'to_alipay_dict'):
                params['business_profile_id'] = self.business_profile_id.to_alipay_dict()
            else:
                params['business_profile_id'] = self.business_profile_id
        if self.business_property_ids:
            if isinstance(self.business_property_ids, list):
                for i in range(0, len(self.business_property_ids)):
                    element = self.business_property_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_property_ids[i] = element.to_alipay_dict()
            if hasattr(self.business_property_ids, 'to_alipay_dict'):
                params['business_property_ids'] = self.business_property_ids.to_alipay_dict()
            else:
                params['business_property_ids'] = self.business_property_ids
        if self.column_guid:
            if hasattr(self.column_guid, 'to_alipay_dict'):
                params['column_guid'] = self.column_guid.to_alipay_dict()
            else:
                params['column_guid'] = self.column_guid
        if self.property_name:
            if hasattr(self.property_name, 'to_alipay_dict'):
                params['property_name'] = self.property_name.to_alipay_dict()
            else:
                params['property_name'] = self.property_name
        if self.status:
            if isinstance(self.status, list):
                for i in range(0, len(self.status)):
                    element = self.status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status[i] = element.to_alipay_dict()
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.table_guid:
            if hasattr(self.table_guid, 'to_alipay_dict'):
                params['table_guid'] = self.table_guid.to_alipay_dict()
            else:
                params['table_guid'] = self.table_guid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataservicePropertyBusinesspropertyBatchqueryModel()
        if 'business_profile_id' in d:
            o.business_profile_id = d['business_profile_id']
        if 'business_property_ids' in d:
            o.business_property_ids = d['business_property_ids']
        if 'column_guid' in d:
            o.column_guid = d['column_guid']
        if 'property_name' in d:
            o.property_name = d['property_name']
        if 'status' in d:
            o.status = d['status']
        if 'table_guid' in d:
            o.table_guid = d['table_guid']
        return o


