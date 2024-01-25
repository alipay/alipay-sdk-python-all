#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizInfo import BizInfo


class AlipayIserviceCcmRobotSessionCreateModel(object):

    def __init__(self):
        self._biz_info = None
        self._robot_code = None
        self._scene_code = None
        self._stream_output = None
        self._visitor_id = None
        self._visitor_ip = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        if isinstance(value, BizInfo):
            self._biz_info = value
        else:
            self._biz_info = BizInfo.from_alipay_dict(value)
    @property
    def robot_code(self):
        return self._robot_code

    @robot_code.setter
    def robot_code(self, value):
        self._robot_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def stream_output(self):
        return self._stream_output

    @stream_output.setter
    def stream_output(self, value):
        self._stream_output = value
    @property
    def visitor_id(self):
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, value):
        self._visitor_id = value
    @property
    def visitor_ip(self):
        return self._visitor_ip

    @visitor_ip.setter
    def visitor_ip(self, value):
        self._visitor_ip = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.robot_code:
            if hasattr(self.robot_code, 'to_alipay_dict'):
                params['robot_code'] = self.robot_code.to_alipay_dict()
            else:
                params['robot_code'] = self.robot_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.stream_output:
            if hasattr(self.stream_output, 'to_alipay_dict'):
                params['stream_output'] = self.stream_output.to_alipay_dict()
            else:
                params['stream_output'] = self.stream_output
        if self.visitor_id:
            if hasattr(self.visitor_id, 'to_alipay_dict'):
                params['visitor_id'] = self.visitor_id.to_alipay_dict()
            else:
                params['visitor_id'] = self.visitor_id
        if self.visitor_ip:
            if hasattr(self.visitor_ip, 'to_alipay_dict'):
                params['visitor_ip'] = self.visitor_ip.to_alipay_dict()
            else:
                params['visitor_ip'] = self.visitor_ip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmRobotSessionCreateModel()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'robot_code' in d:
            o.robot_code = d['robot_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'stream_output' in d:
            o.stream_output = d['stream_output']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        if 'visitor_ip' in d:
            o.visitor_ip = d['visitor_ip']
        return o


