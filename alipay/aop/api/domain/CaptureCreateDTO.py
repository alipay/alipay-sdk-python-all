#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CaptureCreateDTO(object):

    def __init__(self):
        self._capture_no = None
        self._out_biz_no = None

    @property
    def capture_no(self):
        return self._capture_no

    @capture_no.setter
    def capture_no(self, value):
        self._capture_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.capture_no:
            if hasattr(self.capture_no, 'to_alipay_dict'):
                params['capture_no'] = self.capture_no.to_alipay_dict()
            else:
                params['capture_no'] = self.capture_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaptureCreateDTO()
        if 'capture_no' in d:
            o.capture_no = d['capture_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


