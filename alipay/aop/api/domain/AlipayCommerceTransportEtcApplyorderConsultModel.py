#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcApplyorderConsultModel(object):

    def __init__(self):
        self._biz_agreement_no = None
        self._consult_scene = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def consult_scene(self):
        return self._consult_scene

    @consult_scene.setter
    def consult_scene(self, value):
        self._consult_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        if self.consult_scene:
            if hasattr(self.consult_scene, 'to_alipay_dict'):
                params['consult_scene'] = self.consult_scene.to_alipay_dict()
            else:
                params['consult_scene'] = self.consult_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcApplyorderConsultModel()
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'consult_scene' in d:
            o.consult_scene = d['consult_scene']
        return o


