#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAmpeRecommendPreconsultModel(object):

    def __init__(self):
        self._biz_id_list = None
        self._biz_scene = None
        self._device_id = None
        self._product_id = None
        self._req_no = None

    @property
    def biz_id_list(self):
        return self._biz_id_list

    @biz_id_list.setter
    def biz_id_list(self, value):
        if isinstance(value, list):
            self._biz_id_list = list()
            for i in value:
                self._biz_id_list.append(i)
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def req_no(self):
        return self._req_no

    @req_no.setter
    def req_no(self, value):
        self._req_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id_list:
            if isinstance(self.biz_id_list, list):
                for i in range(0, len(self.biz_id_list)):
                    element = self.biz_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_id_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_id_list, 'to_alipay_dict'):
                params['biz_id_list'] = self.biz_id_list.to_alipay_dict()
            else:
                params['biz_id_list'] = self.biz_id_list
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.req_no:
            if hasattr(self.req_no, 'to_alipay_dict'):
                params['req_no'] = self.req_no.to_alipay_dict()
            else:
                params['req_no'] = self.req_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAmpeRecommendPreconsultModel()
        if 'biz_id_list' in d:
            o.biz_id_list = d['biz_id_list']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'req_no' in d:
            o.req_no = d['req_no']
        return o


