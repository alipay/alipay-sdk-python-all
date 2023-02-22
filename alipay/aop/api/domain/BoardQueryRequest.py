#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BoardQueryRequest(object):

    def __init__(self):
        self._crowd_id = None
        self._exclude_import = None
        self._report_date = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def exclude_import(self):
        return self._exclude_import

    @exclude_import.setter
    def exclude_import(self, value):
        self._exclude_import = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.exclude_import:
            if hasattr(self.exclude_import, 'to_alipay_dict'):
                params['exclude_import'] = self.exclude_import.to_alipay_dict()
            else:
                params['exclude_import'] = self.exclude_import
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoardQueryRequest()
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'exclude_import' in d:
            o.exclude_import = d['exclude_import']
        if 'report_date' in d:
            o.report_date = d['report_date']
        return o


