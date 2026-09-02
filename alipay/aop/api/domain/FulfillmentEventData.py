#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExaminationEventParam import ExaminationEventParam


class FulfillmentEventData(object):

    def __init__(self):
        self._examination = None

    @property
    def examination(self):
        return self._examination

    @examination.setter
    def examination(self, value):
        if isinstance(value, ExaminationEventParam):
            self._examination = value
        else:
            self._examination = ExaminationEventParam.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.examination:
            if hasattr(self.examination, 'to_alipay_dict'):
                params['examination'] = self.examination.to_alipay_dict()
            else:
                params['examination'] = self.examination
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentEventData()
        if 'examination' in d:
            o.examination = d['examination']
        return o


