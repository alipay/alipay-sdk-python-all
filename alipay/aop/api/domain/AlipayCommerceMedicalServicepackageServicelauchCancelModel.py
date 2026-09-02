#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServicepackageServicelauchCancelModel(object):

    def __init__(self):
        self._main_user_phone_no = None
        self._out_cancel_time = None
        self._out_unique_biz_no = None
        self._project_id = None

    @property
    def main_user_phone_no(self):
        return self._main_user_phone_no

    @main_user_phone_no.setter
    def main_user_phone_no(self, value):
        self._main_user_phone_no = value
    @property
    def out_cancel_time(self):
        return self._out_cancel_time

    @out_cancel_time.setter
    def out_cancel_time(self, value):
        self._out_cancel_time = value
    @property
    def out_unique_biz_no(self):
        return self._out_unique_biz_no

    @out_unique_biz_no.setter
    def out_unique_biz_no(self, value):
        self._out_unique_biz_no = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.main_user_phone_no:
            if hasattr(self.main_user_phone_no, 'to_alipay_dict'):
                params['main_user_phone_no'] = self.main_user_phone_no.to_alipay_dict()
            else:
                params['main_user_phone_no'] = self.main_user_phone_no
        if self.out_cancel_time:
            if hasattr(self.out_cancel_time, 'to_alipay_dict'):
                params['out_cancel_time'] = self.out_cancel_time.to_alipay_dict()
            else:
                params['out_cancel_time'] = self.out_cancel_time
        if self.out_unique_biz_no:
            if hasattr(self.out_unique_biz_no, 'to_alipay_dict'):
                params['out_unique_biz_no'] = self.out_unique_biz_no.to_alipay_dict()
            else:
                params['out_unique_biz_no'] = self.out_unique_biz_no
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServicepackageServicelauchCancelModel()
        if 'main_user_phone_no' in d:
            o.main_user_phone_no = d['main_user_phone_no']
        if 'out_cancel_time' in d:
            o.out_cancel_time = d['out_cancel_time']
        if 'out_unique_biz_no' in d:
            o.out_unique_biz_no = d['out_unique_biz_no']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


