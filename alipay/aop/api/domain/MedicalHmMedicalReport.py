#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalHmMedicalReport(object):

    def __init__(self):
        self._assessment_record_id = None
        self._gmt_create = None
        self._gmt_modified = None
        self._report_url_json = None
        self._upload_type = None

    @property
    def assessment_record_id(self):
        return self._assessment_record_id

    @assessment_record_id.setter
    def assessment_record_id(self, value):
        self._assessment_record_id = value
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
    @property
    def report_url_json(self):
        return self._report_url_json

    @report_url_json.setter
    def report_url_json(self, value):
        if isinstance(value, list):
            self._report_url_json = list()
            for i in value:
                self._report_url_json.append(i)
    @property
    def upload_type(self):
        return self._upload_type

    @upload_type.setter
    def upload_type(self, value):
        self._upload_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.assessment_record_id:
            if hasattr(self.assessment_record_id, 'to_alipay_dict'):
                params['assessment_record_id'] = self.assessment_record_id.to_alipay_dict()
            else:
                params['assessment_record_id'] = self.assessment_record_id
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
        if self.report_url_json:
            if isinstance(self.report_url_json, list):
                for i in range(0, len(self.report_url_json)):
                    element = self.report_url_json[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_url_json[i] = element.to_alipay_dict()
            if hasattr(self.report_url_json, 'to_alipay_dict'):
                params['report_url_json'] = self.report_url_json.to_alipay_dict()
            else:
                params['report_url_json'] = self.report_url_json
        if self.upload_type:
            if hasattr(self.upload_type, 'to_alipay_dict'):
                params['upload_type'] = self.upload_type.to_alipay_dict()
            else:
                params['upload_type'] = self.upload_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalHmMedicalReport()
        if 'assessment_record_id' in d:
            o.assessment_record_id = d['assessment_record_id']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'report_url_json' in d:
            o.report_url_json = d['report_url_json']
        if 'upload_type' in d:
            o.upload_type = d['upload_type']
        return o


