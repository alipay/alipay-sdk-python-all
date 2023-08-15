#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalopUcdpApecreativeDesigntextQueryModel(object):

    def __init__(self):
        self._design_id = None
        self._group_id = None
        self._project_id = None

    @property
    def design_id(self):
        return self._design_id

    @design_id.setter
    def design_id(self, value):
        self._design_id = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.design_id:
            if hasattr(self.design_id, 'to_alipay_dict'):
                params['design_id'] = self.design_id.to_alipay_dict()
            else:
                params['design_id'] = self.design_id
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalopUcdpApecreativeDesigntextQueryModel()
        if 'design_id' in d:
            o.design_id = d['design_id']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


