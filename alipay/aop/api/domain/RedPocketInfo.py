#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RedPocketInfo(object):

    def __init__(self):
        self._red_pocket_id = None
        self._red_pocket_out_biz_no = None
        self._remark = None
        self._send_time = None

    @property
    def red_pocket_id(self):
        return self._red_pocket_id

    @red_pocket_id.setter
    def red_pocket_id(self, value):
        self._red_pocket_id = value
    @property
    def red_pocket_out_biz_no(self):
        return self._red_pocket_out_biz_no

    @red_pocket_out_biz_no.setter
    def red_pocket_out_biz_no(self, value):
        self._red_pocket_out_biz_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.red_pocket_id:
            if hasattr(self.red_pocket_id, 'to_alipay_dict'):
                params['red_pocket_id'] = self.red_pocket_id.to_alipay_dict()
            else:
                params['red_pocket_id'] = self.red_pocket_id
        if self.red_pocket_out_biz_no:
            if hasattr(self.red_pocket_out_biz_no, 'to_alipay_dict'):
                params['red_pocket_out_biz_no'] = self.red_pocket_out_biz_no.to_alipay_dict()
            else:
                params['red_pocket_out_biz_no'] = self.red_pocket_out_biz_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RedPocketInfo()
        if 'red_pocket_id' in d:
            o.red_pocket_id = d['red_pocket_id']
        if 'red_pocket_out_biz_no' in d:
            o.red_pocket_out_biz_no = d['red_pocket_out_biz_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'send_time' in d:
            o.send_time = d['send_time']
        return o


