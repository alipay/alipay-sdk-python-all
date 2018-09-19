#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CrowdRuleInfo(object):

    def __init__(self):
        self._ruledesc = None
        self._ruleid = None
        self._status = None

    @property
    def ruledesc(self):
        return self._ruledesc

    @ruledesc.setter
    def ruledesc(self, value):
        self._ruledesc = value
    @property
    def ruleid(self):
        return self._ruleid

    @ruleid.setter
    def ruleid(self, value):
        self._ruleid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ruledesc:
            if hasattr(self.ruledesc, 'to_alipay_dict'):
                params['ruledesc'] = self.ruledesc.to_alipay_dict()
            else:
                params['ruledesc'] = self.ruledesc
        if self.ruleid:
            if hasattr(self.ruleid, 'to_alipay_dict'):
                params['ruleid'] = self.ruleid.to_alipay_dict()
            else:
                params['ruleid'] = self.ruleid
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdRuleInfo()
        if 'ruledesc' in d:
            o.ruledesc = d['ruledesc']
        if 'ruleid' in d:
            o.ruleid = d['ruleid']
        if 'status' in d:
            o.status = d['status']
        return o


