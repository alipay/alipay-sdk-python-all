#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsImageModifyModel(object):

    def __init__(self):
        self._image_id_list = None
        self._operate_type = None
        self._project_id = None

    @property
    def image_id_list(self):
        return self._image_id_list

    @image_id_list.setter
    def image_id_list(self, value):
        if isinstance(value, list):
            self._image_id_list = list()
            for i in value:
                self._image_id_list.append(i)
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_id_list:
            if isinstance(self.image_id_list, list):
                for i in range(0, len(self.image_id_list)):
                    element = self.image_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_id_list[i] = element.to_alipay_dict()
            if hasattr(self.image_id_list, 'to_alipay_dict'):
                params['image_id_list'] = self.image_id_list.to_alipay_dict()
            else:
                params['image_id_list'] = self.image_id_list
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsImageModifyModel()
        if 'image_id_list' in d:
            o.image_id_list = d['image_id_list']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


