#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataMallIndicatorQueryModel(object):

    def __init__(self):
        self._begin_date = None
        self._biz_type = None
        self._end_date = None
        self._ext_info = None
        self._page_num = None
        self._page_size = None

    @property
    def begin_date(self):
        return self._begin_date

    @begin_date.setter
    def begin_date(self, value):
        self._begin_date = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
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
        if self.begin_date:
            if hasattr(self.begin_date, 'to_alipay_dict'):
                params['begin_date'] = self.begin_date.to_alipay_dict()
            else:
                params['begin_date'] = self.begin_date
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
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
        o = KoubeiMarketingDataMallIndicatorQueryModel()
        if 'begin_date' in d:
            o.begin_date = d['begin_date']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


