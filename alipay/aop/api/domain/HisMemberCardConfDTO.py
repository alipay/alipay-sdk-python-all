#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HisMemberCardConfDTO(object):

    def __init__(self):
        self._need_fee_type = None
        self._need_guardian_info = None
        self._neeed_his_member_card = None

    @property
    def need_fee_type(self):
        return self._need_fee_type

    @need_fee_type.setter
    def need_fee_type(self, value):
        self._need_fee_type = value
    @property
    def need_guardian_info(self):
        return self._need_guardian_info

    @need_guardian_info.setter
    def need_guardian_info(self, value):
        self._need_guardian_info = value
    @property
    def neeed_his_member_card(self):
        return self._neeed_his_member_card

    @neeed_his_member_card.setter
    def neeed_his_member_card(self, value):
        self._neeed_his_member_card = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_fee_type:
            if hasattr(self.need_fee_type, 'to_alipay_dict'):
                params['need_fee_type'] = self.need_fee_type.to_alipay_dict()
            else:
                params['need_fee_type'] = self.need_fee_type
        if self.need_guardian_info:
            if hasattr(self.need_guardian_info, 'to_alipay_dict'):
                params['need_guardian_info'] = self.need_guardian_info.to_alipay_dict()
            else:
                params['need_guardian_info'] = self.need_guardian_info
        if self.neeed_his_member_card:
            if hasattr(self.neeed_his_member_card, 'to_alipay_dict'):
                params['neeed_his_member_card'] = self.neeed_his_member_card.to_alipay_dict()
            else:
                params['neeed_his_member_card'] = self.neeed_his_member_card
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HisMemberCardConfDTO()
        if 'need_fee_type' in d:
            o.need_fee_type = d['need_fee_type']
        if 'need_guardian_info' in d:
            o.need_guardian_info = d['need_guardian_info']
        if 'neeed_his_member_card' in d:
            o.neeed_his_member_card = d['neeed_his_member_card']
        return o


