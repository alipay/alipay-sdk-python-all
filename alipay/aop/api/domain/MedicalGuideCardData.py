#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SymptomPartInfo import SymptomPartInfo
from alipay.aop.api.domain.MedicalGuideTab import MedicalGuideTab


class MedicalGuideCardData(object):

    def __init__(self):
        self._manual_input = None
        self._options = None
        self._options_choice_type = None
        self._refresh = None
        self._special_options = None
        self._symptom_part_infos = None
        self._tabs = None

    @property
    def manual_input(self):
        return self._manual_input

    @manual_input.setter
    def manual_input(self, value):
        self._manual_input = value
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                self._options.append(i)
    @property
    def options_choice_type(self):
        return self._options_choice_type

    @options_choice_type.setter
    def options_choice_type(self, value):
        self._options_choice_type = value
    @property
    def refresh(self):
        return self._refresh

    @refresh.setter
    def refresh(self, value):
        self._refresh = value
    @property
    def special_options(self):
        return self._special_options

    @special_options.setter
    def special_options(self, value):
        if isinstance(value, list):
            self._special_options = list()
            for i in value:
                self._special_options.append(i)
    @property
    def symptom_part_infos(self):
        return self._symptom_part_infos

    @symptom_part_infos.setter
    def symptom_part_infos(self, value):
        if isinstance(value, list):
            self._symptom_part_infos = list()
            for i in value:
                if isinstance(i, SymptomPartInfo):
                    self._symptom_part_infos.append(i)
                else:
                    self._symptom_part_infos.append(SymptomPartInfo.from_alipay_dict(i))
    @property
    def tabs(self):
        return self._tabs

    @tabs.setter
    def tabs(self, value):
        if isinstance(value, list):
            self._tabs = list()
            for i in value:
                if isinstance(i, MedicalGuideTab):
                    self._tabs.append(i)
                else:
                    self._tabs.append(MedicalGuideTab.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.manual_input:
            if hasattr(self.manual_input, 'to_alipay_dict'):
                params['manual_input'] = self.manual_input.to_alipay_dict()
            else:
                params['manual_input'] = self.manual_input
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        if self.options_choice_type:
            if hasattr(self.options_choice_type, 'to_alipay_dict'):
                params['options_choice_type'] = self.options_choice_type.to_alipay_dict()
            else:
                params['options_choice_type'] = self.options_choice_type
        if self.refresh:
            if hasattr(self.refresh, 'to_alipay_dict'):
                params['refresh'] = self.refresh.to_alipay_dict()
            else:
                params['refresh'] = self.refresh
        if self.special_options:
            if isinstance(self.special_options, list):
                for i in range(0, len(self.special_options)):
                    element = self.special_options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.special_options[i] = element.to_alipay_dict()
            if hasattr(self.special_options, 'to_alipay_dict'):
                params['special_options'] = self.special_options.to_alipay_dict()
            else:
                params['special_options'] = self.special_options
        if self.symptom_part_infos:
            if isinstance(self.symptom_part_infos, list):
                for i in range(0, len(self.symptom_part_infos)):
                    element = self.symptom_part_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symptom_part_infos[i] = element.to_alipay_dict()
            if hasattr(self.symptom_part_infos, 'to_alipay_dict'):
                params['symptom_part_infos'] = self.symptom_part_infos.to_alipay_dict()
            else:
                params['symptom_part_infos'] = self.symptom_part_infos
        if self.tabs:
            if isinstance(self.tabs, list):
                for i in range(0, len(self.tabs)):
                    element = self.tabs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tabs[i] = element.to_alipay_dict()
            if hasattr(self.tabs, 'to_alipay_dict'):
                params['tabs'] = self.tabs.to_alipay_dict()
            else:
                params['tabs'] = self.tabs
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalGuideCardData()
        if 'manual_input' in d:
            o.manual_input = d['manual_input']
        if 'options' in d:
            o.options = d['options']
        if 'options_choice_type' in d:
            o.options_choice_type = d['options_choice_type']
        if 'refresh' in d:
            o.refresh = d['refresh']
        if 'special_options' in d:
            o.special_options = d['special_options']
        if 'symptom_part_infos' in d:
            o.symptom_part_infos = d['symptom_part_infos']
        if 'tabs' in d:
            o.tabs = d['tabs']
        return o


