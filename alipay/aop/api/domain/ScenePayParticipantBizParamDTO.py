#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenePayParticipantBizParamDTO(object):

    def __init__(self):
        self._authorization_id = None
        self._out_card_no = None

    @property
    def authorization_id(self):
        return self._authorization_id

    @authorization_id.setter
    def authorization_id(self, value):
        self._authorization_id = value
    @property
    def out_card_no(self):
        return self._out_card_no

    @out_card_no.setter
    def out_card_no(self, value):
        self._out_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization_id:
            if hasattr(self.authorization_id, 'to_alipay_dict'):
                params['authorization_id'] = self.authorization_id.to_alipay_dict()
            else:
                params['authorization_id'] = self.authorization_id
        if self.out_card_no:
            if hasattr(self.out_card_no, 'to_alipay_dict'):
                params['out_card_no'] = self.out_card_no.to_alipay_dict()
            else:
                params['out_card_no'] = self.out_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenePayParticipantBizParamDTO()
        if 'authorization_id' in d:
            o.authorization_id = d['authorization_id']
        if 'out_card_no' in d:
            o.out_card_no = d['out_card_no']
        return o


