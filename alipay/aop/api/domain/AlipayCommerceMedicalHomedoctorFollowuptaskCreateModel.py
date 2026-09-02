#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FollowUpCreateTaskBizIdRequest import FollowUpCreateTaskBizIdRequest


class AlipayCommerceMedicalHomedoctorFollowuptaskCreateModel(object):

    def __init__(self):
        self._agent_id = None
        self._biz_list = None
        self._dead_line = None
        self._doctor_id = None
        self._doctor_name = None
        self._template_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def biz_list(self):
        return self._biz_list

    @biz_list.setter
    def biz_list(self, value):
        if isinstance(value, list):
            self._biz_list = list()
            for i in value:
                if isinstance(i, FollowUpCreateTaskBizIdRequest):
                    self._biz_list.append(i)
                else:
                    self._biz_list.append(FollowUpCreateTaskBizIdRequest.from_alipay_dict(i))
    @property
    def dead_line(self):
        return self._dead_line

    @dead_line.setter
    def dead_line(self, value):
        self._dead_line = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.biz_list:
            if isinstance(self.biz_list, list):
                for i in range(0, len(self.biz_list)):
                    element = self.biz_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_list, 'to_alipay_dict'):
                params['biz_list'] = self.biz_list.to_alipay_dict()
            else:
                params['biz_list'] = self.biz_list
        if self.dead_line:
            if hasattr(self.dead_line, 'to_alipay_dict'):
                params['dead_line'] = self.dead_line.to_alipay_dict()
            else:
                params['dead_line'] = self.dead_line
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHomedoctorFollowuptaskCreateModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'biz_list' in d:
            o.biz_list = d['biz_list']
        if 'dead_line' in d:
            o.dead_line = d['dead_line']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


