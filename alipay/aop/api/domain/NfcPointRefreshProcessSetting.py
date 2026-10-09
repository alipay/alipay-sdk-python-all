#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NfcPointRefreshShowTime import NfcPointRefreshShowTime


class NfcPointRefreshProcessSetting(object):

    def __init__(self):
        self._show_times = None
        self._show_type = None

    @property
    def show_times(self):
        return self._show_times

    @show_times.setter
    def show_times(self, value):
        if isinstance(value, list):
            self._show_times = list()
            for i in value:
                if isinstance(i, NfcPointRefreshShowTime):
                    self._show_times.append(i)
                else:
                    self._show_times.append(NfcPointRefreshShowTime.from_alipay_dict(i))
    @property
    def show_type(self):
        return self._show_type

    @show_type.setter
    def show_type(self, value):
        self._show_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.show_times:
            if isinstance(self.show_times, list):
                for i in range(0, len(self.show_times)):
                    element = self.show_times[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.show_times[i] = element.to_alipay_dict()
            if hasattr(self.show_times, 'to_alipay_dict'):
                params['show_times'] = self.show_times.to_alipay_dict()
            else:
                params['show_times'] = self.show_times
        if self.show_type:
            if hasattr(self.show_type, 'to_alipay_dict'):
                params['show_type'] = self.show_type.to_alipay_dict()
            else:
                params['show_type'] = self.show_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcPointRefreshProcessSetting()
        if 'show_times' in d:
            o.show_times = d['show_times']
        if 'show_type' in d:
            o.show_type = d['show_type']
        return o


