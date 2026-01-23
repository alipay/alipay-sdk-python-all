#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryRpoInterviewSyncModel(object):

    def __init__(self):
        self._assessment_digest = None
        self._assessment_result = None
        self._completed_status = None
        self._completed_time = None
        self._interview_duration = None
        self._interview_no = None
        self._interview_score = None
        self._interview_status = None
        self._report_time = None
        self._report_url = None

    @property
    def assessment_digest(self):
        return self._assessment_digest

    @assessment_digest.setter
    def assessment_digest(self, value):
        self._assessment_digest = value
    @property
    def assessment_result(self):
        return self._assessment_result

    @assessment_result.setter
    def assessment_result(self, value):
        self._assessment_result = value
    @property
    def completed_status(self):
        return self._completed_status

    @completed_status.setter
    def completed_status(self, value):
        self._completed_status = value
    @property
    def completed_time(self):
        return self._completed_time

    @completed_time.setter
    def completed_time(self, value):
        self._completed_time = value
    @property
    def interview_duration(self):
        return self._interview_duration

    @interview_duration.setter
    def interview_duration(self, value):
        self._interview_duration = value
    @property
    def interview_no(self):
        return self._interview_no

    @interview_no.setter
    def interview_no(self, value):
        self._interview_no = value
    @property
    def interview_score(self):
        return self._interview_score

    @interview_score.setter
    def interview_score(self, value):
        self._interview_score = value
    @property
    def interview_status(self):
        return self._interview_status

    @interview_status.setter
    def interview_status(self, value):
        self._interview_status = value
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value
    @property
    def report_url(self):
        return self._report_url

    @report_url.setter
    def report_url(self, value):
        self._report_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.assessment_digest:
            if hasattr(self.assessment_digest, 'to_alipay_dict'):
                params['assessment_digest'] = self.assessment_digest.to_alipay_dict()
            else:
                params['assessment_digest'] = self.assessment_digest
        if self.assessment_result:
            if hasattr(self.assessment_result, 'to_alipay_dict'):
                params['assessment_result'] = self.assessment_result.to_alipay_dict()
            else:
                params['assessment_result'] = self.assessment_result
        if self.completed_status:
            if hasattr(self.completed_status, 'to_alipay_dict'):
                params['completed_status'] = self.completed_status.to_alipay_dict()
            else:
                params['completed_status'] = self.completed_status
        if self.completed_time:
            if hasattr(self.completed_time, 'to_alipay_dict'):
                params['completed_time'] = self.completed_time.to_alipay_dict()
            else:
                params['completed_time'] = self.completed_time
        if self.interview_duration:
            if hasattr(self.interview_duration, 'to_alipay_dict'):
                params['interview_duration'] = self.interview_duration.to_alipay_dict()
            else:
                params['interview_duration'] = self.interview_duration
        if self.interview_no:
            if hasattr(self.interview_no, 'to_alipay_dict'):
                params['interview_no'] = self.interview_no.to_alipay_dict()
            else:
                params['interview_no'] = self.interview_no
        if self.interview_score:
            if hasattr(self.interview_score, 'to_alipay_dict'):
                params['interview_score'] = self.interview_score.to_alipay_dict()
            else:
                params['interview_score'] = self.interview_score
        if self.interview_status:
            if hasattr(self.interview_status, 'to_alipay_dict'):
                params['interview_status'] = self.interview_status.to_alipay_dict()
            else:
                params['interview_status'] = self.interview_status
        if self.report_time:
            if hasattr(self.report_time, 'to_alipay_dict'):
                params['report_time'] = self.report_time.to_alipay_dict()
            else:
                params['report_time'] = self.report_time
        if self.report_url:
            if hasattr(self.report_url, 'to_alipay_dict'):
                params['report_url'] = self.report_url.to_alipay_dict()
            else:
                params['report_url'] = self.report_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryRpoInterviewSyncModel()
        if 'assessment_digest' in d:
            o.assessment_digest = d['assessment_digest']
        if 'assessment_result' in d:
            o.assessment_result = d['assessment_result']
        if 'completed_status' in d:
            o.completed_status = d['completed_status']
        if 'completed_time' in d:
            o.completed_time = d['completed_time']
        if 'interview_duration' in d:
            o.interview_duration = d['interview_duration']
        if 'interview_no' in d:
            o.interview_no = d['interview_no']
        if 'interview_score' in d:
            o.interview_score = d['interview_score']
        if 'interview_status' in d:
            o.interview_status = d['interview_status']
        if 'report_time' in d:
            o.report_time = d['report_time']
        if 'report_url' in d:
            o.report_url = d['report_url']
        return o


