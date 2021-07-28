#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneApplicationIssueConfirmModel(object):

    def __init__(self):
        self._application_no = None
        self._issue_type = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value
    @property
    def issue_type(self):
        return self._issue_type

    @issue_type.setter
    def issue_type(self, value):
        self._issue_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_no:
            if hasattr(self.application_no, 'to_alipay_dict'):
                params['application_no'] = self.application_no.to_alipay_dict()
            else:
                params['application_no'] = self.application_no
        if self.issue_type:
            if hasattr(self.issue_type, 'to_alipay_dict'):
                params['issue_type'] = self.issue_type.to_alipay_dict()
            else:
                params['issue_type'] = self.issue_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneApplicationIssueConfirmModel()
        if 'application_no' in d:
            o.application_no = d['application_no']
        if 'issue_type' in d:
            o.issue_type = d['issue_type']
        return o


