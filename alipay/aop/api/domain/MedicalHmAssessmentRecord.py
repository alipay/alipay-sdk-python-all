#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalHmAssessmentRecord(object):

    def __init__(self):
        self._answers_json = None
        self._assessment_detail = None
        self._assessment_id = None
        self._assessment_level = None
        self._assessment_name = None
        self._assessment_record_id = None
        self._assessment_score = None
        self._assessment_summary = None
        self._gmt_create = None
        self._gmt_modified = None

    @property
    def answers_json(self):
        return self._answers_json

    @answers_json.setter
    def answers_json(self, value):
        self._answers_json = value
    @property
    def assessment_detail(self):
        return self._assessment_detail

    @assessment_detail.setter
    def assessment_detail(self, value):
        self._assessment_detail = value
    @property
    def assessment_id(self):
        return self._assessment_id

    @assessment_id.setter
    def assessment_id(self, value):
        self._assessment_id = value
    @property
    def assessment_level(self):
        return self._assessment_level

    @assessment_level.setter
    def assessment_level(self, value):
        self._assessment_level = value
    @property
    def assessment_name(self):
        return self._assessment_name

    @assessment_name.setter
    def assessment_name(self, value):
        self._assessment_name = value
    @property
    def assessment_record_id(self):
        return self._assessment_record_id

    @assessment_record_id.setter
    def assessment_record_id(self, value):
        self._assessment_record_id = value
    @property
    def assessment_score(self):
        return self._assessment_score

    @assessment_score.setter
    def assessment_score(self, value):
        self._assessment_score = value
    @property
    def assessment_summary(self):
        return self._assessment_summary

    @assessment_summary.setter
    def assessment_summary(self, value):
        self._assessment_summary = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value


    def to_alipay_dict(self):
        params = dict()
        if self.answers_json:
            if hasattr(self.answers_json, 'to_alipay_dict'):
                params['answers_json'] = self.answers_json.to_alipay_dict()
            else:
                params['answers_json'] = self.answers_json
        if self.assessment_detail:
            if hasattr(self.assessment_detail, 'to_alipay_dict'):
                params['assessment_detail'] = self.assessment_detail.to_alipay_dict()
            else:
                params['assessment_detail'] = self.assessment_detail
        if self.assessment_id:
            if hasattr(self.assessment_id, 'to_alipay_dict'):
                params['assessment_id'] = self.assessment_id.to_alipay_dict()
            else:
                params['assessment_id'] = self.assessment_id
        if self.assessment_level:
            if hasattr(self.assessment_level, 'to_alipay_dict'):
                params['assessment_level'] = self.assessment_level.to_alipay_dict()
            else:
                params['assessment_level'] = self.assessment_level
        if self.assessment_name:
            if hasattr(self.assessment_name, 'to_alipay_dict'):
                params['assessment_name'] = self.assessment_name.to_alipay_dict()
            else:
                params['assessment_name'] = self.assessment_name
        if self.assessment_record_id:
            if hasattr(self.assessment_record_id, 'to_alipay_dict'):
                params['assessment_record_id'] = self.assessment_record_id.to_alipay_dict()
            else:
                params['assessment_record_id'] = self.assessment_record_id
        if self.assessment_score:
            if hasattr(self.assessment_score, 'to_alipay_dict'):
                params['assessment_score'] = self.assessment_score.to_alipay_dict()
            else:
                params['assessment_score'] = self.assessment_score
        if self.assessment_summary:
            if hasattr(self.assessment_summary, 'to_alipay_dict'):
                params['assessment_summary'] = self.assessment_summary.to_alipay_dict()
            else:
                params['assessment_summary'] = self.assessment_summary
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalHmAssessmentRecord()
        if 'answers_json' in d:
            o.answers_json = d['answers_json']
        if 'assessment_detail' in d:
            o.assessment_detail = d['assessment_detail']
        if 'assessment_id' in d:
            o.assessment_id = d['assessment_id']
        if 'assessment_level' in d:
            o.assessment_level = d['assessment_level']
        if 'assessment_name' in d:
            o.assessment_name = d['assessment_name']
        if 'assessment_record_id' in d:
            o.assessment_record_id = d['assessment_record_id']
        if 'assessment_score' in d:
            o.assessment_score = d['assessment_score']
        if 'assessment_summary' in d:
            o.assessment_summary = d['assessment_summary']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        return o


