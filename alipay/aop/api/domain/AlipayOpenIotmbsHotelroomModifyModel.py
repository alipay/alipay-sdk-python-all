#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsHotelroomModifyModel(object):

    def __init__(self):
        self._face_id = None
        self._floor_num = None
        self._source_sn_list = None
        self._target_sn_list = None

    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def floor_num(self):
        return self._floor_num

    @floor_num.setter
    def floor_num(self, value):
        self._floor_num = value
    @property
    def source_sn_list(self):
        return self._source_sn_list

    @source_sn_list.setter
    def source_sn_list(self, value):
        if isinstance(value, list):
            self._source_sn_list = list()
            for i in value:
                self._source_sn_list.append(i)
    @property
    def target_sn_list(self):
        return self._target_sn_list

    @target_sn_list.setter
    def target_sn_list(self, value):
        if isinstance(value, list):
            self._target_sn_list = list()
            for i in value:
                self._target_sn_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.floor_num:
            if hasattr(self.floor_num, 'to_alipay_dict'):
                params['floor_num'] = self.floor_num.to_alipay_dict()
            else:
                params['floor_num'] = self.floor_num
        if self.source_sn_list:
            if isinstance(self.source_sn_list, list):
                for i in range(0, len(self.source_sn_list)):
                    element = self.source_sn_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_sn_list[i] = element.to_alipay_dict()
            if hasattr(self.source_sn_list, 'to_alipay_dict'):
                params['source_sn_list'] = self.source_sn_list.to_alipay_dict()
            else:
                params['source_sn_list'] = self.source_sn_list
        if self.target_sn_list:
            if isinstance(self.target_sn_list, list):
                for i in range(0, len(self.target_sn_list)):
                    element = self.target_sn_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_sn_list[i] = element.to_alipay_dict()
            if hasattr(self.target_sn_list, 'to_alipay_dict'):
                params['target_sn_list'] = self.target_sn_list.to_alipay_dict()
            else:
                params['target_sn_list'] = self.target_sn_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsHotelroomModifyModel()
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'floor_num' in d:
            o.floor_num = d['floor_num']
        if 'source_sn_list' in d:
            o.source_sn_list = d['source_sn_list']
        if 'target_sn_list' in d:
            o.target_sn_list = d['target_sn_list']
        return o


