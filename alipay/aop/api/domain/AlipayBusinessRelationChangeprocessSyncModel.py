#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBusinessRelationChangeprocessSyncModel(object):

    def __init__(self):
        self._group_id = None
        self._group_sub_type = None
        self._group_type = None
        self._process_status = None
        self._process_target_id = None
        self._process_target_type = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_sub_type(self):
        return self._group_sub_type

    @group_sub_type.setter
    def group_sub_type(self, value):
        self._group_sub_type = value
    @property
    def group_type(self):
        return self._group_type

    @group_type.setter
    def group_type(self, value):
        self._group_type = value
    @property
    def process_status(self):
        return self._process_status

    @process_status.setter
    def process_status(self, value):
        self._process_status = value
    @property
    def process_target_id(self):
        return self._process_target_id

    @process_target_id.setter
    def process_target_id(self, value):
        self._process_target_id = value
    @property
    def process_target_type(self):
        return self._process_target_type

    @process_target_type.setter
    def process_target_type(self, value):
        self._process_target_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_sub_type:
            if hasattr(self.group_sub_type, 'to_alipay_dict'):
                params['group_sub_type'] = self.group_sub_type.to_alipay_dict()
            else:
                params['group_sub_type'] = self.group_sub_type
        if self.group_type:
            if hasattr(self.group_type, 'to_alipay_dict'):
                params['group_type'] = self.group_type.to_alipay_dict()
            else:
                params['group_type'] = self.group_type
        if self.process_status:
            if hasattr(self.process_status, 'to_alipay_dict'):
                params['process_status'] = self.process_status.to_alipay_dict()
            else:
                params['process_status'] = self.process_status
        if self.process_target_id:
            if hasattr(self.process_target_id, 'to_alipay_dict'):
                params['process_target_id'] = self.process_target_id.to_alipay_dict()
            else:
                params['process_target_id'] = self.process_target_id
        if self.process_target_type:
            if hasattr(self.process_target_type, 'to_alipay_dict'):
                params['process_target_type'] = self.process_target_type.to_alipay_dict()
            else:
                params['process_target_type'] = self.process_target_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessRelationChangeprocessSyncModel()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_sub_type' in d:
            o.group_sub_type = d['group_sub_type']
        if 'group_type' in d:
            o.group_type = d['group_type']
        if 'process_status' in d:
            o.process_status = d['process_status']
        if 'process_target_id' in d:
            o.process_target_id = d['process_target_id']
        if 'process_target_type' in d:
            o.process_target_type = d['process_target_type']
        return o


