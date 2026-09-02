#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExperimentDetail(object):

    def __init__(self):
        self._experiment_name = None
        self._experiment_parameters = None

    @property
    def experiment_name(self):
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, value):
        self._experiment_name = value
    @property
    def experiment_parameters(self):
        return self._experiment_parameters

    @experiment_parameters.setter
    def experiment_parameters(self, value):
        self._experiment_parameters = value


    def to_alipay_dict(self):
        params = dict()
        if self.experiment_name:
            if hasattr(self.experiment_name, 'to_alipay_dict'):
                params['experiment_name'] = self.experiment_name.to_alipay_dict()
            else:
                params['experiment_name'] = self.experiment_name
        if self.experiment_parameters:
            if hasattr(self.experiment_parameters, 'to_alipay_dict'):
                params['experiment_parameters'] = self.experiment_parameters.to_alipay_dict()
            else:
                params['experiment_parameters'] = self.experiment_parameters
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExperimentDetail()
        if 'experiment_name' in d:
            o.experiment_name = d['experiment_name']
        if 'experiment_parameters' in d:
            o.experiment_parameters = d['experiment_parameters']
        return o


