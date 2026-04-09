#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupmealOpenAuthCancelResult(object):

    def __init__(self):
        self._cancel_openauth_result_status = None

    @property
    def cancel_openauth_result_status(self):
        return self._cancel_openauth_result_status

    @cancel_openauth_result_status.setter
    def cancel_openauth_result_status(self, value):
        self._cancel_openauth_result_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_openauth_result_status:
            if hasattr(self.cancel_openauth_result_status, 'to_alipay_dict'):
                params['cancel_openauth_result_status'] = self.cancel_openauth_result_status.to_alipay_dict()
            else:
                params['cancel_openauth_result_status'] = self.cancel_openauth_result_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupmealOpenAuthCancelResult()
        if 'cancel_openauth_result_status' in d:
            o.cancel_openauth_result_status = d['cancel_openauth_result_status']
        return o


