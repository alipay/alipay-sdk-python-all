#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenePayParticipantInfoDTO import ScenePayParticipantInfoDTO
from alipay.aop.api.domain.GeneralWithholdInfoDTO import GeneralWithholdInfoDTO
from alipay.aop.api.domain.ScenePayParticipantInfoDTO import ScenePayParticipantInfoDTO


class AlipayFundScenepayAuthorizeApplyModel(object):

    def __init__(self):
        self._authorization_type = None
        self._biz_scene = None
        self._business_principal_info = None
        self._general_withhold_info = None
        self._out_biz_no = None
        self._principal_info = None
        self._product_code = None
        self._sub_biz_scene = None

    @property
    def authorization_type(self):
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, value):
        self._authorization_type = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def business_principal_info(self):
        return self._business_principal_info

    @business_principal_info.setter
    def business_principal_info(self, value):
        if isinstance(value, ScenePayParticipantInfoDTO):
            self._business_principal_info = value
        else:
            self._business_principal_info = ScenePayParticipantInfoDTO.from_alipay_dict(value)
    @property
    def general_withhold_info(self):
        return self._general_withhold_info

    @general_withhold_info.setter
    def general_withhold_info(self, value):
        if isinstance(value, GeneralWithholdInfoDTO):
            self._general_withhold_info = value
        else:
            self._general_withhold_info = GeneralWithholdInfoDTO.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_info(self):
        return self._principal_info

    @principal_info.setter
    def principal_info(self, value):
        if isinstance(value, ScenePayParticipantInfoDTO):
            self._principal_info = value
        else:
            self._principal_info = ScenePayParticipantInfoDTO.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization_type:
            if hasattr(self.authorization_type, 'to_alipay_dict'):
                params['authorization_type'] = self.authorization_type.to_alipay_dict()
            else:
                params['authorization_type'] = self.authorization_type
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.business_principal_info:
            if hasattr(self.business_principal_info, 'to_alipay_dict'):
                params['business_principal_info'] = self.business_principal_info.to_alipay_dict()
            else:
                params['business_principal_info'] = self.business_principal_info
        if self.general_withhold_info:
            if hasattr(self.general_withhold_info, 'to_alipay_dict'):
                params['general_withhold_info'] = self.general_withhold_info.to_alipay_dict()
            else:
                params['general_withhold_info'] = self.general_withhold_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.principal_info:
            if hasattr(self.principal_info, 'to_alipay_dict'):
                params['principal_info'] = self.principal_info.to_alipay_dict()
            else:
                params['principal_info'] = self.principal_info
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundScenepayAuthorizeApplyModel()
        if 'authorization_type' in d:
            o.authorization_type = d['authorization_type']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_principal_info' in d:
            o.business_principal_info = d['business_principal_info']
        if 'general_withhold_info' in d:
            o.general_withhold_info = d['general_withhold_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'principal_info' in d:
            o.principal_info = d['principal_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        return o


