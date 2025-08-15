#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCstrainingTrainingdataQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._member_id = None
        self._page_num = None
        self._page_size = None
        self._path_id = None
        self._path_name = None
        self._playscript_id = None
        self._playscript_name = None
        self._start_time = None
        self._tenant_id = None
        self._type = None
        self._user_name = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
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
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayIserviceCstrainingTrainingdataQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
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
        if 'playscript_id' in d:
            o.playscript_id = d['playscript_id']
        if 'playscript_name' in d:
            o.playscript_name = d['playscript_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


