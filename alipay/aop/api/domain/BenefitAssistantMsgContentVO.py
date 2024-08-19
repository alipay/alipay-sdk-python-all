#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitAssistantMsgContentVO(object):

    def __init__(self):
        self._activity_id = None
        self._crowd_code = None
        self._recommend_text = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def recommend_text(self):
        return self._recommend_text

    @recommend_text.setter
    def recommend_text(self, value):
        self._recommend_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.recommend_text:
            if hasattr(self.recommend_text, 'to_alipay_dict'):
                params['recommend_text'] = self.recommend_text.to_alipay_dict()
            else:
                params['recommend_text'] = self.recommend_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitAssistantMsgContentVO()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'recommend_text' in d:
            o.recommend_text = d['recommend_text']
        return o


