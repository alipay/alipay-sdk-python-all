#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogMmtcaftscvTemplateVerifyModel(object):

    def __init__(self):
        self._algorithm_goods_ids = None
        self._device_identify_type = None
        self._good_count = None
        self._machine_type_id = None
        self._scene_id = None
        self._template_id = None
        self._white_list = None

    @property
    def algorithm_goods_ids(self):
        return self._algorithm_goods_ids

    @algorithm_goods_ids.setter
    def algorithm_goods_ids(self, value):
        if isinstance(value, list):
            self._algorithm_goods_ids = list()
            for i in value:
                self._algorithm_goods_ids.append(i)
    @property
    def device_identify_type(self):
        return self._device_identify_type

    @device_identify_type.setter
    def device_identify_type(self, value):
        self._device_identify_type = value
    @property
    def good_count(self):
        return self._good_count

    @good_count.setter
    def good_count(self, value):
        self._good_count = value
    @property
    def machine_type_id(self):
        return self._machine_type_id

    @machine_type_id.setter
    def machine_type_id(self, value):
        self._machine_type_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def white_list(self):
        return self._white_list

    @white_list.setter
    def white_list(self, value):
        if isinstance(value, list):
            self._white_list = list()
            for i in value:
                self._white_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_goods_ids:
            if isinstance(self.algorithm_goods_ids, list):
                for i in range(0, len(self.algorithm_goods_ids)):
                    element = self.algorithm_goods_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.algorithm_goods_ids[i] = element.to_alipay_dict()
            if hasattr(self.algorithm_goods_ids, 'to_alipay_dict'):
                params['algorithm_goods_ids'] = self.algorithm_goods_ids.to_alipay_dict()
            else:
                params['algorithm_goods_ids'] = self.algorithm_goods_ids
        if self.device_identify_type:
            if hasattr(self.device_identify_type, 'to_alipay_dict'):
                params['device_identify_type'] = self.device_identify_type.to_alipay_dict()
            else:
                params['device_identify_type'] = self.device_identify_type
        if self.good_count:
            if hasattr(self.good_count, 'to_alipay_dict'):
                params['good_count'] = self.good_count.to_alipay_dict()
            else:
                params['good_count'] = self.good_count
        if self.machine_type_id:
            if hasattr(self.machine_type_id, 'to_alipay_dict'):
                params['machine_type_id'] = self.machine_type_id.to_alipay_dict()
            else:
                params['machine_type_id'] = self.machine_type_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.white_list:
            if isinstance(self.white_list, list):
                for i in range(0, len(self.white_list)):
                    element = self.white_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.white_list[i] = element.to_alipay_dict()
            if hasattr(self.white_list, 'to_alipay_dict'):
                params['white_list'] = self.white_list.to_alipay_dict()
            else:
                params['white_list'] = self.white_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvTemplateVerifyModel()
        if 'algorithm_goods_ids' in d:
            o.algorithm_goods_ids = d['algorithm_goods_ids']
        if 'device_identify_type' in d:
            o.device_identify_type = d['device_identify_type']
        if 'good_count' in d:
            o.good_count = d['good_count']
        if 'machine_type_id' in d:
            o.machine_type_id = d['machine_type_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'white_list' in d:
            o.white_list = d['white_list']
        return o


