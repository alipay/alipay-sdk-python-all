#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppItemRelativeQueryPeriodInfo(object):

    def __init__(self):
        self._valid_days_after_receive = None
        self._wait_days_after_receive = None

    @property
    def valid_days_after_receive(self):
        return self._valid_days_after_receive

    @valid_days_after_receive.setter
    def valid_days_after_receive(self, value):
        self._valid_days_after_receive = value
    @property
    def wait_days_after_receive(self):
        return self._wait_days_after_receive

    @wait_days_after_receive.setter
    def wait_days_after_receive(self, value):
        self._wait_days_after_receive = value


    def to_alipay_dict(self):
        params = dict()
        if self.valid_days_after_receive:
            if hasattr(self.valid_days_after_receive, 'to_alipay_dict'):
                params['valid_days_after_receive'] = self.valid_days_after_receive.to_alipay_dict()
            else:
                params['valid_days_after_receive'] = self.valid_days_after_receive
        if self.wait_days_after_receive:
            if hasattr(self.wait_days_after_receive, 'to_alipay_dict'):
                params['wait_days_after_receive'] = self.wait_days_after_receive.to_alipay_dict()
            else:
                params['wait_days_after_receive'] = self.wait_days_after_receive
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemRelativeQueryPeriodInfo()
        if 'valid_days_after_receive' in d:
            o.valid_days_after_receive = d['valid_days_after_receive']
        if 'wait_days_after_receive' in d:
            o.wait_days_after_receive = d['wait_days_after_receive']
        return o


