#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DateData import DateData
from alipay.aop.api.domain.DateData import DateData


class ExperimentInfo(object):

    def __init__(self):
        self._algo_group_detail_data = None
        self._control_group_detail_data = None
        self._end_date = None
        self._experiment_id = None
        self._flow = None
        self._start_date = None

    @property
    def algo_group_detail_data(self):
        return self._algo_group_detail_data

    @algo_group_detail_data.setter
    def algo_group_detail_data(self, value):
        if isinstance(value, list):
            self._algo_group_detail_data = list()
            for i in value:
                if isinstance(i, DateData):
                    self._algo_group_detail_data.append(i)
                else:
                    self._algo_group_detail_data.append(DateData.from_alipay_dict(i))
    @property
    def control_group_detail_data(self):
        return self._control_group_detail_data

    @control_group_detail_data.setter
    def control_group_detail_data(self, value):
        if isinstance(value, list):
            self._control_group_detail_data = list()
            for i in value:
                if isinstance(i, DateData):
                    self._control_group_detail_data.append(i)
                else:
                    self._control_group_detail_data.append(DateData.from_alipay_dict(i))
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def experiment_id(self):
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, value):
        self._experiment_id = value
    @property
    def flow(self):
        return self._flow

    @flow.setter
    def flow(self, value):
        self._flow = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.algo_group_detail_data:
            if isinstance(self.algo_group_detail_data, list):
                for i in range(0, len(self.algo_group_detail_data)):
                    element = self.algo_group_detail_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.algo_group_detail_data[i] = element.to_alipay_dict()
            if hasattr(self.algo_group_detail_data, 'to_alipay_dict'):
                params['algo_group_detail_data'] = self.algo_group_detail_data.to_alipay_dict()
            else:
                params['algo_group_detail_data'] = self.algo_group_detail_data
        if self.control_group_detail_data:
            if isinstance(self.control_group_detail_data, list):
                for i in range(0, len(self.control_group_detail_data)):
                    element = self.control_group_detail_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.control_group_detail_data[i] = element.to_alipay_dict()
            if hasattr(self.control_group_detail_data, 'to_alipay_dict'):
                params['control_group_detail_data'] = self.control_group_detail_data.to_alipay_dict()
            else:
                params['control_group_detail_data'] = self.control_group_detail_data
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.experiment_id:
            if hasattr(self.experiment_id, 'to_alipay_dict'):
                params['experiment_id'] = self.experiment_id.to_alipay_dict()
            else:
                params['experiment_id'] = self.experiment_id
        if self.flow:
            if hasattr(self.flow, 'to_alipay_dict'):
                params['flow'] = self.flow.to_alipay_dict()
            else:
                params['flow'] = self.flow
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
        o = ExperimentInfo()
        if 'algo_group_detail_data' in d:
            o.algo_group_detail_data = d['algo_group_detail_data']
        if 'control_group_detail_data' in d:
            o.control_group_detail_data = d['control_group_detail_data']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'experiment_id' in d:
            o.experiment_id = d['experiment_id']
        if 'flow' in d:
            o.flow = d['flow']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


