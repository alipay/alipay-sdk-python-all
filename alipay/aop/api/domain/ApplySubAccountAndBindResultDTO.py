#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApplySubAccountAndBindResultDTO(object):

    def __init__(self):
        self._apply_no = None
        self._apply_status = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplySubAccountAndBindResultDTO()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        return o


