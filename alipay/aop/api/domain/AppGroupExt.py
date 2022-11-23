#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppGroupRelationshipExt import AppGroupRelationshipExt


class AppGroupExt(object):

    def __init__(self):
        self._app_group_relationship_ext = None
        self._gmt_create = None
        self._gmt_modified = None
        self._group_id = None
        self._group_name = None
        self._owner_id = None
        self._owner_type = None

    @property
    def app_group_relationship_ext(self):
        return self._app_group_relationship_ext

    @app_group_relationship_ext.setter
    def app_group_relationship_ext(self, value):
        if isinstance(value, list):
            self._app_group_relationship_ext = list()
            for i in value:
                if isinstance(i, AppGroupRelationshipExt):
                    self._app_group_relationship_ext.append(i)
                else:
                    self._app_group_relationship_ext.append(AppGroupRelationshipExt.from_alipay_dict(i))
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_group_relationship_ext:
            if isinstance(self.app_group_relationship_ext, list):
                for i in range(0, len(self.app_group_relationship_ext)):
                    element = self.app_group_relationship_ext[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_group_relationship_ext[i] = element.to_alipay_dict()
            if hasattr(self.app_group_relationship_ext, 'to_alipay_dict'):
                params['app_group_relationship_ext'] = self.app_group_relationship_ext.to_alipay_dict()
            else:
                params['app_group_relationship_ext'] = self.app_group_relationship_ext
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppGroupExt()
        if 'app_group_relationship_ext' in d:
            o.app_group_relationship_ext = d['app_group_relationship_ext']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        return o


