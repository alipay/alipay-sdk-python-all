#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SameTypeReportInfoDTO(object):

    def __init__(self):
        self._org_name = None
        self._report_id = None
        self._report_name = None
        self._report_type = None
        self._score = None
        self._treatment_time = None

    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def report_id(self):
        return self._report_id

    @report_id.setter
    def report_id(self, value):
        self._report_id = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def treatment_time(self):
        return self._treatment_time

    @treatment_time.setter
    def treatment_time(self, value):
        self._treatment_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.report_id:
            if hasattr(self.report_id, 'to_alipay_dict'):
                params['report_id'] = self.report_id.to_alipay_dict()
            else:
                params['report_id'] = self.report_id
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.treatment_time:
            if hasattr(self.treatment_time, 'to_alipay_dict'):
                params['treatment_time'] = self.treatment_time.to_alipay_dict()
            else:
                params['treatment_time'] = self.treatment_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SameTypeReportInfoDTO()
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'report_id' in d:
            o.report_id = d['report_id']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_type' in d:
            o.report_type = d['report_type']
        if 'score' in d:
            o.score = d['score']
        if 'treatment_time' in d:
            o.treatment_time = d['treatment_time']
        return o


