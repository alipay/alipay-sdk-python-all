#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryFatigueInfo import DeliveryFatigueInfo


class DeliveryDetailPositionContentVO(object):

    def __init__(self):
        self._fatigue_model = None
        self._scm_model = None
        self._view_model = None

    @property
    def fatigue_model(self):
        return self._fatigue_model

    @fatigue_model.setter
    def fatigue_model(self, value):
        if isinstance(value, DeliveryFatigueInfo):
            self._fatigue_model = value
        else:
            self._fatigue_model = DeliveryFatigueInfo.from_alipay_dict(value)
    @property
    def scm_model(self):
        return self._scm_model

    @scm_model.setter
    def scm_model(self, value):
        self._scm_model = value
    @property
    def view_model(self):
        return self._view_model

    @view_model.setter
    def view_model(self, value):
        self._view_model = value


    def to_alipay_dict(self):
        params = dict()
        if self.fatigue_model:
            if hasattr(self.fatigue_model, 'to_alipay_dict'):
                params['fatigue_model'] = self.fatigue_model.to_alipay_dict()
            else:
                params['fatigue_model'] = self.fatigue_model
        if self.scm_model:
            if hasattr(self.scm_model, 'to_alipay_dict'):
                params['scm_model'] = self.scm_model.to_alipay_dict()
            else:
                params['scm_model'] = self.scm_model
        if self.view_model:
            if hasattr(self.view_model, 'to_alipay_dict'):
                params['view_model'] = self.view_model.to_alipay_dict()
            else:
                params['view_model'] = self.view_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryDetailPositionContentVO()
        if 'fatigue_model' in d:
            o.fatigue_model = d['fatigue_model']
        if 'scm_model' in d:
            o.scm_model = d['scm_model']
        if 'view_model' in d:
            o.view_model = d['view_model']
        return o


