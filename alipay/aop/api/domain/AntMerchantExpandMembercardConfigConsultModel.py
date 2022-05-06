#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MemberCardSetModifyRequest import MemberCardSetModifyRequest


class AntMerchantExpandMembercardConfigConsultModel(object):

    def __init__(self):
        self._member_card_set_modify_request = None

    @property
    def member_card_set_modify_request(self):
        return self._member_card_set_modify_request

    @member_card_set_modify_request.setter
    def member_card_set_modify_request(self, value):
        if isinstance(value, MemberCardSetModifyRequest):
            self._member_card_set_modify_request = value
        else:
            self._member_card_set_modify_request = MemberCardSetModifyRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.member_card_set_modify_request:
            if hasattr(self.member_card_set_modify_request, 'to_alipay_dict'):
                params['member_card_set_modify_request'] = self.member_card_set_modify_request.to_alipay_dict()
            else:
                params['member_card_set_modify_request'] = self.member_card_set_modify_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandMembercardConfigConsultModel()
        if 'member_card_set_modify_request' in d:
            o.member_card_set_modify_request = d['member_card_set_modify_request']
        return o


