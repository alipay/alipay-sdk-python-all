#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstallmentPlanPromoDetailInfoVO import InstallmentPlanPromoDetailInfoVO


class StagePromoDetailInfoVO(object):

    def __init__(self):
        self._installment_plan_promo_detail_info_list = None
        self._stage_no = None

    @property
    def installment_plan_promo_detail_info_list(self):
        return self._installment_plan_promo_detail_info_list

    @installment_plan_promo_detail_info_list.setter
    def installment_plan_promo_detail_info_list(self, value):
        if isinstance(value, list):
            self._installment_plan_promo_detail_info_list = list()
            for i in value:
                if isinstance(i, InstallmentPlanPromoDetailInfoVO):
                    self._installment_plan_promo_detail_info_list.append(i)
                else:
                    self._installment_plan_promo_detail_info_list.append(InstallmentPlanPromoDetailInfoVO.from_alipay_dict(i))
    @property
    def stage_no(self):
        return self._stage_no

    @stage_no.setter
    def stage_no(self, value):
        self._stage_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.installment_plan_promo_detail_info_list:
            if isinstance(self.installment_plan_promo_detail_info_list, list):
                for i in range(0, len(self.installment_plan_promo_detail_info_list)):
                    element = self.installment_plan_promo_detail_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installment_plan_promo_detail_info_list[i] = element.to_alipay_dict()
            if hasattr(self.installment_plan_promo_detail_info_list, 'to_alipay_dict'):
                params['installment_plan_promo_detail_info_list'] = self.installment_plan_promo_detail_info_list.to_alipay_dict()
            else:
                params['installment_plan_promo_detail_info_list'] = self.installment_plan_promo_detail_info_list
        if self.stage_no:
            if hasattr(self.stage_no, 'to_alipay_dict'):
                params['stage_no'] = self.stage_no.to_alipay_dict()
            else:
                params['stage_no'] = self.stage_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StagePromoDetailInfoVO()
        if 'installment_plan_promo_detail_info_list' in d:
            o.installment_plan_promo_detail_info_list = d['installment_plan_promo_detail_info_list']
        if 'stage_no' in d:
            o.stage_no = d['stage_no']
        return o


