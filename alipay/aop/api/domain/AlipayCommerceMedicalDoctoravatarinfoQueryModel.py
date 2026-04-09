#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctoravatarinfoQueryModel(object):

    def __init__(self):
        self._pic_sync_task_id = None

    @property
    def pic_sync_task_id(self):
        return self._pic_sync_task_id

    @pic_sync_task_id.setter
    def pic_sync_task_id(self, value):
        self._pic_sync_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.pic_sync_task_id:
            if hasattr(self.pic_sync_task_id, 'to_alipay_dict'):
                params['pic_sync_task_id'] = self.pic_sync_task_id.to_alipay_dict()
            else:
                params['pic_sync_task_id'] = self.pic_sync_task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDoctoravatarinfoQueryModel()
        if 'pic_sync_task_id' in d:
            o.pic_sync_task_id = d['pic_sync_task_id']
        return o


