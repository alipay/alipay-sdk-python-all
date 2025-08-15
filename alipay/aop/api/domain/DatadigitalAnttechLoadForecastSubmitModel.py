#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechLoadForecastSubmitModel(object):

    def __init__(self):
        self._agreement_code = None
        self._future_date = None
        self._history_date = None
        self._history_value = None
        self._request_id = None

    @property
    def agreement_code(self):
        return self._agreement_code

    @agreement_code.setter
    def agreement_code(self, value):
        self._agreement_code = value
    @property
    def future_date(self):
        return self._future_date

    @future_date.setter
    def future_date(self, value):
        if isinstance(value, list):
            self._future_date = list()
            for i in value:
                self._future_date.append(i)
    @property
    def history_date(self):
        return self._history_date

    @history_date.setter
    def history_date(self, value):
        if isinstance(value, list):
            self._history_date = list()
            for i in value:
                self._history_date.append(i)
    @property
    def history_value(self):
        return self._history_value

    @history_value.setter
    def history_value(self, value):
        if isinstance(value, list):
            self._history_value = list()
            for i in value:
                self._history_value.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_code:
            if hasattr(self.agreement_code, 'to_alipay_dict'):
                params['agreement_code'] = self.agreement_code.to_alipay_dict()
            else:
                params['agreement_code'] = self.agreement_code
        if self.future_date:
            if isinstance(self.future_date, list):
                for i in range(0, len(self.future_date)):
                    element = self.future_date[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.future_date[i] = element.to_alipay_dict()
            if hasattr(self.future_date, 'to_alipay_dict'):
                params['future_date'] = self.future_date.to_alipay_dict()
            else:
                params['future_date'] = self.future_date
        if self.history_date:
            if isinstance(self.history_date, list):
                for i in range(0, len(self.history_date)):
                    element = self.history_date[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.history_date[i] = element.to_alipay_dict()
            if hasattr(self.history_date, 'to_alipay_dict'):
                params['history_date'] = self.history_date.to_alipay_dict()
            else:
                params['history_date'] = self.history_date
        if self.history_value:
            if isinstance(self.history_value, list):
                for i in range(0, len(self.history_value)):
                    element = self.history_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.history_value[i] = element.to_alipay_dict()
            if hasattr(self.history_value, 'to_alipay_dict'):
                params['history_value'] = self.history_value.to_alipay_dict()
            else:
                params['history_value'] = self.history_value
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechLoadForecastSubmitModel()
        if 'agreement_code' in d:
            o.agreement_code = d['agreement_code']
        if 'future_date' in d:
            o.future_date = d['future_date']
        if 'history_date' in d:
            o.history_date = d['history_date']
        if 'history_value' in d:
            o.history_value = d['history_value']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


