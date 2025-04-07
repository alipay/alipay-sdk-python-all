#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentRiskConsultModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._consult_risk_types = None
        self._out_biz_no = None
        self._risk_biz_scene = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def consult_risk_types(self):
        return self._consult_risk_types

    @consult_risk_types.setter
    def consult_risk_types(self, value):
        if isinstance(value, list):
            self._consult_risk_types = list()
            for i in value:
                self._consult_risk_types.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def risk_biz_scene(self):
        return self._risk_biz_scene

    @risk_biz_scene.setter
    def risk_biz_scene(self, value):
        self._risk_biz_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.consult_risk_types:
            if isinstance(self.consult_risk_types, list):
                for i in range(0, len(self.consult_risk_types)):
                    element = self.consult_risk_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.consult_risk_types[i] = element.to_alipay_dict()
            if hasattr(self.consult_risk_types, 'to_alipay_dict'):
                params['consult_risk_types'] = self.consult_risk_types.to_alipay_dict()
            else:
                params['consult_risk_types'] = self.consult_risk_types
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.risk_biz_scene:
            if hasattr(self.risk_biz_scene, 'to_alipay_dict'):
                params['risk_biz_scene'] = self.risk_biz_scene.to_alipay_dict()
            else:
                params['risk_biz_scene'] = self.risk_biz_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentRiskConsultModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'consult_risk_types' in d:
            o.consult_risk_types = d['consult_risk_types']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'risk_biz_scene' in d:
            o.risk_biz_scene = d['risk_biz_scene']
        return o


