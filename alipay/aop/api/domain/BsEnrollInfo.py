#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BsEnrollInfo(object):

    def __init__(self):
        self._enroll_id = None
        self._remain_stock = None
        self._status = None
        self._status_reason = None
        self._target_id = None
        self._total_stock = None
        self._update_time = None

    @property
    def enroll_id(self):
        return self._enroll_id

    @enroll_id.setter
    def enroll_id(self, value):
        self._enroll_id = value
    @property
    def remain_stock(self):
        return self._remain_stock

    @remain_stock.setter
    def remain_stock(self, value):
        self._remain_stock = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_reason(self):
        return self._status_reason

    @status_reason.setter
    def status_reason(self, value):
        self._status_reason = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def total_stock(self):
        return self._total_stock

    @total_stock.setter
    def total_stock(self, value):
        self._total_stock = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.enroll_id:
            if hasattr(self.enroll_id, 'to_alipay_dict'):
                params['enroll_id'] = self.enroll_id.to_alipay_dict()
            else:
                params['enroll_id'] = self.enroll_id
        if self.remain_stock:
            if hasattr(self.remain_stock, 'to_alipay_dict'):
                params['remain_stock'] = self.remain_stock.to_alipay_dict()
            else:
                params['remain_stock'] = self.remain_stock
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_reason:
            if hasattr(self.status_reason, 'to_alipay_dict'):
                params['status_reason'] = self.status_reason.to_alipay_dict()
            else:
                params['status_reason'] = self.status_reason
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.total_stock:
            if hasattr(self.total_stock, 'to_alipay_dict'):
                params['total_stock'] = self.total_stock.to_alipay_dict()
            else:
                params['total_stock'] = self.total_stock
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsEnrollInfo()
        if 'enroll_id' in d:
            o.enroll_id = d['enroll_id']
        if 'remain_stock' in d:
            o.remain_stock = d['remain_stock']
        if 'status' in d:
            o.status = d['status']
        if 'status_reason' in d:
            o.status_reason = d['status_reason']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'total_stock' in d:
            o.total_stock = d['total_stock']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


