#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BPOpenApiTask import BPOpenApiTask


class BPOpenApiInstance(object):

    def __init__(self):
        self._biz_context = None
        self._biz_id = None
        self._create_user = None
        self._description = None
        self._duration = None
        self._gmt_create = None
        self._gmt_end = None
        self._gmt_modified = None
        self._ip_role_id = None
        self._modify_user = None
        self._name = None
        self._parent_id = None
        self._parent_node = None
        self._priority = None
        self._puid = None
        self._source_id = None
        self._source_node_name = None
        self._state = None
        self._tasks = None

    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def modify_user(self):
        return self._modify_user

    @modify_user.setter
    def modify_user(self, value):
        self._modify_user = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def parent_node(self):
        return self._parent_node

    @parent_node.setter
    def parent_node(self, value):
        self._parent_node = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def puid(self):
        return self._puid

    @puid.setter
    def puid(self, value):
        self._puid = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_node_name(self):
        return self._source_node_name

    @source_node_name.setter
    def source_node_name(self, value):
        self._source_node_name = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        if isinstance(value, list):
            self._tasks = list()
            for i in value:
                if isinstance(i, BPOpenApiTask):
                    self._tasks.append(i)
                else:
                    self._tasks.append(BPOpenApiTask.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.modify_user:
            if hasattr(self.modify_user, 'to_alipay_dict'):
                params['modify_user'] = self.modify_user.to_alipay_dict()
            else:
                params['modify_user'] = self.modify_user
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.parent_node:
            if hasattr(self.parent_node, 'to_alipay_dict'):
                params['parent_node'] = self.parent_node.to_alipay_dict()
            else:
                params['parent_node'] = self.parent_node
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.puid:
            if hasattr(self.puid, 'to_alipay_dict'):
                params['puid'] = self.puid.to_alipay_dict()
            else:
                params['puid'] = self.puid
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_node_name:
            if hasattr(self.source_node_name, 'to_alipay_dict'):
                params['source_node_name'] = self.source_node_name.to_alipay_dict()
            else:
                params['source_node_name'] = self.source_node_name
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.tasks:
            if isinstance(self.tasks, list):
                for i in range(0, len(self.tasks)):
                    element = self.tasks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tasks[i] = element.to_alipay_dict()
            if hasattr(self.tasks, 'to_alipay_dict'):
                params['tasks'] = self.tasks.to_alipay_dict()
            else:
                params['tasks'] = self.tasks
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BPOpenApiInstance()
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'description' in d:
            o.description = d['description']
        if 'duration' in d:
            o.duration = d['duration']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'modify_user' in d:
            o.modify_user = d['modify_user']
        if 'name' in d:
            o.name = d['name']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'parent_node' in d:
            o.parent_node = d['parent_node']
        if 'priority' in d:
            o.priority = d['priority']
        if 'puid' in d:
            o.puid = d['puid']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_node_name' in d:
            o.source_node_name = d['source_node_name']
        if 'state' in d:
            o.state = d['state']
        if 'tasks' in d:
            o.tasks = d['tasks']
        return o


