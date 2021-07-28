#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateTrainGroupsAddModel(object):

    def __init__(self):
        self._group_ids = None
        self._org_id = None

    @property
    def group_ids(self):
        return self._group_ids

    @group_ids.setter
    def group_ids(self, value):
        if isinstance(value, list):
            self._group_ids = list()
            for i in value:
                self._group_ids.append(i)
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTrainGroupsAddModel()
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        if 'org_id' in d:
            o.org_id = d['org_id']
        return o


