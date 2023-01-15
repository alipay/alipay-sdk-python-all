#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopReportProgressInfo(object):

    def __init__(self):
        self._current_stage = None
        self._current_stage_status = None
        self._description = None
        self._report_result = None
        self._shop_id = None

    @property
    def current_stage(self):
        return self._current_stage

    @current_stage.setter
    def current_stage(self, value):
        self._current_stage = value
    @property
    def current_stage_status(self):
        return self._current_stage_status

    @current_stage_status.setter
    def current_stage_status(self, value):
        self._current_stage_status = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def report_result(self):
        return self._report_result

    @report_result.setter
    def report_result(self, value):
        self._report_result = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_stage:
            if hasattr(self.current_stage, 'to_alipay_dict'):
                params['current_stage'] = self.current_stage.to_alipay_dict()
            else:
                params['current_stage'] = self.current_stage
        if self.current_stage_status:
            if hasattr(self.current_stage_status, 'to_alipay_dict'):
                params['current_stage_status'] = self.current_stage_status.to_alipay_dict()
            else:
                params['current_stage_status'] = self.current_stage_status
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.report_result:
            if hasattr(self.report_result, 'to_alipay_dict'):
                params['report_result'] = self.report_result.to_alipay_dict()
            else:
                params['report_result'] = self.report_result
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopReportProgressInfo()
        if 'current_stage' in d:
            o.current_stage = d['current_stage']
        if 'current_stage_status' in d:
            o.current_stage_status = d['current_stage_status']
        if 'description' in d:
            o.description = d['description']
        if 'report_result' in d:
            o.report_result = d['report_result']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


