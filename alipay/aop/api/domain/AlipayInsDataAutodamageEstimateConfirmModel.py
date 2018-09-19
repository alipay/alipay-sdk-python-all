#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsDataAutodamageEstimateConfirmModel import InsDataAutodamageEstimateConfirmModel


class AlipayInsDataAutodamageEstimateConfirmModel(object):

    def __init__(self):
        self._biz_type = None
        self._commercial_policy_no = None
        self._compulsory_policy_no = None
        self._engine_no = None
        self._estimate_detail_list = None
        self._estimate_no = None
        self._frame_no = None
        self._license_no = None
        self._model_brand = None
        self._repair_corp_name = None
        self._repair_corp_type = None
        self._report_no = None
        self._survey_no = None
        self._total_damage_amount = None
        self._total_remain_value = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def commercial_policy_no(self):
        return self._commercial_policy_no

    @commercial_policy_no.setter
    def commercial_policy_no(self, value):
        self._commercial_policy_no = value
    @property
    def compulsory_policy_no(self):
        return self._compulsory_policy_no

    @compulsory_policy_no.setter
    def compulsory_policy_no(self, value):
        self._compulsory_policy_no = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def estimate_detail_list(self):
        return self._estimate_detail_list

    @estimate_detail_list.setter
    def estimate_detail_list(self, value):
        if isinstance(value, list):
            self._estimate_detail_list = list()
            for i in value:
                if isinstance(i, InsDataAutodamageEstimateConfirmModel):
                    self._estimate_detail_list.append(i)
                else:
                    self._estimate_detail_list.append(InsDataAutodamageEstimateConfirmModel.from_alipay_dict(i))
    @property
    def estimate_no(self):
        return self._estimate_no

    @estimate_no.setter
    def estimate_no(self, value):
        self._estimate_no = value
    @property
    def frame_no(self):
        return self._frame_no

    @frame_no.setter
    def frame_no(self, value):
        self._frame_no = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def model_brand(self):
        return self._model_brand

    @model_brand.setter
    def model_brand(self, value):
        self._model_brand = value
    @property
    def repair_corp_name(self):
        return self._repair_corp_name

    @repair_corp_name.setter
    def repair_corp_name(self, value):
        self._repair_corp_name = value
    @property
    def repair_corp_type(self):
        return self._repair_corp_type

    @repair_corp_type.setter
    def repair_corp_type(self, value):
        self._repair_corp_type = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value
    @property
    def survey_no(self):
        return self._survey_no

    @survey_no.setter
    def survey_no(self, value):
        self._survey_no = value
    @property
    def total_damage_amount(self):
        return self._total_damage_amount

    @total_damage_amount.setter
    def total_damage_amount(self, value):
        self._total_damage_amount = value
    @property
    def total_remain_value(self):
        return self._total_remain_value

    @total_remain_value.setter
    def total_remain_value(self, value):
        self._total_remain_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.commercial_policy_no:
            if hasattr(self.commercial_policy_no, 'to_alipay_dict'):
                params['commercial_policy_no'] = self.commercial_policy_no.to_alipay_dict()
            else:
                params['commercial_policy_no'] = self.commercial_policy_no
        if self.compulsory_policy_no:
            if hasattr(self.compulsory_policy_no, 'to_alipay_dict'):
                params['compulsory_policy_no'] = self.compulsory_policy_no.to_alipay_dict()
            else:
                params['compulsory_policy_no'] = self.compulsory_policy_no
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.estimate_detail_list:
            if isinstance(self.estimate_detail_list, list):
                for i in range(0, len(self.estimate_detail_list)):
                    element = self.estimate_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.estimate_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.estimate_detail_list, 'to_alipay_dict'):
                params['estimate_detail_list'] = self.estimate_detail_list.to_alipay_dict()
            else:
                params['estimate_detail_list'] = self.estimate_detail_list
        if self.estimate_no:
            if hasattr(self.estimate_no, 'to_alipay_dict'):
                params['estimate_no'] = self.estimate_no.to_alipay_dict()
            else:
                params['estimate_no'] = self.estimate_no
        if self.frame_no:
            if hasattr(self.frame_no, 'to_alipay_dict'):
                params['frame_no'] = self.frame_no.to_alipay_dict()
            else:
                params['frame_no'] = self.frame_no
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = self.license_no.to_alipay_dict()
            else:
                params['license_no'] = self.license_no
        if self.model_brand:
            if hasattr(self.model_brand, 'to_alipay_dict'):
                params['model_brand'] = self.model_brand.to_alipay_dict()
            else:
                params['model_brand'] = self.model_brand
        if self.repair_corp_name:
            if hasattr(self.repair_corp_name, 'to_alipay_dict'):
                params['repair_corp_name'] = self.repair_corp_name.to_alipay_dict()
            else:
                params['repair_corp_name'] = self.repair_corp_name
        if self.repair_corp_type:
            if hasattr(self.repair_corp_type, 'to_alipay_dict'):
                params['repair_corp_type'] = self.repair_corp_type.to_alipay_dict()
            else:
                params['repair_corp_type'] = self.repair_corp_type
        if self.report_no:
            if hasattr(self.report_no, 'to_alipay_dict'):
                params['report_no'] = self.report_no.to_alipay_dict()
            else:
                params['report_no'] = self.report_no
        if self.survey_no:
            if hasattr(self.survey_no, 'to_alipay_dict'):
                params['survey_no'] = self.survey_no.to_alipay_dict()
            else:
                params['survey_no'] = self.survey_no
        if self.total_damage_amount:
            if hasattr(self.total_damage_amount, 'to_alipay_dict'):
                params['total_damage_amount'] = self.total_damage_amount.to_alipay_dict()
            else:
                params['total_damage_amount'] = self.total_damage_amount
        if self.total_remain_value:
            if hasattr(self.total_remain_value, 'to_alipay_dict'):
                params['total_remain_value'] = self.total_remain_value.to_alipay_dict()
            else:
                params['total_remain_value'] = self.total_remain_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsDataAutodamageEstimateConfirmModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'commercial_policy_no' in d:
            o.commercial_policy_no = d['commercial_policy_no']
        if 'compulsory_policy_no' in d:
            o.compulsory_policy_no = d['compulsory_policy_no']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'estimate_detail_list' in d:
            o.estimate_detail_list = d['estimate_detail_list']
        if 'estimate_no' in d:
            o.estimate_no = d['estimate_no']
        if 'frame_no' in d:
            o.frame_no = d['frame_no']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'model_brand' in d:
            o.model_brand = d['model_brand']
        if 'repair_corp_name' in d:
            o.repair_corp_name = d['repair_corp_name']
        if 'repair_corp_type' in d:
            o.repair_corp_type = d['repair_corp_type']
        if 'report_no' in d:
            o.report_no = d['report_no']
        if 'survey_no' in d:
            o.survey_no = d['survey_no']
        if 'total_damage_amount' in d:
            o.total_damage_amount = d['total_damage_amount']
        if 'total_remain_value' in d:
            o.total_remain_value = d['total_remain_value']
        return o


