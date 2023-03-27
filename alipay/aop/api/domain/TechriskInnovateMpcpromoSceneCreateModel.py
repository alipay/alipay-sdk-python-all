#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TechriskInnovateMpcpromoSceneCreateModel(object):

    def __init__(self):
        self._data_list = None
        self._recommend_type = None
        self._scene_description = None
        self._scene_project_name = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                self._data_list.append(i)
    @property
    def recommend_type(self):
        return self._recommend_type

    @recommend_type.setter
    def recommend_type(self, value):
        self._recommend_type = value
    @property
    def scene_description(self):
        return self._scene_description

    @scene_description.setter
    def scene_description(self, value):
        self._scene_description = value
    @property
    def scene_project_name(self):
        return self._scene_project_name

    @scene_project_name.setter
    def scene_project_name(self, value):
        self._scene_project_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.recommend_type:
            if hasattr(self.recommend_type, 'to_alipay_dict'):
                params['recommend_type'] = self.recommend_type.to_alipay_dict()
            else:
                params['recommend_type'] = self.recommend_type
        if self.scene_description:
            if hasattr(self.scene_description, 'to_alipay_dict'):
                params['scene_description'] = self.scene_description.to_alipay_dict()
            else:
                params['scene_description'] = self.scene_description
        if self.scene_project_name:
            if hasattr(self.scene_project_name, 'to_alipay_dict'):
                params['scene_project_name'] = self.scene_project_name.to_alipay_dict()
            else:
                params['scene_project_name'] = self.scene_project_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TechriskInnovateMpcpromoSceneCreateModel()
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'recommend_type' in d:
            o.recommend_type = d['recommend_type']
        if 'scene_description' in d:
            o.scene_description = d['scene_description']
        if 'scene_project_name' in d:
            o.scene_project_name = d['scene_project_name']
        return o


