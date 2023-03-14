#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UseCaseStepInfo import UseCaseStepInfo


class AlipayOpenMiniAutocheckCaseCreateModel(object):

    def __init__(self):
        self._biz_line_name = None
        self._case_app_type = None
        self._case_ids = None
        self._case_intro = None
        self._case_name = None
        self._case_step_models = None
        self._creator = None
        self._ext_info = None
        self._time_out = None
        self._use_case_exe_map = None
        self._use_case_type = None

    @property
    def biz_line_name(self):
        return self._biz_line_name

    @biz_line_name.setter
    def biz_line_name(self, value):
        self._biz_line_name = value
    @property
    def case_app_type(self):
        return self._case_app_type

    @case_app_type.setter
    def case_app_type(self, value):
        self._case_app_type = value
    @property
    def case_ids(self):
        return self._case_ids

    @case_ids.setter
    def case_ids(self, value):
        self._case_ids = value
    @property
    def case_intro(self):
        return self._case_intro

    @case_intro.setter
    def case_intro(self, value):
        self._case_intro = value
    @property
    def case_name(self):
        return self._case_name

    @case_name.setter
    def case_name(self, value):
        self._case_name = value
    @property
    def case_step_models(self):
        return self._case_step_models

    @case_step_models.setter
    def case_step_models(self, value):
        if isinstance(value, list):
            self._case_step_models = list()
            for i in value:
                if isinstance(i, UseCaseStepInfo):
                    self._case_step_models.append(i)
                else:
                    self._case_step_models.append(UseCaseStepInfo.from_alipay_dict(i))
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def time_out(self):
        return self._time_out

    @time_out.setter
    def time_out(self, value):
        self._time_out = value
    @property
    def use_case_exe_map(self):
        return self._use_case_exe_map

    @use_case_exe_map.setter
    def use_case_exe_map(self, value):
        self._use_case_exe_map = value
    @property
    def use_case_type(self):
        return self._use_case_type

    @use_case_type.setter
    def use_case_type(self, value):
        self._use_case_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_line_name:
            if hasattr(self.biz_line_name, 'to_alipay_dict'):
                params['biz_line_name'] = self.biz_line_name.to_alipay_dict()
            else:
                params['biz_line_name'] = self.biz_line_name
        if self.case_app_type:
            if hasattr(self.case_app_type, 'to_alipay_dict'):
                params['case_app_type'] = self.case_app_type.to_alipay_dict()
            else:
                params['case_app_type'] = self.case_app_type
        if self.case_ids:
            if hasattr(self.case_ids, 'to_alipay_dict'):
                params['case_ids'] = self.case_ids.to_alipay_dict()
            else:
                params['case_ids'] = self.case_ids
        if self.case_intro:
            if hasattr(self.case_intro, 'to_alipay_dict'):
                params['case_intro'] = self.case_intro.to_alipay_dict()
            else:
                params['case_intro'] = self.case_intro
        if self.case_name:
            if hasattr(self.case_name, 'to_alipay_dict'):
                params['case_name'] = self.case_name.to_alipay_dict()
            else:
                params['case_name'] = self.case_name
        if self.case_step_models:
            if isinstance(self.case_step_models, list):
                for i in range(0, len(self.case_step_models)):
                    element = self.case_step_models[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.case_step_models[i] = element.to_alipay_dict()
            if hasattr(self.case_step_models, 'to_alipay_dict'):
                params['case_step_models'] = self.case_step_models.to_alipay_dict()
            else:
                params['case_step_models'] = self.case_step_models
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.time_out:
            if hasattr(self.time_out, 'to_alipay_dict'):
                params['time_out'] = self.time_out.to_alipay_dict()
            else:
                params['time_out'] = self.time_out
        if self.use_case_exe_map:
            if hasattr(self.use_case_exe_map, 'to_alipay_dict'):
                params['use_case_exe_map'] = self.use_case_exe_map.to_alipay_dict()
            else:
                params['use_case_exe_map'] = self.use_case_exe_map
        if self.use_case_type:
            if hasattr(self.use_case_type, 'to_alipay_dict'):
                params['use_case_type'] = self.use_case_type.to_alipay_dict()
            else:
                params['use_case_type'] = self.use_case_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAutocheckCaseCreateModel()
        if 'biz_line_name' in d:
            o.biz_line_name = d['biz_line_name']
        if 'case_app_type' in d:
            o.case_app_type = d['case_app_type']
        if 'case_ids' in d:
            o.case_ids = d['case_ids']
        if 'case_intro' in d:
            o.case_intro = d['case_intro']
        if 'case_name' in d:
            o.case_name = d['case_name']
        if 'case_step_models' in d:
            o.case_step_models = d['case_step_models']
        if 'creator' in d:
            o.creator = d['creator']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'time_out' in d:
            o.time_out = d['time_out']
        if 'use_case_exe_map' in d:
            o.use_case_exe_map = d['use_case_exe_map']
        if 'use_case_type' in d:
            o.use_case_type = d['use_case_type']
        return o


