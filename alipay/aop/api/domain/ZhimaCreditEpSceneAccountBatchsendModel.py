#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpSceneAccountBatchsendModel(object):

    def __init__(self):
        self._label_scene_code = None
        self._sync_list = None

    @property
    def label_scene_code(self):
        return self._label_scene_code

    @label_scene_code.setter
    def label_scene_code(self, value):
        self._label_scene_code = value
    @property
    def sync_list(self):
        return self._sync_list

    @sync_list.setter
    def sync_list(self, value):
        if isinstance(value, list):
            self._sync_list = list()
            for i in value:
                self._sync_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.label_scene_code:
            if hasattr(self.label_scene_code, 'to_alipay_dict'):
                params['label_scene_code'] = self.label_scene_code.to_alipay_dict()
            else:
                params['label_scene_code'] = self.label_scene_code
        if self.sync_list:
            if isinstance(self.sync_list, list):
                for i in range(0, len(self.sync_list)):
                    element = self.sync_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sync_list[i] = element.to_alipay_dict()
            if hasattr(self.sync_list, 'to_alipay_dict'):
                params['sync_list'] = self.sync_list.to_alipay_dict()
            else:
                params['sync_list'] = self.sync_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpSceneAccountBatchsendModel()
        if 'label_scene_code' in d:
            o.label_scene_code = d['label_scene_code']
        if 'sync_list' in d:
            o.sync_list = d['sync_list']
        return o


