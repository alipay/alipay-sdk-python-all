#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizInfoMap import BizInfoMap
from alipay.aop.api.domain.OtherInfo import OtherInfo
from alipay.aop.api.domain.TargetPoint import TargetPoint


class RobbyOpenTaskCreateModel(object):

    def __init__(self):
        self._biz_info_list = None
        self._biz_no = None
        self._ext_info = None
        self._scene = None
        self._sn = None
        self._sub_biz_no = None
        self._target_point = None
        self._task_type = None
        self._time_out = None

    @property
    def biz_info_list(self):
        return self._biz_info_list

    @biz_info_list.setter
    def biz_info_list(self, value):
        if isinstance(value, list):
            self._biz_info_list = list()
            for i in value:
                if isinstance(i, BizInfoMap):
                    self._biz_info_list.append(i)
                else:
                    self._biz_info_list.append(BizInfoMap.from_alipay_dict(i))
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, OtherInfo):
            self._ext_info = value
        else:
            self._ext_info = OtherInfo.from_alipay_dict(value)
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def sub_biz_no(self):
        return self._sub_biz_no

    @sub_biz_no.setter
    def sub_biz_no(self, value):
        self._sub_biz_no = value
    @property
    def target_point(self):
        return self._target_point

    @target_point.setter
    def target_point(self, value):
        if isinstance(value, TargetPoint):
            self._target_point = value
        else:
            self._target_point = TargetPoint.from_alipay_dict(value)
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def time_out(self):
        return self._time_out

    @time_out.setter
    def time_out(self, value):
        self._time_out = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info_list:
            if isinstance(self.biz_info_list, list):
                for i in range(0, len(self.biz_info_list)):
                    element = self.biz_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_info_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_info_list, 'to_alipay_dict'):
                params['biz_info_list'] = self.biz_info_list.to_alipay_dict()
            else:
                params['biz_info_list'] = self.biz_info_list
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.sub_biz_no:
            if hasattr(self.sub_biz_no, 'to_alipay_dict'):
                params['sub_biz_no'] = self.sub_biz_no.to_alipay_dict()
            else:
                params['sub_biz_no'] = self.sub_biz_no
        if self.target_point:
            if hasattr(self.target_point, 'to_alipay_dict'):
                params['target_point'] = self.target_point.to_alipay_dict()
            else:
                params['target_point'] = self.target_point
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
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
        o = RobbyOpenTaskCreateModel()
        if 'biz_info_list' in d:
            o.biz_info_list = d['biz_info_list']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sn' in d:
            o.sn = d['sn']
        if 'sub_biz_no' in d:
            o.sub_biz_no = d['sub_biz_no']
        if 'target_point' in d:
            o.target_point = d['target_point']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'time_out' in d:
            o.time_out = d['time_out']
        return o


