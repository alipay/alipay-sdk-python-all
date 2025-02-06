#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalEbbenefitMemberGetModel(object):

    def __init__(self):
        self._eb_user_id = None
        self._member_id = None
        self._out_user_id = None

    @property
    def eb_user_id(self):
        return self._eb_user_id

    @eb_user_id.setter
    def eb_user_id(self, value):
        self._eb_user_id = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.eb_user_id:
            if hasattr(self.eb_user_id, 'to_alipay_dict'):
                params['eb_user_id'] = self.eb_user_id.to_alipay_dict()
            else:
                params['eb_user_id'] = self.eb_user_id
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalEbbenefitMemberGetModel()
        if 'eb_user_id' in d:
            o.eb_user_id = d['eb_user_id']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        return o


