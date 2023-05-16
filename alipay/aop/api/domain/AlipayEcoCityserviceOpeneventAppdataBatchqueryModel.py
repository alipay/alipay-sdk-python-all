#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCityserviceOpeneventAppdataBatchqueryModel(object):

    def __init__(self):
        self._biz_code = None
        self._date = None
        self._date_type = None
        self._page_num = None
        self._page_size = None
        self._panel_type = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def date_type(self):
        return self._date_type

    @date_type.setter
    def date_type(self, value):
        self._date_type = value
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
    @property
    def panel_type(self):
        return self._panel_type

    @panel_type.setter
    def panel_type(self, value):
        self._panel_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.date_type:
            if hasattr(self.date_type, 'to_alipay_dict'):
                params['date_type'] = self.date_type.to_alipay_dict()
            else:
                params['date_type'] = self.date_type
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
        if self.panel_type:
            if hasattr(self.panel_type, 'to_alipay_dict'):
                params['panel_type'] = self.panel_type.to_alipay_dict()
            else:
                params['panel_type'] = self.panel_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityserviceOpeneventAppdataBatchqueryModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'date' in d:
            o.date = d['date']
        if 'date_type' in d:
            o.date_type = d['date_type']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'panel_type' in d:
            o.panel_type = d['panel_type']
        return o


