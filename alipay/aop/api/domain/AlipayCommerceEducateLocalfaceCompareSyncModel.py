#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateLocalfaceCompareSyncModel(object):

    def __init__(self):
        self._aes_cypher = None
        self._alg_ver = None
        self._auth_img = None
        self._biz_code = None
        self._biz_id = None
        self._ext_info = None
        self._face_data_type = None
        self._fuid = None
        self._isv_name = None
        self._organize_id = None
        self._quality = None
        self._rect = None
        self._score = None

    @property
    def aes_cypher(self):
        return self._aes_cypher

    @aes_cypher.setter
    def aes_cypher(self, value):
        self._aes_cypher = value
    @property
    def alg_ver(self):
        return self._alg_ver

    @alg_ver.setter
    def alg_ver(self, value):
        self._alg_ver = value
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
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def face_data_type(self):
        return self._face_data_type

    @face_data_type.setter
    def face_data_type(self, value):
        self._face_data_type = value
    @property
    def fuid(self):
        return self._fuid

    @fuid.setter
    def fuid(self, value):
        self._fuid = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def organize_id(self):
        return self._organize_id

    @organize_id.setter
    def organize_id(self, value):
        self._organize_id = value
    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value
    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.aes_cypher:
            if hasattr(self.aes_cypher, 'to_alipay_dict'):
                params['aes_cypher'] = self.aes_cypher.to_alipay_dict()
            else:
                params['aes_cypher'] = self.aes_cypher
        if self.alg_ver:
            if hasattr(self.alg_ver, 'to_alipay_dict'):
                params['alg_ver'] = self.alg_ver.to_alipay_dict()
            else:
                params['alg_ver'] = self.alg_ver
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
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.face_data_type:
            if hasattr(self.face_data_type, 'to_alipay_dict'):
                params['face_data_type'] = self.face_data_type.to_alipay_dict()
            else:
                params['face_data_type'] = self.face_data_type
        if self.fuid:
            if hasattr(self.fuid, 'to_alipay_dict'):
                params['fuid'] = self.fuid.to_alipay_dict()
            else:
                params['fuid'] = self.fuid
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.organize_id:
            if hasattr(self.organize_id, 'to_alipay_dict'):
                params['organize_id'] = self.organize_id.to_alipay_dict()
            else:
                params['organize_id'] = self.organize_id
        if self.quality:
            if hasattr(self.quality, 'to_alipay_dict'):
                params['quality'] = self.quality.to_alipay_dict()
            else:
                params['quality'] = self.quality
        if self.rect:
            if hasattr(self.rect, 'to_alipay_dict'):
                params['rect'] = self.rect.to_alipay_dict()
            else:
                params['rect'] = self.rect
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateLocalfaceCompareSyncModel()
        if 'aes_cypher' in d:
            o.aes_cypher = d['aes_cypher']
        if 'alg_ver' in d:
            o.alg_ver = d['alg_ver']
        if 'auth_img' in d:
            o.auth_img = d['auth_img']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'face_data_type' in d:
            o.face_data_type = d['face_data_type']
        if 'fuid' in d:
            o.fuid = d['fuid']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'organize_id' in d:
            o.organize_id = d['organize_id']
        if 'quality' in d:
            o.quality = d['quality']
        if 'rect' in d:
            o.rect = d['rect']
        if 'score' in d:
            o.score = d['score']
        return o


