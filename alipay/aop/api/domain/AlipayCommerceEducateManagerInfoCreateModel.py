#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateManagerInfoCreateModel(object):

    def __init__(self):
        self._employee_no = None
        self._inst_id = None
        self._manager_type = None
        self._mobile = None
        self._name = None
        self._node_id_list = None
        self._place_id_list = None

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
    def node_id_list(self):
        return self._node_id_list

    @node_id_list.setter
    def node_id_list(self, value):
        if isinstance(value, list):
            self._node_id_list = list()
            for i in value:
                self._node_id_list.append(i)
    @property
    def place_id_list(self):
        return self._place_id_list

    @place_id_list.setter
    def place_id_list(self, value):
        if isinstance(value, list):
            self._place_id_list = list()
            for i in value:
                self._place_id_list.append(i)


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
        if self.node_id_list:
            if isinstance(self.node_id_list, list):
                for i in range(0, len(self.node_id_list)):
                    element = self.node_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_id_list[i] = element.to_alipay_dict()
            if hasattr(self.node_id_list, 'to_alipay_dict'):
                params['node_id_list'] = self.node_id_list.to_alipay_dict()
            else:
                params['node_id_list'] = self.node_id_list
        if self.place_id_list:
            if isinstance(self.place_id_list, list):
                for i in range(0, len(self.place_id_list)):
                    element = self.place_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.place_id_list[i] = element.to_alipay_dict()
            if hasattr(self.place_id_list, 'to_alipay_dict'):
                params['place_id_list'] = self.place_id_list.to_alipay_dict()
            else:
                params['place_id_list'] = self.place_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateManagerInfoCreateModel()
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'manager_type' in d:
            o.manager_type = d['manager_type']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'node_id_list' in d:
            o.node_id_list = d['node_id_list']
        if 'place_id_list' in d:
            o.place_id_list = d['place_id_list']
        return o


