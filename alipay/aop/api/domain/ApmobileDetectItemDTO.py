#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApmobileDetectItemDTO(object):

    def __init__(self):
        self._detect_item_conclusion = None
        self._detect_item_desc = None
        self._detect_item_step = None
        self._detect_item_sub_type = None
        self._evidence_text = None
        self._expert_opinion = None

    @property
    def detect_item_conclusion(self):
        return self._detect_item_conclusion

    @detect_item_conclusion.setter
    def detect_item_conclusion(self, value):
        self._detect_item_conclusion = value
    @property
    def detect_item_desc(self):
        return self._detect_item_desc

    @detect_item_desc.setter
    def detect_item_desc(self, value):
        self._detect_item_desc = value
    @property
    def detect_item_step(self):
        return self._detect_item_step

    @detect_item_step.setter
    def detect_item_step(self, value):
        self._detect_item_step = value
    @property
    def detect_item_sub_type(self):
        return self._detect_item_sub_type

    @detect_item_sub_type.setter
    def detect_item_sub_type(self, value):
        self._detect_item_sub_type = value
    @property
    def evidence_text(self):
        return self._evidence_text

    @evidence_text.setter
    def evidence_text(self, value):
        self._evidence_text = value
    @property
    def expert_opinion(self):
        return self._expert_opinion

    @expert_opinion.setter
    def expert_opinion(self, value):
        self._expert_opinion = value


    def to_alipay_dict(self):
        params = dict()
        if self.detect_item_conclusion:
            if hasattr(self.detect_item_conclusion, 'to_alipay_dict'):
                params['detect_item_conclusion'] = self.detect_item_conclusion.to_alipay_dict()
            else:
                params['detect_item_conclusion'] = self.detect_item_conclusion
        if self.detect_item_desc:
            if hasattr(self.detect_item_desc, 'to_alipay_dict'):
                params['detect_item_desc'] = self.detect_item_desc.to_alipay_dict()
            else:
                params['detect_item_desc'] = self.detect_item_desc
        if self.detect_item_step:
            if hasattr(self.detect_item_step, 'to_alipay_dict'):
                params['detect_item_step'] = self.detect_item_step.to_alipay_dict()
            else:
                params['detect_item_step'] = self.detect_item_step
        if self.detect_item_sub_type:
            if hasattr(self.detect_item_sub_type, 'to_alipay_dict'):
                params['detect_item_sub_type'] = self.detect_item_sub_type.to_alipay_dict()
            else:
                params['detect_item_sub_type'] = self.detect_item_sub_type
        if self.evidence_text:
            if hasattr(self.evidence_text, 'to_alipay_dict'):
                params['evidence_text'] = self.evidence_text.to_alipay_dict()
            else:
                params['evidence_text'] = self.evidence_text
        if self.expert_opinion:
            if hasattr(self.expert_opinion, 'to_alipay_dict'):
                params['expert_opinion'] = self.expert_opinion.to_alipay_dict()
            else:
                params['expert_opinion'] = self.expert_opinion
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileDetectItemDTO()
        if 'detect_item_conclusion' in d:
            o.detect_item_conclusion = d['detect_item_conclusion']
        if 'detect_item_desc' in d:
            o.detect_item_desc = d['detect_item_desc']
        if 'detect_item_step' in d:
            o.detect_item_step = d['detect_item_step']
        if 'detect_item_sub_type' in d:
            o.detect_item_sub_type = d['detect_item_sub_type']
        if 'evidence_text' in d:
            o.evidence_text = d['evidence_text']
        if 'expert_opinion' in d:
            o.expert_opinion = d['expert_opinion']
        return o


