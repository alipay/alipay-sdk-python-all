#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Pariticipant import Pariticipant
from alipay.aop.api.domain.EnterpriseInformation import EnterpriseInformation


class AlipayUserFlexiblestaffingRiskconsultApplyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._consult_party = None
        self._enterprise_info = None
        self._out_biz_no = None
        self._position = None
        self._product_code = None
        self._risk_scene = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def consult_party(self):
        return self._consult_party

    @consult_party.setter
    def consult_party(self, value):
        if isinstance(value, Pariticipant):
            self._consult_party = value
        else:
            self._consult_party = Pariticipant.from_alipay_dict(value)
    @property
    def enterprise_info(self):
        return self._enterprise_info

    @enterprise_info.setter
    def enterprise_info(self, value):
        if isinstance(value, EnterpriseInformation):
            self._enterprise_info = value
        else:
            self._enterprise_info = EnterpriseInformation.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def risk_scene(self):
        return self._risk_scene

    @risk_scene.setter
    def risk_scene(self, value):
        self._risk_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.consult_party:
            if hasattr(self.consult_party, 'to_alipay_dict'):
                params['consult_party'] = self.consult_party.to_alipay_dict()
            else:
                params['consult_party'] = self.consult_party
        if self.enterprise_info:
            if hasattr(self.enterprise_info, 'to_alipay_dict'):
                params['enterprise_info'] = self.enterprise_info.to_alipay_dict()
            else:
                params['enterprise_info'] = self.enterprise_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.position:
            if hasattr(self.position, 'to_alipay_dict'):
                params['position'] = self.position.to_alipay_dict()
            else:
                params['position'] = self.position
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.risk_scene:
            if hasattr(self.risk_scene, 'to_alipay_dict'):
                params['risk_scene'] = self.risk_scene.to_alipay_dict()
            else:
                params['risk_scene'] = self.risk_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserFlexiblestaffingRiskconsultApplyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'consult_party' in d:
            o.consult_party = d['consult_party']
        if 'enterprise_info' in d:
            o.enterprise_info = d['enterprise_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'position' in d:
            o.position = d['position']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'risk_scene' in d:
            o.risk_scene = d['risk_scene']
        return o


