#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchBoxKeyWordModule(object):

    def __init__(self):
        self._apply_no = None
        self._fail_reason = None
        self._gmt_modified = None
        self._keywords = None
        self._latest_audit_keywords = None
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
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, list):
            self._keywords = list()
            for i in value:
                self._keywords.append(i)
    @property
    def latest_audit_keywords(self):
        return self._latest_audit_keywords

    @latest_audit_keywords.setter
    def latest_audit_keywords(self, value):
        if isinstance(value, list):
            self._latest_audit_keywords = list()
            for i in value:
                self._latest_audit_keywords.append(i)
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
        if self.keywords:
            if isinstance(self.keywords, list):
                for i in range(0, len(self.keywords)):
                    element = self.keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keywords[i] = element.to_alipay_dict()
            if hasattr(self.keywords, 'to_alipay_dict'):
                params['keywords'] = self.keywords.to_alipay_dict()
            else:
                params['keywords'] = self.keywords
        if self.latest_audit_keywords:
            if isinstance(self.latest_audit_keywords, list):
                for i in range(0, len(self.latest_audit_keywords)):
                    element = self.latest_audit_keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.latest_audit_keywords[i] = element.to_alipay_dict()
            if hasattr(self.latest_audit_keywords, 'to_alipay_dict'):
                params['latest_audit_keywords'] = self.latest_audit_keywords.to_alipay_dict()
            else:
                params['latest_audit_keywords'] = self.latest_audit_keywords
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
        o = SearchBoxKeyWordModule()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'keywords' in d:
            o.keywords = d['keywords']
        if 'latest_audit_keywords' in d:
            o.latest_audit_keywords = d['latest_audit_keywords']
        if 'module_id' in d:
            o.module_id = d['module_id']
        if 'module_type' in d:
            o.module_type = d['module_type']
        if 'status' in d:
            o.status = d['status']
        return o


