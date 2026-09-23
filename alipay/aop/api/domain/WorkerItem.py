#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WorkerItem(object):

    def __init__(self):
        self._avatar_url = None
        self._creator = None
        self._description = None
        self._display = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._ivr_code = None
        self._modifier = None
        self._name = None
        self._status = None
        self._tenant_id = None
        self._type = None
        self._version_type = None
        self._worker_code = None

    @property
    def avatar_url(self):
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        self._avatar_url = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value
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
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def ivr_code(self):
        return self._ivr_code

    @ivr_code.setter
    def ivr_code(self, value):
        self._ivr_code = value
    @property
    def modifier(self):
        return self._modifier

    @modifier.setter
    def modifier(self, value):
        self._modifier = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def version_type(self):
        return self._version_type

    @version_type.setter
    def version_type(self, value):
        self._version_type = value
    @property
    def worker_code(self):
        return self._worker_code

    @worker_code.setter
    def worker_code(self, value):
        self._worker_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar_url:
            if hasattr(self.avatar_url, 'to_alipay_dict'):
                params['avatar_url'] = self.avatar_url.to_alipay_dict()
            else:
                params['avatar_url'] = self.avatar_url
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.display:
            if hasattr(self.display, 'to_alipay_dict'):
                params['display'] = self.display.to_alipay_dict()
            else:
                params['display'] = self.display
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
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.ivr_code:
            if hasattr(self.ivr_code, 'to_alipay_dict'):
                params['ivr_code'] = self.ivr_code.to_alipay_dict()
            else:
                params['ivr_code'] = self.ivr_code
        if self.modifier:
            if hasattr(self.modifier, 'to_alipay_dict'):
                params['modifier'] = self.modifier.to_alipay_dict()
            else:
                params['modifier'] = self.modifier
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.version_type:
            if hasattr(self.version_type, 'to_alipay_dict'):
                params['version_type'] = self.version_type.to_alipay_dict()
            else:
                params['version_type'] = self.version_type
        if self.worker_code:
            if hasattr(self.worker_code, 'to_alipay_dict'):
                params['worker_code'] = self.worker_code.to_alipay_dict()
            else:
                params['worker_code'] = self.worker_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorkerItem()
        if 'avatar_url' in d:
            o.avatar_url = d['avatar_url']
        if 'creator' in d:
            o.creator = d['creator']
        if 'description' in d:
            o.description = d['description']
        if 'display' in d:
            o.display = d['display']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'ivr_code' in d:
            o.ivr_code = d['ivr_code']
        if 'modifier' in d:
            o.modifier = d['modifier']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'type' in d:
            o.type = d['type']
        if 'version_type' in d:
            o.version_type = d['version_type']
        if 'worker_code' in d:
            o.worker_code = d['worker_code']
        return o


