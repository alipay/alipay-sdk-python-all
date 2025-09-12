#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscribeMemberInfoDTO import SubscribeMemberInfoDTO


class SubscribeStatusApiResponse(object):

    def __init__(self):
        self._member_status = None
        self._subscribe_member_info_d_t_o = None

    @property
    def member_status(self):
        return self._member_status

    @member_status.setter
    def member_status(self, value):
        self._member_status = value
    @property
    def subscribe_member_info_d_t_o(self):
        return self._subscribe_member_info_d_t_o

    @subscribe_member_info_d_t_o.setter
    def subscribe_member_info_d_t_o(self, value):
        if isinstance(value, SubscribeMemberInfoDTO):
            self._subscribe_member_info_d_t_o = value
        else:
            self._subscribe_member_info_d_t_o = SubscribeMemberInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.member_status:
            if hasattr(self.member_status, 'to_alipay_dict'):
                params['member_status'] = self.member_status.to_alipay_dict()
            else:
                params['member_status'] = self.member_status
        if self.subscribe_member_info_d_t_o:
            if hasattr(self.subscribe_member_info_d_t_o, 'to_alipay_dict'):
                params['subscribe_member_info_d_t_o'] = self.subscribe_member_info_d_t_o.to_alipay_dict()
            else:
                params['subscribe_member_info_d_t_o'] = self.subscribe_member_info_d_t_o
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscribeStatusApiResponse()
        if 'member_status' in d:
            o.member_status = d['member_status']
        if 'subscribe_member_info_d_t_o' in d:
            o.subscribe_member_info_d_t_o = d['subscribe_member_info_d_t_o']
        return o


