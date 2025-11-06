#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GuidanceUseDrugItem import GuidanceUseDrugItem


class AlipayCommerceHdfaitransferMedicationguidanceGenerateModel(object):

    def __init__(self):
        self._age = None
        self._allergic_history = None
        self._condition_description = None
        self._diagnosis = None
        self._gestation_str = None
        self._guidance_use_drug_list = None
        self._need_same_time = None
        self._precautions = None
        self._recheck_str = None
        self._sex = None
        self._use_drug_warn_str = None
        self._weight = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def allergic_history(self):
        return self._allergic_history

    @allergic_history.setter
    def allergic_history(self, value):
        self._allergic_history = value
    @property
    def condition_description(self):
        return self._condition_description

    @condition_description.setter
    def condition_description(self, value):
        self._condition_description = value
    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value
    @property
    def gestation_str(self):
        return self._gestation_str

    @gestation_str.setter
    def gestation_str(self, value):
        self._gestation_str = value
    @property
    def guidance_use_drug_list(self):
        return self._guidance_use_drug_list

    @guidance_use_drug_list.setter
    def guidance_use_drug_list(self, value):
        if isinstance(value, list):
            self._guidance_use_drug_list = list()
            for i in value:
                if isinstance(i, GuidanceUseDrugItem):
                    self._guidance_use_drug_list.append(i)
                else:
                    self._guidance_use_drug_list.append(GuidanceUseDrugItem.from_alipay_dict(i))
    @property
    def need_same_time(self):
        return self._need_same_time

    @need_same_time.setter
    def need_same_time(self, value):
        self._need_same_time = value
    @property
    def precautions(self):
        return self._precautions

    @precautions.setter
    def precautions(self, value):
        self._precautions = value
    @property
    def recheck_str(self):
        return self._recheck_str

    @recheck_str.setter
    def recheck_str(self, value):
        self._recheck_str = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def use_drug_warn_str(self):
        return self._use_drug_warn_str

    @use_drug_warn_str.setter
    def use_drug_warn_str(self, value):
        self._use_drug_warn_str = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.allergic_history:
            if hasattr(self.allergic_history, 'to_alipay_dict'):
                params['allergic_history'] = self.allergic_history.to_alipay_dict()
            else:
                params['allergic_history'] = self.allergic_history
        if self.condition_description:
            if hasattr(self.condition_description, 'to_alipay_dict'):
                params['condition_description'] = self.condition_description.to_alipay_dict()
            else:
                params['condition_description'] = self.condition_description
        if self.diagnosis:
            if hasattr(self.diagnosis, 'to_alipay_dict'):
                params['diagnosis'] = self.diagnosis.to_alipay_dict()
            else:
                params['diagnosis'] = self.diagnosis
        if self.gestation_str:
            if hasattr(self.gestation_str, 'to_alipay_dict'):
                params['gestation_str'] = self.gestation_str.to_alipay_dict()
            else:
                params['gestation_str'] = self.gestation_str
        if self.guidance_use_drug_list:
            if isinstance(self.guidance_use_drug_list, list):
                for i in range(0, len(self.guidance_use_drug_list)):
                    element = self.guidance_use_drug_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.guidance_use_drug_list[i] = element.to_alipay_dict()
            if hasattr(self.guidance_use_drug_list, 'to_alipay_dict'):
                params['guidance_use_drug_list'] = self.guidance_use_drug_list.to_alipay_dict()
            else:
                params['guidance_use_drug_list'] = self.guidance_use_drug_list
        if self.need_same_time:
            if hasattr(self.need_same_time, 'to_alipay_dict'):
                params['need_same_time'] = self.need_same_time.to_alipay_dict()
            else:
                params['need_same_time'] = self.need_same_time
        if self.precautions:
            if hasattr(self.precautions, 'to_alipay_dict'):
                params['precautions'] = self.precautions.to_alipay_dict()
            else:
                params['precautions'] = self.precautions
        if self.recheck_str:
            if hasattr(self.recheck_str, 'to_alipay_dict'):
                params['recheck_str'] = self.recheck_str.to_alipay_dict()
            else:
                params['recheck_str'] = self.recheck_str
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        if self.use_drug_warn_str:
            if hasattr(self.use_drug_warn_str, 'to_alipay_dict'):
                params['use_drug_warn_str'] = self.use_drug_warn_str.to_alipay_dict()
            else:
                params['use_drug_warn_str'] = self.use_drug_warn_str
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHdfaitransferMedicationguidanceGenerateModel()
        if 'age' in d:
            o.age = d['age']
        if 'allergic_history' in d:
            o.allergic_history = d['allergic_history']
        if 'condition_description' in d:
            o.condition_description = d['condition_description']
        if 'diagnosis' in d:
            o.diagnosis = d['diagnosis']
        if 'gestation_str' in d:
            o.gestation_str = d['gestation_str']
        if 'guidance_use_drug_list' in d:
            o.guidance_use_drug_list = d['guidance_use_drug_list']
        if 'need_same_time' in d:
            o.need_same_time = d['need_same_time']
        if 'precautions' in d:
            o.precautions = d['precautions']
        if 'recheck_str' in d:
            o.recheck_str = d['recheck_str']
        if 'sex' in d:
            o.sex = d['sex']
        if 'use_drug_warn_str' in d:
            o.use_drug_warn_str = d['use_drug_warn_str']
        if 'weight' in d:
            o.weight = d['weight']
        return o


