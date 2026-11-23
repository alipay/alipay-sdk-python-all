#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExperimentObject(object):

    def __init__(self):
        self._activity_id = None
        self._experiment_group_id = None
        self._experiment_id = None
        self._expose = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def experiment_group_id(self):
        return self._experiment_group_id

    @experiment_group_id.setter
    def experiment_group_id(self, value):
        self._experiment_group_id = value
    @property
    def experiment_id(self):
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, value):
        self._experiment_id = value
    @property
    def expose(self):
        return self._expose

    @expose.setter
    def expose(self, value):
        self._expose = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.experiment_group_id:
            if hasattr(self.experiment_group_id, 'to_alipay_dict'):
                params['experiment_group_id'] = self.experiment_group_id.to_alipay_dict()
            else:
                params['experiment_group_id'] = self.experiment_group_id
        if self.experiment_id:
            if hasattr(self.experiment_id, 'to_alipay_dict'):
                params['experiment_id'] = self.experiment_id.to_alipay_dict()
            else:
                params['experiment_id'] = self.experiment_id
        if self.expose:
            if hasattr(self.expose, 'to_alipay_dict'):
                params['expose'] = self.expose.to_alipay_dict()
            else:
                params['expose'] = self.expose
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExperimentObject()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'experiment_group_id' in d:
            o.experiment_group_id = d['experiment_group_id']
        if 'experiment_id' in d:
            o.experiment_id = d['experiment_id']
        if 'expose' in d:
            o.expose = d['expose']
        return o


