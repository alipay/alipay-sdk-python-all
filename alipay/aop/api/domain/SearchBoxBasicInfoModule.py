#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchBoxBasicInfoModule(object):

    def __init__(self):
        self._apply_no = None
        self._box_desc = None
        self._fail_reason = None
        self._gmt_modified = None
        self._latest_audit_box_desc = None
        self._module_id = None
        self._module_type = None
        self._status = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def box_desc(self):
        return self._box_desc

    @box_desc.setter
    def box_desc(self, value):
        self._box_desc = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def latest_audit_box_desc(self):
        return self._latest_audit_box_desc

    @latest_audit_box_desc.setter
    def latest_audit_box_desc(self, value):
        self._latest_audit_box_desc = value
    @property
    def module_id(self):
        return self._module_id

    @module_id.setter
    def module_id(self, value):
        self._module_id = value
    @property
    def module_type(self):
        return self._module_type

    @module_type.setter
    def module_type(self, value):
        self._module_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.box_desc:
            if hasattr(self.box_desc, 'to_alipay_dict'):
                params['box_desc'] = self.box_desc.to_alipay_dict()
            else:
                params['box_desc'] = self.box_desc
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.latest_audit_box_desc:
            if hasattr(self.latest_audit_box_desc, 'to_alipay_dict'):
                params['latest_audit_box_desc'] = self.latest_audit_box_desc.to_alipay_dict()
            else:
                params['latest_audit_box_desc'] = self.latest_audit_box_desc
        if self.module_id:
            if hasattr(self.module_id, 'to_alipay_dict'):
                params['module_id'] = self.module_id.to_alipay_dict()
            else:
                params['module_id'] = self.module_id
        if self.module_type:
            if hasattr(self.module_type, 'to_alipay_dict'):
                params['module_type'] = self.module_type.to_alipay_dict()
            else:
                params['module_type'] = self.module_type
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
        o = SearchBoxBasicInfoModule()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'box_desc' in d:
            o.box_desc = d['box_desc']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'latest_audit_box_desc' in d:
            o.latest_audit_box_desc = d['latest_audit_box_desc']
        if 'module_id' in d:
            o.module_id = d['module_id']
        if 'module_type' in d:
            o.module_type = d['module_type']
        if 'status' in d:
            o.status = d['status']
        return o


