#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentGovernanceInfoVO(object):

    def __init__(self):
        self._punishment = None
        self._suggestion = None
        self._target_id = None
        self._target_type = None
        self._violation_desc = None

    @property
    def punishment(self):
        return self._punishment

    @punishment.setter
    def punishment(self, value):
        self._punishment = value
    @property
    def suggestion(self):
        return self._suggestion

    @suggestion.setter
    def suggestion(self, value):
        self._suggestion = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value
    @property
    def violation_desc(self):
        return self._violation_desc

    @violation_desc.setter
    def violation_desc(self, value):
        self._violation_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.punishment:
            if hasattr(self.punishment, 'to_alipay_dict'):
                params['punishment'] = self.punishment.to_alipay_dict()
            else:
                params['punishment'] = self.punishment
        if self.suggestion:
            if hasattr(self.suggestion, 'to_alipay_dict'):
                params['suggestion'] = self.suggestion.to_alipay_dict()
            else:
                params['suggestion'] = self.suggestion
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
        if self.violation_desc:
            if hasattr(self.violation_desc, 'to_alipay_dict'):
                params['violation_desc'] = self.violation_desc.to_alipay_dict()
            else:
                params['violation_desc'] = self.violation_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentGovernanceInfoVO()
        if 'punishment' in d:
            o.punishment = d['punishment']
        if 'suggestion' in d:
            o.suggestion = d['suggestion']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        if 'violation_desc' in d:
            o.violation_desc = d['violation_desc']
        return o


