#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppTaskElectricityCancelModel(object):

    def __init__(self):
        self._cancel_reason = None
        self._out_task_id = None

    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def out_task_id(self):
        return self._out_task_id

    @out_task_id.setter
    def out_task_id(self, value):
        self._out_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.out_task_id:
            if hasattr(self.out_task_id, 'to_alipay_dict'):
                params['out_task_id'] = self.out_task_id.to_alipay_dict()
            else:
                params['out_task_id'] = self.out_task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppTaskElectricityCancelModel()
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'out_task_id' in d:
            o.out_task_id = d['out_task_id']
        return o


