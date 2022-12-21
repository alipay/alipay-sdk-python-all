#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IdeployForecastData import IdeployForecastData


class AlipayIserviceIdeployForcecastCreateModel(object):

    def __init__(self):
        self._forecast_data = None
        self._tnt_inst_id = None

    @property
    def forecast_data(self):
        return self._forecast_data

    @forecast_data.setter
    def forecast_data(self, value):
        if isinstance(value, IdeployForecastData):
            self._forecast_data = value
        else:
            self._forecast_data = IdeployForecastData.from_alipay_dict(value)
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.forecast_data:
            if hasattr(self.forecast_data, 'to_alipay_dict'):
                params['forecast_data'] = self.forecast_data.to_alipay_dict()
            else:
                params['forecast_data'] = self.forecast_data
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIdeployForcecastCreateModel()
        if 'forecast_data' in d:
            o.forecast_data = d['forecast_data']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


