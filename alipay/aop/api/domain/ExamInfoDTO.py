#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExamInfoDTO(object):

    def __init__(self):
        self._certificate_issue_date = None
        self._certificate_level = None
        self._certificate_status = None
        self._college_exam_enrollment_id = None
        self._exam_end_time = None
        self._exam_start_time = None
        self._passport_id = None
        self._year_of_birth = None

    @property
    def certificate_issue_date(self):
        return self._certificate_issue_date

    @certificate_issue_date.setter
    def certificate_issue_date(self, value):
        self._certificate_issue_date = value
    @property
    def certificate_level(self):
        return self._certificate_level

    @certificate_level.setter
    def certificate_level(self, value):
        self._certificate_level = value
    @property
    def certificate_status(self):
        return self._certificate_status

    @certificate_status.setter
    def certificate_status(self, value):
        self._certificate_status = value
    @property
    def college_exam_enrollment_id(self):
        return self._college_exam_enrollment_id

    @college_exam_enrollment_id.setter
    def college_exam_enrollment_id(self, value):
        self._college_exam_enrollment_id = value
    @property
    def exam_end_time(self):
        return self._exam_end_time

    @exam_end_time.setter
    def exam_end_time(self, value):
        self._exam_end_time = value
    @property
    def exam_start_time(self):
        return self._exam_start_time

    @exam_start_time.setter
    def exam_start_time(self, value):
        self._exam_start_time = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def year_of_birth(self):
        return self._year_of_birth

    @year_of_birth.setter
    def year_of_birth(self, value):
        self._year_of_birth = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_issue_date:
            if hasattr(self.certificate_issue_date, 'to_alipay_dict'):
                params['certificate_issue_date'] = self.certificate_issue_date.to_alipay_dict()
            else:
                params['certificate_issue_date'] = self.certificate_issue_date
        if self.certificate_level:
            if hasattr(self.certificate_level, 'to_alipay_dict'):
                params['certificate_level'] = self.certificate_level.to_alipay_dict()
            else:
                params['certificate_level'] = self.certificate_level
        if self.certificate_status:
            if hasattr(self.certificate_status, 'to_alipay_dict'):
                params['certificate_status'] = self.certificate_status.to_alipay_dict()
            else:
                params['certificate_status'] = self.certificate_status
        if self.college_exam_enrollment_id:
            if hasattr(self.college_exam_enrollment_id, 'to_alipay_dict'):
                params['college_exam_enrollment_id'] = self.college_exam_enrollment_id.to_alipay_dict()
            else:
                params['college_exam_enrollment_id'] = self.college_exam_enrollment_id
        if self.exam_end_time:
            if hasattr(self.exam_end_time, 'to_alipay_dict'):
                params['exam_end_time'] = self.exam_end_time.to_alipay_dict()
            else:
                params['exam_end_time'] = self.exam_end_time
        if self.exam_start_time:
            if hasattr(self.exam_start_time, 'to_alipay_dict'):
                params['exam_start_time'] = self.exam_start_time.to_alipay_dict()
            else:
                params['exam_start_time'] = self.exam_start_time
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.year_of_birth:
            if hasattr(self.year_of_birth, 'to_alipay_dict'):
                params['year_of_birth'] = self.year_of_birth.to_alipay_dict()
            else:
                params['year_of_birth'] = self.year_of_birth
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExamInfoDTO()
        if 'certificate_issue_date' in d:
            o.certificate_issue_date = d['certificate_issue_date']
        if 'certificate_level' in d:
            o.certificate_level = d['certificate_level']
        if 'certificate_status' in d:
            o.certificate_status = d['certificate_status']
        if 'college_exam_enrollment_id' in d:
            o.college_exam_enrollment_id = d['college_exam_enrollment_id']
        if 'exam_end_time' in d:
            o.exam_end_time = d['exam_end_time']
        if 'exam_start_time' in d:
            o.exam_start_time = d['exam_start_time']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'year_of_birth' in d:
            o.year_of_birth = d['year_of_birth']
        return o


