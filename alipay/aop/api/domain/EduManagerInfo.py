#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduNodeInfo import EduNodeInfo
from alipay.aop.api.domain.EduPlaceInfo import EduPlaceInfo


class EduManagerInfo(object):

    def __init__(self):
        self._employee_no = None
        self._inst_id = None
        self._manager_id = None
        self._manager_type = None
        self._mobile = None
        self._name = None
        self._node_list = None
        self._place_list = None
        self._roster_id = None

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
    def manager_id(self):
        return self._manager_id

    @manager_id.setter
    def manager_id(self, value):
        self._manager_id = value
    @property
    def manager_type(self):
        return self._manager_type

    @manager_type.setter
    def manager_type(self, value):
        self._manager_type = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def node_list(self):
        return self._node_list

    @node_list.setter
    def node_list(self, value):
        if isinstance(value, list):
            self._node_list = list()
            for i in value:
                if isinstance(i, EduNodeInfo):
                    self._node_list.append(i)
                else:
                    self._node_list.append(EduNodeInfo.from_alipay_dict(i))
    @property
    def place_list(self):
        return self._place_list

    @place_list.setter
    def place_list(self, value):
        if isinstance(value, list):
            self._place_list = list()
            for i in value:
                if isinstance(i, EduPlaceInfo):
                    self._place_list.append(i)
                else:
                    self._place_list.append(EduPlaceInfo.from_alipay_dict(i))
    @property
    def roster_id(self):
        return self._roster_id

    @roster_id.setter
    def roster_id(self, value):
        self._roster_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.manager_id:
            if hasattr(self.manager_id, 'to_alipay_dict'):
                params['manager_id'] = self.manager_id.to_alipay_dict()
            else:
                params['manager_id'] = self.manager_id
        if self.manager_type:
            if hasattr(self.manager_type, 'to_alipay_dict'):
                params['manager_type'] = self.manager_type.to_alipay_dict()
            else:
                params['manager_type'] = self.manager_type
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.node_list:
            if isinstance(self.node_list, list):
                for i in range(0, len(self.node_list)):
                    element = self.node_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_list[i] = element.to_alipay_dict()
            if hasattr(self.node_list, 'to_alipay_dict'):
                params['node_list'] = self.node_list.to_alipay_dict()
            else:
                params['node_list'] = self.node_list
        if self.place_list:
            if isinstance(self.place_list, list):
                for i in range(0, len(self.place_list)):
                    element = self.place_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.place_list[i] = element.to_alipay_dict()
            if hasattr(self.place_list, 'to_alipay_dict'):
                params['place_list'] = self.place_list.to_alipay_dict()
            else:
                params['place_list'] = self.place_list
        if self.roster_id:
            if hasattr(self.roster_id, 'to_alipay_dict'):
                params['roster_id'] = self.roster_id.to_alipay_dict()
            else:
                params['roster_id'] = self.roster_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduManagerInfo()
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'manager_id' in d:
            o.manager_id = d['manager_id']
        if 'manager_type' in d:
            o.manager_type = d['manager_type']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'node_list' in d:
            o.node_list = d['node_list']
        if 'place_list' in d:
            o.place_list = d['place_list']
        if 'roster_id' in d:
            o.roster_id = d['roster_id']
        return o


