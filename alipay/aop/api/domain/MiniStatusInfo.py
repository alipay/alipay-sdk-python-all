#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniStatusInfo(object):

    def __init__(self):
        self._display_status = None
        self._display_status_desc = None

    @property
    def display_status(self):
        return self._display_status

    @display_status.setter
    def display_status(self, value):
        self._display_status = value
    @property
    def display_status_desc(self):
        return self._display_status_desc

    @display_status_desc.setter
    def display_status_desc(self, value):
        self._display_status_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_status:
            if hasattr(self.display_status, 'to_alipay_dict'):
                params['display_status'] = self.display_status.to_alipay_dict()
            else:
                params['display_status'] = self.display_status
        if self.display_status_desc:
            if hasattr(self.display_status_desc, 'to_alipay_dict'):
                params['display_status_desc'] = self.display_status_desc.to_alipay_dict()
            else:
                params['display_status_desc'] = self.display_status_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniStatusInfo()
        if 'display_status' in d:
            o.display_status = d['display_status']
        if 'display_status_desc' in d:
            o.display_status_desc = d['display_status_desc']
        return o


