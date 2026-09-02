#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechEnergyPredictionQueryModel(object):

    def __init__(self):
        self._agreement_code = None
        self._data_type = None
        self._end_date = None
        self._forecast_id = None
        self._request_id = None
        self._start_date = None

    @property
    def agreement_code(self):
        return self._agreement_code

    @agreement_code.setter
    def agreement_code(self, value):
        self._agreement_code = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def forecast_id(self):
        return self._forecast_id

    @forecast_id.setter
    def forecast_id(self, value):
        self._forecast_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_code:
            if hasattr(self.agreement_code, 'to_alipay_dict'):
                params['agreement_code'] = self.agreement_code.to_alipay_dict()
            else:
                params['agreement_code'] = self.agreement_code
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.forecast_id:
            if hasattr(self.forecast_id, 'to_alipay_dict'):
                params['forecast_id'] = self.forecast_id.to_alipay_dict()
            else:
                params['forecast_id'] = self.forecast_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
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
        o = DatadigitalAnttechEnergyPredictionQueryModel()
        if 'agreement_code' in d:
            o.agreement_code = d['agreement_code']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'forecast_id' in d:
            o.forecast_id = d['forecast_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


