#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CheckInUnusualNotifyDetail(object):

    def __init__(self):
        self._checked_total = None
        self._gmt_push = None
        self._inst_id = None
        self._inst_name = None
        self._total = None
        self._unchecked_total = None

    @property
    def checked_total(self):
        return self._checked_total

    @checked_total.setter
    def checked_total(self, value):
        self._checked_total = value
    @property
    def gmt_push(self):
        return self._gmt_push

    @gmt_push.setter
    def gmt_push(self, value):
        self._gmt_push = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def unchecked_total(self):
        return self._unchecked_total

    @unchecked_total.setter
    def unchecked_total(self, value):
        self._unchecked_total = value


    def to_alipay_dict(self):
        params = dict()
        if self.checked_total:
            if hasattr(self.checked_total, 'to_alipay_dict'):
                params['checked_total'] = self.checked_total.to_alipay_dict()
            else:
                params['checked_total'] = self.checked_total
        if self.gmt_push:
            if hasattr(self.gmt_push, 'to_alipay_dict'):
                params['gmt_push'] = self.gmt_push.to_alipay_dict()
            else:
                params['gmt_push'] = self.gmt_push
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        if self.unchecked_total:
            if hasattr(self.unchecked_total, 'to_alipay_dict'):
                params['unchecked_total'] = self.unchecked_total.to_alipay_dict()
            else:
                params['unchecked_total'] = self.unchecked_total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckInUnusualNotifyDetail()
        if 'checked_total' in d:
            o.checked_total = d['checked_total']
        if 'gmt_push' in d:
            o.gmt_push = d['gmt_push']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'total' in d:
            o.total = d['total']
        if 'unchecked_total' in d:
            o.unchecked_total = d['unchecked_total']
        return o


