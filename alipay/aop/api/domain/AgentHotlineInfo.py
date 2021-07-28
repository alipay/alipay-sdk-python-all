#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgentHotlineInfo(object):

    def __init__(self):
        self._ccs_instance_id = None
        self._group_ids = None

    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def group_ids(self):
        return self._group_ids

    @group_ids.setter
    def group_ids(self, value):
        if isinstance(value, list):
            self._group_ids = list()
            for i in value:
                self._group_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.group_ids:
            if isinstance(self.group_ids, list):
                for i in range(0, len(self.group_ids)):
                    element = self.group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_ids[i] = element.to_alipay_dict()
            if hasattr(self.group_ids, 'to_alipay_dict'):
                params['group_ids'] = self.group_ids.to_alipay_dict()
            else:
                params['group_ids'] = self.group_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgentHotlineInfo()
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        return o


