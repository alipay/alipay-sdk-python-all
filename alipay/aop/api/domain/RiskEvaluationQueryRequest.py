#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskEvaluationQueryRequest(object):

    def __init__(self):
        self._biz_detail = None
        self._biz_no = None
        self._control_obj_code = None
        self._work_no = None

    @property
    def biz_detail(self):
        return self._biz_detail

    @biz_detail.setter
    def biz_detail(self, value):
        self._biz_detail = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def control_obj_code(self):
        return self._control_obj_code

    @control_obj_code.setter
    def control_obj_code(self, value):
        self._control_obj_code = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_detail:
            if hasattr(self.biz_detail, 'to_alipay_dict'):
                params['biz_detail'] = self.biz_detail.to_alipay_dict()
            else:
                params['biz_detail'] = self.biz_detail
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.control_obj_code:
            if hasattr(self.control_obj_code, 'to_alipay_dict'):
                params['control_obj_code'] = self.control_obj_code.to_alipay_dict()
            else:
                params['control_obj_code'] = self.control_obj_code
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskEvaluationQueryRequest()
        if 'biz_detail' in d:
            o.biz_detail = d['biz_detail']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'control_obj_code' in d:
            o.control_obj_code = d['control_obj_code']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


