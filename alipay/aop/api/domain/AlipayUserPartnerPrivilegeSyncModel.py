#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserPartnerPrivilegeSyncModel(object):

    def __init__(self):
        self._biz_time = None
        self._current_count = None
        self._grade = None
        self._max_count = None
        self._out_biz_no = None
        self._privilege_id = None
        self._status = None
        self._title = None
        self._trans_quantum = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def current_count(self):
        return self._current_count

    @current_count.setter
    def current_count(self, value):
        self._current_count = value
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
    @property
    def max_count(self):
        return self._max_count

    @max_count.setter
    def max_count(self, value):
        self._max_count = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def privilege_id(self):
        return self._privilege_id

    @privilege_id.setter
    def privilege_id(self, value):
        self._privilege_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def trans_quantum(self):
        return self._trans_quantum

    @trans_quantum.setter
    def trans_quantum(self, value):
        self._trans_quantum = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.current_count:
            if hasattr(self.current_count, 'to_alipay_dict'):
                params['current_count'] = self.current_count.to_alipay_dict()
            else:
                params['current_count'] = self.current_count
        if self.grade:
            if hasattr(self.grade, 'to_alipay_dict'):
                params['grade'] = self.grade.to_alipay_dict()
            else:
                params['grade'] = self.grade
        if self.max_count:
            if hasattr(self.max_count, 'to_alipay_dict'):
                params['max_count'] = self.max_count.to_alipay_dict()
            else:
                params['max_count'] = self.max_count
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.privilege_id:
            if hasattr(self.privilege_id, 'to_alipay_dict'):
                params['privilege_id'] = self.privilege_id.to_alipay_dict()
            else:
                params['privilege_id'] = self.privilege_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.trans_quantum:
            if hasattr(self.trans_quantum, 'to_alipay_dict'):
                params['trans_quantum'] = self.trans_quantum.to_alipay_dict()
            else:
                params['trans_quantum'] = self.trans_quantum
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPartnerPrivilegeSyncModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'current_count' in d:
            o.current_count = d['current_count']
        if 'grade' in d:
            o.grade = d['grade']
        if 'max_count' in d:
            o.max_count = d['max_count']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'privilege_id' in d:
            o.privilege_id = d['privilege_id']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        if 'trans_quantum' in d:
            o.trans_quantum = d['trans_quantum']
        return o


