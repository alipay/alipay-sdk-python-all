#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpProductCodeQueryModel(object):

    def __init__(self):
        self._code_id = None
        self._end_date = None
        self._page_num = None
        self._start_date = None

    @property
    def code_id(self):
        return self._code_id

    @code_id.setter
    def code_id(self, value):
        self._code_id = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_id:
            if hasattr(self.code_id, 'to_alipay_dict'):
                params['code_id'] = self.code_id.to_alipay_dict()
            else:
                params['code_id'] = self.code_id
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpProductCodeQueryModel()
        if 'code_id' in d:
            o.code_id = d['code_id']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


