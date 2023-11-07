#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArtifactProjectNameDTO(object):

    def __init__(self):
        self._artifact_project_name_list = None

    @property
    def artifact_project_name_list(self):
        return self._artifact_project_name_list

    @artifact_project_name_list.setter
    def artifact_project_name_list(self, value):
        if isinstance(value, list):
            self._artifact_project_name_list = list()
            for i in value:
                self._artifact_project_name_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.artifact_project_name_list:
            if isinstance(self.artifact_project_name_list, list):
                for i in range(0, len(self.artifact_project_name_list)):
                    element = self.artifact_project_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.artifact_project_name_list[i] = element.to_alipay_dict()
            if hasattr(self.artifact_project_name_list, 'to_alipay_dict'):
                params['artifact_project_name_list'] = self.artifact_project_name_list.to_alipay_dict()
            else:
                params['artifact_project_name_list'] = self.artifact_project_name_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArtifactProjectNameDTO()
        if 'artifact_project_name_list' in d:
            o.artifact_project_name_list = d['artifact_project_name_list']
        return o


