#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantActivityModifyModel(object):

    def __init__(self):
        self._action = None
        self._activity_no = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def activity_no(self):
        return self._activity_no

    @activity_no.setter
    def activity_no(self, value):
        self._activity_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.activity_no:
            if hasattr(self.activity_no, 'to_alipay_dict'):
                params['activity_no'] = self.activity_no.to_alipay_dict()
            else:
                params['activity_no'] = self.activity_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantActivityModifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'activity_no' in d:
            o.activity_no = d['activity_no']
        return o


