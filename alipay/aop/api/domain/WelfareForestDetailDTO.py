#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RewardDTO import RewardDTO
from alipay.aop.api.domain.WelfareForestEntityDTO import WelfareForestEntityDTO
from alipay.aop.api.domain.WelfareForestPersonWaterDTO import WelfareForestPersonWaterDTO
from alipay.aop.api.domain.WelfareForestWaterSummaryDTO import WelfareForestWaterSummaryDTO


class WelfareForestDetailDTO(object):

    def __init__(self):
        self._reward_info_list = None
        self._rewarded_code_list = None
        self._welfare_forest_entity = None
        self._welfare_forest_person_water_info = None
        self._welfare_forest_water_summary_info = None

    @property
    def reward_info_list(self):
        return self._reward_info_list

    @reward_info_list.setter
    def reward_info_list(self, value):
        if isinstance(value, list):
            self._reward_info_list = list()
            for i in value:
                if isinstance(i, RewardDTO):
                    self._reward_info_list.append(i)
                else:
                    self._reward_info_list.append(RewardDTO.from_alipay_dict(i))
    @property
    def rewarded_code_list(self):
        return self._rewarded_code_list

    @rewarded_code_list.setter
    def rewarded_code_list(self, value):
        if isinstance(value, list):
            self._rewarded_code_list = list()
            for i in value:
                self._rewarded_code_list.append(i)
    @property
    def welfare_forest_entity(self):
        return self._welfare_forest_entity

    @welfare_forest_entity.setter
    def welfare_forest_entity(self, value):
        if isinstance(value, WelfareForestEntityDTO):
            self._welfare_forest_entity = value
        else:
            self._welfare_forest_entity = WelfareForestEntityDTO.from_alipay_dict(value)
    @property
    def welfare_forest_person_water_info(self):
        return self._welfare_forest_person_water_info

    @welfare_forest_person_water_info.setter
    def welfare_forest_person_water_info(self, value):
        if isinstance(value, WelfareForestPersonWaterDTO):
            self._welfare_forest_person_water_info = value
        else:
            self._welfare_forest_person_water_info = WelfareForestPersonWaterDTO.from_alipay_dict(value)
    @property
    def welfare_forest_water_summary_info(self):
        return self._welfare_forest_water_summary_info

    @welfare_forest_water_summary_info.setter
    def welfare_forest_water_summary_info(self, value):
        if isinstance(value, WelfareForestWaterSummaryDTO):
            self._welfare_forest_water_summary_info = value
        else:
            self._welfare_forest_water_summary_info = WelfareForestWaterSummaryDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.reward_info_list:
            if isinstance(self.reward_info_list, list):
                for i in range(0, len(self.reward_info_list)):
                    element = self.reward_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reward_info_list[i] = element.to_alipay_dict()
            if hasattr(self.reward_info_list, 'to_alipay_dict'):
                params['reward_info_list'] = self.reward_info_list.to_alipay_dict()
            else:
                params['reward_info_list'] = self.reward_info_list
        if self.rewarded_code_list:
            if isinstance(self.rewarded_code_list, list):
                for i in range(0, len(self.rewarded_code_list)):
                    element = self.rewarded_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rewarded_code_list[i] = element.to_alipay_dict()
            if hasattr(self.rewarded_code_list, 'to_alipay_dict'):
                params['rewarded_code_list'] = self.rewarded_code_list.to_alipay_dict()
            else:
                params['rewarded_code_list'] = self.rewarded_code_list
        if self.welfare_forest_entity:
            if hasattr(self.welfare_forest_entity, 'to_alipay_dict'):
                params['welfare_forest_entity'] = self.welfare_forest_entity.to_alipay_dict()
            else:
                params['welfare_forest_entity'] = self.welfare_forest_entity
        if self.welfare_forest_person_water_info:
            if hasattr(self.welfare_forest_person_water_info, 'to_alipay_dict'):
                params['welfare_forest_person_water_info'] = self.welfare_forest_person_water_info.to_alipay_dict()
            else:
                params['welfare_forest_person_water_info'] = self.welfare_forest_person_water_info
        if self.welfare_forest_water_summary_info:
            if hasattr(self.welfare_forest_water_summary_info, 'to_alipay_dict'):
                params['welfare_forest_water_summary_info'] = self.welfare_forest_water_summary_info.to_alipay_dict()
            else:
                params['welfare_forest_water_summary_info'] = self.welfare_forest_water_summary_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WelfareForestDetailDTO()
        if 'reward_info_list' in d:
            o.reward_info_list = d['reward_info_list']
        if 'rewarded_code_list' in d:
            o.rewarded_code_list = d['rewarded_code_list']
        if 'welfare_forest_entity' in d:
            o.welfare_forest_entity = d['welfare_forest_entity']
        if 'welfare_forest_person_water_info' in d:
            o.welfare_forest_person_water_info = d['welfare_forest_person_water_info']
        if 'welfare_forest_water_summary_info' in d:
            o.welfare_forest_water_summary_info = d['welfare_forest_water_summary_info']
        return o


