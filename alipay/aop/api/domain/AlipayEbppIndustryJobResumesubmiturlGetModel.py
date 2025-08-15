#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryJobResumesubmiturlGetModel(object):

    def __init__(self):
        self._job_id = None
        self._job_name = None
        self._out_job_id = None
        self._recruitment_platform_name = None
        self._required_attributes = None
        self._source_return_url = None
        self._template_id = None

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def out_job_id(self):
        return self._out_job_id

    @out_job_id.setter
    def out_job_id(self, value):
        self._out_job_id = value
    @property
    def recruitment_platform_name(self):
        return self._recruitment_platform_name

    @recruitment_platform_name.setter
    def recruitment_platform_name(self, value):
        self._recruitment_platform_name = value
    @property
    def required_attributes(self):
        return self._required_attributes

    @required_attributes.setter
    def required_attributes(self, value):
        if isinstance(value, list):
            self._required_attributes = list()
            for i in value:
                self._required_attributes.append(i)
    @property
    def source_return_url(self):
        return self._source_return_url

    @source_return_url.setter
    def source_return_url(self, value):
        self._source_return_url = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.out_job_id:
            if hasattr(self.out_job_id, 'to_alipay_dict'):
                params['out_job_id'] = self.out_job_id.to_alipay_dict()
            else:
                params['out_job_id'] = self.out_job_id
        if self.recruitment_platform_name:
            if hasattr(self.recruitment_platform_name, 'to_alipay_dict'):
                params['recruitment_platform_name'] = self.recruitment_platform_name.to_alipay_dict()
            else:
                params['recruitment_platform_name'] = self.recruitment_platform_name
        if self.required_attributes:
            if isinstance(self.required_attributes, list):
                for i in range(0, len(self.required_attributes)):
                    element = self.required_attributes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.required_attributes[i] = element.to_alipay_dict()
            if hasattr(self.required_attributes, 'to_alipay_dict'):
                params['required_attributes'] = self.required_attributes.to_alipay_dict()
            else:
                params['required_attributes'] = self.required_attributes
        if self.source_return_url:
            if hasattr(self.source_return_url, 'to_alipay_dict'):
                params['source_return_url'] = self.source_return_url.to_alipay_dict()
            else:
                params['source_return_url'] = self.source_return_url
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryJobResumesubmiturlGetModel()
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        if 'recruitment_platform_name' in d:
            o.recruitment_platform_name = d['recruitment_platform_name']
        if 'required_attributes' in d:
            o.required_attributes = d['required_attributes']
        if 'source_return_url' in d:
            o.source_return_url = d['source_return_url']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


