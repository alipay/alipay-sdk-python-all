#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateFacefeatureReportUploadModel(object):

    def __init__(self):
        self._aes_cypher = None
        self._auth_img = None
        self._biz_code = None
        self._device_num = None
        self._inst_id = None
        self._isv_name = None
        self._scene_code = None
        self._z_face_info = None

    @property
    def aes_cypher(self):
        return self._aes_cypher

    @aes_cypher.setter
    def aes_cypher(self, value):
        self._aes_cypher = value
    @property
    def auth_img(self):
        return self._auth_img

    @auth_img.setter
    def auth_img(self, value):
        self._auth_img = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def device_num(self):
        return self._device_num

    @device_num.setter
    def device_num(self, value):
        self._device_num = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def z_face_info(self):
        return self._z_face_info

    @z_face_info.setter
    def z_face_info(self, value):
        self._z_face_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.aes_cypher:
            if hasattr(self.aes_cypher, 'to_alipay_dict'):
                params['aes_cypher'] = self.aes_cypher.to_alipay_dict()
            else:
                params['aes_cypher'] = self.aes_cypher
        if self.auth_img:
            if hasattr(self.auth_img, 'to_alipay_dict'):
                params['auth_img'] = self.auth_img.to_alipay_dict()
            else:
                params['auth_img'] = self.auth_img
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.device_num:
            if hasattr(self.device_num, 'to_alipay_dict'):
                params['device_num'] = self.device_num.to_alipay_dict()
            else:
                params['device_num'] = self.device_num
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.z_face_info:
            if hasattr(self.z_face_info, 'to_alipay_dict'):
                params['z_face_info'] = self.z_face_info.to_alipay_dict()
            else:
                params['z_face_info'] = self.z_face_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateFacefeatureReportUploadModel()
        if 'aes_cypher' in d:
            o.aes_cypher = d['aes_cypher']
        if 'auth_img' in d:
            o.auth_img = d['auth_img']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'device_num' in d:
            o.device_num = d['device_num']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'z_face_info' in d:
            o.z_face_info = d['z_face_info']
        return o


