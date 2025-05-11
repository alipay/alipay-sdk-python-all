#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCheckinRecordBatchqueryModel(object):

    def __init__(self):
        self._check_in_end_time = None
        self._check_in_result = None
        self._check_in_start_time = None
        self._check_in_type = None
        self._employee_no = None
        self._inst_id = None
        self._name = None
        self._node_id_list = None
        self._page_num = None
        self._page_size = None
        self._place_id_list = None

    @property
    def check_in_end_time(self):
        return self._check_in_end_time

    @check_in_end_time.setter
    def check_in_end_time(self, value):
        self._check_in_end_time = value
    @property
    def check_in_result(self):
        return self._check_in_result

    @check_in_result.setter
    def check_in_result(self, value):
        self._check_in_result = value
    @property
    def check_in_start_time(self):
        return self._check_in_start_time

    @check_in_start_time.setter
    def check_in_start_time(self, value):
        self._check_in_start_time = value
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
    def node_id_list(self):
        return self._node_id_list

    @node_id_list.setter
    def node_id_list(self, value):
        if isinstance(value, list):
            self._node_id_list = list()
            for i in value:
                self._node_id_list.append(i)
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
        if self.check_in_end_time:
            if hasattr(self.check_in_end_time, 'to_alipay_dict'):
                params['check_in_end_time'] = self.check_in_end_time.to_alipay_dict()
            else:
                params['check_in_end_time'] = self.check_in_end_time
        if self.check_in_result:
            if hasattr(self.check_in_result, 'to_alipay_dict'):
                params['check_in_result'] = self.check_in_result.to_alipay_dict()
            else:
                params['check_in_result'] = self.check_in_result
        if self.check_in_start_time:
            if hasattr(self.check_in_start_time, 'to_alipay_dict'):
                params['check_in_start_time'] = self.check_in_start_time.to_alipay_dict()
            else:
                params['check_in_start_time'] = self.check_in_start_time
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
        o = AlipayCommerceEducateCheckinRecordBatchqueryModel()
        if 'check_in_end_time' in d:
            o.check_in_end_time = d['check_in_end_time']
        if 'check_in_result' in d:
            o.check_in_result = d['check_in_result']
        if 'check_in_start_time' in d:
            o.check_in_start_time = d['check_in_start_time']
        if 'check_in_type' in d:
            o.check_in_type = d['check_in_type']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'name' in d:
            o.name = d['name']
        if 'node_id_list' in d:
            o.node_id_list = d['node_id_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'place_id_list' in d:
            o.place_id_list = d['place_id_list']
        return o


