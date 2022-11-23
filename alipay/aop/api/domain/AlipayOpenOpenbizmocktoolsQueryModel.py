#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOpenbizmocktoolsQueryModel(object):

    def __init__(self):
        self._app_number = None
        self._biz_id = None
        self._biz_type = None
        self._condition = None
        self._env = None
        self._group_id = None
        self._interface_name = None
        self._oid = None
        self._operation_type = None
        self._pid = None
        self._service = None

    @property
    def app_number(self):
        return self._app_number

    @app_number.setter
    def app_number(self, value):
        self._app_number = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def interface_name(self):
        return self._interface_name

    @interface_name.setter
    def interface_name(self, value):
        self._interface_name = value
    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_number:
            if hasattr(self.app_number, 'to_alipay_dict'):
                params['app_number'] = self.app_number.to_alipay_dict()
            else:
                params['app_number'] = self.app_number
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.condition:
            if hasattr(self.condition, 'to_alipay_dict'):
                params['condition'] = self.condition.to_alipay_dict()
            else:
                params['condition'] = self.condition
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.interface_name:
            if hasattr(self.interface_name, 'to_alipay_dict'):
                params['interface_name'] = self.interface_name.to_alipay_dict()
            else:
                params['interface_name'] = self.interface_name
        if self.oid:
            if hasattr(self.oid, 'to_alipay_dict'):
                params['oid'] = self.oid.to_alipay_dict()
            else:
                params['oid'] = self.oid
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.service:
            if hasattr(self.service, 'to_alipay_dict'):
                params['service'] = self.service.to_alipay_dict()
            else:
                params['service'] = self.service
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOpenbizmocktoolsQueryModel()
        if 'app_number' in d:
            o.app_number = d['app_number']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'condition' in d:
            o.condition = d['condition']
        if 'env' in d:
            o.env = d['env']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'interface_name' in d:
            o.interface_name = d['interface_name']
        if 'oid' in d:
            o.oid = d['oid']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'pid' in d:
            o.pid = d['pid']
        if 'service' in d:
            o.service = d['service']
        return o


