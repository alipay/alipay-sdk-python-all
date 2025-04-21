#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduCheckInRecord(object):

    def __init__(self):
        self._check_in_picture = None
        self._check_in_result = None
        self._check_in_time = None
        self._check_in_type = None
        self._employee_no = None
        self._inst_id = None
        self._name = None
        self._node_id = None
        self._node_name = None
        self._place_id = None
        self._place_name = None
        self._roster_id = None
        self._user_check_in_id = None

    @property
    def check_in_picture(self):
        return self._check_in_picture

    @check_in_picture.setter
    def check_in_picture(self, value):
        self._check_in_picture = value
    @property
    def check_in_result(self):
        return self._check_in_result

    @check_in_result.setter
    def check_in_result(self, value):
        self._check_in_result = value
    @property
    def check_in_time(self):
        return self._check_in_time

    @check_in_time.setter
    def check_in_time(self, value):
        self._check_in_time = value
    @property
    def check_in_type(self):
        return self._check_in_type

    @check_in_type.setter
    def check_in_type(self, value):
        self._check_in_type = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value
    @property
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value
    @property
    def roster_id(self):
        return self._roster_id

    @roster_id.setter
    def roster_id(self, value):
        self._roster_id = value
    @property
    def user_check_in_id(self):
        return self._user_check_in_id

    @user_check_in_id.setter
    def user_check_in_id(self, value):
        self._user_check_in_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_in_picture:
            if hasattr(self.check_in_picture, 'to_alipay_dict'):
                params['check_in_picture'] = self.check_in_picture.to_alipay_dict()
            else:
                params['check_in_picture'] = self.check_in_picture
        if self.check_in_result:
            if hasattr(self.check_in_result, 'to_alipay_dict'):
                params['check_in_result'] = self.check_in_result.to_alipay_dict()
            else:
                params['check_in_result'] = self.check_in_result
        if self.check_in_time:
            if hasattr(self.check_in_time, 'to_alipay_dict'):
                params['check_in_time'] = self.check_in_time.to_alipay_dict()
            else:
                params['check_in_time'] = self.check_in_time
        if self.check_in_type:
            if hasattr(self.check_in_type, 'to_alipay_dict'):
                params['check_in_type'] = self.check_in_type.to_alipay_dict()
            else:
                params['check_in_type'] = self.check_in_type
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.node_id:
            if hasattr(self.node_id, 'to_alipay_dict'):
                params['node_id'] = self.node_id.to_alipay_dict()
            else:
                params['node_id'] = self.node_id
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
        if self.place_id:
            if hasattr(self.place_id, 'to_alipay_dict'):
                params['place_id'] = self.place_id.to_alipay_dict()
            else:
                params['place_id'] = self.place_id
        if self.place_name:
            if hasattr(self.place_name, 'to_alipay_dict'):
                params['place_name'] = self.place_name.to_alipay_dict()
            else:
                params['place_name'] = self.place_name
        if self.roster_id:
            if hasattr(self.roster_id, 'to_alipay_dict'):
                params['roster_id'] = self.roster_id.to_alipay_dict()
            else:
                params['roster_id'] = self.roster_id
        if self.user_check_in_id:
            if hasattr(self.user_check_in_id, 'to_alipay_dict'):
                params['user_check_in_id'] = self.user_check_in_id.to_alipay_dict()
            else:
                params['user_check_in_id'] = self.user_check_in_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduCheckInRecord()
        if 'check_in_picture' in d:
            o.check_in_picture = d['check_in_picture']
        if 'check_in_result' in d:
            o.check_in_result = d['check_in_result']
        if 'check_in_time' in d:
            o.check_in_time = d['check_in_time']
        if 'check_in_type' in d:
            o.check_in_type = d['check_in_type']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'name' in d:
            o.name = d['name']
        if 'node_id' in d:
            o.node_id = d['node_id']
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'place_id' in d:
            o.place_id = d['place_id']
        if 'place_name' in d:
            o.place_name = d['place_name']
        if 'roster_id' in d:
            o.roster_id = d['roster_id']
        if 'user_check_in_id' in d:
            o.user_check_in_id = d['user_check_in_id']
        return o


