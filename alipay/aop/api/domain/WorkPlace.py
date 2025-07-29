#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WorkPlace(object):

    def __init__(self):
        self._work_place_id = None

    @property
    def work_place_id(self):
        return self._work_place_id

    @work_place_id.setter
    def work_place_id(self, value):
        self._work_place_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.work_place_id:
            if hasattr(self.work_place_id, 'to_alipay_dict'):
                params['work_place_id'] = self.work_place_id.to_alipay_dict()
            else:
                params['work_place_id'] = self.work_place_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorkPlace()
        if 'work_place_id' in d:
            o.work_place_id = d['work_place_id']
        return o


