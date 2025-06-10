#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommonQaDTO(object):

    def __init__(self):
        self._city_code = None
        self._content = None
        self._out_faq_id = None
        self._report_department = None
        self._run_status = None
        self._title = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def out_faq_id(self):
        return self._out_faq_id

    @out_faq_id.setter
    def out_faq_id(self, value):
        self._out_faq_id = value
    @property
    def report_department(self):
        return self._report_department

    @report_department.setter
    def report_department(self, value):
        self._report_department = value
    @property
    def run_status(self):
        return self._run_status

    @run_status.setter
    def run_status(self, value):
        self._run_status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.out_faq_id:
            if hasattr(self.out_faq_id, 'to_alipay_dict'):
                params['out_faq_id'] = self.out_faq_id.to_alipay_dict()
            else:
                params['out_faq_id'] = self.out_faq_id
        if self.report_department:
            if hasattr(self.report_department, 'to_alipay_dict'):
                params['report_department'] = self.report_department.to_alipay_dict()
            else:
                params['report_department'] = self.report_department
        if self.run_status:
            if hasattr(self.run_status, 'to_alipay_dict'):
                params['run_status'] = self.run_status.to_alipay_dict()
            else:
                params['run_status'] = self.run_status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonQaDTO()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'content' in d:
            o.content = d['content']
        if 'out_faq_id' in d:
            o.out_faq_id = d['out_faq_id']
        if 'report_department' in d:
            o.report_department = d['report_department']
        if 'run_status' in d:
            o.run_status = d['run_status']
        if 'title' in d:
            o.title = d['title']
        return o


