#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceMediaReportQueryModel(object):

    def __init__(self):
        self._ad_pos_id = None
        self._application_id = None
        self._end_date = None
        self._m_pid = None
        self._page_no = None
        self._page_size = None
        self._space_code = None
        self._start_date = None
        self._type = None

    @property
    def ad_pos_id(self):
        return self._ad_pos_id

    @ad_pos_id.setter
    def ad_pos_id(self, value):
        self._ad_pos_id = value
    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def m_pid(self):
        return self._m_pid

    @m_pid.setter
    def m_pid(self, value):
        self._m_pid = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def space_code(self):
        return self._space_code

    @space_code.setter
    def space_code(self, value):
        self._space_code = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_pos_id:
            if hasattr(self.ad_pos_id, 'to_alipay_dict'):
                params['ad_pos_id'] = self.ad_pos_id.to_alipay_dict()
            else:
                params['ad_pos_id'] = self.ad_pos_id
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.m_pid:
            if hasattr(self.m_pid, 'to_alipay_dict'):
                params['m_pid'] = self.m_pid.to_alipay_dict()
            else:
                params['m_pid'] = self.m_pid
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.space_code:
            if hasattr(self.space_code, 'to_alipay_dict'):
                params['space_code'] = self.space_code.to_alipay_dict()
            else:
                params['space_code'] = self.space_code
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceMediaReportQueryModel()
        if 'ad_pos_id' in d:
            o.ad_pos_id = d['ad_pos_id']
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'm_pid' in d:
            o.m_pid = d['m_pid']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'space_code' in d:
            o.space_code = d['space_code']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'type' in d:
            o.type = d['type']
        return o


