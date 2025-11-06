#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCstrainingUserdatapageQueryModel(object):

    def __init__(self):
        self._business_id = None
        self._end_time = None
        self._group_id = None
        self._is_passed = None
        self._member_id = None
        self._page_num = None
        self._page_size = None
        self._path_id = None
        self._path_name = None
        self._path_status = None
        self._playscript_id = None
        self._playscript_name = None
        self._resource_name = None
        self._resource_type = None
        self._stage_name = None
        self._start_time = None
        self._tenant_id = None
        self._training_type = None
        self._user_name = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def is_passed(self):
        return self._is_passed

    @is_passed.setter
    def is_passed(self, value):
        self._is_passed = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def path_id(self):
        return self._path_id

    @path_id.setter
    def path_id(self, value):
        self._path_id = value
    @property
    def path_name(self):
        return self._path_name

    @path_name.setter
    def path_name(self, value):
        self._path_name = value
    @property
    def path_status(self):
        return self._path_status

    @path_status.setter
    def path_status(self, value):
        self._path_status = value
    @property
    def playscript_id(self):
        return self._playscript_id

    @playscript_id.setter
    def playscript_id(self, value):
        self._playscript_id = value
    @property
    def playscript_name(self):
        return self._playscript_name

    @playscript_name.setter
    def playscript_name(self, value):
        self._playscript_name = value
    @property
    def resource_name(self):
        return self._resource_name

    @resource_name.setter
    def resource_name(self, value):
        self._resource_name = value
    @property
    def resource_type(self):
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value):
        self._resource_type = value
    @property
    def stage_name(self):
        return self._stage_name

    @stage_name.setter
    def stage_name(self, value):
        self._stage_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def training_type(self):
        return self._training_type

    @training_type.setter
    def training_type(self, value):
        self._training_type = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.is_passed:
            if hasattr(self.is_passed, 'to_alipay_dict'):
                params['is_passed'] = self.is_passed.to_alipay_dict()
            else:
                params['is_passed'] = self.is_passed
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.path_id:
            if hasattr(self.path_id, 'to_alipay_dict'):
                params['path_id'] = self.path_id.to_alipay_dict()
            else:
                params['path_id'] = self.path_id
        if self.path_name:
            if hasattr(self.path_name, 'to_alipay_dict'):
                params['path_name'] = self.path_name.to_alipay_dict()
            else:
                params['path_name'] = self.path_name
        if self.path_status:
            if hasattr(self.path_status, 'to_alipay_dict'):
                params['path_status'] = self.path_status.to_alipay_dict()
            else:
                params['path_status'] = self.path_status
        if self.playscript_id:
            if hasattr(self.playscript_id, 'to_alipay_dict'):
                params['playscript_id'] = self.playscript_id.to_alipay_dict()
            else:
                params['playscript_id'] = self.playscript_id
        if self.playscript_name:
            if hasattr(self.playscript_name, 'to_alipay_dict'):
                params['playscript_name'] = self.playscript_name.to_alipay_dict()
            else:
                params['playscript_name'] = self.playscript_name
        if self.resource_name:
            if hasattr(self.resource_name, 'to_alipay_dict'):
                params['resource_name'] = self.resource_name.to_alipay_dict()
            else:
                params['resource_name'] = self.resource_name
        if self.resource_type:
            if hasattr(self.resource_type, 'to_alipay_dict'):
                params['resource_type'] = self.resource_type.to_alipay_dict()
            else:
                params['resource_type'] = self.resource_type
        if self.stage_name:
            if hasattr(self.stage_name, 'to_alipay_dict'):
                params['stage_name'] = self.stage_name.to_alipay_dict()
            else:
                params['stage_name'] = self.stage_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.training_type:
            if hasattr(self.training_type, 'to_alipay_dict'):
                params['training_type'] = self.training_type.to_alipay_dict()
            else:
                params['training_type'] = self.training_type
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCstrainingUserdatapageQueryModel()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'is_passed' in d:
            o.is_passed = d['is_passed']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'path_id' in d:
            o.path_id = d['path_id']
        if 'path_name' in d:
            o.path_name = d['path_name']
        if 'path_status' in d:
            o.path_status = d['path_status']
        if 'playscript_id' in d:
            o.playscript_id = d['playscript_id']
        if 'playscript_name' in d:
            o.playscript_name = d['playscript_name']
        if 'resource_name' in d:
            o.resource_name = d['resource_name']
        if 'resource_type' in d:
            o.resource_type = d['resource_type']
        if 'stage_name' in d:
            o.stage_name = d['stage_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'training_type' in d:
            o.training_type = d['training_type']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


