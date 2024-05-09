#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StagePayPlanInfoVO import StagePayPlanInfoVO


class StagePayPlanVO(object):

    def __init__(self):
        self._stage_no = None
        self._stage_pay_plan_infos = None

    @property
    def stage_no(self):
        return self._stage_no

    @stage_no.setter
    def stage_no(self, value):
        self._stage_no = value
    @property
    def stage_pay_plan_infos(self):
        return self._stage_pay_plan_infos

    @stage_pay_plan_infos.setter
    def stage_pay_plan_infos(self, value):
        if isinstance(value, StagePayPlanInfoVO):
            self._stage_pay_plan_infos = value
        else:
            self._stage_pay_plan_infos = StagePayPlanInfoVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.stage_no:
            if hasattr(self.stage_no, 'to_alipay_dict'):
                params['stage_no'] = self.stage_no.to_alipay_dict()
            else:
                params['stage_no'] = self.stage_no
        if self.stage_pay_plan_infos:
            if hasattr(self.stage_pay_plan_infos, 'to_alipay_dict'):
                params['stage_pay_plan_infos'] = self.stage_pay_plan_infos.to_alipay_dict()
            else:
                params['stage_pay_plan_infos'] = self.stage_pay_plan_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StagePayPlanVO()
        if 'stage_no' in d:
            o.stage_no = d['stage_no']
        if 'stage_pay_plan_infos' in d:
            o.stage_pay_plan_infos = d['stage_pay_plan_infos']
        return o


