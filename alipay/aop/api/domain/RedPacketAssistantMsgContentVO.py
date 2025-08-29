#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssistantRedPacketVO import AssistantRedPacketVO


class RedPacketAssistantMsgContentVO(object):

    def __init__(self):
        self._recommend_text = None
        self._red_packet_list = None

    @property
    def recommend_text(self):
        return self._recommend_text

    @recommend_text.setter
    def recommend_text(self, value):
        self._recommend_text = value
    @property
    def red_packet_list(self):
        return self._red_packet_list

    @red_packet_list.setter
    def red_packet_list(self, value):
        if isinstance(value, list):
            self._red_packet_list = list()
            for i in value:
                if isinstance(i, AssistantRedPacketVO):
                    self._red_packet_list.append(i)
                else:
                    self._red_packet_list.append(AssistantRedPacketVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.recommend_text:
            if hasattr(self.recommend_text, 'to_alipay_dict'):
                params['recommend_text'] = self.recommend_text.to_alipay_dict()
            else:
                params['recommend_text'] = self.recommend_text
        if self.red_packet_list:
            if isinstance(self.red_packet_list, list):
                for i in range(0, len(self.red_packet_list)):
                    element = self.red_packet_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.red_packet_list[i] = element.to_alipay_dict()
            if hasattr(self.red_packet_list, 'to_alipay_dict'):
                params['red_packet_list'] = self.red_packet_list.to_alipay_dict()
            else:
                params['red_packet_list'] = self.red_packet_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RedPacketAssistantMsgContentVO()
        if 'recommend_text' in d:
            o.recommend_text = d['recommend_text']
        if 'red_packet_list' in d:
            o.red_packet_list = d['red_packet_list']
        return o


