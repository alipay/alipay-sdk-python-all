#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdInteractiveprodBatchInitializeModel(object):

    def __init__(self):
        self._batch_biz_id = None
        self._commodity_id = None
        self._commodity_scene = None
        self._data_count = None
        self._data_url = None
        self._ext_params = None
        self._operator_id = None
        self._operator_open_id = None
        self._task_desc = None
        self._task_name = None
        self._tenant_id = None

    @property
    def batch_biz_id(self):
        return self._batch_biz_id

    @batch_biz_id.setter
    def batch_biz_id(self, value):
        self._batch_biz_id = value
    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def commodity_scene(self):
        return self._commodity_scene

    @commodity_scene.setter
    def commodity_scene(self, value):
        self._commodity_scene = value
    @property
    def data_count(self):
        return self._data_count

    @data_count.setter
    def data_count(self, value):
        self._data_count = value
    @property
    def data_url(self):
        return self._data_url

    @data_url.setter
    def data_url(self, value):
        self._data_url = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_open_id(self):
        return self._operator_open_id

    @operator_open_id.setter
    def operator_open_id(self, value):
        self._operator_open_id = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_biz_id:
            if hasattr(self.batch_biz_id, 'to_alipay_dict'):
                params['batch_biz_id'] = self.batch_biz_id.to_alipay_dict()
            else:
                params['batch_biz_id'] = self.batch_biz_id
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.commodity_scene:
            if hasattr(self.commodity_scene, 'to_alipay_dict'):
                params['commodity_scene'] = self.commodity_scene.to_alipay_dict()
            else:
                params['commodity_scene'] = self.commodity_scene
        if self.data_count:
            if hasattr(self.data_count, 'to_alipay_dict'):
                params['data_count'] = self.data_count.to_alipay_dict()
            else:
                params['data_count'] = self.data_count
        if self.data_url:
            if hasattr(self.data_url, 'to_alipay_dict'):
                params['data_url'] = self.data_url.to_alipay_dict()
            else:
                params['data_url'] = self.data_url
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_open_id:
            if hasattr(self.operator_open_id, 'to_alipay_dict'):
                params['operator_open_id'] = self.operator_open_id.to_alipay_dict()
            else:
                params['operator_open_id'] = self.operator_open_id
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdInteractiveprodBatchInitializeModel()
        if 'batch_biz_id' in d:
            o.batch_biz_id = d['batch_biz_id']
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'commodity_scene' in d:
            o.commodity_scene = d['commodity_scene']
        if 'data_count' in d:
            o.data_count = d['data_count']
        if 'data_url' in d:
            o.data_url = d['data_url']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_open_id' in d:
            o.operator_open_id = d['operator_open_id']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


