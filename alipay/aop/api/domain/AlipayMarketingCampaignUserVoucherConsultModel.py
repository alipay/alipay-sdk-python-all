#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignUserVoucherConsultModel(object):

    def __init__(self):
        self._activity_id_list = None
        self._scene_code = None

    @property
    def activity_id_list(self):
        return self._activity_id_list

    @activity_id_list.setter
    def activity_id_list(self, value):
        if isinstance(value, list):
            self._activity_id_list = list()
            for i in value:
                self._activity_id_list.append(i)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        if isinstance(value, list):
            self._scene_code = list()
            for i in value:
                self._scene_code.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id_list:
            if isinstance(self.activity_id_list, list):
                for i in range(0, len(self.activity_id_list)):
                    element = self.activity_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_id_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_id_list, 'to_alipay_dict'):
                params['activity_id_list'] = self.activity_id_list.to_alipay_dict()
            else:
                params['activity_id_list'] = self.activity_id_list
        if self.scene_code:
            if isinstance(self.scene_code, list):
                for i in range(0, len(self.scene_code)):
                    element = self.scene_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_code[i] = element.to_alipay_dict()
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignUserVoucherConsultModel()
        if 'activity_id_list' in d:
            o.activity_id_list = d['activity_id_list']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


