#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SpecialCardInfoModel import SpecialCardInfoModel


class SubSceneCardModel(object):

    def __init__(self):
        self._sub_scene_card_list = None
        self._sub_scene_code = None
        self._sub_scene_code_name = None

    @property
    def sub_scene_card_list(self):
        return self._sub_scene_card_list

    @sub_scene_card_list.setter
    def sub_scene_card_list(self, value):
        if isinstance(value, list):
            self._sub_scene_card_list = list()
            for i in value:
                if isinstance(i, SpecialCardInfoModel):
                    self._sub_scene_card_list.append(i)
                else:
                    self._sub_scene_card_list.append(SpecialCardInfoModel.from_alipay_dict(i))
    @property
    def sub_scene_code(self):
        return self._sub_scene_code

    @sub_scene_code.setter
    def sub_scene_code(self, value):
        self._sub_scene_code = value
    @property
    def sub_scene_code_name(self):
        return self._sub_scene_code_name

    @sub_scene_code_name.setter
    def sub_scene_code_name(self, value):
        self._sub_scene_code_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_scene_card_list:
            if isinstance(self.sub_scene_card_list, list):
                for i in range(0, len(self.sub_scene_card_list)):
                    element = self.sub_scene_card_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_scene_card_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_scene_card_list, 'to_alipay_dict'):
                params['sub_scene_card_list'] = self.sub_scene_card_list.to_alipay_dict()
            else:
                params['sub_scene_card_list'] = self.sub_scene_card_list
        if self.sub_scene_code:
            if hasattr(self.sub_scene_code, 'to_alipay_dict'):
                params['sub_scene_code'] = self.sub_scene_code.to_alipay_dict()
            else:
                params['sub_scene_code'] = self.sub_scene_code
        if self.sub_scene_code_name:
            if hasattr(self.sub_scene_code_name, 'to_alipay_dict'):
                params['sub_scene_code_name'] = self.sub_scene_code_name.to_alipay_dict()
            else:
                params['sub_scene_code_name'] = self.sub_scene_code_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubSceneCardModel()
        if 'sub_scene_card_list' in d:
            o.sub_scene_card_list = d['sub_scene_card_list']
        if 'sub_scene_code' in d:
            o.sub_scene_code = d['sub_scene_code']
        if 'sub_scene_code_name' in d:
            o.sub_scene_code_name = d['sub_scene_code_name']
        return o


