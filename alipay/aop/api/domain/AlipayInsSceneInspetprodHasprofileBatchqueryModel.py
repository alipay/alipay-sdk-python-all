#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PetMarkIdDTO import PetMarkIdDTO


class AlipayInsSceneInspetprodHasprofileBatchqueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._channel = None
        self._mark_id_list = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def mark_id_list(self):
        return self._mark_id_list

    @mark_id_list.setter
    def mark_id_list(self, value):
        if isinstance(value, list):
            self._mark_id_list = list()
            for i in value:
                if isinstance(i, PetMarkIdDTO):
                    self._mark_id_list.append(i)
                else:
                    self._mark_id_list.append(PetMarkIdDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.mark_id_list:
            if isinstance(self.mark_id_list, list):
                for i in range(0, len(self.mark_id_list)):
                    element = self.mark_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mark_id_list[i] = element.to_alipay_dict()
            if hasattr(self.mark_id_list, 'to_alipay_dict'):
                params['mark_id_list'] = self.mark_id_list.to_alipay_dict()
            else:
                params['mark_id_list'] = self.mark_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInspetprodHasprofileBatchqueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'mark_id_list' in d:
            o.mark_id_list = d['mark_id_list']
        return o


