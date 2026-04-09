#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalDeptSyncModel(object):

    def __init__(self):
        self._dept_name = None
        self._dept_no = None
        self._master_work_no = None
        self._parent_dept_id = None
        self._parent_path = None
        self._status = None

    @property
    def dept_name(self):
        return self._dept_name

    @dept_name.setter
    def dept_name(self, value):
        self._dept_name = value
    @property
    def dept_no(self):
        return self._dept_no

    @dept_no.setter
    def dept_no(self, value):
        self._dept_no = value
    @property
    def master_work_no(self):
        return self._master_work_no

    @master_work_no.setter
    def master_work_no(self, value):
        self._master_work_no = value
    @property
    def parent_dept_id(self):
        return self._parent_dept_id

    @parent_dept_id.setter
    def parent_dept_id(self, value):
        self._parent_dept_id = value
    @property
    def parent_path(self):
        return self._parent_path

    @parent_path.setter
    def parent_path(self, value):
        self._parent_path = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.dept_name:
            if hasattr(self.dept_name, 'to_alipay_dict'):
                params['dept_name'] = self.dept_name.to_alipay_dict()
            else:
                params['dept_name'] = self.dept_name
        if self.dept_no:
            if hasattr(self.dept_no, 'to_alipay_dict'):
                params['dept_no'] = self.dept_no.to_alipay_dict()
            else:
                params['dept_no'] = self.dept_no
        if self.master_work_no:
            if hasattr(self.master_work_no, 'to_alipay_dict'):
                params['master_work_no'] = self.master_work_no.to_alipay_dict()
            else:
                params['master_work_no'] = self.master_work_no
        if self.parent_dept_id:
            if hasattr(self.parent_dept_id, 'to_alipay_dict'):
                params['parent_dept_id'] = self.parent_dept_id.to_alipay_dict()
            else:
                params['parent_dept_id'] = self.parent_dept_id
        if self.parent_path:
            if hasattr(self.parent_path, 'to_alipay_dict'):
                params['parent_path'] = self.parent_path.to_alipay_dict()
            else:
                params['parent_path'] = self.parent_path
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalDeptSyncModel()
        if 'dept_name' in d:
            o.dept_name = d['dept_name']
        if 'dept_no' in d:
            o.dept_no = d['dept_no']
        if 'master_work_no' in d:
            o.master_work_no = d['master_work_no']
        if 'parent_dept_id' in d:
            o.parent_dept_id = d['parent_dept_id']
        if 'parent_path' in d:
            o.parent_path = d['parent_path']
        if 'status' in d:
            o.status = d['status']
        return o


