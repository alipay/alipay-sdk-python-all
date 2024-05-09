#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenePayToken import ScenePayToken
from alipay.aop.api.domain.UnionCodeExtendParam import UnionCodeExtendParam


class AlipayTradeScenepayTokenSyncModel(object):

    def __init__(self):
        self._agreement_no = None
        self._biz_scene = None
        self._product_code = None
        self._scene_pay_token = None
        self._sub_biz_scene = None
        self._union_code_extend_params = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_pay_token(self):
        return self._scene_pay_token

    @scene_pay_token.setter
    def scene_pay_token(self, value):
        if isinstance(value, ScenePayToken):
            self._scene_pay_token = value
        else:
            self._scene_pay_token = ScenePayToken.from_alipay_dict(value)
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value
    @property
    def union_code_extend_params(self):
        return self._union_code_extend_params

    @union_code_extend_params.setter
    def union_code_extend_params(self, value):
        if isinstance(value, UnionCodeExtendParam):
            self._union_code_extend_params = value
        else:
            self._union_code_extend_params = UnionCodeExtendParam.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_pay_token:
            if hasattr(self.scene_pay_token, 'to_alipay_dict'):
                params['scene_pay_token'] = self.scene_pay_token.to_alipay_dict()
            else:
                params['scene_pay_token'] = self.scene_pay_token
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        if self.union_code_extend_params:
            if hasattr(self.union_code_extend_params, 'to_alipay_dict'):
                params['union_code_extend_params'] = self.union_code_extend_params.to_alipay_dict()
            else:
                params['union_code_extend_params'] = self.union_code_extend_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeScenepayTokenSyncModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_pay_token' in d:
            o.scene_pay_token = d['scene_pay_token']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        if 'union_code_extend_params' in d:
            o.union_code_extend_params = d['union_code_extend_params']
        return o


