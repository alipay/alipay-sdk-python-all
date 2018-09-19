#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsDataDsbEstimateResultDetail import InsDataDsbEstimateResultDetail


class AlipayInsDataDsbEstimateSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._estimate_detail_list = None
        self._estimate_no = None
        self._frame_no = None
        self._license_no = None
        self._repair_corp_properties = None
        self._total_damage_amount = None
        self._total_remain_value = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def estimate_detail_list(self):
        return self._estimate_detail_list

    @estimate_detail_list.setter
    def estimate_detail_list(self, value):
        if isinstance(value, list):
            self._estimate_detail_list = list()
            for i in value:
                if isinstance(i, InsDataDsbEstimateResultDetail):
                    self._estimate_detail_list.append(i)
                else:
                    self._estimate_detail_list.append(InsDataDsbEstimateResultDetail.from_alipay_dict(i))
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
    def repair_corp_properties(self):
        return self._repair_corp_properties

    @repair_corp_properties.setter
    def repair_corp_properties(self, value):
        self._repair_corp_properties = value
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
        if self.repair_corp_properties:
            if hasattr(self.repair_corp_properties, 'to_alipay_dict'):
                params['repair_corp_properties'] = self.repair_corp_properties.to_alipay_dict()
            else:
                params['repair_corp_properties'] = self.repair_corp_properties
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
        o = AlipayInsDataDsbEstimateSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'estimate_detail_list' in d:
            o.estimate_detail_list = d['estimate_detail_list']
        if 'estimate_no' in d:
            o.estimate_no = d['estimate_no']
        if 'frame_no' in d:
            o.frame_no = d['frame_no']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'repair_corp_properties' in d:
            o.repair_corp_properties = d['repair_corp_properties']
        if 'total_damage_amount' in d:
            o.total_damage_amount = d['total_damage_amount']
        if 'total_remain_value' in d:
            o.total_remain_value = d['total_remain_value']
        return o


