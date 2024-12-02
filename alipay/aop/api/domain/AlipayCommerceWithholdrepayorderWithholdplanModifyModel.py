#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndustryWithholdPlanDTO import IndustryWithholdPlanDTO


class AlipayCommerceWithholdrepayorderWithholdplanModifyModel(object):

    def __init__(self):
        self._agreement_no = None
        self._external_agreement_no = None
        self._open_id = None
        self._out_biz_no = None
        self._repay_plan = None
        self._sign_scene = None
        self._stage = None
        self._user_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def external_agreement_no(self):
        return self._external_agreement_no

    @external_agreement_no.setter
    def external_agreement_no(self, value):
        self._external_agreement_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def repay_plan(self):
        return self._repay_plan

    @repay_plan.setter
    def repay_plan(self, value):
        if isinstance(value, list):
            self._repay_plan = list()
            for i in value:
                if isinstance(i, IndustryWithholdPlanDTO):
                    self._repay_plan.append(i)
                else:
                    self._repay_plan.append(IndustryWithholdPlanDTO.from_alipay_dict(i))
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.external_agreement_no:
            if hasattr(self.external_agreement_no, 'to_alipay_dict'):
                params['external_agreement_no'] = self.external_agreement_no.to_alipay_dict()
            else:
                params['external_agreement_no'] = self.external_agreement_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.repay_plan:
            if isinstance(self.repay_plan, list):
                for i in range(0, len(self.repay_plan)):
                    element = self.repay_plan[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_plan[i] = element.to_alipay_dict()
            if hasattr(self.repay_plan, 'to_alipay_dict'):
                params['repay_plan'] = self.repay_plan.to_alipay_dict()
            else:
                params['repay_plan'] = self.repay_plan
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        if self.stage:
            if hasattr(self.stage, 'to_alipay_dict'):
                params['stage'] = self.stage.to_alipay_dict()
            else:
                params['stage'] = self.stage
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceWithholdrepayorderWithholdplanModifyModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'external_agreement_no' in d:
            o.external_agreement_no = d['external_agreement_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'repay_plan' in d:
            o.repay_plan = d['repay_plan']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        if 'stage' in d:
            o.stage = d['stage']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


