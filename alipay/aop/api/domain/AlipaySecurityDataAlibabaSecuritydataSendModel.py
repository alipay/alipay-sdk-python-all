#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataAlibabaSecuritydataSendModel(object):

    def __init__(self):
        self._biz_content_value = None
        self._biz_id = None
        self._ingest_name = None
        self._main_target_type = None
        self._main_target_value = None
        self._property = None
        self._property_second = None
        self._property_third = None
        self._risk_type = None
        self._scope = None
        self._source = None
        self._system_name = None
        self._table_name = None
        self._time = None
        self._use_scope = None
        self._user_id = None

    @property
    def biz_content_value(self):
        return self._biz_content_value

    @biz_content_value.setter
    def biz_content_value(self, value):
        self._biz_content_value = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ingest_name(self):
        return self._ingest_name

    @ingest_name.setter
    def ingest_name(self, value):
        self._ingest_name = value
    @property
    def main_target_type(self):
        return self._main_target_type

    @main_target_type.setter
    def main_target_type(self, value):
        self._main_target_type = value
    @property
    def main_target_value(self):
        return self._main_target_value

    @main_target_value.setter
    def main_target_value(self, value):
        self._main_target_value = value
    @property
    def property(self):
        return self._property

    @property.setter
    def property(self, value):
        self._property = value
    @property
    def property_second(self):
        return self._property_second

    @property_second.setter
    def property_second(self, value):
        self._property_second = value
    @property
    def property_third(self):
        return self._property_third

    @property_third.setter
    def property_third(self, value):
        self._property_third = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def system_name(self):
        return self._system_name

    @system_name.setter
    def system_name(self, value):
        self._system_name = value
    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def use_scope(self):
        return self._use_scope

    @use_scope.setter
    def use_scope(self, value):
        self._use_scope = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_content_value:
            if hasattr(self.biz_content_value, 'to_alipay_dict'):
                params['biz_content_value'] = self.biz_content_value.to_alipay_dict()
            else:
                params['biz_content_value'] = self.biz_content_value
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.ingest_name:
            if hasattr(self.ingest_name, 'to_alipay_dict'):
                params['ingest_name'] = self.ingest_name.to_alipay_dict()
            else:
                params['ingest_name'] = self.ingest_name
        if self.main_target_type:
            if hasattr(self.main_target_type, 'to_alipay_dict'):
                params['main_target_type'] = self.main_target_type.to_alipay_dict()
            else:
                params['main_target_type'] = self.main_target_type
        if self.main_target_value:
            if hasattr(self.main_target_value, 'to_alipay_dict'):
                params['main_target_value'] = self.main_target_value.to_alipay_dict()
            else:
                params['main_target_value'] = self.main_target_value
        if self.property:
            if hasattr(self.property, 'to_alipay_dict'):
                params['property'] = self.property.to_alipay_dict()
            else:
                params['property'] = self.property
        if self.property_second:
            if hasattr(self.property_second, 'to_alipay_dict'):
                params['property_second'] = self.property_second.to_alipay_dict()
            else:
                params['property_second'] = self.property_second
        if self.property_third:
            if hasattr(self.property_third, 'to_alipay_dict'):
                params['property_third'] = self.property_third.to_alipay_dict()
            else:
                params['property_third'] = self.property_third
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.system_name:
            if hasattr(self.system_name, 'to_alipay_dict'):
                params['system_name'] = self.system_name.to_alipay_dict()
            else:
                params['system_name'] = self.system_name
        if self.table_name:
            if hasattr(self.table_name, 'to_alipay_dict'):
                params['table_name'] = self.table_name.to_alipay_dict()
            else:
                params['table_name'] = self.table_name
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.use_scope:
            if hasattr(self.use_scope, 'to_alipay_dict'):
                params['use_scope'] = self.use_scope.to_alipay_dict()
            else:
                params['use_scope'] = self.use_scope
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataAlibabaSecuritydataSendModel()
        if 'biz_content_value' in d:
            o.biz_content_value = d['biz_content_value']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ingest_name' in d:
            o.ingest_name = d['ingest_name']
        if 'main_target_type' in d:
            o.main_target_type = d['main_target_type']
        if 'main_target_value' in d:
            o.main_target_value = d['main_target_value']
        if 'property' in d:
            o.property = d['property']
        if 'property_second' in d:
            o.property_second = d['property_second']
        if 'property_third' in d:
            o.property_third = d['property_third']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'scope' in d:
            o.scope = d['scope']
        if 'source' in d:
            o.source = d['source']
        if 'system_name' in d:
            o.system_name = d['system_name']
        if 'table_name' in d:
            o.table_name = d['table_name']
        if 'time' in d:
            o.time = d['time']
        if 'use_scope' in d:
            o.use_scope = d['use_scope']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


