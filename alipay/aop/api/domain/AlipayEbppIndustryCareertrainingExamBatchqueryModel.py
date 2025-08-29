#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingExamBatchqueryModel(object):

    def __init__(self):
        self._city_code = None
        self._exam_name = None
        self._out_exam_id = None
        self._page_num = None
        self._page_size = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def exam_name(self):
        return self._exam_name

    @exam_name.setter
    def exam_name(self, value):
        self._exam_name = value
    @property
    def out_exam_id(self):
        return self._out_exam_id

    @out_exam_id.setter
    def out_exam_id(self, value):
        self._out_exam_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.exam_name:
            if hasattr(self.exam_name, 'to_alipay_dict'):
                params['exam_name'] = self.exam_name.to_alipay_dict()
            else:
                params['exam_name'] = self.exam_name
        if self.out_exam_id:
            if hasattr(self.out_exam_id, 'to_alipay_dict'):
                params['out_exam_id'] = self.out_exam_id.to_alipay_dict()
            else:
                params['out_exam_id'] = self.out_exam_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCareertrainingExamBatchqueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'exam_name' in d:
            o.exam_name = d['exam_name']
        if 'out_exam_id' in d:
            o.out_exam_id = d['out_exam_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


