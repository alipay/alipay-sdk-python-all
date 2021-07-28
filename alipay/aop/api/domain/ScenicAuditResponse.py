#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicAuditInfo import ScenicAuditInfo


class ScenicAuditResponse(object):

    def __init__(self):
        self._scenic_audit_info = None

    @property
    def scenic_audit_info(self):
        return self._scenic_audit_info

    @scenic_audit_info.setter
    def scenic_audit_info(self, value):
        if isinstance(value, list):
            self._scenic_audit_info = list()
            for i in value:
                if isinstance(i, ScenicAuditInfo):
                    self._scenic_audit_info.append(i)
                else:
                    self._scenic_audit_info.append(ScenicAuditInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.scenic_audit_info:
            if isinstance(self.scenic_audit_info, list):
                for i in range(0, len(self.scenic_audit_info)):
                    element = self.scenic_audit_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scenic_audit_info[i] = element.to_alipay_dict()
            if hasattr(self.scenic_audit_info, 'to_alipay_dict'):
                params['scenic_audit_info'] = self.scenic_audit_info.to_alipay_dict()
            else:
                params['scenic_audit_info'] = self.scenic_audit_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenicAuditResponse()
        if 'scenic_audit_info' in d:
            o.scenic_audit_info = d['scenic_audit_info']
        return o


