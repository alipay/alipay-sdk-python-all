#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DxDeployOrderInfo(object):

    def __init__(self):
        self._biz_ns = None
        self._deploy_event_type = None
        self._deploy_object_type = None
        self._deploy_payload = None
        self._gmt_biz_create = None
        self._group = None
        self._pre_record_id = None
        self._record_id = None
        self._retry = None

    @property
    def biz_ns(self):
        return self._biz_ns

    @biz_ns.setter
    def biz_ns(self, value):
        self._biz_ns = value
    @property
    def deploy_event_type(self):
        return self._deploy_event_type

    @deploy_event_type.setter
    def deploy_event_type(self, value):
        self._deploy_event_type = value
    @property
    def deploy_object_type(self):
        return self._deploy_object_type

    @deploy_object_type.setter
    def deploy_object_type(self, value):
        self._deploy_object_type = value
    @property
    def deploy_payload(self):
        return self._deploy_payload

    @deploy_payload.setter
    def deploy_payload(self, value):
        self._deploy_payload = value
    @property
    def gmt_biz_create(self):
        return self._gmt_biz_create

    @gmt_biz_create.setter
    def gmt_biz_create(self, value):
        self._gmt_biz_create = value
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value
    @property
    def pre_record_id(self):
        return self._pre_record_id

    @pre_record_id.setter
    def pre_record_id(self, value):
        self._pre_record_id = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_ns:
            if hasattr(self.biz_ns, 'to_alipay_dict'):
                params['biz_ns'] = self.biz_ns.to_alipay_dict()
            else:
                params['biz_ns'] = self.biz_ns
        if self.deploy_event_type:
            if hasattr(self.deploy_event_type, 'to_alipay_dict'):
                params['deploy_event_type'] = self.deploy_event_type.to_alipay_dict()
            else:
                params['deploy_event_type'] = self.deploy_event_type
        if self.deploy_object_type:
            if hasattr(self.deploy_object_type, 'to_alipay_dict'):
                params['deploy_object_type'] = self.deploy_object_type.to_alipay_dict()
            else:
                params['deploy_object_type'] = self.deploy_object_type
        if self.deploy_payload:
            if hasattr(self.deploy_payload, 'to_alipay_dict'):
                params['deploy_payload'] = self.deploy_payload.to_alipay_dict()
            else:
                params['deploy_payload'] = self.deploy_payload
        if self.gmt_biz_create:
            if hasattr(self.gmt_biz_create, 'to_alipay_dict'):
                params['gmt_biz_create'] = self.gmt_biz_create.to_alipay_dict()
            else:
                params['gmt_biz_create'] = self.gmt_biz_create
        if self.group:
            if hasattr(self.group, 'to_alipay_dict'):
                params['group'] = self.group.to_alipay_dict()
            else:
                params['group'] = self.group
        if self.pre_record_id:
            if hasattr(self.pre_record_id, 'to_alipay_dict'):
                params['pre_record_id'] = self.pre_record_id.to_alipay_dict()
            else:
                params['pre_record_id'] = self.pre_record_id
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.retry:
            if hasattr(self.retry, 'to_alipay_dict'):
                params['retry'] = self.retry.to_alipay_dict()
            else:
                params['retry'] = self.retry
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DxDeployOrderInfo()
        if 'biz_ns' in d:
            o.biz_ns = d['biz_ns']
        if 'deploy_event_type' in d:
            o.deploy_event_type = d['deploy_event_type']
        if 'deploy_object_type' in d:
            o.deploy_object_type = d['deploy_object_type']
        if 'deploy_payload' in d:
            o.deploy_payload = d['deploy_payload']
        if 'gmt_biz_create' in d:
            o.gmt_biz_create = d['gmt_biz_create']
        if 'group' in d:
            o.group = d['group']
        if 'pre_record_id' in d:
            o.pre_record_id = d['pre_record_id']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'retry' in d:
            o.retry = d['retry']
        return o


