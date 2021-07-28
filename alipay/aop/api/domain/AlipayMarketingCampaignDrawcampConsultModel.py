#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsultExtParams import ConsultExtParams


class AlipayMarketingCampaignDrawcampConsultModel(object):

    def __init__(self):
        self._camp_id = None
        self._ext_params = None
        self._prize_id_list = None
        self._source = None
        self._user_id = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        if isinstance(value, ConsultExtParams):
            self._ext_params = value
        else:
            self._ext_params = ConsultExtParams.from_alipay_dict(value)
    @property
    def prize_id_list(self):
        return self._prize_id_list

    @prize_id_list.setter
    def prize_id_list(self, value):
        self._prize_id_list = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.prize_id_list:
            if hasattr(self.prize_id_list, 'to_alipay_dict'):
                params['prize_id_list'] = self.prize_id_list.to_alipay_dict()
            else:
                params['prize_id_list'] = self.prize_id_list
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignDrawcampConsultModel()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'prize_id_list' in d:
            o.prize_id_list = d['prize_id_list']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


