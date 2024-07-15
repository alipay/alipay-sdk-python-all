#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssistantActivityVO import AssistantActivityVO


class ActivityAssistantMsgContentVO(object):

    def __init__(self):
        self._activity_list = None
        self._recommend_text = None

    @property
    def activity_list(self):
        return self._activity_list

    @activity_list.setter
    def activity_list(self, value):
        if isinstance(value, list):
            self._activity_list = list()
            for i in value:
                if isinstance(i, AssistantActivityVO):
                    self._activity_list.append(i)
                else:
                    self._activity_list.append(AssistantActivityVO.from_alipay_dict(i))
    @property
    def recommend_text(self):
        return self._recommend_text

    @recommend_text.setter
    def recommend_text(self, value):
        self._recommend_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_list:
            if isinstance(self.activity_list, list):
                for i in range(0, len(self.activity_list)):
                    element = self.activity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_list, 'to_alipay_dict'):
                params['activity_list'] = self.activity_list.to_alipay_dict()
            else:
                params['activity_list'] = self.activity_list
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
        o = ActivityAssistantMsgContentVO()
        if 'activity_list' in d:
            o.activity_list = d['activity_list']
        if 'recommend_text' in d:
            o.recommend_text = d['recommend_text']
        return o


