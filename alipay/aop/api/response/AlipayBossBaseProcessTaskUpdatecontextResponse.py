#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BPOpenApiTask import BPOpenApiTask


class AlipayBossBaseProcessTaskUpdatecontextResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseProcessTaskUpdatecontextResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseProcessTaskUpdatecontextResponse, self).parse_response_content(response_content)
        if 'biz_context' in response:
            self.biz_context = response['biz_context']
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'create_user' in response:
            self.create_user = response['create_user']
        if 'description' in response:
            self.description = response['description']
        if 'duration' in response:
            self.duration = response['duration']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_end' in response:
            self.gmt_end = response['gmt_end']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'modify_user' in response:
            self.modify_user = response['modify_user']
        if 'name' in response:
            self.name = response['name']
        if 'parent_id' in response:
            self.parent_id = response['parent_id']
        if 'parent_node' in response:
            self.parent_node = response['parent_node']
        if 'priority' in response:
            self.priority = response['priority']
        if 'puid' in response:
            self.puid = response['puid']
        if 'source_id' in response:
            self.source_id = response['source_id']
        if 'source_node_name' in response:
            self.source_node_name = response['source_node_name']
        if 'state' in response:
            self.state = response['state']
        if 'tasks' in response:
            self.tasks = response['tasks']
