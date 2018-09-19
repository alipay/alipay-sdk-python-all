#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantOperatorSearchQueryModel(object):

    def __init__(self):
        self._auth_code = None
        self._dept_ids = None
        self._dept_paths = None
        self._page_num = None
        self._page_size = None
        self._role_ids = None
        self._search_key = None
        self._status = None
        self._unassign = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def dept_ids(self):
        return self._dept_ids

    @dept_ids.setter
    def dept_ids(self, value):
        if isinstance(value, list):
            self._dept_ids = list()
            for i in value:
                self._dept_ids.append(i)
    @property
    def dept_paths(self):
        return self._dept_paths

    @dept_paths.setter
    def dept_paths(self, value):
        if isinstance(value, list):
            self._dept_paths = list()
            for i in value:
                self._dept_paths.append(i)
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
    def role_ids(self):
        return self._role_ids

    @role_ids.setter
    def role_ids(self, value):
        if isinstance(value, list):
            self._role_ids = list()
            for i in value:
                self._role_ids.append(i)
    @property
    def search_key(self):
        return self._search_key

    @search_key.setter
    def search_key(self, value):
        self._search_key = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, list):
            self._status = list()
            for i in value:
                self._status.append(i)
    @property
    def unassign(self):
        return self._unassign

    @unassign.setter
    def unassign(self, value):
        self._unassign = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.dept_ids:
            if isinstance(self.dept_ids, list):
                for i in range(0, len(self.dept_ids)):
                    element = self.dept_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dept_ids[i] = element.to_alipay_dict()
            if hasattr(self.dept_ids, 'to_alipay_dict'):
                params['dept_ids'] = self.dept_ids.to_alipay_dict()
            else:
                params['dept_ids'] = self.dept_ids
        if self.dept_paths:
            if isinstance(self.dept_paths, list):
                for i in range(0, len(self.dept_paths)):
                    element = self.dept_paths[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dept_paths[i] = element.to_alipay_dict()
            if hasattr(self.dept_paths, 'to_alipay_dict'):
                params['dept_paths'] = self.dept_paths.to_alipay_dict()
            else:
                params['dept_paths'] = self.dept_paths
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
        if self.role_ids:
            if isinstance(self.role_ids, list):
                for i in range(0, len(self.role_ids)):
                    element = self.role_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_ids[i] = element.to_alipay_dict()
            if hasattr(self.role_ids, 'to_alipay_dict'):
                params['role_ids'] = self.role_ids.to_alipay_dict()
            else:
                params['role_ids'] = self.role_ids
        if self.search_key:
            if hasattr(self.search_key, 'to_alipay_dict'):
                params['search_key'] = self.search_key.to_alipay_dict()
            else:
                params['search_key'] = self.search_key
        if self.status:
            if isinstance(self.status, list):
                for i in range(0, len(self.status)):
                    element = self.status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status[i] = element.to_alipay_dict()
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unassign:
            if hasattr(self.unassign, 'to_alipay_dict'):
                params['unassign'] = self.unassign.to_alipay_dict()
            else:
                params['unassign'] = self.unassign
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantOperatorSearchQueryModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'dept_ids' in d:
            o.dept_ids = d['dept_ids']
        if 'dept_paths' in d:
            o.dept_paths = d['dept_paths']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'role_ids' in d:
            o.role_ids = d['role_ids']
        if 'search_key' in d:
            o.search_key = d['search_key']
        if 'status' in d:
            o.status = d['status']
        if 'unassign' in d:
            o.unassign = d['unassign']
        return o


