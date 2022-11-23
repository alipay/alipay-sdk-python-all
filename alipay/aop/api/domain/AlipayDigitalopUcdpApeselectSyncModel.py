#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApeSelect import ApeSelect


class AlipayDigitalopUcdpApeselectSyncModel(object):

    def __init__(self):
        self._project_id = None
        self._select_list = None

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def select_list(self):
        return self._select_list

    @select_list.setter
    def select_list(self, value):
        if isinstance(value, ApeSelect):
            self._select_list = value
        else:
            self._select_list = ApeSelect.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.select_list:
            if hasattr(self.select_list, 'to_alipay_dict'):
                params['select_list'] = self.select_list.to_alipay_dict()
            else:
                params['select_list'] = self.select_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalopUcdpApeselectSyncModel()
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'select_list' in d:
            o.select_list = d['select_list']
        return o


