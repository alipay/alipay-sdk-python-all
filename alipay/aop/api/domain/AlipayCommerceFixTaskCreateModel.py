#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FixExtData import FixExtData


class AlipayCommerceFixTaskCreateModel(object):

    def __init__(self):
        self._biz_type = None
        self._contact = None
        self._contact_phone = None
        self._description = None
        self._extra = None
        self._file_ids = None
        self._handler_id = None
        self._outer_id = None
        self._outer_system = None
        self._problem_id = None
        self._rule_scene = None
        self._source = None
        self._task_category = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, value):
        if isinstance(value, list):
            self._extra = list()
            for i in value:
                if isinstance(i, FixExtData):
                    self._extra.append(i)
                else:
                    self._extra.append(FixExtData.from_alipay_dict(i))
    @property
    def file_ids(self):
        return self._file_ids

    @file_ids.setter
    def file_ids(self, value):
        self._file_ids = value
    @property
    def handler_id(self):
        return self._handler_id

    @handler_id.setter
    def handler_id(self, value):
        self._handler_id = value
    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, value):
        self._outer_id = value
    @property
    def outer_system(self):
        return self._outer_system

    @outer_system.setter
    def outer_system(self, value):
        self._outer_system = value
    @property
    def problem_id(self):
        return self._problem_id

    @problem_id.setter
    def problem_id(self, value):
        self._problem_id = value
    @property
    def rule_scene(self):
        return self._rule_scene

    @rule_scene.setter
    def rule_scene(self, value):
        self._rule_scene = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def task_category(self):
        return self._task_category

    @task_category.setter
    def task_category(self, value):
        self._task_category = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.contact:
            if hasattr(self.contact, 'to_alipay_dict'):
                params['contact'] = self.contact.to_alipay_dict()
            else:
                params['contact'] = self.contact
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.extra:
            if isinstance(self.extra, list):
                for i in range(0, len(self.extra)):
                    element = self.extra[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extra[i] = element.to_alipay_dict()
            if hasattr(self.extra, 'to_alipay_dict'):
                params['extra'] = self.extra.to_alipay_dict()
            else:
                params['extra'] = self.extra
        if self.file_ids:
            if hasattr(self.file_ids, 'to_alipay_dict'):
                params['file_ids'] = self.file_ids.to_alipay_dict()
            else:
                params['file_ids'] = self.file_ids
        if self.handler_id:
            if hasattr(self.handler_id, 'to_alipay_dict'):
                params['handler_id'] = self.handler_id.to_alipay_dict()
            else:
                params['handler_id'] = self.handler_id
        if self.outer_id:
            if hasattr(self.outer_id, 'to_alipay_dict'):
                params['outer_id'] = self.outer_id.to_alipay_dict()
            else:
                params['outer_id'] = self.outer_id
        if self.outer_system:
            if hasattr(self.outer_system, 'to_alipay_dict'):
                params['outer_system'] = self.outer_system.to_alipay_dict()
            else:
                params['outer_system'] = self.outer_system
        if self.problem_id:
            if hasattr(self.problem_id, 'to_alipay_dict'):
                params['problem_id'] = self.problem_id.to_alipay_dict()
            else:
                params['problem_id'] = self.problem_id
        if self.rule_scene:
            if hasattr(self.rule_scene, 'to_alipay_dict'):
                params['rule_scene'] = self.rule_scene.to_alipay_dict()
            else:
                params['rule_scene'] = self.rule_scene
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.task_category:
            if hasattr(self.task_category, 'to_alipay_dict'):
                params['task_category'] = self.task_category.to_alipay_dict()
            else:
                params['task_category'] = self.task_category
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFixTaskCreateModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'contact' in d:
            o.contact = d['contact']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'description' in d:
            o.description = d['description']
        if 'extra' in d:
            o.extra = d['extra']
        if 'file_ids' in d:
            o.file_ids = d['file_ids']
        if 'handler_id' in d:
            o.handler_id = d['handler_id']
        if 'outer_id' in d:
            o.outer_id = d['outer_id']
        if 'outer_system' in d:
            o.outer_system = d['outer_system']
        if 'problem_id' in d:
            o.problem_id = d['problem_id']
        if 'rule_scene' in d:
            o.rule_scene = d['rule_scene']
        if 'source' in d:
            o.source = d['source']
        if 'task_category' in d:
            o.task_category = d['task_category']
        return o


