#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RcsmartAuditContent import RcsmartAuditContent


class RcsmartSceneContentData(object):

    def __init__(self):
        self._audit_content_list = None
        self._scene_code = None

    @property
    def audit_content_list(self):
        return self._audit_content_list

    @audit_content_list.setter
    def audit_content_list(self, value):
        if isinstance(value, list):
            self._audit_content_list = list()
            for i in value:
                if isinstance(i, RcsmartAuditContent):
                    self._audit_content_list.append(i)
                else:
                    self._audit_content_list.append(RcsmartAuditContent.from_alipay_dict(i))
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_content_list:
            if isinstance(self.audit_content_list, list):
                for i in range(0, len(self.audit_content_list)):
                    element = self.audit_content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.audit_content_list[i] = element.to_alipay_dict()
            if hasattr(self.audit_content_list, 'to_alipay_dict'):
                params['audit_content_list'] = self.audit_content_list.to_alipay_dict()
            else:
                params['audit_content_list'] = self.audit_content_list
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcsmartSceneContentData()
        if 'audit_content_list' in d:
            o.audit_content_list = d['audit_content_list']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


