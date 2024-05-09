#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessIndustryDTO import BusinessIndustryDTO
from alipay.aop.api.domain.PortraitInMallReqDTO import PortraitInMallReqDTO


class AlipayDataDataserviceBusinessReportQueryModel(object):

    def __init__(self):
        self._brand_rank_industry_dto = None
        self._business_code = None
        self._metric_keys = None
        self._partner_id = None
        self._portrait_in_mall_dto = None
        self._task_id = None

    @property
    def brand_rank_industry_dto(self):
        return self._brand_rank_industry_dto

    @brand_rank_industry_dto.setter
    def brand_rank_industry_dto(self, value):
        if isinstance(value, list):
            self._brand_rank_industry_dto = list()
            for i in value:
                if isinstance(i, BusinessIndustryDTO):
                    self._brand_rank_industry_dto.append(i)
                else:
                    self._brand_rank_industry_dto.append(BusinessIndustryDTO.from_alipay_dict(i))
    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def metric_keys(self):
        return self._metric_keys

    @metric_keys.setter
    def metric_keys(self, value):
        if isinstance(value, list):
            self._metric_keys = list()
            for i in value:
                self._metric_keys.append(i)
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def portrait_in_mall_dto(self):
        return self._portrait_in_mall_dto

    @portrait_in_mall_dto.setter
    def portrait_in_mall_dto(self, value):
        if isinstance(value, PortraitInMallReqDTO):
            self._portrait_in_mall_dto = value
        else:
            self._portrait_in_mall_dto = PortraitInMallReqDTO.from_alipay_dict(value)
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_rank_industry_dto:
            if isinstance(self.brand_rank_industry_dto, list):
                for i in range(0, len(self.brand_rank_industry_dto)):
                    element = self.brand_rank_industry_dto[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_rank_industry_dto[i] = element.to_alipay_dict()
            if hasattr(self.brand_rank_industry_dto, 'to_alipay_dict'):
                params['brand_rank_industry_dto'] = self.brand_rank_industry_dto.to_alipay_dict()
            else:
                params['brand_rank_industry_dto'] = self.brand_rank_industry_dto
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.metric_keys:
            if isinstance(self.metric_keys, list):
                for i in range(0, len(self.metric_keys)):
                    element = self.metric_keys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.metric_keys[i] = element.to_alipay_dict()
            if hasattr(self.metric_keys, 'to_alipay_dict'):
                params['metric_keys'] = self.metric_keys.to_alipay_dict()
            else:
                params['metric_keys'] = self.metric_keys
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.portrait_in_mall_dto:
            if hasattr(self.portrait_in_mall_dto, 'to_alipay_dict'):
                params['portrait_in_mall_dto'] = self.portrait_in_mall_dto.to_alipay_dict()
            else:
                params['portrait_in_mall_dto'] = self.portrait_in_mall_dto
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceBusinessReportQueryModel()
        if 'brand_rank_industry_dto' in d:
            o.brand_rank_industry_dto = d['brand_rank_industry_dto']
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'metric_keys' in d:
            o.metric_keys = d['metric_keys']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'portrait_in_mall_dto' in d:
            o.portrait_in_mall_dto = d['portrait_in_mall_dto']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


