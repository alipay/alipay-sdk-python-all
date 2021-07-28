#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataBillBailQueryModel(object):

    def __init__(self):
        self._bail_type = None
        self._biz_orig_no = None
        self._end_time = None
        self._start_time = None
        self._trans_log_id = None

    @property
    def bail_type(self):
        return self._bail_type

    @bail_type.setter
    def bail_type(self, value):
        self._bail_type = value
    @property
    def biz_orig_no(self):
        return self._biz_orig_no

    @biz_orig_no.setter
    def biz_orig_no(self, value):
        self._biz_orig_no = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def trans_log_id(self):
        return self._trans_log_id

    @trans_log_id.setter
    def trans_log_id(self, value):
        self._trans_log_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bail_type:
            if hasattr(self.bail_type, 'to_alipay_dict'):
                params['bail_type'] = self.bail_type.to_alipay_dict()
            else:
                params['bail_type'] = self.bail_type
        if self.biz_orig_no:
            if hasattr(self.biz_orig_no, 'to_alipay_dict'):
                params['biz_orig_no'] = self.biz_orig_no.to_alipay_dict()
            else:
                params['biz_orig_no'] = self.biz_orig_no
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.trans_log_id:
            if hasattr(self.trans_log_id, 'to_alipay_dict'):
                params['trans_log_id'] = self.trans_log_id.to_alipay_dict()
            else:
                params['trans_log_id'] = self.trans_log_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataBillBailQueryModel()
        if 'bail_type' in d:
            o.bail_type = d['bail_type']
        if 'biz_orig_no' in d:
            o.biz_orig_no = d['biz_orig_no']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'trans_log_id' in d:
            o.trans_log_id = d['trans_log_id']
        return o


