#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppItemRelativeModifyPeriodInfo(object):

    def __init__(self):
        self._valid_days_after_receive = None

    @property
    def valid_days_after_receive(self):
        return self._valid_days_after_receive

    @valid_days_after_receive.setter
    def valid_days_after_receive(self, value):
        self._valid_days_after_receive = value


    def to_alipay_dict(self):
        params = dict()
        if self.valid_days_after_receive:
            if hasattr(self.valid_days_after_receive, 'to_alipay_dict'):
                params['valid_days_after_receive'] = self.valid_days_after_receive.to_alipay_dict()
            else:
                params['valid_days_after_receive'] = self.valid_days_after_receive
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemRelativeModifyPeriodInfo()
        if 'valid_days_after_receive' in d:
            o.valid_days_after_receive = d['valid_days_after_receive']
        return o


