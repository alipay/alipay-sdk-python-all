#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupmealOpenAuthAddResult(object):

    def __init__(self):
        self._add_openauth_result_status = None

    @property
    def add_openauth_result_status(self):
        return self._add_openauth_result_status

    @add_openauth_result_status.setter
    def add_openauth_result_status(self, value):
        self._add_openauth_result_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_openauth_result_status:
            if hasattr(self.add_openauth_result_status, 'to_alipay_dict'):
                params['add_openauth_result_status'] = self.add_openauth_result_status.to_alipay_dict()
            else:
                params['add_openauth_result_status'] = self.add_openauth_result_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupmealOpenAuthAddResult()
        if 'add_openauth_result_status' in d:
            o.add_openauth_result_status = d['add_openauth_result_status']
        return o


