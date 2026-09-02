#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PassengerFlowPredictObject(object):

    def __init__(self):
        self._enter_passenger_flow_predict_count = None
        self._exit_passenger_flow_predict_count = None
        self._station_index = None
        self._station_name = None

    @property
    def enter_passenger_flow_predict_count(self):
        return self._enter_passenger_flow_predict_count

    @enter_passenger_flow_predict_count.setter
    def enter_passenger_flow_predict_count(self, value):
        self._enter_passenger_flow_predict_count = value
    @property
    def exit_passenger_flow_predict_count(self):
        return self._exit_passenger_flow_predict_count

    @exit_passenger_flow_predict_count.setter
    def exit_passenger_flow_predict_count(self, value):
        self._exit_passenger_flow_predict_count = value
    @property
    def station_index(self):
        return self._station_index

    @station_index.setter
    def station_index(self, value):
        self._station_index = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.enter_passenger_flow_predict_count:
            if hasattr(self.enter_passenger_flow_predict_count, 'to_alipay_dict'):
                params['enter_passenger_flow_predict_count'] = self.enter_passenger_flow_predict_count.to_alipay_dict()
            else:
                params['enter_passenger_flow_predict_count'] = self.enter_passenger_flow_predict_count
        if self.exit_passenger_flow_predict_count:
            if hasattr(self.exit_passenger_flow_predict_count, 'to_alipay_dict'):
                params['exit_passenger_flow_predict_count'] = self.exit_passenger_flow_predict_count.to_alipay_dict()
            else:
                params['exit_passenger_flow_predict_count'] = self.exit_passenger_flow_predict_count
        if self.station_index:
            if hasattr(self.station_index, 'to_alipay_dict'):
                params['station_index'] = self.station_index.to_alipay_dict()
            else:
                params['station_index'] = self.station_index
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PassengerFlowPredictObject()
        if 'enter_passenger_flow_predict_count' in d:
            o.enter_passenger_flow_predict_count = d['enter_passenger_flow_predict_count']
        if 'exit_passenger_flow_predict_count' in d:
            o.exit_passenger_flow_predict_count = d['exit_passenger_flow_predict_count']
        if 'station_index' in d:
            o.station_index = d['station_index']
        if 'station_name' in d:
            o.station_name = d['station_name']
        return o


