#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PariticipantDTO import PariticipantDTO


class AlipayUserFlexiblestaffingRiskconsultQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._consult_party = None
        self._enterprise_name = None
        self._out_biz_no = None
        self._product_code = None

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
        if isinstance(value, PariticipantDTO):
            self._consult_party = value
        else:
            self._consult_party = PariticipantDTO.from_alipay_dict(value)
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


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
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserFlexiblestaffingRiskconsultQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'consult_party' in d:
            o.consult_party = d['consult_party']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


