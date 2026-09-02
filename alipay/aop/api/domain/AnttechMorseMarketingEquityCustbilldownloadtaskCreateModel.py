#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingEquityCustbilldownloadtaskCreateModel(object):

    def __init__(self):
        self._end_time = None
        self._inst_morse_id = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def inst_morse_id(self):
        return self._inst_morse_id

    @inst_morse_id.setter
    def inst_morse_id(self, value):
        self._inst_morse_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.inst_morse_id:
            if hasattr(self.inst_morse_id, 'to_alipay_dict'):
                params['inst_morse_id'] = self.inst_morse_id.to_alipay_dict()
            else:
                params['inst_morse_id'] = self.inst_morse_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingEquityCustbilldownloadtaskCreateModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'inst_morse_id' in d:
            o.inst_morse_id = d['inst_morse_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


