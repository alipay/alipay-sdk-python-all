#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BPOpenApiAddSignContent import BPOpenApiAddSignContent
from alipay.aop.api.domain.BPOpenApiPUID import BPOpenApiPUID


class AlipayBossBaseProcessInstanceCreateModel(object):

    def __init__(self):
        self._add_sign_content = None
        self._context = None
        self._creator = None
        self._description = None
        self._ip_role_id = None
        self._name = None
        self._priority = None
        self._puid = None
        self._source_node_name = None
        self._source_puid = None
        self._sub_contexts = None

    @property
    def add_sign_content(self):
        return self._add_sign_content

    @add_sign_content.setter
    def add_sign_content(self, value):
        if isinstance(value, list):
            self._add_sign_content = list()
            for i in value:
                if isinstance(i, BPOpenApiAddSignContent):
                    self._add_sign_content.append(i)
                else:
                    self._add_sign_content.append(BPOpenApiAddSignContent.from_alipay_dict(i))
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value
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
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
        if isinstance(value, BPOpenApiPUID):
            self._puid = value
        else:
            self._puid = BPOpenApiPUID.from_alipay_dict(value)
    @property
    def source_node_name(self):
        return self._source_node_name

    @source_node_name.setter
    def source_node_name(self, value):
        self._source_node_name = value
    @property
    def source_puid(self):
        return self._source_puid

    @source_puid.setter
    def source_puid(self, value):
        self._source_puid = value
    @property
    def sub_contexts(self):
        return self._sub_contexts

    @sub_contexts.setter
    def sub_contexts(self, value):
        if isinstance(value, list):
            self._sub_contexts = list()
            for i in value:
                self._sub_contexts.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.add_sign_content:
            if isinstance(self.add_sign_content, list):
                for i in range(0, len(self.add_sign_content)):
                    element = self.add_sign_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_sign_content[i] = element.to_alipay_dict()
            if hasattr(self.add_sign_content, 'to_alipay_dict'):
                params['add_sign_content'] = self.add_sign_content.to_alipay_dict()
            else:
                params['add_sign_content'] = self.add_sign_content
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
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
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        if self.source_node_name:
            if hasattr(self.source_node_name, 'to_alipay_dict'):
                params['source_node_name'] = self.source_node_name.to_alipay_dict()
            else:
                params['source_node_name'] = self.source_node_name
        if self.source_puid:
            if hasattr(self.source_puid, 'to_alipay_dict'):
                params['source_puid'] = self.source_puid.to_alipay_dict()
            else:
                params['source_puid'] = self.source_puid
        if self.sub_contexts:
            if isinstance(self.sub_contexts, list):
                for i in range(0, len(self.sub_contexts)):
                    element = self.sub_contexts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_contexts[i] = element.to_alipay_dict()
            if hasattr(self.sub_contexts, 'to_alipay_dict'):
                params['sub_contexts'] = self.sub_contexts.to_alipay_dict()
            else:
                params['sub_contexts'] = self.sub_contexts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseProcessInstanceCreateModel()
        if 'add_sign_content' in d:
            o.add_sign_content = d['add_sign_content']
        if 'context' in d:
            o.context = d['context']
        if 'creator' in d:
            o.creator = d['creator']
        if 'description' in d:
            o.description = d['description']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'name' in d:
            o.name = d['name']
        if 'priority' in d:
            o.priority = d['priority']
        if 'puid' in d:
            o.puid = d['puid']
        if 'source_node_name' in d:
            o.source_node_name = d['source_node_name']
        if 'source_puid' in d:
            o.source_puid = d['source_puid']
        if 'sub_contexts' in d:
            o.sub_contexts = d['sub_contexts']
        return o


