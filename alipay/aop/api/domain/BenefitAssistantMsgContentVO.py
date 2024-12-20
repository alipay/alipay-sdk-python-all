#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitAssistantMsgContentVO(object):

    def __init__(self):
        self._activity_id = None
        self._activity_id_list = None
        self._crowd_code = None
        self._multi_coupon = None
        self._recommend_text = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_id_list(self):
        return self._activity_id_list

    @activity_id_list.setter
    def activity_id_list(self, value):
        if isinstance(value, list):
            self._activity_id_list = list()
            for i in value:
                self._activity_id_list.append(i)
    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def multi_coupon(self):
        return self._multi_coupon

    @multi_coupon.setter
    def multi_coupon(self, value):
        self._multi_coupon = value
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
        if self.activity_id_list:
            if isinstance(self.activity_id_list, list):
                for i in range(0, len(self.activity_id_list)):
                    element = self.activity_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_id_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_id_list, 'to_alipay_dict'):
                params['activity_id_list'] = self.activity_id_list.to_alipay_dict()
            else:
                params['activity_id_list'] = self.activity_id_list
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.multi_coupon:
            if hasattr(self.multi_coupon, 'to_alipay_dict'):
                params['multi_coupon'] = self.multi_coupon.to_alipay_dict()
            else:
                params['multi_coupon'] = self.multi_coupon
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
        if 'activity_id_list' in d:
            o.activity_id_list = d['activity_id_list']
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'multi_coupon' in d:
            o.multi_coupon = d['multi_coupon']
        if 'recommend_text' in d:
            o.recommend_text = d['recommend_text']
        return o


