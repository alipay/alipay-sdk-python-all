#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntLinkeQueryreimbursequotaQueryModel(object):

    def __init__(self):
        self._months = None
        self._work_no = None

    @property
    def months(self):
        return self._months

    @months.setter
    def months(self, value):
        if isinstance(value, list):
            self._months = list()
            for i in value:
                self._months.append(i)
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.months:
            if isinstance(self.months, list):
                for i in range(0, len(self.months)):
                    element = self.months[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.months[i] = element.to_alipay_dict()
            if hasattr(self.months, 'to_alipay_dict'):
                params['months'] = self.months.to_alipay_dict()
            else:
                params['months'] = self.months
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntLinkeQueryreimbursequotaQueryModel()
        if 'months' in d:
            o.months = d['months']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


