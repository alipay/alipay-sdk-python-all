#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReportData import ReportData


class AlipayDataDataserviceOrderreportCreateModel(object):

    def __init__(self):
        self._biz_token = None
        self._data = None
        self._order_outer_id = None
        self._report_date = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, ReportData):
                    self._data.append(i)
                else:
                    self._data.append(ReportData.from_alipay_dict(i))
    @property
    def order_outer_id(self):
        return self._order_outer_id

    @order_outer_id.setter
    def order_outer_id(self, value):
        self._order_outer_id = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.data:
            if isinstance(self.data, list):
                for i in range(0, len(self.data)):
                    element = self.data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data[i] = element.to_alipay_dict()
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.order_outer_id:
            if hasattr(self.order_outer_id, 'to_alipay_dict'):
                params['order_outer_id'] = self.order_outer_id.to_alipay_dict()
            else:
                params['order_outer_id'] = self.order_outer_id
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceOrderreportCreateModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'data' in d:
            o.data = d['data']
        if 'order_outer_id' in d:
            o.order_outer_id = d['order_outer_id']
        if 'report_date' in d:
            o.report_date = d['report_date']
        return o


