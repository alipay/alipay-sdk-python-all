#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayUserVO import CreditPayUserVO


class MybankCreditLoantradePayerArConsultModel(object):

    def __init__(self):
        self._biz_scene = None
        self._user_info = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, CreditPayUserVO):
            self._user_info = value
        else:
            self._user_info = CreditPayUserVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradePayerArConsultModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o


