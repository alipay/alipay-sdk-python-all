#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationPromokernelPrizeRecommendModel(object):

    def __init__(self):
        self._alipay_user_unique_identifier = None
        self._camp_id = None
        self._out_biz_no = None
        self._prize_id = None

    @property
    def alipay_user_unique_identifier(self):
        return self._alipay_user_unique_identifier

    @alipay_user_unique_identifier.setter
    def alipay_user_unique_identifier(self, value):
        self._alipay_user_unique_identifier = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_unique_identifier:
            if hasattr(self.alipay_user_unique_identifier, 'to_alipay_dict'):
                params['alipay_user_unique_identifier'] = self.alipay_user_unique_identifier.to_alipay_dict()
            else:
                params['alipay_user_unique_identifier'] = self.alipay_user_unique_identifier
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationPromokernelPrizeRecommendModel()
        if 'alipay_user_unique_identifier' in d:
            o.alipay_user_unique_identifier = d['alipay_user_unique_identifier']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        return o


