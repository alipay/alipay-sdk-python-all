#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrReferralCodeRequestParamDTO import IndrReferralCodeRequestParamDTO


class AlipayOverseasOpenIndrreferralCreateModel(object):

    def __init__(self):
        self._referral_params = None
        self._scene_type = None

    @property
    def referral_params(self):
        return self._referral_params

    @referral_params.setter
    def referral_params(self, value):
        if isinstance(value, IndrReferralCodeRequestParamDTO):
            self._referral_params = value
        else:
            self._referral_params = IndrReferralCodeRequestParamDTO.from_alipay_dict(value)
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.referral_params:
            if hasattr(self.referral_params, 'to_alipay_dict'):
                params['referral_params'] = self.referral_params.to_alipay_dict()
            else:
                params['referral_params'] = self.referral_params
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenIndrreferralCreateModel()
        if 'referral_params' in d:
            o.referral_params = d['referral_params']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


