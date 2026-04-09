#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssistantLicenseInfo(object):

    def __init__(self):
        self._begin_time = None
        self._end_time = None
        self._license = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def license(self):
        return self._license

    @license.setter
    def license(self, value):
        self._license = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.license:
            if hasattr(self.license, 'to_alipay_dict'):
                params['license'] = self.license.to_alipay_dict()
            else:
                params['license'] = self.license
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssistantLicenseInfo()
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'license' in d:
            o.license = d['license']
        return o


