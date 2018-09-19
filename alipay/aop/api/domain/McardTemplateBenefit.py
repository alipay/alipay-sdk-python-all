#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class McardTemplateBenefit(object):

    def __init__(self):
        self._benefit_desc = None
        self._end_date = None
        self._ext_info = None
        self._start_date = None
        self._template_id = None
        self._title = None

    @property
    def benefit_desc(self):
        return self._benefit_desc

    @benefit_desc.setter
    def benefit_desc(self, value):
        if isinstance(value, list):
            self._benefit_desc = list()
            for i in value:
                self._benefit_desc.append(i)
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_desc:
            if isinstance(self.benefit_desc, list):
                for i in range(0, len(self.benefit_desc)):
                    element = self.benefit_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_desc[i] = element.to_alipay_dict()
            if hasattr(self.benefit_desc, 'to_alipay_dict'):
                params['benefit_desc'] = self.benefit_desc.to_alipay_dict()
            else:
                params['benefit_desc'] = self.benefit_desc
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
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
        o = McardTemplateBenefit()
        if 'benefit_desc' in d:
            o.benefit_desc = d['benefit_desc']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'title' in d:
            o.title = d['title']
        return o


