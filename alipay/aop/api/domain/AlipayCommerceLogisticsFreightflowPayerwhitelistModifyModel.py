#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FreightFlowAllowedAccount import FreightFlowAllowedAccount


class AlipayCommerceLogisticsFreightflowPayerwhitelistModifyModel(object):

    def __init__(self):
        self._allowed_account_white_list = None
        self._logistics_code = None
        self._mode = None
        self._owner_account_no = None
        self._owner_account_type = None
        self._scene = None

    @property
    def allowed_account_white_list(self):
        return self._allowed_account_white_list

    @allowed_account_white_list.setter
    def allowed_account_white_list(self, value):
        if isinstance(value, list):
            self._allowed_account_white_list = list()
            for i in value:
                if isinstance(i, FreightFlowAllowedAccount):
                    self._allowed_account_white_list.append(i)
                else:
                    self._allowed_account_white_list.append(FreightFlowAllowedAccount.from_alipay_dict(i))
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def owner_account_no(self):
        return self._owner_account_no

    @owner_account_no.setter
    def owner_account_no(self, value):
        self._owner_account_no = value
    @property
    def owner_account_type(self):
        return self._owner_account_type

    @owner_account_type.setter
    def owner_account_type(self, value):
        self._owner_account_type = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.allowed_account_white_list:
            if isinstance(self.allowed_account_white_list, list):
                for i in range(0, len(self.allowed_account_white_list)):
                    element = self.allowed_account_white_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.allowed_account_white_list[i] = element.to_alipay_dict()
            if hasattr(self.allowed_account_white_list, 'to_alipay_dict'):
                params['allowed_account_white_list'] = self.allowed_account_white_list.to_alipay_dict()
            else:
                params['allowed_account_white_list'] = self.allowed_account_white_list
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.owner_account_no:
            if hasattr(self.owner_account_no, 'to_alipay_dict'):
                params['owner_account_no'] = self.owner_account_no.to_alipay_dict()
            else:
                params['owner_account_no'] = self.owner_account_no
        if self.owner_account_type:
            if hasattr(self.owner_account_type, 'to_alipay_dict'):
                params['owner_account_type'] = self.owner_account_type.to_alipay_dict()
            else:
                params['owner_account_type'] = self.owner_account_type
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowPayerwhitelistModifyModel()
        if 'allowed_account_white_list' in d:
            o.allowed_account_white_list = d['allowed_account_white_list']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'owner_account_no' in d:
            o.owner_account_no = d['owner_account_no']
        if 'owner_account_type' in d:
            o.owner_account_type = d['owner_account_type']
        if 'scene' in d:
            o.scene = d['scene']
        return o


