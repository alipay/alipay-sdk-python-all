#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleCharityProjectTest(object):

    def __init__(self):
        self._project_id = None
        self._project_open_id = None

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_open_id(self):
        return self._project_open_id

    @project_open_id.setter
    def project_open_id(self, value):
        self._project_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_open_id:
            if hasattr(self.project_open_id, 'to_alipay_dict'):
                params['project_open_id'] = self.project_open_id.to_alipay_dict()
            else:
                params['project_open_id'] = self.project_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleCharityProjectTest()
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_open_id' in d:
            o.project_open_id = d['project_open_id']
        return o


