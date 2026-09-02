#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VerifyParamList import VerifyParamList


class AlipayCommerceMedicalInsuranceClaimreportVerifyModel(object):

    def __init__(self):
        self._check_scene = None
        self._secret_key = None
        self._verify_param_list = None

    @property
    def check_scene(self):
        return self._check_scene

    @check_scene.setter
    def check_scene(self, value):
        self._check_scene = value
    @property
    def secret_key(self):
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = value
    @property
    def verify_param_list(self):
        return self._verify_param_list

    @verify_param_list.setter
    def verify_param_list(self, value):
        if isinstance(value, list):
            self._verify_param_list = list()
            for i in value:
                if isinstance(i, VerifyParamList):
                    self._verify_param_list.append(i)
                else:
                    self._verify_param_list.append(VerifyParamList.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.check_scene:
            if hasattr(self.check_scene, 'to_alipay_dict'):
                params['check_scene'] = self.check_scene.to_alipay_dict()
            else:
                params['check_scene'] = self.check_scene
        if self.secret_key:
            if hasattr(self.secret_key, 'to_alipay_dict'):
                params['secret_key'] = self.secret_key.to_alipay_dict()
            else:
                params['secret_key'] = self.secret_key
        if self.verify_param_list:
            if isinstance(self.verify_param_list, list):
                for i in range(0, len(self.verify_param_list)):
                    element = self.verify_param_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.verify_param_list[i] = element.to_alipay_dict()
            if hasattr(self.verify_param_list, 'to_alipay_dict'):
                params['verify_param_list'] = self.verify_param_list.to_alipay_dict()
            else:
                params['verify_param_list'] = self.verify_param_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceClaimreportVerifyModel()
        if 'check_scene' in d:
            o.check_scene = d['check_scene']
        if 'secret_key' in d:
            o.secret_key = d['secret_key']
        if 'verify_param_list' in d:
            o.verify_param_list = d['verify_param_list']
        return o


