#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SlmAppInfo import SlmAppInfo
from alipay.aop.api.domain.CheckPointVO import CheckPointVO
from alipay.aop.api.domain.SlmArtifactInfo import SlmArtifactInfo
from alipay.aop.api.domain.SlmCaseErrorInfo import SlmCaseErrorInfo
from alipay.aop.api.domain.SlmDeviceInfo import SlmDeviceInfo
from alipay.aop.api.domain.SlmArtifactInfo import SlmArtifactInfo


class OneStopCheckTaskDetailDTO(object):

    def __init__(self):
        self._app_info = None
        self._auto_screen_cap = None
        self._case_ame = None
        self._case_desc = None
        self._check_points = None
        self._custom_log = None
        self._custom_screen_caps = None
        self._end_time = None
        self._error_info = None
        self._model = None
        self._result = None
        self._screenshot_list = None
        self._start_time = None
        self._task_id = None

    @property
    def app_info(self):
        return self._app_info

    @app_info.setter
    def app_info(self, value):
        if isinstance(value, SlmAppInfo):
            self._app_info = value
        else:
            self._app_info = SlmAppInfo.from_alipay_dict(value)
    @property
    def auto_screen_cap(self):
        return self._auto_screen_cap

    @auto_screen_cap.setter
    def auto_screen_cap(self, value):
        self._auto_screen_cap = value
    @property
    def case_ame(self):
        return self._case_ame

    @case_ame.setter
    def case_ame(self, value):
        self._case_ame = value
    @property
    def case_desc(self):
        return self._case_desc

    @case_desc.setter
    def case_desc(self, value):
        self._case_desc = value
    @property
    def check_points(self):
        return self._check_points

    @check_points.setter
    def check_points(self, value):
        if isinstance(value, list):
            self._check_points = list()
            for i in value:
                if isinstance(i, CheckPointVO):
                    self._check_points.append(i)
                else:
                    self._check_points.append(CheckPointVO.from_alipay_dict(i))
    @property
    def custom_log(self):
        return self._custom_log

    @custom_log.setter
    def custom_log(self, value):
        self._custom_log = value
    @property
    def custom_screen_caps(self):
        return self._custom_screen_caps

    @custom_screen_caps.setter
    def custom_screen_caps(self, value):
        if isinstance(value, list):
            self._custom_screen_caps = list()
            for i in value:
                if isinstance(i, SlmArtifactInfo):
                    self._custom_screen_caps.append(i)
                else:
                    self._custom_screen_caps.append(SlmArtifactInfo.from_alipay_dict(i))
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def error_info(self):
        return self._error_info

    @error_info.setter
    def error_info(self, value):
        if isinstance(value, SlmCaseErrorInfo):
            self._error_info = value
        else:
            self._error_info = SlmCaseErrorInfo.from_alipay_dict(value)
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if isinstance(value, SlmDeviceInfo):
            self._model = value
        else:
            self._model = SlmDeviceInfo.from_alipay_dict(value)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def screenshot_list(self):
        return self._screenshot_list

    @screenshot_list.setter
    def screenshot_list(self, value):
        if isinstance(value, list):
            self._screenshot_list = list()
            for i in value:
                if isinstance(i, SlmArtifactInfo):
                    self._screenshot_list.append(i)
                else:
                    self._screenshot_list.append(SlmArtifactInfo.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_info:
            if hasattr(self.app_info, 'to_alipay_dict'):
                params['app_info'] = self.app_info.to_alipay_dict()
            else:
                params['app_info'] = self.app_info
        if self.auto_screen_cap:
            if hasattr(self.auto_screen_cap, 'to_alipay_dict'):
                params['auto_screen_cap'] = self.auto_screen_cap.to_alipay_dict()
            else:
                params['auto_screen_cap'] = self.auto_screen_cap
        if self.case_ame:
            if hasattr(self.case_ame, 'to_alipay_dict'):
                params['case_ame'] = self.case_ame.to_alipay_dict()
            else:
                params['case_ame'] = self.case_ame
        if self.case_desc:
            if hasattr(self.case_desc, 'to_alipay_dict'):
                params['case_desc'] = self.case_desc.to_alipay_dict()
            else:
                params['case_desc'] = self.case_desc
        if self.check_points:
            if isinstance(self.check_points, list):
                for i in range(0, len(self.check_points)):
                    element = self.check_points[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_points[i] = element.to_alipay_dict()
            if hasattr(self.check_points, 'to_alipay_dict'):
                params['check_points'] = self.check_points.to_alipay_dict()
            else:
                params['check_points'] = self.check_points
        if self.custom_log:
            if hasattr(self.custom_log, 'to_alipay_dict'):
                params['custom_log'] = self.custom_log.to_alipay_dict()
            else:
                params['custom_log'] = self.custom_log
        if self.custom_screen_caps:
            if isinstance(self.custom_screen_caps, list):
                for i in range(0, len(self.custom_screen_caps)):
                    element = self.custom_screen_caps[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.custom_screen_caps[i] = element.to_alipay_dict()
            if hasattr(self.custom_screen_caps, 'to_alipay_dict'):
                params['custom_screen_caps'] = self.custom_screen_caps.to_alipay_dict()
            else:
                params['custom_screen_caps'] = self.custom_screen_caps
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.error_info:
            if hasattr(self.error_info, 'to_alipay_dict'):
                params['error_info'] = self.error_info.to_alipay_dict()
            else:
                params['error_info'] = self.error_info
        if self.model:
            if hasattr(self.model, 'to_alipay_dict'):
                params['model'] = self.model.to_alipay_dict()
            else:
                params['model'] = self.model
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.screenshot_list:
            if isinstance(self.screenshot_list, list):
                for i in range(0, len(self.screenshot_list)):
                    element = self.screenshot_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.screenshot_list[i] = element.to_alipay_dict()
            if hasattr(self.screenshot_list, 'to_alipay_dict'):
                params['screenshot_list'] = self.screenshot_list.to_alipay_dict()
            else:
                params['screenshot_list'] = self.screenshot_list
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OneStopCheckTaskDetailDTO()
        if 'app_info' in d:
            o.app_info = d['app_info']
        if 'auto_screen_cap' in d:
            o.auto_screen_cap = d['auto_screen_cap']
        if 'case_ame' in d:
            o.case_ame = d['case_ame']
        if 'case_desc' in d:
            o.case_desc = d['case_desc']
        if 'check_points' in d:
            o.check_points = d['check_points']
        if 'custom_log' in d:
            o.custom_log = d['custom_log']
        if 'custom_screen_caps' in d:
            o.custom_screen_caps = d['custom_screen_caps']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'error_info' in d:
            o.error_info = d['error_info']
        if 'model' in d:
            o.model = d['model']
        if 'result' in d:
            o.result = d['result']
        if 'screenshot_list' in d:
            o.screenshot_list = d['screenshot_list']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


