#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BcGroupClusterDetail(object):

    def __init__(self):
        self._auto_create_group = None
        self._cluster_admin_ids = None
        self._cluster_id = None
        self._cluster_name = None
        self._default_admin_ids = None
        self._default_group_name = None
        self._default_master_id = None

    @property
    def auto_create_group(self):
        return self._auto_create_group

    @auto_create_group.setter
    def auto_create_group(self, value):
        self._auto_create_group = value
    @property
    def cluster_admin_ids(self):
        return self._cluster_admin_ids

    @cluster_admin_ids.setter
    def cluster_admin_ids(self, value):
        if isinstance(value, list):
            self._cluster_admin_ids = list()
            for i in value:
                self._cluster_admin_ids.append(i)
    @property
    def cluster_id(self):
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, value):
        self._cluster_id = value
    @property
    def cluster_name(self):
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, value):
        self._cluster_name = value
    @property
    def default_admin_ids(self):
        return self._default_admin_ids

    @default_admin_ids.setter
    def default_admin_ids(self, value):
        if isinstance(value, list):
            self._default_admin_ids = list()
            for i in value:
                self._default_admin_ids.append(i)
    @property
    def default_group_name(self):
        return self._default_group_name

    @default_group_name.setter
    def default_group_name(self, value):
        self._default_group_name = value
    @property
    def default_master_id(self):
        return self._default_master_id

    @default_master_id.setter
    def default_master_id(self, value):
        self._default_master_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_create_group:
            if hasattr(self.auto_create_group, 'to_alipay_dict'):
                params['auto_create_group'] = self.auto_create_group.to_alipay_dict()
            else:
                params['auto_create_group'] = self.auto_create_group
        if self.cluster_admin_ids:
            if isinstance(self.cluster_admin_ids, list):
                for i in range(0, len(self.cluster_admin_ids)):
                    element = self.cluster_admin_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cluster_admin_ids[i] = element.to_alipay_dict()
            if hasattr(self.cluster_admin_ids, 'to_alipay_dict'):
                params['cluster_admin_ids'] = self.cluster_admin_ids.to_alipay_dict()
            else:
                params['cluster_admin_ids'] = self.cluster_admin_ids
        if self.cluster_id:
            if hasattr(self.cluster_id, 'to_alipay_dict'):
                params['cluster_id'] = self.cluster_id.to_alipay_dict()
            else:
                params['cluster_id'] = self.cluster_id
        if self.cluster_name:
            if hasattr(self.cluster_name, 'to_alipay_dict'):
                params['cluster_name'] = self.cluster_name.to_alipay_dict()
            else:
                params['cluster_name'] = self.cluster_name
        if self.default_admin_ids:
            if isinstance(self.default_admin_ids, list):
                for i in range(0, len(self.default_admin_ids)):
                    element = self.default_admin_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.default_admin_ids[i] = element.to_alipay_dict()
            if hasattr(self.default_admin_ids, 'to_alipay_dict'):
                params['default_admin_ids'] = self.default_admin_ids.to_alipay_dict()
            else:
                params['default_admin_ids'] = self.default_admin_ids
        if self.default_group_name:
            if hasattr(self.default_group_name, 'to_alipay_dict'):
                params['default_group_name'] = self.default_group_name.to_alipay_dict()
            else:
                params['default_group_name'] = self.default_group_name
        if self.default_master_id:
            if hasattr(self.default_master_id, 'to_alipay_dict'):
                params['default_master_id'] = self.default_master_id.to_alipay_dict()
            else:
                params['default_master_id'] = self.default_master_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BcGroupClusterDetail()
        if 'auto_create_group' in d:
            o.auto_create_group = d['auto_create_group']
        if 'cluster_admin_ids' in d:
            o.cluster_admin_ids = d['cluster_admin_ids']
        if 'cluster_id' in d:
            o.cluster_id = d['cluster_id']
        if 'cluster_name' in d:
            o.cluster_name = d['cluster_name']
        if 'default_admin_ids' in d:
            o.default_admin_ids = d['default_admin_ids']
        if 'default_group_name' in d:
            o.default_group_name = d['default_group_name']
        if 'default_master_id' in d:
            o.default_master_id = d['default_master_id']
        return o


