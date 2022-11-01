#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UseCaseStepInfo import UseCaseStepInfo


class AlipayOpenMiniAutocheckCaseCreateModel(object):

    def __init__(self):
        self._case_intro = None
        self._case_name = None
        self._case_step_models = None
        self._creator = None
        self._ext_info = None
        self._time_out = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAutocheckCaseCreateModel()
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
        return o


