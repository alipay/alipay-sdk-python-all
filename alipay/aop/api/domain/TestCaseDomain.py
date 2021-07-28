#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TestCaseDomain(object):

    def __init__(self):
        self._action = None
        self._case_id = None
        self._collection_id = None
        self._desc = None
        self._ext_infos = None
        self._priority = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def case_id(self):
        return self._case_id

    @case_id.setter
    def case_id(self, value):
        self._case_id = value
    @property
    def collection_id(self):
        return self._collection_id

    @collection_id.setter
    def collection_id(self, value):
        self._collection_id = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.case_id:
            if hasattr(self.case_id, 'to_alipay_dict'):
                params['case_id'] = self.case_id.to_alipay_dict()
            else:
                params['case_id'] = self.case_id
        if self.collection_id:
            if hasattr(self.collection_id, 'to_alipay_dict'):
                params['collection_id'] = self.collection_id.to_alipay_dict()
            else:
                params['collection_id'] = self.collection_id
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TestCaseDomain()
        if 'action' in d:
            o.action = d['action']
        if 'case_id' in d:
            o.case_id = d['case_id']
        if 'collection_id' in d:
            o.collection_id = d['collection_id']
        if 'desc' in d:
            o.desc = d['desc']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'priority' in d:
            o.priority = d['priority']
        return o


