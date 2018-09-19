#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CraftsmanWorkOutIdOpenModel(object):

    def __init__(self):
        self._out_work_id = None
        self._work_id = None

    @property
    def out_work_id(self):
        return self._out_work_id

    @out_work_id.setter
    def out_work_id(self, value):
        self._out_work_id = value
    @property
    def work_id(self):
        return self._work_id

    @work_id.setter
    def work_id(self, value):
        self._work_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_work_id:
            if hasattr(self.out_work_id, 'to_alipay_dict'):
                params['out_work_id'] = self.out_work_id.to_alipay_dict()
            else:
                params['out_work_id'] = self.out_work_id
        if self.work_id:
            if hasattr(self.work_id, 'to_alipay_dict'):
                params['work_id'] = self.work_id.to_alipay_dict()
            else:
                params['work_id'] = self.work_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CraftsmanWorkOutIdOpenModel()
        if 'out_work_id' in d:
            o.out_work_id = d['out_work_id']
        if 'work_id' in d:
            o.work_id = d['work_id']
        return o


