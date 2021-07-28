#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntfarmProjectTargetInfo import AntfarmProjectTargetInfo


class AntfarmProjectInfo(object):

    def __init__(self):
        self._project_id = None
        self._project_name = None
        self._target_list = None

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def target_list(self):
        return self._target_list

    @target_list.setter
    def target_list(self, value):
        if isinstance(value, list):
            self._target_list = list()
            for i in value:
                if isinstance(i, AntfarmProjectTargetInfo):
                    self._target_list.append(i)
                else:
                    self._target_list.append(AntfarmProjectTargetInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.target_list:
            if isinstance(self.target_list, list):
                for i in range(0, len(self.target_list)):
                    element = self.target_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_list[i] = element.to_alipay_dict()
            if hasattr(self.target_list, 'to_alipay_dict'):
                params['target_list'] = self.target_list.to_alipay_dict()
            else:
                params['target_list'] = self.target_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfarmProjectInfo()
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'target_list' in d:
            o.target_list = d['target_list']
        return o


